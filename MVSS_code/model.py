import time
import requests
import json
from tqdm import tqdm
import threading

class APIModel:

    def __init__(self, model, api_key, api_url) -> None:
        self.__api_key = api_key
        self.__api_url = api_url
        self.model = model
        
    def __req(self, text, temperature, max_try = 5):
        url = f"{self.__api_url}"
        pay_load_dict = {
            "model": f"{self.model}",
            "messages": [{
                "role": "user",
                "content": f"{text}"
            }],
            "temperature": temperature
        }
        payload = json.dumps(pay_load_dict)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.__api_key}',
            'User-Agent': 'Survey-Generator/1.0',
            'Content-Type': 'application/json'
        }
        
        last_exception = None
        
        for attempt in range(max_try):
            try:
                response = requests.request("POST", url, headers=headers, data=payload, timeout=300)
                response.raise_for_status() 
                response_data = response.json()

                if 'choices' in response_data and response_data['choices']:
                    return response_data['choices'][0]['message']['content']
                elif 'error' in response_data:
                    last_exception = Exception(f"API Error: {response_data['error'].get('message', 'Unknown error')}")
                    print(f"API Logic Error: {last_exception}")
                else:
                    last_exception = Exception(f"Invalid API response format: {response.text}")
                    print(f"Invalid API response format: {response.text}")

            except requests.exceptions.RequestException as e:
                last_exception = e
                print(f"Request failed (Attempt {attempt + 1}/{max_try}): {e}")
            except (json.JSONDecodeError, KeyError, IndexError) as e:
                last_exception = e
                print(f"Failed to parse response (Attempt {attempt + 1}/{max_try}): {e} - Response: {response.text[:200]}...")
            
            if attempt < max_try - 1:
                time.sleep(1.0 * (attempt + 1)) 
                
        print(f"API request finally failed after {max_try} attempts. Last error: {last_exception}")
        return None
    
    def chat(self, text, temperature=1):
        response = self.__req(text, temperature=temperature, max_try=5)
        return response

    def __chat(self, text, temperature, res_l, idx, pbar=None):
        response = self.__req(text, temperature=temperature)
        res_l[idx] = response
        if pbar:
            pbar.update(1) 
        return response
        
    def batch_chat(self, text_batch, temperature=0):
        max_threads=15 
        res_l = ['No response'] * len(text_batch)
        
        pbar = tqdm(total=len(text_batch), desc="Processing batch requests")
        
        active_threads = []
        idx = 0
        
        try:
            while idx < len(text_batch) or active_threads:
                while len(active_threads) < max_threads and idx < len(text_batch):
                    text = text_batch[idx]
                    thread = threading.Thread(target=self.__chat, args=(text, temperature, res_l, idx, pbar))
                    thread.start()
                    active_threads.append(thread)
                    idx += 1
                
                active_threads = [t for t in active_threads if t.is_alive()]
                
                time.sleep(0.1) 

        except KeyboardInterrupt:
            print("\nInterrupt detected! Attempting safe stop...")
        finally:
            for t in active_threads:
                t.join()
            pbar.close() 
            
        return res_l