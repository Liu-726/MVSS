import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


class APIModel:

    def __init__(
        self,
        model: str,
        api_key: str,
        api_url: str,
        timeout=(10, 1000),
    ) -> None:
        self.model = model
        self.api_key = api_key
        self.api_url = api_url

        if isinstance(timeout, (int, float)):
            self.timeout = (10, int(timeout))
        else:
            self.timeout = timeout

    def chat(self, text: str, temperature: float = 0.0, max_try: int = 10) -> str:
        url = self.api_url
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": text}],
            "temperature": float(temperature),
            "stream": False,
        }

        last_err = None
        for i in range(max_try):
            try:
                resp = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
                if resp.status_code != 200:
                    raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            except Exception as e:
                last_err = e
                time.sleep(min(2 ** i, 8))

        raise RuntimeError(f"APIModel.chat failed after {max_try} tries. Last error: {last_err}")

    def batch_chat(
        self,
        text_batch,
        temperature: float = 0.0,
        max_try: int = 5,
        max_workers: int = 1,
    ):
        if text_batch is None:
            return []
        if not isinstance(text_batch, (list, tuple)):
            raise TypeError(f"text_batch must be list/tuple, got {type(text_batch)}")

        n = len(text_batch)
        if n == 0:
            return []

        workers = max(1, min(int(max_workers), n))
        results = [None] * n

        def _one(i, txt):
            results[i] = self.chat(txt, temperature=temperature, max_try=max_try)

        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = [ex.submit(_one, i, t) for i, t in enumerate(text_batch)]
            for f in as_completed(futures):
                f.result()

        return results