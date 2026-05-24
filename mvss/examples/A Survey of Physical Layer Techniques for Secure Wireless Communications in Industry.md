# A Comprehensive Survey of Physical Layer Security for Industrial Wireless Communications: Fundamentals, Techniques, and Applications

## 1 Introduction to Physical Layer Security in Industrial Wireless Networks

This section introduces the critical need for robust security in industrial wireless communications, highlighting the unique challenges and requirements of industrial environments. It defines Physical Layer Security (PLS), contrasts it with traditional cryptographic approaches, and outlines the core information-theoretic principles, scope, and structure of the survey.

### 1.1 The Imperative for Security in Industrial Wireless Networks

The ongoing digital transformation of industrial processes, often encapsulated by the terms Industry 4.0 and the emerging human-centric Industry 5.0, is fundamentally reshaping manufacturing, logistics, and critical infrastructure. At the heart of this revolution lies the pervasive adoption of wireless communication technologies, which serve as the central nervous system for a new generation of smart, flexible, and autonomous systems. This paradigm shift moves away from rigid, wired fieldbus architectures towards dynamic networks that interconnect a vast array of Industrial Internet of Things (IIoT) devices, including sensors, actuators, autonomous mobile robots (AMRs), and collaborative robots (cobots) [1]. Wireless connectivity is the key enabler for highly flexible manufacturing processes, allowing for rapid reconfiguration of production lines, real-time asset tracking, and the integration of mobile platforms like drones and automated guided vehicles (AGVs) [2]. Technologies such as 5G, with its Ultra-Reliable Low Latency Communication (URLLC) capabilities, and Time-Sensitive Networking (TSN) for deterministic performance, are being integrated to meet the stringent requirements of closed-loop control, machine synchronization, and real-time process automation [3] [4]. This wireless fabric supports applications ranging from environmental monitoring in chemical warehouses [5] to precision control in additive manufacturing and the orchestration of complex cyber-physical systems (CPS) [6].

However, the immense benefits of this wireless industrial ecosystem are inextricably linked to profound and unprecedented security challenges. The transition from isolated, air-gapped wired networks to open, heterogeneous wireless communication fundamentally expands the attack surface. The broadcast nature of the wireless medium inherently exposes communications to potential eavesdroppers and malicious actors who may be physically outside the traditional perimeter of the factory floor [7]. This shift from offline to online infrastructure introduces severe novel risks, as highlighted in [8]. Industrial control systems (ICS) and operational technology (OT), which were historically separated from information technology (IT) networks, are now converging, exposing legacy systems with long lifecycles and often minimal built-in security to modern cyber threats [9]. The consequences of security breaches in this context transcend mere data theft or privacy violations; they directly threaten physical safety, operational continuity, and economic viability.

The potential impacts of compromised industrial wireless networks are catastrophic. From a safety perspective, an attacker who intercepts or maliciously alters sensor data from a pressure vessel or manipulates commands sent to a robotic arm can trigger industrial accidents, equipment damage, and loss of life [5]. Jamming attacks, which deliberately interfere with radio signals, can disrupt the real-time communication essential for synchronization and control, causing production lines to halt unpredictably or safety mechanisms to fail [10]. The financial ramifications are equally severe. Unplanned downtime in a high-throughput manufacturing facility can result in losses of hundreds of thousands of dollars per hour. Furthermore, intellectual property theft through the eavesdropping of proprietary process data or machine telemetry can erode a company's competitive advantage. Attacks can also target the integrity of the production process itself, leading to the manufacture of defective or sabotaged goods, which damages brand reputation and incurs massive recall costs. As noted in [6], smart manufacturing has become a prime target for cyber threats, questioning the fundamental security of connecting manufacturing resources and integrating entire process chains.

The unique constraints of industrial environments further complicate security provisioning. IIoT devices are often resource-constrained, with limited processing power, memory, and energy budgets, making the deployment of complex, traditional cryptographic suites challenging [11]. Networks must support ultra-low latency and ultra-high reliability (e.g., for URLLC) while simultaneously performing security functions like authentication and encryption [12]. The scale is also immense, with thousands of devices needing secure management, which creates key distribution and identity management nightmares [13]. Moreover, industrial systems have long operational lifespans, requiring security solutions that remain effective against evolving threats over decades, a challenge highlighted in the discussion of embedded security research [14].

Therefore, security in industrial wireless networks cannot be an afterthought or a mere software add-on; it must be a non-negotiable, foundational design principle. A holistic, defense-in-depth strategy is imperative, as advocated in [15]. This strategy must extend beyond conventional network-layer protocols to include the physical (PHY) layer of wireless communication. The physical layer offers unique properties—such as channel randomness, hardware imperfections, and spatial characteristics—that can be harnessed to create intrinsic security mechanisms. Techniques like physical layer security (PLS) can provide information-theoretic guarantees of confidentiality against eavesdroppers, while RF fingerprinting can offer robust device authentication based on hardware-specific imperfections [16]. By integrating these PHY-layer techniques with higher-layer cryptographic and network security measures, a more resilient and comprehensive security posture can be achieved. This approach is crucial for building trust in wireless systems for critical applications, from functional safety communication [17] to the protection of future 6G-enabled smart manufacturing [18]. In essence, securing the industrial wireless frontier is not just a technical challenge but a prerequisite for realizing the full promise of Industry 4.0 and 5.0, ensuring that the drive for efficiency and flexibility does not come at the cost of safety, reliability, and resilience.

**Table: Comparison of approaches in 1.1 The Imperative for Security in Industrial Wireless Networks**

| Aspect | Key Technologies/Concepts | Role/Function in Industrial Wireless | Security Challenges/Considerations | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Core Enabling Technologies | 5G (URLLC), Time-Sensitive Networking (TSN), Wireless Sensor Networks (WSN) | Provides ultra-reliable, low-latency, deterministic communication for closed-loop control, machine synchronization, and flexible, reconfigurable production lines. | Integration expands attack surface; requires security that does not compromise latency/reliability. | [1], [4], [5] |
| Security Threats & Attack Vectors | Eavesdropping, Jamming, Data/Command Manipulation, Legacy System Exposure | The broadcast nature of wireless and convergence of IT/OT networks expose systems to interception, disruption, and integrity attacks. | Directly threatens physical safety (accidents), operational continuity (downtime), and economic viability (IP theft, defective goods). | [7], [8], [10], [9] |
| Device & Network Constraints | Resource-constrained IIoT devices, Large-scale deployments, Long lifecycles | Limits the applicability of complex cryptographic suites and complicates key management and identity provisioning. | Creates challenges for deploying robust security on devices with limited power, memory, and processing capabilities over decades-long operational spans. | [11], [13], [14] |
| Holistic Security Strategy | Defence-in-Depth, Physical Layer Security (PLS), RF Fingerprinting, AI/ML | Advocates for a multi-layered approach integrating PHY-layer intrinsic properties (channel randomness, hardware imperfections) with higher-layer cryptography. | Aims to provide information-theoretic security, robust device authentication, and adaptive threat detection to build comprehensive resilience. | [15], [16], [6] |
| Future & Enabling Concepts | 6G, Intelligent Reflecting Surfaces (IRS), Underlayer Networks | Envisions next-generation wireless with enhanced reliability, low latency, and controllability for human-centric Industry 5.0 and smart manufacturing. | Security must be a foundational design principle for these future networks to ensure safety and trust in critical applications. | [18], [19], [17] |


### 1.2 Unique Challenges and Requirements of the Industrial Environment

The industrial wireless environment presents a unique and formidable set of constraints that fundamentally differentiate it from conventional consumer or enterprise networks, imposing stringent demands on the design and efficacy of physical layer security (PLS) solutions. These challenges stem from the mission-critical nature of industrial operations, where communication failures can lead to catastrophic safety incidents, significant financial loss, and severe production downtime. The primary differentiators can be categorized into the harshness of the radio frequency (RF) environment, the extreme quality-of-service (QoS) requirements, the scale and heterogeneity of connected devices, and the extended lifecycle of industrial assets.

Firstly, the industrial RF environment is notoriously hostile and dynamic. Factories are dense with metallic machinery, reflective surfaces, and moving objects, creating a complex propagation landscape characterized by severe multipath fading, deep shadowing, and rapid temporal variations [20]. This rich scattering can degrade channel estimation accuracy, which is foundational for many PLS techniques like secret key generation from channel state information (CSI). Furthermore, the proliferation of wireless devices for diverse purposes—from high-precision sensors to autonomous guided vehicles—operating over both licensed and unlicensed bands leads to significant co-channel and adjacent-channel interference [21]. This interference is not merely noise; it can be intentional jamming, a potent threat where an adversary transmits high-power signals to disrupt legitimate communications. Jamming attacks are particularly devastating in industrial settings, as they can directly halt production lines or induce unsafe states in control loops [22]. The PLS framework must therefore be robust not only against passive eavesdropping but also against these active denial-of-service attacks, requiring techniques that ensure reliability under intentional interference.

Secondly, and most critically, industrial applications demand Ultra-Reliable Low-Latency Communication (URLLC). Use cases such as closed-loop motion control, cooperative robotics, and safety system actuation require end-to-end latencies as low as 1 ms with packet error rates below 10^-9 [23]. This "finite blocklength" regime, where packets are short to minimize latency, invalidates classical information-theoretic results based on infinite coding blocklengths. The achievable secrecy rate drops, and decoding error probabilities increase, making it exponentially harder to guarantee both reliability and confidentiality simultaneously [24]. Traditional upper-layer cryptographic handshakes and key exchanges introduce prohibitive latency and overhead, creating a compelling case for lightweight, low-latency PLS mechanisms that can operate within these stringent timing budgets. Security cannot be an afterthought that compromises the latency or reliability guarantee; it must be intrinsically woven into the physical layer design.

Thirdly, the Industrial Internet of Things (IIoT) landscape is defined by massive scale and extreme heterogeneity. A single smart factory may deploy thousands of sensors, actuators, and controllers [25]. These devices exhibit vast disparities in computational capability, memory, and energy budget. While some controllers may have substantial resources, many sensors are severely resource-constrained, incapable of running complex cryptographic suites or sophisticated signal processing algorithms. This heterogeneity precludes a one-size-fits-all security solution. PLS techniques must be inherently lightweight to be deployable on the simplest devices. Furthermore, the sheer number of devices creates a massive attack surface and complicates network-wide security management. Authentication becomes a paramount challenge, as traditional certificate-based methods may not scale efficiently. This has spurred interest in physical-layer authentication methods like RF fingerprinting, which leverages hardware imperfections as a unique device identifier [26]. However, the industrial environment's dynamic channel conditions can obscure these subtle fingerprints, requiring adaptive and robust authentication schemes.

Finally, the long lifecycle of industrial assets, often spanning decades, poses a unique challenge for security sustainability. Unlike consumer devices with rapid replacement cycles, industrial machinery and control systems are deployed for the long term. This longevity conflicts with the rapid evolution of both communication technology and cyber threats. A PLS solution designed today must remain effective against future adversarial capabilities. Moreover, updating security protocols or cryptographic algorithms on field-deployed, legacy brownfield devices is often impractical or impossible [27]. This necessitates security by design with forward-looking properties and mechanisms that can be upgraded or adapted through software or reconfigurable hardware components, such as Reconfigurable Intelligent Surfaces (RIS) [28]. The security architecture must also account for the convergence of once-isolated Operational Technology (OT) networks with Information Technology (IT) systems, which exposes previously air-gapped critical infrastructure to a broader range of network-based attacks, including sophisticated insider threats and ransomware [9].

In summary, securing wireless communications in industry requires PLS techniques that are robust against harsh and interfering channels, efficient enough to operate within the ultra-stringent bounds of URLLC, scalable and lightweight to accommodate massive, heterogeneous IIoT deployments, and sustainable over the extended lifespan of industrial equipment. These are not incremental challenges but fundamental constraints that shape the entire research agenda for physical layer security in industrial networks, pushing the field beyond theoretical models towards practical, resilient, and integrated solutions.

**Table: Comparison of approaches in 1.2 Unique Challenges and Requirements of the Industrial Environment**

| Challenge Category | Key Constraint | Impact on PLS Design | Relevant PLS Techniques / Solutions | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Harsh & Dynamic RF Environment | Severe multipath fading, shadowing, rapid temporal variations, co-channel/adjacent-channel interference, intentional jamming. | Degrades channel estimation accuracy (critical for CSI-based key generation); requires robustness against active denial-of-service (jamming) in addition to passive eavesdropping. | Robust channel estimation; interference detection/classification & mapping; jamming-resistant transmission schemes. | [20]; [21]; [22] |
| Ultra-Reliable Low-Latency Communication (URLLC) | End-to-end latencies as low as 1 ms, packet error rates below 10^-9, finite blocklength regime. | Invalidates classical infinite-blocklength information theory; reduces achievable secrecy rate, increases decoding errors; traditional crypto handshakes introduce prohibitive latency. | Lightweight, low-latency PLS integrated into PHY design; resource allocation for secure URLLC under finite blocklength; short-packet secure communications. | [23]; [24]; [29] |
| Massive Scale & Heterogeneity of IIoT | Thousands of devices with vast disparities in computational capability, memory, and energy; massive attack surface. | Precludes one-size-fits-all security; requires inherently lightweight PLS; complicates authentication and network-wide security management. | Physical-layer authentication (e.g., RF fingerprinting); adaptive and robust authentication schemes; lightweight cryptographic suites. | [25]; [26] |
| Extended Lifecycle of Industrial Assets | Long deployment spans (decades) conflict with rapid evolution of tech and threats; updating security on legacy brownfield devices is often impractical. | Requires forward-looking security by design; mechanisms must be sustainable and upgradable over long periods. | Security architectures with upgradeable components (e.g., via software or reconfigurable hardware like RIS); security testbeds for brownfield systems. | [27]; [28]; [9] |


### 1.3 Physical Layer Security: Definition and Core Philosophy

Physical Layer Security (PLS) represents a foundational paradigm shift in securing wireless communications, moving beyond the traditional reliance on cryptographic protocols implemented at higher network layers. At its core, PLS is defined as the exploitation of the inherent, uncontrollable properties of the wireless physical medium—specifically the randomness of the communication channel and the unique characteristics of transceiver hardware—to achieve fundamental security objectives such as confidentiality, authentication, and integrity [30]. The key philosophical tenet is to leverage the natural advantages of the legitimate communication link over that of a potential adversary, thereby creating a security barrier rooted in the laws of physics and information theory rather than computational complexity.

This approach stands in stark contrast to conventional cryptographic methods. Traditional cryptography, such as public-key infrastructure (PKI) and symmetric encryption, operates under the assumption of computational security. Its strength is predicated on the computational intractability of mathematical problems (e.g., integer factorization) for any adversary with bounded resources. However, this model faces significant challenges in modern industrial wireless networks: the advent of quantum computing threatens to break widely used algorithms [31]; the stringent latency, reliability, and energy constraints of Industrial Internet of Things (IIoT) devices often preclude the execution of complex cryptographic protocols [32]; and the management of cryptographic keys across vast, heterogeneous networks presents a substantial logistical overhead.

PLS addresses these challenges by offering several distinct advantages rooted in its information-theoretic foundation. First and foremost, information-theoretic security, as pioneered by Shannon's notion of perfect secrecy and the wiretap channel model, provides security guarantees that are not contingent on an adversary's computational power. A system is considered information-theoretically secure if the mutual information between the secret message and the signal observed by the eavesdropper is zero, meaning the eavesdropper gains no information regardless of their computational capabilities [33]. This makes PLS inherently resistant to attacks from quantum computers, positioning it as a crucial component of quantum-safe networks for future industrial systems. Secondly, PLS techniques are often characterized by lower computational complexity and latency. By operating directly on the physical waveforms and channel properties, they can provide security with minimal processing overhead. This is particularly vital for ultra-reliable low-latency communication (URLLC) in industrial automation, where traditional encryption and decryption cycles may introduce unacceptable delays [34]. Furthermore, PLS can function in a lightweight manner, generating secret keys from channel measurements or authenticating devices based on radio frequency fingerprints without requiring extensive key pre-distribution, making it highly suitable for resource-constrained IoT sensors and actuators [35].

The core mechanisms of PLS are built upon the unique properties of the wireless medium. For confidentiality, the principle of the wiretap channel is central. It aims to ensure that the channel to the legitimate receiver (Bob) is of better quality—a higher signal-to-noise ratio (SNR) or capacity—than the channel to the eavesdropper (Eve). Techniques such as beamforming, artificial noise, and cooperative jamming are then employed to actively degrade Eve's channel or enhance Bob's, thereby maximizing the secrecy capacity, defined as the maximum rate at which information can be transmitted reliably and confidentially [36]. For authentication and integrity, PLS utilizes the physical uniqueness of devices and channels. Hardware imperfections in radio frequency circuits create distinct, device-specific fingerprints in the transmitted signal, known as RF fingerprints, which can be used for device authentication [37]. Similarly, the spatial decorrelation property of wireless channels ensures that the Channel State Information (CSI) measured by two spatially separated nodes (like a legitimate receiver and an eavesdropper) is largely independent. This spatial uniqueness can be used for location-based authentication or as a source of shared entropy for secret key generation (SKG) between legitimate parties [38].

It is critical to emphasize that PLS is not envisioned as a wholesale replacement for cryptographic security but as a powerful and essential complement within a defense-in-depth strategy for industrial wireless networks. A holistic security architecture should leverage the strengths of both approaches. Cryptography provides robust, well-understood frameworks for secure key exchange, non-repudiation, and securing data at rest, which remain indispensable. PLS adds an additional, lower-layer barrier that can protect against attacks that bypass or compromise cryptographic systems. For instance, PLS can provide lightweight, continuous authentication to detect spoofing attacks, generate fresh encryption keys on-the-fly to achieve perfect forward secrecy, or use friendly jamming to protect transmissions in hard-to-encrypt scenarios like broadcast control signals. This synergistic integration creates a more resilient security posture. Even if an adversary manages to break the cryptographic layer through a novel attack or future quantum computer, the physical layer barriers—rooted in the instantaneous and location-specific state of the wireless environment—would remain a formidable obstacle [39]. Therefore, the core philosophy of PLS in industrial contexts is to harness the immutable characteristics of the physical world to build a pervasive, lightweight, and future-proof security substrate that works in concert with traditional methods to safeguard critical communications against an evolving threat landscape.

**Table: Comparison of approaches in 1.3 Physical Layer Security: Definition and Core Philosophy**

| Method / Technique | Core Principle / Mechanism | Key Advantages / Applications | Reference |
| :--- | :--- | :--- | :--- |
| **Wiretap Channel & Secrecy Capacity Maximization** | Exploits the quality difference between the legitimate (Bob) and eavesdropper (Eve) channels (e.g., higher SNR/capacity for Bob). Employs beamforming, artificial noise, and cooperative jamming to degrade Eve's channel. | Achieves information-theoretic confidentiality. Provides security guarantees independent of adversary's computational power (quantum-resistant). | [36] |
| **RF Fingerprinting for Authentication** | Utilizes unique, device-specific hardware imperfections in radio frequency circuits to create a distinct fingerprint in the transmitted signal. | Provides lightweight, continuous device authentication. Difficult for an adversary to forge, enhancing spoofing attack detection. | [37] |
| **Channel State Information (CSI) for Secret Key Generation (SKG)** | Leverages the spatial decorrelation property of wireless channels. The CSI measured by spatially separated legitimate nodes is independent from that of an eavesdropper, providing shared entropy. | Enables on-the-fly generation of fresh encryption keys (perfect forward secrecy). Low overhead, suitable for resource-constrained IoT devices. | [38] |
| **Artificial Noise & Friendly Jamming** | Actively transmits noise/jamming signals to interfere with the eavesdropper's reception while minimizing impact on the legitimate receiver. | Enhances secrecy capacity in hard-to-encrypt scenarios (e.g., broadcast). Can be implemented with low complexity. | [40], [41] |
| **Lightweight SKG from Channel Measurements** | Generates secret keys from reciprocal channel measurements using quantization and error correction codes (e.g., LDPC codes). | Minimal computational and latency overhead. Ideal for URLLC and low-power IoT sensors/actuators. | [35] |


### 1.4 Scope, Contributions, and Structure of the Survey

This survey is dedicated to a systematic exploration of Physical Layer Security (PLS) techniques specifically designed for, and critically evaluated within, the context of industrial wireless communications. The scope is deliberately focused on the unique confluence of stringent industrial requirements—ultra-reliability, low latency, deterministic performance, and operational longevity—with the security challenges inherent to the wireless medium. We concentrate on techniques that leverage the physical properties of the wireless channel and transceiver hardware to provide authentication, confidentiality, and integrity, moving beyond traditional cryptographic approaches to offer complementary or alternative security primitives suitable for resource-constrained Industrial Internet of Things (IIoT) devices and mission-critical control loops. The analysis spans from foundational information-theoretic principles to the implementation challenges of emerging hardware technologies, with a constant emphasis on practical deployment considerations, channel characteristics in harsh industrial settings, and integration with existing industrial network architectures. Notably, while we reference broader wireless concepts, our examination is filtered through the lens of industrial applicability, prioritizing solutions that address concrete threats like jamming on factory floors, eavesdropping on sensitive process data, and spoofing of mobile robots or drones.

The primary contribution of this work is a holistic synthesis that bridges theoretical PLS foundations with the pragmatic realities of industrial deployment. First, we provide a consolidated tutorial on core PLS metrics and threat models, contextualizing them within industrial scenarios such as smart manufacturing plants and automated warehouses. Second, we offer a comprehensive and critical review of how transformative technologies like Reconfigurable Intelligent Surfaces (RIS) and Non-Orthogonal Multiple Access (NOMA) are being tailored for industrial security. This includes not only their performance benefits but also a frank discussion of their deployment challenges, such as the real-time channel estimation requirements for RIS in dynamic environments [42] and the security-complexity trade-offs in NOMA power allocation for untrusted devices. Third, we dedicate significant attention to the often-overlooked aspect of key management at the physical layer, surveying practical key generation from Channel State Information (CSI) and RIS-assisted schemes, which are vital for lightweight security in IIoT networks. Finally, a forward-looking contribution is our detailed analysis of PLS integration within next-generation industrial paradigms, including Cyber-Physical Systems (CPS), UAV-assisted logistics, and 6G infrastructures, highlighting the role of AI for adaptive security [43] and the vision of programmable wireless environments as a security service [44].

To guide the reader through this comprehensive landscape, the survey is structured into four logically consecutive sections. **Section 1** has established the fundamentals, introducing the core concepts, metrics, and threat models of PLS, with a specific focus on eavesdropping, jamming, and insider threats relevant to industrial settings. It also covered active countermeasures like artificial noise techniques. **Section 2** delves into advanced communication techniques that enhance PLS. It begins with a detailed analysis of RIS, covering secure beamforming design, phase shift optimization, and the practical challenges of deploying these surfaces in industrial halls [45]. It then examines the PLS aspects of NOMA, including secrecy rate optimization and power allocation among trusted and untrusted users. The section concludes with an overview of Visible Light Communication (VLC) as a complementary secure medium for controlled industrial environments.

**Section 3** shifts focus to the crucial backend of security: key management. It systematically reviews physical-layer key generation techniques, from traditional CSI-based methods to novel RIS-assisted approaches and efficient quantization schemes. It then explores cryptographic techniques that interface with the physical layer, including Quantum Key Distribution (QKD) for long-term security and lightweight authentication/encryption schemes suitable for IIoT devices. **Finally, Section 4** grounds the preceding technical discussion in real-world applications and future trends. It analyzes PLS for critical industrial verticals: IIoT (featuring RF fingerprinting for device authentication [46]), UAV communications (secure trajectory and jamming resilience), and CPS (resilience modeling and attack detection). The survey culminates by exploring the future of industrial PLS in the 6G era, discussing the opportunities and new vulnerabilities presented by terahertz communications, AI-driven security orchestration, and the need for quantum-safe networks. This structure is designed to provide researchers and practitioners with a clear roadmap, from understanding the basic principles of securing the wireless physical layer to navigating the implementation complexities and future directions for building robust, secure, and intelligent industrial wireless networks.

**Table: Comparison of approaches in 1.4 Scope, Contributions, and Structure of the Survey**

| Method / Technology | Key Idea / Contribution | Application Context in Survey | Reference |
| :--- | :--- | :--- | :--- |
| Reconfigurable Intelligent Surfaces (RIS) | Artificial planar structures with integrated circuits that can be programmed to manipulate incoming electromagnetic waves, enabling dynamic control of the wireless propagation environment. | Secure beamforming design, phase shift optimization, and providing lightweight security for IIoT devices. Discussed in the context of deployment challenges in dynamic industrial environments. | [42] |
| Non-Orthogonal Multiple Access (NOMA) | A multiple access scheme allowing multiple users to share the same time/frequency resource via power-domain multiplexing, requiring sophisticated power allocation. | PLS aspects including secrecy rate optimization and power allocation among trusted/untrusted users. The survey discusses the security-complexity trade-offs involved. | *[47, 48]* |
| Physical-Layer Key Generation (from CSI) | Generating secret cryptographic keys from the shared randomness of reciprocal wireless Channel State Information (CSI) between two communicating parties. | A practical key management technique surveyed as vital for lightweight security in resource-constrained IIoT networks. | [33] |
| RF Fingerprinting | Utilizing unique, hardware-induced features in wireless physical-layer waveforms to identify and authenticate devices. | Mentioned as a technique for device authentication in Industrial IoT (IIoT) networks. | [46] |
| Visible Light Communication (VLC) | Using modulated light (typically LEDs) for data transmission, offering a complementary medium to RF. | Presented as a complementary secure medium for controlled industrial environments, leveraging its line-of-sight nature. | *[47, 48]* |
| Artificial Intelligence / Machine Learning for Security | Applying ML/AI techniques to enable adaptive, intelligent security orchestration and configuration in wireless networks. | Highlighted as a forward-looking approach for adaptive security in next-generation industrial paradigms like 6G and CPS. | [43] |
| Programmable Wireless Environments / Wireless Environment as a Service | A paradigm where the wireless propagation environment itself (via RISs) is dynamically controlled and optimized as a service to meet diverse objectives. | Discussed as a visionary concept for future industrial security services, enabling goal-oriented control of the radio environment. | [44] |



### Roadmap and Taxonomy

The following taxonomy tree outlines the structure of this survey:


```markdown
A Survey of Physical Layer Techniques for Secure Wireless Communications in Industry
|----Section 1: Fundamentals of Physical Layer Security
|     |----Subsection 1.1: Core Concepts and Metrics
|     |     |----Secrecy Capacity: [49][50][51]
|     |     |----Secrecy Outage Probability: [52][53][54]
|     |     |----Information-Theoretic Security: [55][56][57]
|     |     |----Physical Layer Authentication: [58][59][60]
|     |----Subsection 1.2: Threat Models and Attack Scenarios
|     |     |----Eavesdropping Analysis: [61][62][63]
|     |     |----Jamming Attacks: [64][65][66]
|     |     |----Insider Threats: [67][68][69]
|     |     |----Relay Attacks: [22][70][71]
|     |----Subsection 1.3: Artificial Noise Techniques
|     |     |----Friendly Jamming: [72][73][74]
|     |     |----Directional Modulation: [75][76][77]
|     |     |----Noise Alignment: [78][79][80]

|----Section 2: Enhancing Secure Communication
|     |----Subsection 2.1: Reconfigurable Intelligent Surfaces (RIS)
|     |     |----Beamforming Design: [81][82][83]
|     |     |----Phase Shift Optimization: [84][85][86]
|     |     |----Secure Key Generation: [87][88][89]
|     |     |----RIS Deployment Challenges: [45][90][91]
|     |----Subsection 2.2: Non-Orthogonal Multiple Access (NOMA)
|     |     |----Secrecy Rate Optimization: [92][93][94]
|     |     |----Power Allocation Schemes: [95][96][86]
|     |     |----Untrusted User Handling: [97][98][99]
|     |----Subsection 2.3: Visible Light Communication (VLC)
|     |     |----Secrecy Capacity in VLC: [100][76][101]
|     |     |----Jamming Resilience: [53][91][102]
|     |     |----Beamforming in VLC: [103][104][59]

|----Section 3: Physical Layer Key Management
|     |----Subsection 3.1: Key Generation Techniques
|     |     |----Channel State Information (CSI): [105][106][107]
|     |     |----RIS-Assisted Key Generation: [87][88][108]
|     |     |----One-Bit Quantization for Keys: [35][109][110]
|     |----Subsection 3.2: Cryptographic Techniques
|     |     |----Quantum Key Distribution: [111][112][113]
|     |     |----Physical Layer Authentication: [38][114][95]
|     |     |----Lightweight Encryption: [115][46][116]

|----Section 4: Industry Applications and Emerging Trends
|     |----Subsection 4.1: Internet of Things (IoT)
|     |     |----RF Fingerprinting for IoT: [59][117][81]
|     |     |----Industrial IoT Authentication: [118][119][120]
|     |     |----Lightweight IoT Security: [121][122][123]
|     |----Subsection 4.2: UAV Communications
|     |     |----Secure Trajectory Optimization: [64][124][125]
|     |     |----Jamming Resilience in UAVs: [126][127][85]
|     |     |----Relay-Assisted Secure UAV Links: [128][129][130]
|     |----Subsection 4.3: Cyber-Physical Systems (CPS)
|     |     |----Resilience Modeling in CPS: [89][131][132]
|     |     |----Attack Detection Frameworks: [133][134][135]
|     |     |----Smart Manufacturing Security: [136][137][138]
|     |----Subsection 4.4: 6G and Beyond
|     |     |----Terahertz Communication: [81][122][139]
|     |     |----AI-Driven Security: [140][141][142]
|     |     |----Quantum-Safe Networks: [143][144][145]
```


## 2 Foundational Principles, Metrics, and Threat Models

This section establishes the theoretical and practical groundwork for PLS. It covers information-theoretic foundations, including key metrics like secrecy capacity and secrecy outage probability. It details comprehensive threat models specific to industrial settings and analyzes the impact of practical impairments and security-reliability-delay trade-offs.

### 2.1 Information-Theoretic Foundations and Core Security Metrics

The cornerstone of physical layer security (PLS) is Wyner's wiretap channel model, which established the possibility of achieving information-theoretic secrecy—security guaranteed against an eavesdropper with unlimited computational power—by exploiting the inherent randomness and noise of the communication medium. In this foundational model, a transmitter (Alice) sends a confidential message to a legitimate receiver (Bob) over a *main channel*, while an eavesdropper (Eve) attempts to intercept the transmission over a *wiretap channel*. The seminal result is that a non-zero secrecy rate is achievable if the wiretap channel is a *degraded* version of the main channel, meaning Eve's observation is a noisier version of Bob's. This concept was later generalized by Csiszár and Körner to non-degraded broadcast channels with confidential messages, forming the bedrock for all subsequent PLS analyses. The ultimate performance limit is characterized by the **secrecy capacity**, defined as the maximum rate at which information can be transmitted reliably to Bob while remaining perfectly secret from Eve. For a discrete memoryless wiretap channel, the secrecy capacity \( C_s \) is given by the difference between the capacity of the main channel \( C_m \) and the capacity of the wiretap channel \( C_e \), maximized over the input distribution: \( C_s = \max_{P_X} [146]^+ \), where \( I(\cdot;\cdot) \) denotes mutual information, and \( [147]^+ = \max(0, x) \). Recent breakthroughs have focused on achieving this fundamental limit with practical, polynomial-time schemes that also satisfy the stronger **semantic security** criterion, which requires negligible mutual information between the message and Eve's observations for *all* possible message distributions, not just uniform ones [148].

In practical wireless systems, channels experience fading, making the instantaneous capacities \( C_m \) and \( C_e \) random variables. Consequently, the secrecy capacity cannot be guaranteed for every channel realization, leading to the definition of key probabilistic performance metrics. The most widely used is the **Secrecy Outage Probability (SOP)**, defined as the probability that the instantaneous secrecy capacity falls below a target secrecy rate \( R_s \): \( P_{out}(R_s) = \Pr(C_s < R_s) \). Deriving tractable, often closed-form, expressions for the SOP under various fading models is a central theme in PLS analysis. Extensive work has been done for generalized fading distributions like \(\kappa\)-\(\mu\) shadowed [149], Fisher-Snedecor \(\mathcal{F}\) [150], Fluctuating Beckmann [151], and \(\alpha\)-\(\kappa\)-\(\mu\) shadowed [152]. These models unify multipath and shadowing effects, providing accurate characterization of industrial environments. The SOP analysis often extends to relay-assisted systems, analyzing decode-and-forward protocols under different wiretap link conditions [153], and to systems with correlated main and wiretap channels, where counterintuitively, increased correlation can sometimes improve secrecy performance by reducing the probability of Eve having a significantly better channel than Bob [154]. To gain deeper insights, asymptotic SOP analysis in the high signal-to-noise ratio (SNR) regime reveals the **secrecy diversity order**, quantifying how fast the SOP decreases with increasing SNR [155].

Complementary metrics provide a fuller picture of system performance. The **Probability of Strictly Positive Secrecy Capacity (SPSC)** is the probability that the instantaneous secrecy capacity is greater than zero, indicating the fraction of time secure communication is theoretically possible. The **Average Secrecy Capacity (ASC)** quantifies the ergodic average of the instantaneous secrecy capacity, representing the long-term achievable secure throughput. Closed-form expressions for these metrics have been derived for numerous fading models [156]. Furthermore, alternative formulations like the **conditional information leakage given the eavesdropper's received signals** have been proposed to develop fast algorithms for evaluating information leakage with linear complexity in code length, as opposed to the exponential complexity of computing standard mutual information [157]. For active attack scenarios, such as the adversarial wiretap channel where Eve can read and modify a fraction of the transmitted symbols, the secrecy capacity and achievable code constructions have also been characterized [158].

A critical shift in modern industrial communications, particularly for ultra-reliable low-latency communications (URLLC) and massive machine-type communications (mMTC), is the use of short packets or **finite blocklength (FBL) codes**. In the FBL regime, the idealized assumptions of infinite coding blocklength underpinning the secrecy capacity formula break down. The decoding error probability at Bob becomes non-negligible, and information leakage to Eve must be re-evaluated. This has led to the development of new metrics and design frameworks. The **effective secrecy throughput (EST)** emerges as a key metric, explicitly capturing the trade-off between reliability (correct decoding at Bob) and secrecy (non-decoding at Eve), measuring the average rate of confidential information successfully delivered [159]. Similarly, the **leakage-failure probability** jointly characterizes both reliability and security performances for short-packet transmissions, with studies showing that system performance can sometimes be enhanced by counter-intuitively allocating *fewer* resources when using FBL codes [160]. The **average information leakage (AIL)** is another FBL metric used to assess secrecy performance when only statistical CSI of the eavesdropper is available, revealing an inherent statistical relationship between AIL and the conventional SOP [161]. Performance analysis in the FBL regime also confirms that increasing blocklength generally benefits both reliability and secrecy, and that secrecy throughput is a concave function of the secrecy rate, necessitating an optimal rate selection [162]. The fundamental limits of wiretap channels in the non-asymptotic blocklength regime have been tightly bounded, establishing the optimal tradeoff between reliability, secrecy, and rate for finite blocklengths [163].

Finally, the design of practical codes achieving these information-theoretic limits is paramount. **Lattice codes** have been shown to be strong candidates, with constructions from algebraic number fields and division algebras achieving strong secrecy and semantic security for fading and MIMO wiretap channels, exhibiting almost universal properties across a wide range of channel models [164]. Furthermore, **polar codes** have been constructed to achieve the secrecy capacity of general wiretap channels and the capacity region of broadcast channels with confidential messages under strong secrecy constraints [165]. For the FBL regime, novel deep learning-based approaches decouple reliability and secrecy constraints, using autoencoders for reliability and hash functions for secrecy, to design short blocklength wiretap codes that outperform known achievable rates [166]. Together, these information-theoretic foundations and evolving metrics provide the rigorous mathematical framework necessary to analyze, design, and deploy physically secure wireless systems capable of meeting the stringent and diverse requirements of modern industrial applications.

**Table: Comparison of approaches in 2.1 Information-Theoretic Foundations and Core Security Metrics**

| Method/Model | Key Idea/Contribution | Reference |
| :--- | :--- | :--- |
| Wyner's Wiretap Channel & Csiszár-Körner Generalization | Establishes information-theoretic secrecy via channel noise; non-zero secrecy rate achievable if wiretap channel is degraded; generalized to non-degraded broadcast channels. | [148] |
| Secrecy Outage Probability (SOP) Analysis for Generalized Fading | Deriving tractable/closed-form SOP expressions under various fading models (e.g., κ-μ shadowed, Fisher-Snedecor F, Fluctuating Beckmann, α-κ-μ shadowed) to characterize performance in random fading channels. | [149], [150], [151], [152] |
| SOP Analysis for Relay & Correlated Channels | Analyzing SOP for decode-and-forward relay systems under different wiretap link conditions and for systems with correlated main/wiretap channels, where increased correlation can sometimes improve secrecy. | [153], [154] |
| Asymptotic SOP & Secrecy Diversity Order | High-SNR asymptotic analysis of SOP to reveal the secrecy diversity order, quantifying how fast SOP decreases with increasing SNR. | [155] |
| Complementary Metrics (SPSC, ASC) | Probability of Strictly Positive Secrecy Capacity (SPSC) and Average Secrecy Capacity (ASC) provide a fuller performance picture, with closed-form expressions derived for various fading models. | [156] |
| Conditional Information Leakage Metric | Proposes "conditional information leakage given eavesdropper's received signals" to enable fast linear-complexity algorithms for evaluating leakage vs. exponential complexity of standard mutual information. | [157] |
| Adversarial Wiretap Channel Model | Models active attacks where Eve can read and modify a fraction of transmitted symbols; characterizes secrecy capacity and achievable code constructions. | [158] |
| Finite Blocklength (FBL) Metrics: Effective Secrecy Throughput (EST) | Metric for short-packet (FBL) regimes capturing trade-off between reliability (correct decoding at Bob) and secrecy (non-decoding at Eve); measures average rate of confidential information successfully delivered. | [159] |
| Finite Blocklength (FBL) Metrics: Leakage-Failure Probability | Jointly characterizes reliability and security for short packets; shows system performance can be enhanced by counter-intuitively allocating fewer resources with FBL codes. | [160] |
| Finite Blocklength (FBL) Metrics: Average Information Leakage (AIL) | Assesses secrecy performance with only statistical CSI of eavesdropper; reveals inherent statistical relationship between AIL and conventional SOP. | [161] |
| FBL Performance Analysis & Optimization | Analysis confirms increasing blocklength benefits reliability and secrecy; secrecy throughput is concave in secrecy rate, necessitating optimal rate selection. | [162] |
| Non-Asymptotic Fundamental Limits for FBL | Establishes tight bounds on the optimal tradeoff between reliability, secrecy, and rate for finite blocklengths in wiretap channels. | [163] |
| Lattice Codes for Secrecy | Constructions from algebraic number fields/division algebras achieve strong and semantic security for fading/MIMO wiretap channels with almost universal properties across channel models. | [164] |
| Polar Codes for Secrecy | Constructed to achieve secrecy capacity of general wiretap channels and capacity region of broadcast channels with confidential messages under strong secrecy. | [165] |
| Deep Learning-based FBL Code Design | Decouples reliability and secrecy constraints using autoencoders for reliability and hash functions for secrecy to design short blocklength wiretap codes outperforming known achievable rates. | [166] |


### 2.2 Comprehensive Threat Models for Industrial Wireless Networks

The industrial wireless landscape presents a unique and challenging security environment, characterized by mission-critical operations, long device lifecycles, and the convergence of information technology (IT) with operational technology (OT). This convergence, while enabling advanced functionalities like remote monitoring and predictive maintenance, dramatically expands the attack surface. A robust understanding of adversarial models specific to this domain is therefore paramount for designing effective physical layer security (PLS) countermeasures. Threat models in industrial settings can be broadly categorized into passive and active attacks, with increasing sophistication that directly targets the cyber-physical nexus.

**Passive Eavesdropping** remains a fundamental threat, where an adversary attempts to intercept confidential data without altering transmissions. In industrial environments, eavesdroppers may target sensitive process data, control commands, or cryptographic key material exchanged between sensors, actuators, and controllers. The analysis of eavesdropping must consider advanced scenarios, such as **colluding eavesdroppers** that pool their intercepted signals to improve decoding capabilities, a significant threat in dense IIoT deployments. Furthermore, the assumption of **randomly located eavesdroppers** is critical for risk assessment, as security guarantees must hold statistically over potential eavesdropper positions, not just for a fixed location. The vulnerability is exacerbated in systems where the main (legitimate) and wiretap (eavesdropper) channels are highly correlated, making it difficult to design secure beamforming strategies without additional countermeasures [167].

**Active attacks** pose a more direct and immediate danger to industrial operations. **Jamming attacks** aim to disrupt communication by injecting interfering signals into the wireless medium. These range from simple barrage jamming, which floods a frequency band with noise, to more sophisticated **protocol-aware jamming** that targets specific packet types or protocol handshakes to maximize disruption while conserving the attacker's energy. In control systems, even short-term communication loss can lead to process instability or safety system failures. A particularly insidious form of active attack is the **deception attack**, such as **False Data Injection (FDI)**, where an adversary with access to the network hijacks communication channels—like those between a Human-Machine Interface (HMI) and Programmable Logic Controllers (PLCs)—and manipulates sensor readings or control commands [168]. These attacks are designed to be **stealthy**, meaning they present a coherent but false view of the physical process to operators, potentially leading to manual interventions that cause damage or allowing the physical system to drift into an unsafe state undetected. The synthesis of such attacks can be formally modeled using discrete event systems to find strategies that induce undesirable states while avoiding detection mechanisms [169]. Furthermore, **reactive injection attacks** represent a class where adversaries opportunistically inject spoofing packets, forcing base stations to expend resources on impersonation detection [170].

The relay-centric architecture of many industrial and IoT networks introduces another vector: **relay-based attacks**. Here, a relay node, which is essential for extending coverage or improving reliability, can itself be malicious or **untrusted**. An untrusted relay participates in communication but may also attempt to decode confidential information. This creates a complex trade-off between leveraging the relay for performance and securing data from it, a central challenge in schemes like Non-Orthogonal Multiple Access (NOMA) with untrusted users [171]. PLS techniques must be designed to work with or against such relays, for instance, by using artificial noise to degrade the relay's eavesdropping capability while preserving the legitimate link.

Perhaps the most challenging threats are **insider attacks**, where the adversary is a legitimate but compromised entity within the system. In the context of PLS, this includes attacks on **physical-layer key generation** processes. Key generation often relies on the reciprocity and randomness of the wireless channel between two legitimate parties. An insider with partial knowledge of the system or the ability to influence channel measurements can launch attacks to reduce the key entropy or predict the generated keys, breaking the security premise. Similarly, **active linkability attacks** demonstrate that an active adversary, capable of not just observing but also subtly manipulating protocol exchanges, can be strictly more powerful than a passive eavesdropper in determining whether two communication sessions belong to the same entity, violating privacy guarantees [172].

Finally, the threat model must account for **adversarial machine learning** targeting the security systems themselves. As machine learning-based intrusion detection systems (IDS) and anomaly detectors become prevalent in ICS, they become new attack vectors. Adversaries can craft **adversarial examples**—perturbations to network traffic features—to evade detection [173]. More critically, they can perform **poisoning attacks** during the training phase of online-learning detectors, injecting malicious data to manipulate the learned model and create blind spots for future attacks [174]. The threat extends to deep reinforcement learning agents used for network control or resource allocation, where an adversary snooping on action and reward signals can train a proxy model to craft effective attacks [175].

These comprehensive threat models are inextricably linked to the vulnerabilities inherent in industrial systems. The long deployment cycles of IIoT devices and PLCs, often with limited computational resources, make them ill-suited for frequent cryptographic updates, emphasizing the need for lightweight and inherent PHY security [176]. The deterministic, predictable nature of industrial control traffic, while beneficial for reliability, makes it easier for attackers to model and craft stealthy deception attacks [177]. Therefore, securing industrial wireless communications requires PLS techniques that are resilient not only to traditional eavesdroppers and jammers but also to these sophisticated, domain-specific threats that exploit the unique intersection of cyber and physical processes in IIoT, CPS, and industrial control networks.

**Table: Comparison of approaches in 2.2 Comprehensive Threat Models for Industrial Wireless Networks**

| Threat Category | Specific Attack Type | Key Characteristics / Description | Reference |
| :--- | :--- | :--- | :--- |
| Passive Eavesdropping | Colluding Eavesdroppers | Multiple eavesdroppers pool intercepted signals to improve decoding capabilities, a significant threat in dense IIoT deployments. | [167] |
| Passive Eavesdropping | Randomly Located Eavesdroppers | Security guarantees must hold statistically over potential eavesdropper positions, not just for a fixed location. | [167] |
| Active Attacks | Jamming / Protocol-Aware Jamming | Aims to disrupt communication by injecting interfering signals; can range from simple barrage jamming to sophisticated attacks targeting specific protocol handshakes. | [168] |
| Active Attacks | Deception / False Data Injection (FDI) | Adversary hijacks communication channels (e.g., HMI-PLC) to manipulate sensor readings or control commands, presenting a coherent but false view to operators. | [168] |
| Active Attacks | Stealthy Deception Attacks | Attacks designed to be stealthy, avoiding detection mechanisms while inducing undesirable system states. | [169] |
| Active Attacks | Reactive Injection Attacks | Adversary opportunistically injects spoofing packets, forcing base stations to expend resources on impersonation detection. | [170] |
| Relay-based Attacks | Untrusted Relay Attacks | A relay node, essential for extending coverage, can itself be malicious and attempt to decode confidential information, creating a security-performance trade-off. | [171] |
| Insider Attacks | Attacks on Physical-Layer Key Generation | Insider with partial system knowledge can launch attacks to reduce key entropy or predict generated keys, breaking the security premise of channel-based key generation. | [172] |
| Insider Attacks | Active Linkability Attacks | An active adversary, capable of subtly manipulating protocol exchanges, can be more powerful than a passive eavesdropper in determining if two communication sessions belong to the same entity. | [172] |
| Adversarial Machine Learning | Adversarial Examples | Crafting perturbations to network traffic features to evade ML-based intrusion detection systems (IDS). | [173] |
| Adversarial Machine Learning | Poisoning Attacks | Injecting malicious data during the training phase of online-learning detectors to manipulate the learned model and create blind spots for future attacks. | [174] |
| Adversarial Machine Learning | Snooping Attacks on DRL | Adversary snooping on action and reward signals can train a proxy model to craft effective attacks against deep reinforcement learning agents used for network control. | [175] |


### 2.3 Security-Reliability-Delay Trade-offs and Cross-Layer Considerations

The stringent requirements of industrial wireless systems, particularly for Ultra-Reliable Low-Latency Communications (URLLC) and Time-Sensitive Networking (TSN), necessitate a holistic view where security, reliability, and latency are not independent design goals but are intrinsically coupled. The physical layer security (PLS) paradigm, while promising for low-complexity confidentiality, directly impacts and is constrained by these other critical performance metrics. A fundamental trade-off exists between reliability and security. Enhancing transmission reliability, typically by increasing transmit power or lowering the data rate to reduce the connection outage probability (COP), often inadvertently improves the channel conditions for a passive eavesdropper, thereby increasing the risk of interception and degrading security, as quantified by the secrecy outage probability (SOP). This security-reliability tradeoff (SRT) is a core consideration, as analyzed in works like [178] and [179]. To formally characterize this relationship, the reliability-security ratio (RSR) has been introduced as a metric to analyze the asymptotic behavior of how reliability improvements compare to security degradation under specific system configurations [180].

The advent of URLLC, with its mandate for packet error rates as low as \(10^{-9}\) and millisecond-level latencies, intensifies these trade-offs. The use of short packets (finite blocklength coding) to meet latency constraints invalidates the classic Shannon capacity formula, leading to a non-zero decoding error probability even at high signal-to-noise ratios. This directly affects PLS, as the achievable secrecy rate in the finite blocklength regime is degraded. Consequently, new composite metrics have emerged to jointly capture these intertwined constraints. The **leakage-failure probability** is one such metric, defined to jointly characterize both reliability (decoding failure) and security (information leakage) performances for short-packet transmissions, revealing that system performance can sometimes be enhanced by counter-intuitively allocating *fewer* resources [160]. Similarly, the concept of **effective secrecy throughput**—the product of the secrecy rate and the probability of achieving both reliable and secure connection (RSCP)—is used to evaluate overall system efficiency under outage constraints [180]. For mission-critical systems where both covertness (low probability of detection) and secrecy (low probability of interception) are required, a unified metric like the **covert secrecy rate (CSR)** is necessary, characterizing the maximum rate under joint constraints on covertness outage probability, SOP, and transmission probability [181].

These physical-layer trade-offs cannot be managed in isolation; they fundamentally dictate and must be integrated with higher-layer protocols through cross-layer design. The PHY-layer security constraints, such as a target SOP, directly influence resource allocation, scheduling, and admission control decisions at the Medium Access Control (MAC) and network layers. For instance, in multi-user industrial IoT networks, scheduling algorithms must account for heterogeneous traffic profiles—such as AoI-oriented monitoring traffic and deadline-oriented safety alarms—while considering the security vulnerabilities of shared channels [182]. A scheduler must solve the observer selection problem (OSP) to maximize the controller's knowledge of the system state, where communication reliability is defined not merely by packet loss rate but by the executive's state estimation quality, inherently incorporating security risks of missed or intercepted observations [183]. Furthermore, scheduling algorithms for URLLC must provide probabilistic per-packet real-time (PPRC) guarantees in large-scale, multi-channel networks with interference, where the schedulability test and resource allocation must implicitly or explicitly consider that allocating power for artificial noise (AN) to ensure secrecy consumes resources that could otherwise improve reliability or reduce latency [184].

Cross-layer optimization frameworks are essential to navigate these multidimensional constraints. In downlink multi-user MISO-URLLC systems, resource allocation must jointly minimize total transmit power while guaranteeing constraints on the number of transmitted bits, packet error probability, information leakage, and delay, often using successive convex approximation to handle the non-convex problem [185]. Similarly, optimization in cell-free massive MIMO-enabled URLLC systems involves jointly allocating pilot and payload power to maximize the weighted sum rate under finite blocklength constraints and imperfect CSI, demonstrating that PHY security and URLLC performance are co-dependent [186]. The trade-off extends to the network layer, where routing algorithms in ad hoc networks must find paths that optimally balance end-to-end COP and SOP, demonstrating that security-aware routing decisions directly impact the latency-reliability performance [187]. In TSN for industrial automation, the synthesis of system configurations—including task schedules, disjoint message routes, and gate control lists—must jointly uphold real-time, safety, and security requirements, using protocols like TESLA for authentication within stringent latency bounds [188].

Ultimately, achieving secure industrial communications requires moving beyond isolated layer-specific designs. The interplay between the statistical delay bounds (analyzed using tools like stochastic network calculus [189]), the finite blocklength effects on secrecy, and the higher-layer scheduling and resource allocation creates a complex design space. Strategies like multi-connectivity, which uses both D2D and cellular links, can enhance network availability and range subject to joint reliability-latency-security requirements [190]. Proactive packet dropping may also be introduced as a cross-layer control action to manage queueing delay violations and unbounded power requirements, making the overall packet loss a sum of transmission error, queueing delay violation, and proactive dropping probabilities [191]. This intricate dance between security, reliability, and delay underscores that for industrial URLLC, the physical layer is not just a bit pipe but a foundational element in a tightly integrated, cross-layer control system where security is a pervasive constraint shaping every aspect of communication resource management.

**Table: Comparison of approaches in 2.3 Security-Reliability-Delay Trade-offs and Cross-Layer Considerations**

| Metric / Concept | Primary Purpose / Definition | Key Trade-offs / Relationships | Reference |
| :--- | :--- | :--- | :--- |
| **Security-Reliability Tradeoff (SRT)** | Characterizes the fundamental conflict where improving transmission reliability (e.g., lower COP) often degrades security (e.g., higher SOP) by improving the eavesdropper's channel. | Reliability (COP) vs. Security (SOP). Enhancing one typically worsens the other. | [178], [179] |
| **Reliability-Security Ratio (RSR)** | A metric to analyze the asymptotic behavior comparing the improvement in reliability to the degradation in security under specific system configurations. | Quantifies the relative rate of change between COP and SOP. | [180] |
| **Leakage-Failure Probability** | A composite metric for short-packet URLLC that jointly characterizes reliability (decoding failure) and security (information leakage) performances. | Joint reliability-security tradeoff. Counter-intuitively, system performance can sometimes be enhanced by allocating *fewer* resources. | [160] |
| **Effective Secrecy Throughput** | The product of the secrecy rate and the probability of achieving both a reliable and secure connection (RSCP), evaluating overall system efficiency under outage constraints. | Throughput vs. Joint Reliability-Security (RSCP). Balances rate with the likelihood of successful, secure transmission. | [180] |
| **Covert Secrecy Rate (CSR)** | The maximum transmission rate under joint constraints on covertness outage probability (COP), secrecy outage probability (SOP), and transmission probability (TP) for mission-critical systems requiring both low probability of detection and interception. | Rate vs. Covertness (COP) vs. Secrecy (SOP) vs. Transmission Opportunity (TP). A unified metric for joint covertness and secrecy. | [181] |
| **AoI-Reliability Tradeoff** | In heterogeneous IIoT networks, reflects the conflict between maintaining fresh status updates (low Age of Information) and delivering sporadic safety-critical alarms with high reliability within a deadline. | Timeliness (AoI) vs. Reliability (Packet Loss Probability). Network configuration must balance these for different traffic flows. | [182] |
| **Probabilistic Per-Packet Real-Time (PPRC) Guarantee** | A scheduling guarantee for URLLC ensuring the communication quality (reliability and latency) of individual packets in large-scale, multi-channel networks with interference. | Per-packet latency/reliability vs. Network capacity and schedulability. Resource allocation must consider trade-offs with security measures like artificial noise. | [184] |
| **Cross-layer Optimization (Power Minimization)** | A framework to jointly minimize total transmit power under constraints on transmitted bits, packet error probability, information leakage, and delay for secure multi-user MISO-URLLC systems. | Transmit Power vs. Multi-dimensional QoS (Rate, Reliability, Secrecy, Latency). Demonstrates the co-dependence of PHY security and URLLC performance. | [185] |
| **Cross-layer Optimization (Queueing & Proactive Dropping)** | A framework managing overall packet loss as a sum of transmission error, queueing delay violation, and proactive packet dropping probabilities to meet URLLC QoS with finite power. | Total Packet Loss vs. Transmit Power. Introduces proactive dropping as a control action to manage unbounded power needs from stringent delay constraints. | [191] |
| **Security-Aware Routing Tradeoffs** | In multi-hop ad hoc networks, finding paths that optimally balance end-to-end connection outage probability (COP) and secrecy outage probability (SOP). | End-to-end Reliability (COP) vs. End-to-end Security (SOP). Routing decisions directly impact the latency-reliability-security trade-off. | [187] |
| **Dependability-Aware Synthesis** | In Time-Sensitive Networking (TSN), synthesizing system configurations (task schedules, disjoint routes, gate control lists) to jointly uphold real-time, safety, and security requirements using protocols like TESLA. | Real-time Latency vs. Safety (via redundancy) vs. Security (via authentication). Integrated design of scheduling and routing under composite constraints. | [188] |
| **Multi-Connectivity for Network Availability** | Using both D2D and cellular links to transmit packets, maximizing the available communication range subject to joint reliability-latency-security requirements. | Communication Range/Availability vs. Joint Reliability-Latency-Security. Exploits link diversity to meet stringent URLLC availability targets. | [190] |


### 2.4 Secrecy Performance under Practical Impairments and Uncertainties

The theoretical foundations of physical layer security (PLS) often rely on idealized assumptions, such as perfect channel state information (CSI), ideal transceiver hardware, and independent fading processes. However, the deployment of secure wireless systems in industrial environments necessitates a rigorous assessment of performance under practical impairments and uncertainties. These non-idealities can severely degrade secrecy metrics, introduce new vulnerabilities, and fundamentally alter system design principles.

A primary source of performance degradation is **imperfect channel state information (CSI)**. In practice, CSI is acquired through estimation processes that are inherently imperfect due to noise, limited pilot resources, and mobility. For the legitimate link, channel estimation errors (CEEs) distort the beamforming or precoding vectors, reducing the signal strength at the intended receiver and potentially increasing information leakage. The impact is analyzed in systems ranging from single-antenna setups [192] to large-scale MIMO [193]. More critically, CSI of the eavesdropper's channel is often completely unknown or only statistically known at the transmitter. This uncertainty forces the use of outage-based formulations, where secrecy is guaranteed probabilistically. The secrecy outage probability (SOP) becomes a key metric under such conditions [194]. The problem is exacerbated by **feedback delays**, where the CSI available at the transmitter is outdated relative to the current channel state. This temporal mismatch can render beamforming directions ineffective and significantly increase the risk of secrecy outage, particularly in mobile scenarios or systems with low-latency requirements [180]. The quality of feedback links themselves can be intermittent, further complicating capacity analysis and scheme design [195].

Closely related are **hardware impairments (HIs)** inherent in radio-frequency circuits. These include phase noise, in-phase/quadrature (I/Q) imbalance, and high-power amplifier nonlinearities. Contrary to the ideal hardware (ID) assumption, these impairments generate distortion noise that is proportional to the signal power, creating a fundamental performance ceiling. At high signal-to-noise ratios (SNRs), the effective signal-to-noise-and-distortion ratio (SNDR) saturates at a level inversely proportional to the aggregate impairment level, rather than growing unbounded [196][197]. This ceiling effect has profound implications for secrecy capacity and outage probability, as increasing transmit power beyond a certain point yields no secrecy benefit and may even aid the eavesdropper. The joint effect of I/Q imbalance and residual hardware impairments (RHIs) has been shown to severely degrade metrics like outage probability and channel capacity, especially in higher-frequency bands envisioned for 5G and beyond [198]. These impairments are equally critical in emerging paradigms like ambient backscatter-NOMA systems and wireless-powered communication networks (WPCNs), where they directly impact both reliability (outage probability) and security (intercept probability) [199][200].

The statistical **dependency between communication links** is another critical, often overlooked, factor. Traditional analyses frequently assume the main (legitimate) and wiretap (eavesdropper) channels are independent. In reality, spatial proximity or similar scattering environments can lead to correlated fading. This correlation, particularly when it is positive and high, is detrimental to PLS. If the main and wiretap channel gains are highly correlated, a deep fade for the legitimate user likely coincides with a deep fade for the eavesdropper, nullifying the legitimate user's advantage. Analytical bounds on the SOP under arbitrary dependency structures have been derived, showing that the joint distribution of the channels has a tremendous impact on achievable performance [201]. In extreme cases of near-collinear channel vectors, conventional beamforming and artificial noise at the transmitter become ineffective, necessitating innovative solutions like cooperative jamming relays [167]. Dependency also plays a role in wireless-powered systems, where correlation between the energy harvesting link and the information link can affect the secrecy capacity trade-off [202].

Furthermore, the **finite blocklength (FBL) regime** is a crucial consideration for low-latency industrial applications such as URLLC. Classical information-theoretic secrecy results assume asymptotically long codewords, which allow for perfect secrecy and error correction. In the FBL regime, short packets incur a non-zero probability of decoding error at the legitimate receiver and a non-zero information leakage to the eavesdropper. This transforms the design problem, requiring a joint optimization of blocklength, transmission rate, and power allocation to maximize metrics like secrecy throughput or to minimize the average information leakage [162][203]. The reliability-latency-rate tradeoff becomes paramount under such constraints [204].

Finally, the **integration of advanced technologies** introduces new layers of uncertainty. In reconfigurable intelligent surface (RIS)-aided systems, imperfections arise from discrete phase shifts, quantization errors, and estimation errors in the RIS-reflected channels. These imperfections must be accounted for in robust beamforming design to prevent severe outages [205][91]. Similarly, in cognitive radio networks, secondary users must operate under interference constraints to primary users with imperfect knowledge of the cross-channel CSI. This leads to a fundamental estimation-throughput tradeoff, where resources must be allocated between channel estimation and data transmission to maximize secondary throughput while protecting the primary network [206][207].

In conclusion, a realistic assessment of PLS for industrial wireless systems must move beyond ideal models. The joint and several effects of imperfect CSI, hardware impairments, channel correlation, and finite blocklength constraints create complex trade-offs and impose fundamental limits on achievable secrecy performance. Robust system design, therefore, requires optimization frameworks and transmission strategies that explicitly account for these practical impairments, ensuring that promised security guarantees hold under the non-ideal conditions of real-world industrial deployments.

**Table: Comparison of approaches in 2.4 Secrecy Performance under Practical Impairments and Uncertainties**

| Impairment/Constraint Category | Key Challenges & Effects on PLS | System Contexts / Schemes Analyzed | Key Performance Metrics (Degraded/Introduced) | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Imperfect Channel State Information (CSI) | Channel estimation errors (CEEs) distort beamforming, reducing signal strength and increasing leakage. Eavesdropper CSI often unknown, forcing probabilistic (outage) secrecy guarantees. Feedback delays cause outdated CSI, increasing secrecy outage risk. Intermittent feedback links complicate capacity analysis. | Single-antenna setups; Large-scale MIMO relaying; MISO broadcast systems with regularized zero-forcing precoding; Relay and jammer selection schemes; Erasure broadcast channels. | Secrecy outage probability (SOP); Connection outage probability (COP); Effective secrecy throughput; Reliable-and-secure connection probability (RSCP). | [192]; [193]; [194]; [180]; [195] |
| Hardware Impairments (HIs) | Phase noise, I/Q imbalance, amplifier nonlinearities generate distortion noise proportional to signal power, creating a performance ceiling (SNDR saturation) at high SNR. Impairs secrecy capacity and outage probability. | Multi-hop wireless relaying (AF/DF); Dual-hop relaying; Ambient backscatter NOMA systems; Wireless-powered communication networks (WPCNs); Systems over Fox's H-fading channels. | Outage probability (OP); Bit error probability; Ergodic capacity; Effective SNDR; Intercept probability (IP). | [196]; [197]; [199]; [200]; [198] |
| Statistical Dependency Between Links | High positive correlation between main and wiretap channels nullifies legitimate user's advantage during deep fades, making beamforming/AN ineffective. Impacts secrecy capacity trade-off in wireless-powered systems. | Systems with dependent fading channels; Scenarios with nearly collinear main and wiretap channels; Wireless-powered communication systems. | Secrecy outage probability (SOP) bounds; Secrecy capacity. | [201]; [167]; [202] |
| Finite Blocklength (FBL) Regime | Short packets incur non-zero decoding error at receiver and non-zero information leakage to eavesdropper, requiring joint optimization of blocklength, rate, and power. | Low-latency industrial applications (e.g., URLLC); Fading wiretap channels. | Secrecy throughput; Average information leakage (AIL); Reliability-latency-rate tradeoff. | [162]; [203]; [204] |
| Integration of Advanced Technologies | RIS: imperfections from discrete phase shifts, quantization, and channel estimation errors. Cognitive Radio: imperfect cross-channel CSI leads to estimation-throughput tradeoff. | Reconfigurable intelligent surface (RIS)-aided secure massive MIMO; Cognitive radio networks (interweave and underlay systems). | Outage probability; Secrecy rate; Secondary throughput; Robust beamforming design. | [205]; [91]; [206]; [207] |


### 2.5 Advanced Eavesdropper Characterization and Attack Frameworks

While foundational models like Wyner's wiretap channel provide a crucial theoretical baseline, real-world industrial wireless security must contend with far more sophisticated and capable adversaries. Advanced eavesdropper characterization moves beyond the passive, statistically degraded receiver to model adversaries with enhanced capabilities, strategic intelligence, and objectives aligned with disrupting complex cyber-physical operations. A critical evolution is the model of an **energy-harvesting eavesdropper**. In scenarios involving wireless-powered devices or ambient backscatter communications, an adversary is not merely an information sink but can also scavenge energy from the transmitted signals. This dual objective—intercepting information while potentially harvesting energy to sustain its own covert operation—fundamentally alters the threat landscape. Security strategies must now jointly optimize for secrecy rate and energy leakage, as techniques like friendly jamming or power allocation that degrade the eavesdropper's channel also reduce its harvested energy, creating a complex trade-off that departs from classical secrecy capacity formulations [208].

Furthermore, eavesdroppers are increasingly modeled as employing **advanced detection and learning strategies**. The assumption of a simple matched-filter receiver is inadequate. Adversaries may utilize sophisticated signal processing, machine learning (ML), or even deep neural networks (DNNs) to classify, demodulate, or reconstruct transmitted data, especially in multicarrier systems like OFDM. For instance, research demonstrates that adversaries equipped with supervised or unsupervised ML tools, such as variational autoencoders (VAEs), can learn physical layer characteristics like frequency patterns and modulation schemes from non-contiguous OFDM signals—systems previously argued to have low probability of exploitation. This enables powerful **learning-aided PHY spoofing attacks** where the adversary injects bogus data that appears legitimate to the receiver [209]. Similarly, the threat of **"limited-view" or "causal" adversaries** is paramount in control systems. These attackers do not have full, instantaneous knowledge of the entire system state but can only observe a subset of sensor outputs or network traffic over time. Their attacks are crafted based on this partial, sequential information, making them stealthier and more aligned with realistic intrusion scenarios where attackers gradually explore a system.

To systematically understand and defend against such threats in industrial environments, structured **attack frameworks and threat modeling methodologies** are essential. These frameworks move beyond abstract communication links to model the multi-stage, goal-oriented nature of attacks on Cyber-Physical Systems (CPS) and Industrial Control Systems (ICS). **Heuristic inference attacks** represent a class of such threats where an adversary, potentially with zero domain knowledge of proprietary ICS protocols, uses a vendor-agnostic analytics framework. By intercepting network traffic between components like Human-Machine Interfaces (HMIs) and Programmable Logic Controllers (PLCs), and applying heuristic analysis to packet structures and timing, an attacker can infer system semantics, paving the way for stealthy false data injection or deception attacks [177]. This highlights the risk posed by protocol-agnostic adversaries who exploit statistical patterns rather than specific vulnerabilities.

Quantitative threat modeling approaches like the **Threat Modeling and Attack Path Analysis (TMAP)** framework are designed to systematically identify probable attack vectors, assess attack paths, and evaluate their impact in complex Industrial IoT (IIoT) systems such as smart manufacturing lines (Internet of Manufacturing - IoM) or power plants (Internet of Production - IoP). TMAP and similar methodologies aim to provide a comprehensive analysis of cyber threats across the system lifecycle, facilitating effective path analysis that considers the interconnectedness of smart devices, controllers, and network segments [210]. These models often leverage standardized knowledge bases like the **MITRE ATT&CK® for ICS** framework, which catalogs real-world adversary Tactics, Techniques, and Procedures (TTPs). By mapping system assets and vulnerabilities to these TTPs, defenders can generate **attack graphs** that visualize potential multi-step intrusion paths, identifying critical chokepoints where defenses like deception (e.g., honeypots) or monitoring can be most effectively deployed [211].

The integration of **learning-empowered attack frameworks** further escalates the threat. Adversaries are no longer static; they can actively adapt their strategies using AI/ML. In cooperative systems like spectrum sensing, an attacker can use a black-box ML approach to construct a surrogate model of the fusion center's decision algorithm. By querying this model, the adversary can generate malicious sensing data specifically crafted to evade detection while maximizing disruption, a method demonstrated to defeat a wide range of traditional Byzantine defense strategies [212]. This represents a shift towards dynamic, adaptive adversaries whose capabilities evolve, necessitating equally adaptive and resilient defense mechanisms that anticipate not just known attacks, but the *process* by which new attacks are generated. Consequently, modern physical layer security for industry must be developed and evaluated within the context of these advanced, structured, and often AI-enhanced threat models, ensuring robustness against adversaries who are strategic, resourceful, and deeply knowledgeable about the cyber-physical systems they target.

**Table: Comparison of approaches in 2.5 Advanced Eavesdropper Characterization and Attack Frameworks**

| Threat Model / Attack Framework | Key Adversarial Capabilities / Objectives | Primary Application Context / Target | Reference |
| :--- | :--- | :--- | :--- |
| Energy-Harvesting Eavesdropper | Intercepting information while scavenging energy from transmitted signals to sustain covert operation; creates a joint secrecy rate and energy leakage trade-off. | Wireless-powered devices, ambient backscatter communications, Battery-less IoT. | [208] |
| Advanced Detection & Learning Strategies (e.g., ML/DNN/VAE) | Utilizing sophisticated signal processing, ML, or DNNs to classify, demodulate, or reconstruct transmitted data; enables learning-aided PHY spoofing attacks. | Multicarrier systems (e.g., OFDM), IoT physical layer communications. | [209] |
| Heuristic Inference Attacks | Vendor-agnostic analytics to infer system semantics (e.g., control logic, packet structures) from network traffic with zero prior domain knowledge; enables stealthy false data injection. | Industrial Control Systems (ICS), communication between HMIs and PLCs. | [177] |
| Threat Modeling and Attack Path Analysis (TMAP) | Quantitative framework to systematically identify probable attack vectors, assess attack paths, and evaluate impact magnitude in complex IIoT systems. | Industrial IoT (IIoT) systems, e.g., smart manufacturing (IoM) and power plants (IoP). | [210] |
| MITRE ATT&CK-based Attack Graph Modeling | Mapping system assets/vulnerabilities to standardized adversary TTPs to generate attack graphs visualizing multi-step intrusion paths; informs proactive defense placement (e.g., decoys). | Enterprise and Industrial Control Systems (ICS). | [211] |
| Learning-Empowered Attack Frameworks (e.g., LEB) | Adversaries use black-box ML to construct a surrogate model of a defender's decision algorithm (e.g., fusion center); generate adaptive, evasive malicious inputs. | Cooperative systems (e.g., spectrum sensing), systems using ML-based decision models. | [212] |


## 3 Core Physical Layer Security Techniques and Signal Design

This section provides a deep dive into fundamental PLS techniques and their underlying signal processing. It covers artificial noise generation, secure beamforming, foundational modulation/coding strategies, anti-jamming methods, and the emerging role of AI/ML in optimizing these techniques.

### 3.1 Artificial Noise Generation and Friendly Jamming

Artificial Noise (AN) and Friendly Jamming (FJ) are cornerstone techniques in physical layer security, designed to proactively degrade the channel quality at potential eavesdroppers while preserving or even enhancing the signal quality at the intended receiver. The fundamental principle involves the strategic transmission of interference signals—AN or jamming—that are structured to be nullified at the legitimate user but remain destructive to unauthorized listeners. This subsection details the core design methodologies, their integration with advanced transmission schemes, and the critical optimization of system resources under practical constraints.

The most prevalent AN design is based on **null-space projection (NSP)**, where AN is transmitted in the orthogonal complement of the legitimate channel's subspace. In a multiple-input multiple-output (MIMO) wiretap channel, this ensures the AN does not interfere with the intended receiver. The performance, however, is highly dependent on the availability and quality of Channel State Information (CSI). For scenarios with **imperfect CSI**, robust designs are essential. Research such as [213] investigates optimal power splitting between the information signal and AN to minimize the secrecy outage probability or maximize the secrecy rate under channel estimation errors. Interestingly, it finds that the impact of estimation error on the optimal strategy depends on the objective: to decrease a rate-constrained outage probability, more power should go to the information signal as error increases, whereas to increase an outage-constrained secrecy rate, more power should be allocated to the AN. This highlights the nuanced trade-off in resource allocation under uncertainty.

Moving beyond simple isotropic AN in the null space, **constructive interference-based AN** represents a paradigm shift by turning interference into a beneficial component for the legitimate link. As explored in [214], AN beamformers can be designed to be constructive to the intended receiver's signal detection while remaining disruptive to eavesdroppers. This approach allows part of the AN power to contribute positively to the receive signal-to-interference-and-noise ratio (SINR) at the legitimate user, thereby reducing the total transmit power required to achieve a target secrecy performance or symbol error rate (SER). This is particularly advantageous in power-constrained industrial IoT devices.

The integration of AN with **Directional Modulation (DM)** enables **secure precise wireless transmission (SPWT)** and **precise jamming (PJ)**, creating spatially focused security. Techniques like those in [215] and [216] combine DM, random subcarrier selection (RSS), phase alignment (PA), and amplitude beamforming. The goal is to focus the confidential message's energy precisely at the desired receiver's location (SPWT) while concentrating the AN's energy in the neighborhood of the eavesdropper (PJ). Advanced beamforming schemes, such as maximizing receive power (Max-RP) and signal-to-leakage ratio, are developed to optimize this spatial focusing. The result is a significant improvement in both bit-error-rate (BER) at the legitimate receiver and the achievable secrecy rate, especially at medium-to-high SNR regions.

The performance of AN-aided systems is critically governed by **power allocation strategies** between the information-bearing signal and the AN. This is not a static parameter but one that must be dynamically optimized based on system state. For instance, [217] proposes an alternating iterative structure to jointly optimize beamforming vectors and the power allocation factor, rapidly converging to a near-optimal secrecy rate. In massive MIMO systems with hardware constraints, such as those employing **low-resolution Digital-to-Analog Converters (DACs)**, the power allocation problem becomes more complex. As analyzed in [218], the presence of quantization noise alters the optimal operating point. A closed-form SNR threshold can determine whether low-resolution or high-resolution DACs are preferable for secrecy, and the optimal power allocation factor is derived. Interestingly, when AN is generated randomly (as opposed to in the null-space), the negative impact of low-resolution DAC quantization noise can be compensated for by reducing the AN power, leaving the secrecy rate largely unaffected.

**Friendly Jamming (FJ)** extends the AN concept by employing dedicated cooperative nodes, or even the legitimate transceivers themselves, to generate jamming signals. This is particularly useful when the primary transmitter lacks sufficient spatial degrees of freedom for effective AN projection. In **full-duplex (FD)** systems, a legitimate receiver can simultaneously receive information and transmit jamming signals to confound nearby eavesdroppers, as studied in [219]. This Rx-based FJ (RxFJ) complements Tx-based FJ to eliminate "vulnerability regions" around the receiver. However, the benefits of FD jamming must be weighed against the power costs of jamming and self-interference cancellation, as examined in [220], which finds that the secrecy energy efficiency gain is often marginal unless self-interference is efficiently mitigated.

FJ is also pivotal in **covert communication**, where the goal is to hide the very existence of a transmission. Works like [221] and [222] demonstrate that a friendly jammer can create uncertainty in the adversary's detection metric, allowing for a positive covert communication rate. The optimal jamming strategy, especially with multiple antennas, involves a careful trade-off: beamforming jamming power to maximize interference at the warden while minimizing leakage to the legitimate receiver. When the jammer lacks channel knowledge, an isotropic transmission or transmission in the null-space of the legitimate channel may be optimal.

Furthermore, AN and FJ techniques are being adapted for emerging systems and technologies. In **Visible Light Communication (VLC)**, the design must account for LED clipping distortion. [223] proposes an AN transmission scheme that divides LED chips within a luminaire to separately handle the information signal and AN, mitigating clipping effects and improving secrecy performance. For **reconfigurable intelligent surface (RIS)**-assisted systems, [73] derives optimal power allocation between the transmitter and a friendly jammer to minimize the secrecy outage probability, showing significant gains over equal power allocation.

Finally, the role of AN is not limited to the data transmission phase. Research in [224] shows that injecting AN during the **channel training phase** can prevent an eavesdropper from acquiring accurate CSI, which can be more efficient for secrecy than using AN only in the data phase, especially when the channel coherence time is large. This underscores the holistic view required for system design, where security considerations permeate all stages of communication.

In summary, AN generation and FJ are versatile and powerful tools for physical layer security. Their effectiveness hinges on sophisticated signal design (NSP, constructive interference, directional modulation), careful optimization of power and spatial resources, and adaptation to practical imperfections in CSI and hardware. As wireless systems for industrial applications grow in complexity and density, these techniques will remain essential for ensuring robust and efficient secure communications.

**Table: Comparison of approaches in 3.1 Artificial Noise Generation and Friendly Jamming**

| Technique / Method | Core Principle / Design | Key Findings / Advantages | Reference |
| :--- | :--- | :--- | :--- |
| Null-Space Projection (NSP) AN | AN is transmitted in the orthogonal complement of the legitimate channel's subspace to avoid interference at the intended receiver. | Performance highly dependent on CSI quality. Under imperfect CSI, optimal power allocation between signal and AN depends on the objective (minimizing SOP vs. maximizing secrecy rate). | [213] |
| Constructive Interference-based AN | AN beamformers are designed to be constructive to the intended receiver's signal detection while remaining disruptive to eavesdroppers. | Part of the AN power contributes positively to the legitimate user's SINR, reducing total transmit power required for target secrecy performance or SER. | [214] |
| AN with Directional Modulation (Secure Precise Wireless Transmission & Precise Jamming) | Combines DM, random subcarrier selection (RSS), phase alignment (PA), and amplitude beamforming to focus confidential message energy at the desired receiver and AN energy near the eavesdropper. | Advanced beamforming schemes (e.g., Max-RP, signal-to-leakage ratio) optimize spatial focusing, significantly improving BER at the legitimate receiver and achievable secrecy rate, especially at medium-to-high SNR. | [215], [216] |
| Power Allocation Optimization (e.g., in Directional Modulation Networks) | Jointly optimizes beamforming vectors and the power allocation factor between the information signal and AN via an alternating iterative structure. | Rapidly converges to a near-optimal secrecy rate, showing much better performance than NSP-based PA, especially with a small number of transmit antennas. | [217] |
| AN with Low-Resolution DACs in Massive MIMO | Analyzes secure transmission with AN in massive MIMO systems employing low-resolution DACs, deriving optimal power allocation. | A closed-form SNR threshold determines DAC preference. For random AN (not null-space), the negative impact of quantization noise can be compensated by reducing AN power, leaving the secrecy rate largely unaffected. | [218] |
| Friendly Jamming (FJ) with Full-Duplex Receivers | Legitimate receiver uses full-duplex capability to simultaneously receive information and transmit jamming signals to confound nearby eavesdroppers (Rx-based FJ). | Complements Tx-based FJ to eliminate "vulnerability regions" around the receiver. Benefits must be weighed against the power costs of jamming and self-interference cancellation. | [219], [220] |
| FJ for Covert Communication | A friendly jammer creates uncertainty in the adversary's detection metric to hide the existence of a transmission. | Enables a positive covert communication rate. Optimal jamming strategy involves a trade-off: beamforming jamming to maximize interference at the warden while minimizing leakage to the legitimate receiver. | [221], [222] |
| AN Design for Visible Light Communication (VLC) | AN design accounts for LED clipping distortion. A scheme divides LED chips within a luminaire to separately handle the information signal and AN. | Mitigates clipping effects and improves secrecy performance compared to traditional approaches. | [223] |
| FJ in RIS-assisted Systems | Derives optimal power allocation between the transmitter and a friendly jammer to minimize the secrecy outage probability in RIS-assisted secure communication. | Shows significant gains over equal power allocation. | [73] |
| AN in Channel Training Phase | Injecting AN during the channel training phase prevents an eavesdropper from acquiring accurate CSI. | Can be more efficient for secrecy than using AN only in the data phase, especially when the channel coherence time is large. | [224] |


### 3.2 Secure Beamforming and Directional Modulation

Beamforming techniques explicitly designed for security, particularly Directional Modulation (DM) and its advanced variants, represent a paradigm shift from merely managing interference to actively sculpting the physical signal for confidentiality. The core principle is to exploit the spatial degrees of freedom offered by antenna arrays to create a secure transmission zone. In conventional DM, the transmitter designs its beamforming vector such that the constellation of the confidential message (CM) is correctly and coherently received only along a specific physical direction corresponding to the legitimate receiver (Bob) [75]. For receivers located at other angles, the signal constellation appears distorted, leading to a high symbol error rate (SER) at the eavesdropper (Eve) without requiring precise knowledge of Eve's channel state information (CSI) [225]. This is achieved by manipulating the amplitude and phase across antenna elements to ensure the received signal vector at Bob's location aligns with the intended symbol phase.

The security of basic DM, which relies solely on angular discrimination, can be compromised if an eavesdropper is located within the main beam directed at Bob. To address this, the integration of Artificial Noise (AN) is fundamental. The transmitted signal becomes a composite of the beamformed CM and AN, which is projected onto directions orthogonal to Bob's channel or, more aggressively, towards suspected eavesdropper locations. The design of the CM beamforming vector and the AN projection matrix is therefore a joint optimization problem critical to maximizing the secrecy rate (SR). Common design criteria include maximizing the signal-to-leakage-and-noise ratio (Max-SLNR) for the CM and maximizing the AN-to-leakage-and-noise ratio (Max-ANLNR) to focus interference on Eve [226]. Alternatively, the null-space projection (NSP) method projects AN onto the null space of Bob's channel, ensuring it does not interfere with the legitimate link while degrading Eve's reception [227]. More sophisticated generalized AN schemes, where noise can be injected even in the direction of the message under certain conditions, have been shown to outperform traditional orthogonal AN, especially when the legitimate channel is weaker than the eavesdropper's [228].

To achieve security that is robust against eavesdropper mobility and location uncertainty, the concept of Secure Precise Wireless Transmission (SPWT) or Secure Precise Jamming and Communication (SPJC) has emerged. This advanced paradigm aims to confine the CM's energy to a precise two- or three-dimensional region (angle and range) around Bob, while simultaneously focusing AN onto a region around Eve. A key enabler is the Random Frequency Diverse Array (RFDA), where different carrier frequencies are assigned to different antenna elements. This creates a range-dependent beam pattern, moving beyond the angle-only focus of conventional phased arrays. When combined with DM and AN, RFDA enables two-dimensional secure transmission, significantly enhancing the ergodic secrecy capacity compared to one-dimensional schemes [229]. The "precise jamming" aspect is realized by making the AN's energy peak specifically at Eve's suspected location, severely degrading her interception capability [215].

Further refinement is achieved through techniques like Random Subcarrier Selection (RSS) in OFDM-based systems. In schemes such as RSCS-OFDM-DM, subcarriers are randomly assigned across antennas according to specific sets (e.g., quadratic or prime number indices). This randomization, followed by a block interleaving procedure, ensures that within a single OFDM symbol, the receive power of the CM forms a single, sharp peak only at Bob's precise location. Outside this small neighborhood, the received signal is weak and heavily corrupted by AN, achieving SPWT in a per-symbol instantaneous sense rather than just a long-term statistical average [230] [216]. The phase alignment (PA) constraint is often used to simplify the joint optimization of phase and amplitude, reducing the problem to amplitude beamforming design, with schemes like maximizing receive power (Max-RP) or minimizing transmit power (Min-TP) under PA showing superior bit-error-rate and SR performance [231].

Robustness is a critical concern, as practical systems must contend with estimation errors in direction of arrival (DOA), imperfect CSI, and active attacks. Robust beamforming designs account for these uncertainties. For instance, when only statistical information about eavesdropper locations is available, beamforming can be designed to minimize the spatial secrecy outage probability over an exposure region [232]. In the presence of DOA estimation errors, robust methods like main-lobe-integration (MLI) combined with leakage beamforming can be employed. This approach minimizes the CM power leakage from the main lobe of one desired user to the integrated main lobes of other users and all potential eavesdropper directions, without requiring knowledge of the error distribution [233]. Against active eavesdroppers who may spoof pilots to manipulate the transmitter's CSI, countermeasures like the VILLAIN estimator use secret pilots to produce a channel estimate orthogonal to the eavesdropper's channel, enabling beamforming that delivers power to the legitimate receiver while nulling the eavesdropper [234].

The integration of emerging technologies further amplifies the capabilities of secure beamforming. Reconfigurable Intelligent Surfaces (RIS) act as passive beamformers that can create favorable multipath or enhance signal focus. In DM networks, an RIS can be optimized to reflect signals in a way that maximizes the SR, often through alternating optimization algorithms that jointly design the transmit beamforming at the base station and the phase shift matrix at the RIS [235]. Active RIS, which can amplify signals, helps overcome the "double fading" loss of passive RIS and allows for dynamic power allocation between the transmitter and the RIS, leading to significant SR gains [236]. Furthermore, the combination of UAV mobility with DM creates dynamic secure zones. By jointly optimizing the UAV's trajectory, its beamforming vectors, and power allocation between CM and AN, the system can maintain a high secrecy rate throughout the flight, even outperforming fixed half-duplex strategies [237] [238].

In summary, secure beamforming and directional modulation have evolved from simple directional transmission to sophisticated techniques for SPWT. By jointly designing CM beamforming and AN projection using criteria like Max-SLNR, NSP, or leakage, and by incorporating RFDA, RSS, and PA, these methods can focus energy with high precision. Their robustness is ensured through designs that account for estimation errors and active attacks, while their performance is significantly boosted by integration with RIS and UAVs. This makes them a potent suite of physical-layer security solutions for industrial applications requiring high-confidence, location-aware secure wireless links.

**Table: Comparison of approaches in 3.2 Secure Beamforming and Directional Modulation**

| Method/Model | Core Idea/Mechanism | Key Components/Techniques | Security Metric(s) | Reference(s) |
|---|---|---|---|---|
| Conventional Directional Modulation (DM) | Exploits spatial degrees of freedom to distort signal constellation for receivers outside a specific direction. | Antenna array beamforming, phase and amplitude manipulation. | Symbol Error Rate (SER) at eavesdropper. | [225], [75] |
| DM with Artificial Noise (AN) | Augments DM with AN projected orthogonally to the legitimate channel or towards eavesdroppers to degrade interception. | Joint optimization of CM beamforming and AN projection (e.g., NSP, Max-SLNR, Max-ANLNR). | Secrecy Rate (SR). | [226], [227], [228] |
| Secure Precise Wireless Transmission (SPWT) / Secure Precise Jamming and Communication (SPJC) | Confines CM energy to a precise 2D/3D region around Bob and focuses AN onto a region around Eve using range-angle dependent beams. | Random Frequency Diverse Array (RFDA), Directional Modulation, AN, Phase Alignment (PA). | Ergodic Secrecy Capacity, Bit-Error-Rate (BER), Secrecy Rate (SR). | [229], [215] |
| Random Subcarrier Selection (RSS) based SPWT (e.g., RSCS-OFDM-DM) | Achieves per-symbol instantaneous SPWT by randomizing subcarrier assignment across antennas to create a single sharp receive power peak only at Bob's location. | OFDM, Random Subcarrier Selection (RSS), block interleaving, AN projection, Phase Alignment. | Receive Signal-to-Interference-and-Noise Ratio (SINR), Average Secrecy Rate. | [230], [216] |
| Robust Beamforming against Imperfect CSI/DOA | Designs beamformers to maintain security despite estimation errors in Direction of Arrival (DOA) or imperfect Channel State Information (CSI). | Main-Lobe-Integration (MLI) based leakage beamforming, statistical error models, worst-case optimization. | Secrecy Outage Probability, Secrecy Sum-Rate. | [232], [233] |
| Active Eavesdropper Mitigation (e.g., VILLAIN) | Uses secret pilots to produce a channel estimate orthogonal to an active eavesdropper's channel, nulling the eavesdropper. | Secret pilot sequences, orthogonal channel estimation. | Signal power delivered to legitimate receiver vs. eavesdropper. | [234] |
| DM integrated with Reconfigurable Intelligent Surface (RIS) | Uses RIS to create favorable multipath or enhance signal focus, jointly optimized with transmit beamforming to maximize SR. | Alternating optimization of transmit beamforming and RIS phase shift matrix. | Secrecy Rate (SR). | [235], [236] |
| DM integrated with Unmanned Aerial Vehicle (UAV) | Leverages UAV mobility to create dynamic secure zones; jointly optimizes trajectory, beamforming, and power allocation. | Joint optimization of UAV trajectory, beamforming vectors, power allocation between CM and AN. | Secrecy Rate (SR). | [237], [238] |


### 3.3 Modulation, Coding, and Waveform Design for Security

Beyond antenna-level beamforming and resource allocation, the fundamental design of the transmitted signal itself—its modulation, coding structure, and waveform—offers a potent dimension for enhancing physical layer security. These techniques aim to intrinsically obfuscate the signal from unintended receivers, introduce controlled interference, or exploit the practical limitations of coding to degrade an eavesdropper's decoding capability without relying on precise channel state information (CSI) of the eavesdropper.

Spatial Modulation (SM) and its secure variants represent a paradigm where security is embedded into the transmission scheme's core principle. In conventional SM, information is conveyed through both the index of the active transmit antenna and the modulated symbol, offering inherent energy efficiency and reduced hardware complexity. This spatial dimension can be leveraged for security by making the antenna index pattern unpredictable or by integrating it with other security mechanisms. For instance, pseudo-random phase precoding applied to SM (PRPP-SM) significantly increases the diversity order and complicates signal recovery for an eavesdropper lacking the precoder knowledge, achieving substantial bit error rate (BER) gains over standard SM [239]. Secure SM systems often combine antenna selection (TAS), artificial noise (AN) projection, and optimized power allocation to maximize the secrecy rate. At the receiver, the joint detection of the antenna index and the symbol is critical; deep neural network (DNN)-based joint detectors have been proposed to approach the performance of optimal maximum likelihood (ML) detection with far lower complexity, making secure SM practical for real-time systems [240]. Furthermore, SM can be hybridized with other techniques like coordinate interleaved orthogonal design (CIOD-IM) to exploit diversity gain while using index modulation for improved spectral efficiency, where a specially designed AN matrix degrades the eavesdropper's performance without affecting the legitimate receiver [241]. The integration of SM with OFDM, particularly in optical wireless communications (OWC), has been shown to be a strong candidate for future systems, with time-domain SM (TD-SM) outperforming frequency-domain SM (FD-SM) when using an optimal detector [242].

The concept of Waveform-Defined Security (WDS) presents a fundamentally different, low-cost framework that moves beyond traditional assumptions of channel advantage. WDS does not depend on the eavesdropper having a worse channel or lacking CSI. Instead, it operates by intentionally designing or selecting waveform parameters to manipulate signal features in a way that confuses an eavesdropper's classification and detection algorithms. The core idea is to weaken feature diversity and enhance similarity between different signal formats, leading an eavesdropper to misidentify the transmission mode. Subsequent processing, such as demodulation and decoding, will then fail even if brute-force detection is attempted. This approach is particularly suitable for resource-constrained systems, as it can be integrated into existing standards like IEEE 802.11a with minimal added complexity. Key factors for a robust WDS framework include the training data features, oversampling factor, and bandwidth compression factor offset [106]. Relatedly, the use of non-orthogonal multi-carrier waveforms (e.g., SEFDM) combined with index modulation creates a natural defence due to the sophisticated detection required. By scaling the number of non-orthogonally packed sub-carriers or tuning waveform parameters to enhance feature similarity, the detection complexity for an eavesdropper is dramatically increased, preventing successful interception [243] [244].

The transition from infinite to finite blocklength (FBL) coding is a critical consideration for modern low-latency industrial applications, such as ultra-reliable low-latency communications (URLLC) and massive machine-type communications (mMTC). In the FBL regime, the classical secrecy capacity metric is no longer attainable, and new performance metrics like secrecy throughput, effective throughput, and average information leakage (AIL) must be analyzed. The finite length introduces a fundamental trade-off: shorter packets reduce latency but increase the probability of decoding errors at both the legitimate receiver and the eavesdropper, impacting reliability and secrecy simultaneously. Research shows that under a given secrecy outage probability constraint, there exists an optimal blocklength that maximizes the secrecy throughput [245] [246]. Furthermore, increasing transmission power or blocklength can benefit both reliability and secrecy under well-designed transmission policies [162]. The FBL analysis also necessitates new wiretap coding models that use practical linear error-correcting codes combined with hash functions for privacy amplification, providing finite-length semantic secrecy guarantees as demonstrated in secure RF satellite link designs [247]. The impact of FBL is also studied in conjunction with deception technology, where non-orthogonal multiplexing in the FBL regime can enhance security by actively deceiving the eavesdropper [248].

These signal design strategies are highly complementary to system-level techniques. For example, secure waveform design can be integrated with AN injection in MIMO-OFDM systems. Here, transmit filters or temporal/spatial AN can be designed to destroy the orthogonality of the eavesdropper's signals while preserving the legitimate link's quality [249] [250]. Similarly, in directional modulation (DM) schemes, the combination of random subcarrier selection (RSCS) with OFDM and AN projection enables secure and precise wireless transmission, concentrating signal power only in a small region around the intended receiver [216]. The choice of modulation constellation itself is also a degree of freedom; optimizing non-uniform constellations and pre-scaling coefficients based on bit-interleaved coded modulation (BICM) capacity can yield significant performance gains without requiring CSI feedback [251].

In summary, modulation, coding, and waveform design provide a foundational layer for security that is agile and integrable. Secure SM embeds secrecy into the spatial signaling dimension, WDS exploits signal feature obfuscation, and FBL coding analysis addresses the practical constraints of modern industrial traffic. These techniques collectively enhance the resilience of the physical layer by increasing the cost and complexity of successful eavesdropping, making them vital components in the layered security architecture for future industrial wireless networks.

**Table: Comparison of approaches in 3.3 Modulation, Coding, and Waveform Design for Security**

| Method Category | Core Idea / Mechanism | Key Advantages / Features | Reference(s) |
| :--- | :--- | :--- | :--- |
| Secure Spatial Modulation (SM) | Embeds security into the transmission scheme by using the index of the active transmit antenna to convey information, combined with techniques like pseudo-random phase precoding, antenna selection, artificial noise, and optimized power allocation. | Inherent energy efficiency, reduced hardware complexity, increased diversity order, complicates eavesdropper signal recovery, enables high secrecy rates with joint detection (e.g., DNN-based). | [239], [240], [241], [242] |
| Waveform-Defined Security (WDS) | Designs or selects waveform parameters to manipulate signal features, confusing an eavesdropper's classification/detection algorithms by weakening feature diversity and enhancing similarity between formats. | Low-cost, does not rely on channel advantage or eavesdropper CSI, compatible with existing standards (e.g., IEEE 802.11a), increases eavesdropper detection complexity and error rate. | [106], [243], [244] |
| Finite Blocklength (FBL) Coding & Analysis | Addresses security in low-latency applications by analyzing performance with short packets, using metrics like secrecy throughput and average information leakage, and designing practical wiretap codes. | Addresses practical constraints of URLLC/mMTC, reveals optimal blocklength for secrecy, uses practical codes and hash functions for finite-length semantic secrecy. | [245], [246], [162], [247], [248] |
| Complementary System-Level Integration | Combines secure signal design with system-level techniques like artificial noise injection, directional modulation, and optimized modulation constellations in MIMO-OFDM and other systems. | Destroys eavesdropper signal orthogonality while preserving legitimate link quality, enables secure precise wireless transmission, yields performance gains without CSI feedback. | [249], [250], [216], [251] |


### 3.4 Anti-Jamming Signal Processing and Receiver Design

Active jamming attacks, which aim to disrupt legitimate communications by injecting high-power interference, pose a severe threat to the reliability and availability of industrial wireless systems. Countering these attacks requires sophisticated signal processing at the receiver and, increasingly, proactive strategies that turn the jammer's aggression into an advantage. This subsection explores key techniques in anti-jamming signal processing and receiver design, ranging from spatial filtering and subspace methods to novel deception and modulation schemes.

A foundational approach leverages the spatial degrees of freedom offered by Multiple-Input Multiple-Output (MIMO) systems. Conventional beamforming can nullify jamming signals if the jammer's spatial signature is known and static. However, smart jammers evade such mitigation by transmitting only during specific instants (e.g., control signals) or by using time-varying beamforming [252]. To address this, advanced joint estimation and detection frameworks have been developed. For instance, the MAED (MitigAtion, Estimation, and Detection) algorithm formulates a unified optimization problem that performs jammer estimation, channel estimation, and data detection simultaneously, exploiting the fact that a jammer cannot alter its spatial subspace within a channel coherence interval [253]. This method proves effective against a wide range of smart jamming attacks without requiring prior knowledge of the attack pattern. Similarly, for scenarios with colored interference, such as when a full-duplex attacker simultaneously jams and eavesdrops, whitening-filter-based receive beamformers like the Whitening-Filter-based Maximum Ratio Combining (WFMRC) are proposed to maximize the signal-to-jamming-plus-noise ratio, offering significant performance gains over conventional methods [254].

A significant challenge in mitigating smart jammers is the initial acquisition of their spatial characteristics. The MASH (Universal MIMO Jammer Mitigation via Secret Temporal Subspace Embeddings) protocol provides an elegant, information-theoretic solution. By having the transmitter and receiver share a common secret, the legitimate signal is embedded into a secret temporal subspace. The reciprocal linear transform applied at the receiver not only retrieves the legitimate signal but also provably transforms any jammer—regardless of its strategy—into an equivalent barrage jammer with a static signature, making its estimation and subsequent spatial filtering straightforward [255]. This "resilient-by-design" philosophy is also evident in frameworks that integrate wireless sensing services. For example, one approach replaces traditional noise covariance estimation with a surrogate model built using sensed Direction-of-Arrival (DoA) information of the jamming signal, which is then used to optimize beamforming and scheduling without assumptions about the jammer's strategy [256].

Beyond spatial filtering, proactive anti-jamming schemes fundamentally rethink the role of the jamming signal. Instead of treating it solely as destructive interference, these strategies exploit it. **Jamming Modulation** is one such active anti-jamming (AAJ) scheme where a transmitter, equipped with a programmable-gain amplifier, re-modulates the received jamming signal itself to convey information. This allows reliable communication even under extremely strong broadband jamming, as the bit error rate can become independent of the jamming-to-noise ratio at high levels [257]. A more radical paradigm shift is seen in deception strategies inspired by the "Borrowing Arrows with Thatched Boats" tactic. Here, the legitimate system transmits "fake" signals to deliberately attract a reactive jammer. Once the jammer attacks, its powerful signal is harvested for energy or used as a carrier for ambient backscatter communications. An IoT device can backscatter its data onto the jamming signal, meaning that higher jamming power can paradoxically lead to better communication performance for the legitimate system [258]. This concept is extended in frameworks like DeepFake, which uses deep reinforcement learning (DRL) to optimally decide when to deploy such deception, effectively leveraging the jammer's power [259].

Machine learning, particularly deep learning, is becoming integral to both jamming mitigation and the design of intelligent jammers, creating an adversarial AI landscape. Deep learning classifiers can be used by a jammer to predict and target successful transmissions with high efficiency [260]. In response, defenders employ DRL to learn optimal anti-jamming policies. For example, DRL agents can be trained to select transmission parameters that maximize throughput under jamming, with architectures like the deep dueling network enabling faster convergence than traditional Q-learning [261]. Furthermore, deep learning is applied directly at the receiver for tasks like jamming cancellation. Convolutional Neural Networks (CNNs) can be used to infer the existence, number, and parameters of interfering signals, enabling a cancellation block that operates agnostically of the underlying communication modulation [262].

The integration of new technologies like Reconfigurable Intelligent Surfaces (RIS) and full-duplex radios further enriches the anti-jamming toolkit. A STAR-RIS can assist a full-duplex legitimate receiver in directing jamming signals precisely toward an eavesdropper while simultaneously canceling self-interference, thereby enhancing secrecy [40]. Conversely, RIS can also be weaponized as a "green jammer," reflecting ambient signals to create destructive interference at a legitimate receiver without consuming any active power [263]. For reliable low-latency communication, cooperative schemes using delay-aware full-duplex relays have been proposed. These helpers forward the victim's message within strict latency constraints while using residual power to keep the jammer engaged on a decoy frequency, thus evading the attack [264].

In summary, modern anti-jamming signal processing has evolved from passive spatial nulling to a dynamic, intelligent, and often proactive discipline. The convergence of advanced MIMO processing, subspace techniques, cross-layer deception strategies, ambient backscatter, and machine learning provides a multi-faceted defense-in-depth approach. These techniques are crucial for ensuring the ultra-reliable and resilient communications required in adversarial industrial environments, where jamming can cripple critical control and sensing functions. The ongoing co-evolution of jamming attacks and defense mechanisms underscores the need for continuous innovation in this domain.

**Table: Comparison of approaches in 3.4 Anti-Jamming Signal Processing and Receiver Design**

| Method/Technique Name | Core Idea | Key Mechanism/Algorithm | Reference |
| :--- | :--- | :--- | :--- |
| MAED (MitigAtion, Estimation, and Detection) | Jointly estimates jammer, channel, and data to mitigate smart jammers that evade conventional nulling. | Formulates a unified optimization problem for simultaneous jammer estimation, channel estimation, and data detection. | [253] |
| Whitening-Filter-based Maximum Ratio Combining (WFMRC) | Maximizes signal-to-jamming-plus-noise ratio under colored interference from a full-duplex attacker. | Applies a whitening filter to the received signal before MRC to handle colored jamming-plus-noise. | [254] |
| MASH (Universal MIMO Jammer Mitigation via Secret Temporal Subspace Embeddings) | Transforms any jammer into an equivalent barrage jammer with a static signature for easy mitigation. | Uses a shared secret to embed the legitimate signal into a secret temporal subspace via a linear transform. | [255] |
| Resilient-By-Design Framework with Sensing | Replaces noise covariance estimation with a surrogate model using sensed DoA information of the jammer. | Integrates wireless sensing (e.g., jamming signal DoA) to optimize beamforming and scheduling without prior jammer strategy. | [256] |
| Jamming Modulation | Actively re-modulates the received jamming signal itself to convey information. | Uses a programmable-gain amplifier at the transmitter to modulate information onto the intercepted jamming signal. | [257] |
| "Borrowing Arrows with Thatched Boats" Deception | Transmits fake signals to attract a reactive jammer, then harvests its energy or uses its signal for backscatter. | Uses deliberate deception (fake transmissions) to trigger jamming, then leverages the jamming signal for energy harvesting or ambient backscatter communication. | [258] |
| DeepFake (Deep Dueling-based Deception) | Uses deep reinforcement learning to optimally decide when to deploy deception strategies against reactive jammers. | Employs a Deep Dueling Neural Network architecture within a DRL agent to learn optimal deception policies. | [259] |
| Deep Learning for Jamming Mitigation & Attack | Employs deep learning for both launching efficient jamming attacks and defending against them. | Attack: Uses a deep learning classifier to predict and jam successful transmissions. Defense: Uses DRL for optimal anti-jamming policy. | [260] |
| "Jam Me If You Can" with Deep Dueling DRL | Uses a deep dueling neural network architecture for fast convergence to optimal anti-jamming transmission policies. | DRL agent selects transmission parameters to maximize throughput, augmented with ambient backscattering. | [261] |
| Convolutional Interference Cancellation Network (CICN) | Uses a CNN to infer interference parameters for agnostic jamming cancellation at the receiver. | A CNN architecture detects jamming existence, number, and parameters to drive a cancellation block. | [262] |
| STAR-RIS-Assisted Full-Duplex Jamming | Uses a STAR-RIS to direct jamming signals toward an eavesdropper while canceling self-interference at a full-duplex receiver. | Jointly optimizes FD beamforming vectors and STAR-RIS coefficients to concentrate jamming on the eavesdropper. | [40] |
| IRS-based "Green Jammer" | Uses an IRS as a passive jammer to create destructive interference at a legitimate receiver without active power. | Optimizes IRS reflection coefficients to destructively combine direct and reflected signals at the target receiver. | [263] |
| Low-Latency Communication with Delay-Aware Relays | Uses a cooperative, delay-aware full-duplex relay to forward victim messages while engaging the jammer on a decoy frequency. | The helper node splits power to forward the victim's message within latency constraints and keep the jammer engaged on a different band. | [264] |


### 3.5 AI/ML-Driven Secure Signal Design and Optimization

The integration of Artificial Intelligence and Machine Learning (AI/ML) into the physical layer represents a paradigm shift from model-based optimization to data-driven, adaptive, and intelligent secure communication systems. This approach is particularly potent for addressing the high-dimensional, non-convex, and dynamic optimization problems inherent in modern PLS, especially in complex environments like those involving Reconfigurable Intelligent Surfaces (RIS), dynamic jamming, and end-to-end system design.

A prominent application is the use of **Deep Learning (DL) for joint beamforming and RIS configuration**. Optimizing the transmit precoding at a base station alongside the phase shifts of hundreds of RIS elements to maximize secrecy rates is a computationally intensive, non-convex problem. Traditional alternating optimization (AO) methods often involve iterative algorithms with high complexity. DL offers a compelling alternative by learning a direct mapping from channel state information (or other system parameters) to near-optimal beamforming vectors and phase shift matrices. For instance, a deep neural network can be trained to minimize the secrecy outage probability in an IRS-assisted MIMOME system, achieving performance comparable to conventional AO algorithms but with significantly reduced online computational complexity [265]. Similarly, DL techniques have been developed to tune IRS reflections in real-time to create a channel advantage for a legitimate receiver, maximizing the secrecy rate with lower complexity than conventional approaches [266]. Beyond standard DL, meta-learning techniques like Gradient-based Manifold Meta Learning (GMML) have been introduced to enhance robustness and adaptability across diverse communication environments without extensive pre-training, feeding gradients of the optimization variables into neural networks for efficient learning [267]. For RIS with low-resolution (e.g., 1-bit) elements, specialized Deep Reinforcement Learning (DRL) agents that efficiently explore the binary action space have been shown to effectively configure large-scale surfaces [268].

**Reinforcement Learning (RL) and Deep RL (DRL)** excel in environments requiring sequential decision-making under uncertainty, making them ideal for **adaptive anti-jamming and secure resource allocation**. Instead of relying on pre-defined jamming models, DRL agents can learn optimal transmission policies by interacting with the wireless environment. For example, DRL agents can be trained to select channels, adjust power, and modulate signals to maximize throughput under proactive jamming attacks, eliminating the need for explicit jamming pattern recognition [269]. In RIS-aided systems, DRL can jointly optimize user selection, channel allocation, modulation-coding schemes, and RIS configuration to resist jamming by learning only from changes in user data rates, without requiring explicit CSI of the jammer [270]. Furthermore, advanced DRL architectures like the deep dueling network have been employed to rapidly learn and counteract reactive jamming strategies, enabling transmitters to make decisions thousands of times faster than conventional Q-learning, and even leverage jamming signals for backscatter communication or energy harvesting [261] [259]. To defend against adversarial attacks on the RL agents themselves, frameworks like the Meta-Learned Advantage Hierarchy (MLAH) have been proposed, which use a meta-learner to detect the presence of an adversary and switch between nominal and robust sub-policies, maintaining performance even under state-information attacks [271] [272].

The concept of **end-to-end learning via autoencoders** provides a radical departure from traditional modular transceiver design. Here, the transmitter (encoder) and receiver (decoder) are represented as deep neural networks and trained jointly as an autoencoder to minimize a loss function such as symbol error rate, effectively learning optimal constellations and waveforms tailored to the channel. This approach inherently optimizes for security when the channel model includes an eavesdropper. For RIS-aided systems, this can be extended to a tripartite design where the RIS beam selection is also modeled as a DNN, jointly trained with the transmitter and receiver autoencoder. This co-design has been shown to achieve superior error performance compared to schemes where the RIS is optimized separately [273]. This data-driven method can also optimize waveforms under practical hardware constraints, such as minimizing out-of-band emissions under nonlinear power amplifier effects, leading to more spectrally efficient and secure communications [274].

However, the reliance on ML models introduces a new attack surface: **adversarial machine learning**. ML-based signal classifiers, such as those for Automatic Modulation Classification (AMC), are highly vulnerable to adversarial examples—carefully crafted perturbations that cause misclassification. Studies have shown that adversarial attacks can significantly degrade the performance of deep learning-based AMC, posing a severe threat to RFML systems [275] [276]. These attacks can be white-box (with full knowledge of the model) or black-box, and importantly, adversarial examples often transfer between different models. Attacks must also be realistic in the wireless domain, considering channel effects; channel-aware adversarial perturbations can be designed to fool classifiers at specific receivers, while broadcast attacks aim to fool multiple receivers simultaneously [277]. Defending against these threats is an active area of research. Proposed defenses include **adversarial training**, where the classifier is retrained on a mixture of clean and adversarial samples to improve robustness [278]. Other strategies involve designing classifiers that are inherently more robust, such as using **frequency-domain features** instead of time-domain IQ samples, as attacks crafted for one domain may not transfer well to the other [279]. **Randomized smoothing**, which augments training with noise, can also provide certified robustness guarantees [277]. Furthermore, system-level defenses can be employed, such as a fusion architecture that combines a DL-based classifier with an adversarial example detector and a traditional ML model, leveraging the low transferability of attacks between different model types to maintain robust performance [280].

In summary, AI/ML-driven signal design offers powerful tools for adaptive, complex, and efficient PLS optimization, from configuring smart radio environments with RIS to learning optimal anti-jamming policies and end-to-end secure waveforms. Yet, this power comes with the critical responsibility of securing the ML models themselves against a new class of adversarial threats, necessitating a co-evolution of AI-driven security and security for AI within the wireless physical layer.

**Table: Comparison of approaches in 3.5 AI/ML-Driven Secure Signal Design and Optimization**

| Method/Model Category | Key Idea/Application | Key Techniques/Algorithms | Reference |
| :--- | :--- | :--- | :--- |
| Deep Learning (DL) for Joint Beamforming and RIS Configuration | Uses DL to learn a direct mapping from CSI to near-optimal beamforming vectors and RIS phase shifts, minimizing secrecy outage probability with lower online complexity than conventional AO. | Deep Neural Networks (DNNs) | [265] |
| Meta-Learning for RIS-aided Communications | Enhances robustness and adaptability across diverse environments without extensive pre-training by feeding gradients of optimization variables into neural networks. | Gradient-based Manifold Meta Learning (GMML) | [267] |
| Deep Reinforcement Learning (DRL) for RIS with Low-Resolution Elements | Configures large-scale RIS with 1-bit phase resolution elements by efficiently exploring the binary action space. | Deep Reinforcement Learning (DRL), Deep Q-Network (DQN), Deep Deterministic Policy Gradient (DDPG) variants | [268] |
| Deep Reinforcement Learning (DRL) for Adaptive Anti-Jamming | Learns optimal transmission policies (channel selection, power adjustment) by interacting with the environment to maximize throughput under proactive jamming, without needing explicit jamming pattern recognition. | Deep Reinforcement Learning (DRL), Deep Q-Network (DQN) variants | [269] |
| DRL for Joint Resource Allocation in RIS-aided Anti-Jamming | Jointly optimizes user selection, channel allocation, modulation-coding, and RIS configuration to resist jamming by learning only from changes in user data rates, without requiring eavesdropper CSI. | Deep Reinforcement Learning (DRL), Twin Delayed Deep Deterministic Policy Gradient (TD3) | [270] |
| Advanced DRL Architectures for Countering Reactive Jamming | Uses deep dueling network architectures to rapidly learn and counteract reactive jamming strategies, enabling faster decisions than Q-learning and leveraging jamming signals for backscatter/energy harvesting. | Deep Dueling Neural Network Architecture | [261] [259] |
| Meta-Learning for Defending RL Agents Against Adversaries | Uses a meta-learner (MLAH) to detect adversaries and switch between nominal and robust sub-policies to maintain performance under state-information attacks on the RL agent. | Meta-Learned Advantage Hierarchy (MLAH) | [271] [272] |
| End-to-End Learning via Autoencoders for RIS-aided Systems | Models transmitter, receiver, and RIS beam selection as DNNs trained jointly as an autoencoder to minimize symbol error rate, learning optimal constellations and waveforms tailored to the channel. | Autoencoder, Deep Neural Networks (DNNs) | [273] |
| End-to-End Waveform Learning under Hardware Constraints | Uses ML to jointly learn transmit waveform and receiver to minimize out-of-band emissions under nonlinear power amplifier effects, leading to spectrally efficient communications. | Machine Learning (End-to-end learning) | [274] |
| Adversarial Attacks on DL-based Signal Classifiers | Crafting small perturbations (adversarial examples) to cause misclassification in DL-based Automatic Modulation Classification (AMC) systems. | White-box and Black-box Adversarial Attacks (e.g., Carlini-Wagner, FGSM) | [275] [276] |
| Channel-Aware and Broadcast Adversarial Attacks | Designs adversarial perturbations considering channel effects to fool specific receivers or craft a common perturbation to fool multiple receivers simultaneously. | Channel-Aware Adversarial Attacks, Broadcast Adversarial Attacks | [277] |
| Defense: Adversarial Training | Retraining the classifier on a mixture of clean and adversarial samples to improve robustness against attacks. | Adversarial Training | [278] |
| Defense: Frequency-Domain Features | Using frequency-domain features instead of time-domain IQ samples for AMC, as attacks crafted for one domain may not transfer well. | Frequency-domain feature extraction | [279] |
| Defense: Randomized Smoothing | Augmenting training data with noise to provide certified robustness guarantees against adversarial perturbations. | Randomized Smoothing | [277] |
| Defense: Fusion Architecture with Adversarial Detector | Combines a DL-based classifier with an adversarial example detector and a traditional ML model to leverage low attack transferability for robust performance. | Fusion Architecture, Local Intrinsic Dimensionality (LID) based detector | [280] |


## 4 Key Generation, Authentication, and Cryptographic Integration

This section focuses on establishing and managing security credentials at the physical layer. It details methods for secret key generation from Channel State Information (CSI) and hardware fingerprints (e.g., RF-PUFs). It covers physical-layer authentication techniques and explores the integration of these PLS mechanisms with lightweight and post-quantum cryptographic protocols for hybrid, end-to-end security architectures suitable for Industrial IoT.

### 4.1 Secret Key Generation from Physical Layer Characteristics

The generation of secret keys directly from the physical characteristics of the wireless channel or the underlying hardware offers a paradigm shift for secure communications in industrial settings. This approach moves away from the complex logistics of pre-shared key distribution and storage, leveraging inherent, device-specific randomness to establish cryptographic material on-demand. Two primary methodologies dominate this domain: exploiting the reciprocity and randomness of the wireless channel and harnessing manufacturing variations in silicon through Physical Unclonable Functions (PUFs).

Channel State Information (CSI)-based key generation capitalizes on the principle that the wireless channel between two legitimate parties, Alice and Bob, is reciprocal and uniquely time-varying within a local spatial area. The core process involves three canonical steps: advantage distillation, information reconciliation, and privacy amplification. Initially, during advantage distillation, both parties independently measure the channel's impulse response or frequency-selective fading coefficients—collectively termed CSI—over the same time interval and frequency band. These measurements are reciprocal but noisy. To extract a shared bit sequence, quantization is applied. Simple multi-level quantization or adaptive schemes like the equal-probability quantizer convert analog CSI measurements into initial bit sequences. However, due to noise and non-simultaneous measurements, Alice's and Bob's bit sequences will have mismatches. Information reconciliation, such as using the Cascade protocol as demonstrated in [110], is then employed to correct these discrepancies over a public channel, resulting in identical bit strings at both ends. The final and crucial step is privacy amplification, where a cryptographic hash function is applied to the reconciled bits to distill a shorter, uniformly random secret key, eliminating any partial information that may have been leaked to an eavesdropper, Eve, whose observations are decorrelated if she is more than half a wavelength away [110]. A significant challenge in slowly varying industrial environments is the low entropy of the channel. To address this, techniques like deliberate device shaking to induce artificial randomness [110] or the use of Reconfigurable Intelligent Surfaces (RIS) to dynamically alter the propagation environment [281] have been proposed to boost the key generation rate. Furthermore, advanced signal processing, such as using a Kalman filter to detrend CSI measurements and isolate the unpredictable small-scale fading component from deterministic large-scale fading, is essential for maximizing the achievable secret bit rate [282].

Complementing channel-based methods, hardware-intrinsic key generation via Physical Unclonable Functions provides a robust, static fingerprint derived from uncontrollable microscopic variations introduced during semiconductor manufacturing. A PUF is a physical structure that, when queried with a challenge, produces a response that is unique to each instance, reproducible under similar conditions, but unpredictable and unclonable [283]. For key generation, weak PUFs, which have a limited number of Challenge-Response Pairs (CRPs), are typically used. Common silicon PUF implementations include SRAM PUFs, which exploit the random power-up state of static memory cells [284]; Ring Oscillator (RO) PUFs, which compare frequencies of identically laid-out oscillators [285]; and emerging memory technologies like Resistive RAM (ReRAM) PUFs, which utilize the stochastic switching behavior of memristive devices [286]. The raw PUF response is noisy, affected by temperature, voltage fluctuations, and aging, as noted in [287]. Therefore, a fuzzy extractor is employed to reliably reproduce a stable cryptographic key. A fuzzy extractor consists of a secure sketch (for error correction) and an entropy extractor (for randomness distillation). During enrollment, a reference PUF response `R` is measured, and a helper data `P` (the secure sketch) is generated and stored publicly. The key `K` is derived from `R` using the entropy extractor. Later, during reconstruction, a noisy measurement `R'` is combined with the helper data `P` to recover the original `R` and subsequently the same key `K`. Error-correcting codes like BCH, Polar, or convolutional codes are central to this process [288][289]. To reduce the overhead of error correction, innovative techniques such as enrolling Multiple Reference Responses (MRR) under different operating conditions have been proposed, bringing the operational point closer to a reference and minimizing the required error correction capability [290]. Furthermore, modeling the PUF's physical behavior allows for the intelligent selection of challenges that yield error-free responses across environmental variations, potentially bypassing the need for complex on-chip error correction logic [291].

The security of PUF-based systems is paramount. Strong PUFs, used for authentication, are vulnerable to machine learning (ML) modeling attacks where an adversary uses collected CRPs to build a digital clone. Significant research is dedicated to designing ML-resilient PUFs. Defenses include structural obfuscation, such as introducing non-linearities via XOR networks or creating cyclic PUF circuits to expand the output behavior space [292], and protocol-level countermeasures like challenge obfuscation through random set-based XOR operations [293]. The intersection of AI and PUF security is bidirectional: while ML poses a threat, it also offers solutions, such as using deep learning models to authenticate noisy PUF responses directly based on a "PUF-Phenotype," acting as an alternative to traditional error correction [294]. For industrial IoT applications, the appeal of PUFs lies in their lightweight nature. They enable secure key generation and device authentication without the need for secure, non-volatile key storage, which is often costly or absent in resource-constrained sensors and actuators. Protocols like TREVERSE leverage a simulated PUF model on a trusted server to enable lightweight authentication for a prover device [295]. Moreover, the ability to generate a shared key across multiple devices using configurable PUF structures opens the door for lightweight group key establishment in industrial networks [296].

In summary, secret key generation from physical layer characteristics provides a foundational security mechanism tailored for dynamic and constrained industrial environments. CSI-based methods offer a decentralized and ephemeral key agreement solution leveraging the wireless medium's natural randomness, while PUF-based methods provide a hardware-rooted, persistent identity for authentication and key storage. The ongoing integration of advanced signal processing, innovative coding schemes, and machine learning is crucial to enhancing the reliability, security, and practicality of these physical-layer security primitives for the demanding landscape of Industry 4.0 and beyond.

**Table: Comparison of approaches in 4.1 Secret Key Generation from Physical Layer Characteristics**

| Method | Core Principle | Key Steps / Components | Primary Challenges & Solutions | Security Considerations | Reference |
|---|---|---|---|---|---|
| CSI-based Key Generation | Exploits reciprocity and time-varying randomness of the wireless channel between legitimate parties. | 1. Advantage Distillation (CSI measurement & quantization).<br>2. Information Reconciliation (e.g., Cascade protocol).<br>3. Privacy Amplification (cryptographic hash). | **Challenge**: Low entropy in static/slowly varying environments.<br>**Solutions**: Artificial randomness induction (device shaking), use of Reconfigurable Intelligent Surfaces (RIS), advanced signal processing (e.g., Kalman filter detrending). | Eavesdropper's observations are decorrelated if >0.5 wavelength away. Privacy amplification eliminates leaked partial information. | [110], [281], [282] |
| PUF-based Key Generation (Weak PUFs) | Harnesses uncontrollable manufacturing variations in silicon to create a static, device-unique fingerprint. | 1. PUF Enrollment (measure reference response `R`, generate helper data `P`).<br>2. Key Reconstruction (use noisy `R'` and `P` via fuzzy extractor to recover key `K`).<br>3. Error Correction (using BCH, Polar, Convolutional codes). | **Challenge**: Noisy responses due to environmental variations (temperature, voltage, aging).<br>**Solutions**: Fuzzy extractors, enrolling Multiple Reference Responses (MRR), model-based challenge selection for error-free responses. | Raw PUF response is noisy; helper data is public but must not leak secrecy. Fuzzy extractor provides reliability and randomness. | [283], [290], [291], [288], [289] |
| PUF-based Authentication (Strong PUFs) | Uses a large set of Challenge-Response Pairs (CRPs) for device authentication. | 1. CRP-based protocol.<br>2. Defense mechanisms against modeling attacks (e.g., structural obfuscation, challenge obfuscation).<br>3. Machine Learning for authentication (PUF-Phenotype). | **Challenge**: Vulnerable to Machine Learning (ML) modeling attacks.<br>**Solutions**: Non-linear/cyclic circuits (e.g., XOR networks, CycPUF), protocol-level obfuscation (e.g., Set-based Obfuscation), ML-based authentication models. | ML poses a dual threat (modeling attacks) and solution (noise-resilient authentication). Security relies on the unpredictability and unclonability of the physical structure. | [292], [293], [294] |


### 4.2 Physical-Layer Authentication and Device Identification

Physical-layer authentication (PLA) and device identification represent a paradigm shift from traditional cryptographic methods by exploiting the inherent, hard-to-forge characteristics of the wireless transmission medium and hardware itself. This approach is particularly vital for the Industrial Internet of Things (IIoT), where resource-constrained devices, heterogeneous deployments, and the critical nature of operations render conventional key-based authentication inadequate or vulnerable. PLA techniques primarily bifurcate into two complementary categories: Radio Frequency (RF) Fingerprinting, which leverages unique hardware imperfections, and Channel-based Authentication, which utilizes the location-specific and context-specific properties of the propagation environment. Together, they enable lightweight, continuous, and robust verification of devices and messages without relying solely on pre-shared secrets.

**Radio Frequency Fingerprinting (RFF)** is founded on the principle that minute manufacturing variations in analog radio components (e.g., power amplifiers, oscillators, mixers) impart a distinctive, device-specific signature onto every transmitted signal, akin to a physical unclonable function (PUF) for wireless transmitters. This signature, or RF fingerprint, is theoretically immutable and extremely difficult for an adversary to replicate perfectly. Early RFF approaches relied on handcrafted feature extraction from signals, such as transient onset characteristics, carrier frequency offset (CFO), I/Q imbalance, or spectral features. For instance, the RF-Distinct Native Attribute (RF-DNA) fingerprinting method uses statistical features of instantaneous amplitude, phase, and frequency responses for classification, often paired with traditional machine learning classifiers like Support Vector Machines (SVM), achieving high accuracy in controlled settings [297]. However, the performance of these traditional methods can degrade under low signal-to-noise ratios (SNR) and dynamic channel conditions.

The advent of deep learning (DL) has revolutionized RFF, enabling end-to-end learning of complex, high-dimensional features directly from raw in-phase and quadrature (I/Q) samples or transformed signal representations like spectrograms. Convolutional Neural Networks (CNNs) are particularly effective at capturing spatial patterns in time-frequency representations, as demonstrated in work on LoRa device identification using spectrograms, which achieved high classification accuracy by capturing fine-grained hardware impairments [298]. Recurrent architectures like Long Short-Term Memory (LSTM) networks are also employed to model temporal dependencies in signal sequences. The core promise of DL-based RFF is its ability to achieve exceptional discrimination among large populations of devices, even those that are nominally identical, making it a powerful tool for device-specific authentication in massive IoT deployments [16].

Despite its promise, RFF faces significant practical challenges that must be addressed for real-world industrial deployment. A primary issue is **domain portability and generalization**. A model trained on data collected with a specific receiver, under particular channel conditions, on a given day, often suffers severe performance degradation when tested on data from a different domain (e.g., a different receiver, location, or time). This is because the learned features can become entangled with domain-specific artifacts like receiver hardware biases or static channel effects, rather than purely device-specific impairments [299]. This "Day-After-Tomorrow" (DAT) effect is a critical bottleneck, attributed not only to channel variability but also to device power-cycling, which can cause subtle shifts in hardware operating points [300]. To combat this, researchers are developing more robust feature representations and learning frameworks. Techniques include designing domain-invariant features like the Double-Sided Envelope Power Spectrum (EPS) [301], employing disentangled representation learning to separate device-relevant from device-irrelevant (channel) components [302], and using semi-supervised or unsupervised learning with consistency regularization to leverage abundant unlabeled data from new domains [303]. Furthermore, federated learning frameworks with model transfer and adaptation (MTA) are proposed to enable collaborative, privacy-preserving model training across different edge locations while adapting to local channel conditions [304].

Another critical challenge is **robustness against adversarial attacks**. As deep learning models become the core authenticator, they inherit vulnerabilities to adversarial examples. An adversary can craft subtle perturbations to transmitted signals that cause the authenticator to misclassify a rogue device as legitimate. White-box attacks using methods like the Fast Gradient Sign Method (FGSM) and Projected Gradient Descent (PGD) have been shown to successfully fool CNN and LSTM-based RFF classifiers [305]. Even more concerning are black-box attacks where an impersonator, using only feedback on authentication success/failure, can use reinforcement learning to iteratively distort its signal and penetrate the system [306]. These threats necessitate the development of adversarial training, defensive distillation, and signal preprocessing techniques to harden RFF systems.

**Channel-based Authentication** complements RFF by exploiting the unique spatial and temporal properties of the wireless channel between a specific transmitter and receiver pair. The core premise is that the channel state information (CSI) or received signal strength (RSS) is location-specific and difficult for an attacker not colocated with the legitimate device to replicate. This method is highly effective for detecting spoofing and man-in-the-middle attacks, as an attacker at a different physical location will exhibit a different channel fingerprint. Traditional hypothesis testing frameworks compare recent channel estimates with a stored profile of the legitimate channel. However, the random and time-varying nature of wireless channels is a major obstacle, causing high false alarm and missed detection rates.

To enhance reliability, advanced signal processing and machine learning techniques are employed. One approach uses **information reconciliation** via distributed source coding (e.g., Slepian-Wolf coding using polar codes) to correct mismatches between channel measurements taken at different times, followed by hypothesis testing on the reconciled vectors, significantly improving performance in low-SNR scenarios [307]. For on-body IoT devices, where authentication must be resilient to user motion, adversarial learning frameworks have been proposed. These frameworks use multi-player neural networks to disentangle the underlying radio propagation pattern (e.g., on-body vs. off-body) from motion-induced variances, enabling accurate authentication even during dynamic activities [308] [309]. In RFID backscatter systems, channel non-reciprocity can be exploited as a fingerprint, with the reader performing least-squares estimation and binary hypothesis testing to authenticate tags, providing a lightweight solution suitable for passive devices [310].

The ultimate goal for industrial IoT is **continuous and lightweight authentication**. Static, one-time authentication at session initiation is insufficient for long-lived sessions in critical environments. PLA is inherently suited for continuous verification, as every packet transmission provides an opportunity to validate the channel or hardware signature. Lightweight schemes are being designed to minimize computational overhead. For example, one proposed method bypasses repeated key generation and verification by instead checking the consistency of inherent transmission properties like access time slots and spreading sequences, achieving a low false alarm rate with significantly reduced complexity [311]. Furthermore, the concept of a **Device Authentication Code (DAC)** has been introduced, where an autoencoder reconstructs a received signal, and the distribution of the reconstruction error serves as a unique, message-dependent authenticator verifiable via statistical tests, offering resilience against impersonation [312].

Integration of RFF and channel-based methods is a promising research direction to create more robust and multi-factor physical-layer authentication systems. A smart pre-processing scheme can decompose Channel State Information (CSI) into predictable (large-scale, location-based) and unpredictable (small-scale, fading) components. The predictable component can be used for RF fingerprinting and coarse location-based authentication, while the unpredictable component is reserved for secret key generation, enabling joint authentication and key distillation [105]. Similarly, multi-layer fingerprinting frameworks aim to jointly exploit PHY-layer hardware features and upper-layer behavioral traits (e.g., traffic patterns) for improved identification, using multi-view machine learning to cluster shared device information across these layers [313].

In conclusion, physical-layer authentication and device identification offer a foundational and complementary security layer for industrial wireless systems. While RF fingerprinting provides a strong, hardware-bound identity, channel-based methods offer context-aware spoofing detection. The convergence of advanced deep learning, robust feature engineering, and adversarial resilience techniques is actively addressing the core challenges of domain variability, environmental dynamics, and security against sophisticated attacks. As these solutions mature, their integration into lightweight, continuous authentication protocols will be instrumental in securing the vast, heterogeneous, and safety-critical deployments of the Industrial IoT.

**Table: Comparison of approaches in 4.2 Physical-Layer Authentication and Device Identification**

| Method Category | Specific Technique / Model | Key Idea / Contribution | Reference |
| :--- | :--- | :--- | :--- |
| Radio Frequency Fingerprinting (Traditional) | RF-DNA Fingerprinting with SVM | Uses statistical features of instantaneous amplitude, phase, and frequency responses for classification, paired with SVM. | [297] |
| Radio Frequency Fingerprinting (Deep Learning) | Spectrogram and CNN for LoRa | Uses spectrogram to represent fine-grained time-frequency characteristics of LoRa signals and a CNN for classification, with CFO compensation. | [298] |
| Radio Frequency Fingerprinting (Deep Learning) | Double-Sided Envelope Power Spectrum (EPS) | Proposes a novel IQ data representation (EPS) designed to capture hardware impairments while suppressing irrelevant domain information for better domain adaptation. | [301] |
| Radio Frequency Fingerprinting (Deep Learning) | Disentangled Representation (DR) Learning | Uses adversarial learning to factor signals into device-relevant and device-irrelevant components, then shuffles them for implicit data augmentation to avoid overfitting to channel statistics. | [302] |
| Radio Frequency Fingerprinting (Deep Learning) | Semi-Supervised Learning with Consistency Regularization | Leverages deep semi-supervised learning with a composite data augmentation scheme for radio signals, combined with consistency-based regularization and pseudo-labeling. | [303] |
| Radio Frequency Fingerprinting (Federated Learning) | Federated Learning with Model Transfer and Adaptation (MTA) | Implements federated learning for privacy-preserving model training across edge locations, with a novel MTA strategy to adapt models to local channel conditions. | [304] |
| Channel-based Authentication | Information Reconciliation with Polar Codes | Uses distributed source coding (Slepian-Wolf) reconciliation via polar codes to correct mismatches between channel measurements over time, followed by hypothesis testing. | [307] |
| Channel-based Authentication (On-body IoT) | Adversarial Multi-player Neural Network | Uses an adversarial multi-player neural network to disentangle underlying radio propagation patterns (e.g., on-body vs. off-body) from motion-induced variances for authentication. | [308] |
| Channel-based Authentication (RFID) | Exploiting Channel Non-Reciprocity | Exploits the non-reciprocity of the end-to-end channel as a fingerprint for RFID tags, using least-squares estimation and binary hypothesis testing at the reader. | [310] |
| Lightweight Continuous Authentication | Access-based Scheme (Time Slots & Spreading Sequences) | Provides continuous authentication by checking the consistency of inherent transmission properties like access time slots and spreading sequences, avoiding repeated key operations. | [311] |
| Hybrid / Multi-Factor Authentication | Device Authentication Code (DAC) using Autoencoder | Uses an autoencoder to reconstruct a received signal; the distribution of the reconstruction error serves as a unique, message-dependent authenticator verifiable via statistical tests. | [312] |
| Hybrid / Multi-Factor Authentication | Smart CSI Pre-processing for Joint Authentication & Key Distillation | Decomposes CSI into predictable (large-scale) and unpredictable (small-scale) components. The predictable part is used for RF fingerprinting/authentication, the unpredictable part for secret key generation. | [105] |
| Hybrid / Multi-Factor Authentication | Multi-Layer Fingerprinting with Wyner Variational Autoencoder | A multi-view learning framework that jointly exploits PHY-layer hardware features and upper-layer behavioral traits (e.g., traffic patterns) for improved device identification. | [313] |


### 4.3 Integration with Lightweight and Post-Quantum Cryptography

The inherent information-theoretic security of physical layer security (PLS) primitives offers a powerful foundation, but a holistic security architecture for industrial wireless systems often requires their integration with cryptographic protocols. This synergistic approach creates hybrid, robust security frameworks that leverage the strengths of both paradigms: the unconditional security and low computational overhead of PLS for key establishment and authentication, combined with the mature, versatile functionalities of cryptography for encryption, integrity, and non-repudiation. This integration is particularly vital in two critical domains: enabling efficient security for resource-constrained Industrial Internet of Things (IIoT) devices through lightweight cryptography, and facilitating the transition to quantum-resistant security via post-quantum cryptography (PQC).

For IIoT deployments, where devices are severely limited in computational power, energy, and memory, traditional cryptographic suites can be prohibitively expensive. Here, PLS-generated keys serve as an ideal bootstrap mechanism. Techniques such as channel state information (CSI)-based key generation or RF fingerprinting can produce shared secret bits between a sensor and its gateway with minimal processing. These "seed" keys, derived from the unique and random properties of the wireless medium, can then directly feed into lightweight cryptographic (LWC) algorithms designed for such environments. The PLS key generation obviates the need for complex asymmetric key exchange protocols (like Diffie-Hellman), which are computationally intensive and, as noted in the context papers, vulnerable to quantum attacks [314]. The generated symmetric keys can be used for authenticated encryption with associated data (AEAD) using LWC standards, providing confidentiality and integrity for sensor data with minimal overhead. This hybrid model—PLS for key provisioning and LWC for data protection—ensures a practical, energy-efficient security solution that meets the stringent constraints of industrial edge devices. Furthermore, physical unclonable functions (PUFs), which exploit manufacturing variations in hardware to create device-unique fingerprints, provide a robust root of trust. A PUF response can be used to generate or encrypt device-specific cryptographic keys, binding the key material inextricably to the physical device and preventing cloning or software-based key extraction. This PUF-enhanced key storage, combined with PLS-based key agreement, creates a multi-layered, hardware-anchored security foundation for IIoT authentication and secure communication.

The impending threat of cryptographically relevant quantum computers necessitates a migration to PQC. PLS plays a crucial dual role in this transition. First, as a complementary technology, PLS can enhance the practical security and efficiency of PQC systems. Many PQC algorithms, particularly those based on lattices (e.g., CRYSTALS-Kyber, CRYSTALS-Dilithium) or codes, have larger key sizes, ciphertexts, and computational demands than their classical counterparts [315]. PLS can be used to establish high-entropy secret keys for symmetric encryption, reducing the reliance on frequent PQC key exchanges for bulk data encryption. This is exemplified in hybrid approaches proposed for protocols like TLS 1.3, where a combination of classical (or PQC) key encapsulation and symmetric encryption is used [316]. PLS-generated keys could serve as the symmetric component, leveraging information-theoretic security derived from the channel. Second, PLS primitives like PUFs are instrumental in building quantum-safe roots of trust for key storage and device identity, which is a critical challenge in the PQC migration for embedded systems [317]. A PUF-based identity can be used in conjunction with a post-quantum digital signature scheme, ensuring that the signing key is both quantum-resistant and physically bound to the device.

Hash-Based Signatures (HBS), such as SPHINCS⁺, are leading PQC candidates for digital signatures due to their well-understood security based solely on cryptographic hash functions [318]. However, many HBS schemes are stateful or have large signature sizes. PLS can augment HBS frameworks in several ways. The entropy required for the one-time signature keys within an HBS scheme can be sourced from physical randomness, such as channel variations or PUFs, ensuring high-quality randomness that is critical for security. Furthermore, PLS-based authentication (e.g., using RF fingerprinting or CSI) can provide a fast, lightweight first layer of device authentication, triggering the more expensive HBS verification only when necessary, thus optimizing overall system performance. This is especially relevant for industrial systems where devices may need to authenticate frequently. The integration also addresses forward security concerns; while some PQC signature schemes are being adapted for forward security [319], PLS key generation inherently provides fresh key material for each session, contributing to forward secrecy when used in key derivation.

However, the integration path is not without challenges. The reliability of PLS key generation can be affected by slow fading or static environments, leading to low key generation rates. Techniques using reconfigurable intelligent surfaces (RIS) to artificially induce channel variations show promise in addressing this. Standardization of interfaces between PLS key derivation modules and cryptographic protocols is also nascent. Moreover, the security proofs of the integrated hybrid system must be carefully composed, ensuring that the failure of one component (e.g., a computational assumption in PQC) does not catastrophically compromise the entire system. The concept of "cryptographic agility" – the ability to seamlessly update cryptographic algorithms – is paramount [320]. A well-designed architecture would allow the PLS layer to remain constant while the cryptographic algorithm it feeds can be upgraded from a lightweight cipher to a PQC algorithm as the threat landscape evolves.

In conclusion, the integration of PLS with lightweight and post-quantum cryptography represents a pragmatic and powerful strategy for securing industrial wireless communications. By using PLS for efficient, information-theoretically secure key generation and device authentication, and leveraging cryptography for its algorithmic versatility and advanced security properties, this hybrid approach meets the dual demands of resource efficiency and quantum resilience. As the industry progresses towards 6G and the quantum era, such synergistic architectures, underpinned by PUFs and agile cryptographic modules, will be essential for building secure, sustainable, and future-proof industrial networks.

**Table: Comparison of approaches in 4.3 Integration with Lightweight and Post-Quantum Cryptography**

| Method / Approach | Primary Purpose / Advantage | Key Technique / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| PLS + Lightweight Cryptography (LWC) | Enables efficient, energy-saving security for resource-constrained IIoT devices. PLS provides low-overhead key generation, LWC provides data protection. | PLS-based key generation (e.g., CSI, RF fingerprinting) to create seed keys, feeding into lightweight AEAD algorithms. | [39] |
| PLS + Post-Quantum Cryptography (PQC) | Facilitates transition to quantum-resistant security. PLS enhances PQC efficiency and provides a quantum-safe root of trust. | PLS generates high-entropy keys for symmetric encryption, reducing reliance on frequent PQC key exchanges. PUFs provide hardware-anchored key storage. | [317] |
| Hash-Based Signatures (HBS) augmented with PLS | Provides quantum-resistant digital signatures. PLS can optimize performance and ensure high-quality randomness. | PLS sources entropy for one-time signature keys (e.g., from channel variations or PUFs). PLS-based authentication can trigger HBS verification only when needed. | [318] |
| PUF-enhanced key storage | Creates a robust, hardware-anchored root of trust for device identity and key protection, preventing cloning. | Uses manufacturing variations to generate a device-unique fingerprint (PUF response) to encrypt or generate device-specific cryptographic keys. | [39] |
| Hybrid TLS with PLS/PQC | Achieves quantum-secure communication with potential FIPS compliance, balancing security and performance. | Combines PLS-generated symmetric keys or PQC KEM with symmetric encryption in a nested or hybrid TLS 1.3 protocol structure. | [316] |
| Forward-secure post-quantum signatures (e.g., FROG) | Provides compromise resiliency (forward security) for post-quantum digital signatures. | Transforms standard PQC signatures (e.g., Dilithium) into forward-secure settings using methods like the MMM construction. | [319] |


### 4.4 Advanced Authentication Protocols and System Architectures

Advanced authentication protocols and system architectures represent a paradigm shift from using physical layer security (PLS) primitives in isolation to integrating them into holistic, end-to-end secure communication frameworks. These designs aim to provide robust mutual authentication, forward secrecy, and resilience against sophisticated attacks, moving beyond the passive exploitation of the wireless environment to its active and intelligent control. A cornerstone of this approach is the construction of complete authentication and key agreement protocols that leverage the unique properties of Physical Unclonable Functions (PUFs) and Secret Key Generation (SKG). For instance, a lightweight authentication protocol can be built upon a novel Linear Feedback Shift Register-based Arbiter PUF (LFSR-APUF) [321]. This design obfuscates the linear challenge-response mapping to resist modeling attacks, and when integrated into a full protocol with dynamic obfuscation and a device-bound "Cover" function, it ensures mutual authentication and protects against spoofing and physical attacks. Similarly, the concept of a PUF Phenotype—a noise-tolerant, structure-agnostic representation of a PUF's identity—enables protocols like PhenoAuth, which provides mutual authentication and forward secrecy for IoT device-to-device communication without the need for complex error correction [322]. For delay-constrained industrial applications, such as haptics or V2X, protocols that combine PUF authentication with SKG are proposed. These can feature zero-round-trip-time (0-RTT) resumption for fast re-authentication and pipeline the SKG process with encrypted data transfer to minimize latency [323]. The fusion of keys from multiple imperfect sources, such as combining PLS-generated keys with those from lattice-based or quantum cryptography, is another architectural advancement. This key-fusing framework dramatically reduces the secret outage probability, enhancing resilience against key exposure and paving a practical path toward information-theoretic security [324].

A revolutionary architectural concept that decouples security from the vagaries of the wireless channel is Graph Layer Security (GLS). Traditional PLS relies on the reciprocity and randomness of the wireless channel state information (CSI), which can be estimated by an eavesdropper and is vulnerable in static environments. GLS proposes an alternative by exploiting the common, channel-irrelevant physical dynamics of a networked infrastructure shared between legitimate IoT devices—such as signal-flows in a common water distribution network or power grid [325]. The dependency among sensor readings across the network graph is characterized using tools like Graph Fourier Transform (GFT) to generate cipher keys. This method is inherently resistant to wireless eavesdroppers who lack access to the physical process dynamics. A federated multi-agent deep reinforcement learning-assisted scheme (FD2K) has been proposed to achieve distributed key generation in this GLS paradigm, demonstrating considerable key agreement rates and randomness by exploiting common features of the physical dynamics [326]. This approach is particularly promising for securing cyber-physical systems and digital twins in adversarial radio environments.

The integration of Reconfigurable Intelligent Surfaces (RIS) introduces an active, programmable dimension to PLS system architecture, transforming the wireless environment from a static given into a dynamically controllable security parameter. RIS can be strategically deployed to enhance the entropy and reciprocity of the channel for SKG in otherwise static or low-randomness industrial settings. By intelligently altering its reflection patterns, an RIS can create artificial channel randomness. Experimental results show that an RIS can enhance secret key entropy, achieving a key generation rate 15-fold higher than without RIS in a static indoor environment [327]. Advanced protocols involve the joint optimization of transmit precoding at a base station and the phase shift matrix at the RIS to maximize the secret key rate by fully extracting randomness from the cascaded channel [88]. Beyond key generation, RIS can be integral to physical-layer authentication (PLA) systems. An RIS-assisted PLA system allows a legitimate transmitter to customize channel fingerprints by controlling the ON-OFF state of the RIS, thereby improving spoofing detection performance significantly, as validated by prototype experiments [328]. This capability to manipulate the propagation environment also opens novel attack vectors, necessitating advanced defensive architectures. For example, a malicious RIS can perform a manipulating attack (RISM) to destroy channel reciprocity during the SKG probing phase [329]. Countermeasures employ adversarial learning frameworks, where legitimate parties use Generative Adversarial Networks (GANs) to learn a common feature space that has minimal mutual information overlap with an eavesdropper controlling a malicious RIS [330].

These advanced protocols and architectures signify a maturation of PLS from theoretical constructs and isolated techniques to practical, system-level security solutions. They combine the information-theoretic strengths of the physical layer with modern cryptographic principles and intelligent control of the wireless medium. By designing protocols that ensure mutual authentication and forward secrecy using PUFs and SKG, pioneering new paradigms like GLS that leverage shared physical dynamics, and actively engineering the channel with RIS for enhanced security, these approaches address the stringent latency, complexity, and robustness requirements of future industrial wireless systems, including 6G networks and the Industrial Internet of Things.

**Table: Comparison of approaches in 4.4 Advanced Authentication Protocols and System Architectures**

| Category | Method / Protocol / Concept | Core Idea / Mechanism | Key Benefits / Claims | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **PUF-based Authentication** | Lightweight Authentication Protocol based on LFSR-APUF | Uses a Linear Feedback Shift Register-based Arbiter PUF (LFSR-APUF) to obfuscate the linear challenge-response mapping. Integrated with a dynamic obfuscation scheme and a device-bound "Cover" function. | Resists modeling attacks; ensures mutual authentication; protects against spoofing and physical attacks. | [321] |
| **PUF-based Authentication** | PhenoAuth Protocol | Uses a PUF Phenotype—a noise-tolerant, structure-agnostic representation of a PUF's identity—for authentication. | Provides mutual authentication and forward secrecy for IoT device-to-device communication without complex error correction. | [322] |
| **Integrated PUF/SKG for Latency** | Authenticated Secret Key Generation for Delay-Constrained Systems | Combines PUF authentication with Secret Key Generation (SKG). Features 0-RTT resumption for fast re-authentication and pipelines SKG with encrypted data transfer. | Minimizes latency for delay-constrained applications (e.g., haptics, V2X); reduces computational overhead. | [323] |
| **Key Fusion Architecture** | Key-Fusing Framework | Fuses keys from multiple imperfect sources (e.g., PLS-generated keys with lattice-based or quantum cryptography keys). | Dramatically reduces secret outage probability; enhances resilience against key exposure; paves a practical path toward information-theoretic security. | [324] |
| **New Security Paradigm** | Graph Layer Security (GLS) | Exploits common, channel-irrelevant physical dynamics of a networked infrastructure (e.g., signal-flows in utility networks) shared between legitimate IoT devices. Uses Graph Fourier Transform (GFT) to generate cipher keys. | Inherently resistant to wireless eavesdroppers who lack access to the physical process dynamics; secures cyber-physical systems in adversarial radio environments. | [325] |
| **GLS Implementation** | Federated Multi-Agent Deep RL-assisted Distributed Key Generation (FD2K) | A federated multi-agent deep reinforcement learning scheme to achieve distributed key generation in the GLS paradigm by exploiting common features of physical dynamics. | Achieves considerable key agreement rates and randomness for securing IoT communication. | [326] |
| **RIS for SKG Enhancement** | RIS-assisted Secret Key Generation | Deploys Reconfigurable Intelligent Surfaces (RIS) to create artificial channel randomness by altering reflection patterns, enhancing entropy and reciprocity in static/low-randomness environments. | Experimental results show a key generation rate 15-fold higher than without RIS in a static indoor environment. | [327] |
| **RIS for SKG Optimization** | Joint Precoding and Phase Shift Design for RIS-assisted SKG | Jointly optimizes transmit precoding at a base station and the phase shift matrix at the RIS to maximize the secret key rate by fully extracting randomness from the cascaded channel. | Significantly improves the secret key rate compared to existing protocols. | [88] |
| **RIS for Authentication** | RIS-assisted Physical-Layer Authentication (PLA) | Allows a legitimate transmitter to customize channel fingerprints by controlling the ON-OFF state of an RIS, improving spoofing detection performance. | Prototype experiments validate significant improvements in spoofing detection performance. | [328] |
| **RIS Attack & Defense** | Countermeasures against RIS Manipulating (RISM) Attack | Addresses a malicious RIS attack that destroys channel reciprocity during SKG probing. Employs an adversarial learning framework where legitimate parties use GANs to learn a common feature space with minimal mutual information overlap with an eavesdropper. | Proposed GAN-based and symbolic-based PL-SKG schemes achieve high key agreement rates and are resistant to MITM-RIS eavesdroppers. | [330] |


## 5 Enhancing Security with Advanced and Emerging Technologies

This section explores how modern wireless technologies and paradigms are harnessed to augment PLS capabilities. Key topics include the role of Reconfigurable Intelligent Surfaces (RIS), the application of Non-Orthogonal Multiple Access (NOMA), and the inherent security properties and challenges of Visible Light Communication (VLC) and Terahertz (THz) communications in industrial settings.

### 5.1 Reconfigurable Intelligent Surfaces (RIS) for Secure Beamforming and Environment Control

Reconfigurable Intelligent Surfaces (RISs) have emerged as a transformative technology for physical layer security (PLS), offering an unprecedented ability to programmatically shape and control the wireless propagation environment. By deploying a planar array of low-cost, passive, and nearly passive reflecting elements, each capable of inducing a controllable phase shift (and potentially amplitude change) on an impinging electromagnetic wave, RISs can create favorable signal conditions for legitimate receivers while degrading the channel quality for potential eavesdroppers. This capability moves beyond traditional security paradigms that rely solely on endpoint signal processing, introducing the wireless channel itself as a dynamic, optimizable entity for enhancing secrecy.

The foundational application of RIS in PLS is **secure beamforming and environment control**. The core objective is to jointly optimize the active beamforming (precoding) at the transmitter and the passive beamforming (phase shifts) at the RIS to maximize the secrecy rate—the rate at which information can be transmitted reliably to the intended receiver while remaining confidential from an eavesdropper. This typically involves formulating a non-convex optimization problem where the RIS phase shifts are subject to unit-modulus constraints (if purely passive). Advanced algorithms, such as alternating optimization (AO), semidefinite relaxation (SDR), majorization-minimization (MM), and successive convex approximation (SCA), are employed to find efficient solutions [331] [332]. For instance, an AO framework can decouple the problem, iteratively solving for the transmit beamformer with fixed RIS coefficients and then optimizing the RIS configuration given the beamformer.

A significant limitation of conventional **passive RIS** is the "double fading" effect, where the signal traverses the transmitter-RIS and RIS-receiver links, suffering path loss twice. This can severely limit the achievable secrecy gain, especially when the direct link is weak [333]. To overcome this, **active RIS** architectures have been proposed. Unlike passive elements that only reflect signals, active RIS elements integrate reflection-type amplifiers, allowing them to not only adjust the phase but also amplify the reflected signal. This active amplification can effectively counteract the double-fading attenuation, leading to substantially higher secrecy rates for a given power budget [334] [82]. However, active RISs introduce new challenges, including managing the RIS's own power consumption, dealing with amplified thermal noise, and designing robust beamforming under these new constraints [335].

A major evolution beyond traditional reflective-only RIS is the **Simultaneously Transmitting and Reflecting RIS (STAR-RIS)**. A STAR-RIS can partition its elements to simultaneously serve users located on both sides of the surface, providing full 360° coverage. This is particularly valuable for industrial settings where devices may be scattered around obstacles or on opposite sides of a wall. From a security perspective, STAR-RIS introduces new degrees of freedom but also new challenges, such as managing mutual interference between users on the transmission and reflection sides and addressing the unique "full-space mutual eavesdropping" threat [336] [337]. Protocols like Energy Splitting (ES) and Mode Switching (MS) govern how each element divides its energy between transmission and reflection, requiring sophisticated joint optimization of the partition strategy, phase shifts, and transmit beamforming [338] [40].

The practical deployment and optimization of RIS for security are fraught with challenges. **Channel State Information (CSI) acquisition** is paramount, as optimal beamforming requires knowledge of the cascaded channels through the RIS. Estimating these high-dimensional channels with low overhead is critical. Two-timescale protocols that optimize long-term RIS configurations based on statistical CSI and short-term power allocation based on instantaneous effective channels have been proposed to reduce pilot overhead [338] [339]. Furthermore, **hardware imperfections (HWIs)** at both the transceiver and the RIS, such as phase noise, amplitude errors, and non-linearities, can severely degrade theoretical performance. Robust beamforming designs that account for these impairments and imperfect CSI are essential for real-world systems [340] [341].

Another critical consideration is **electromagnetic interference (EMI)**. An RIS, while manipulating intended signals, can also unintentionally reflect and focus ambient EMI from the surrounding environment toward the receiver, degrading the signal-to-interference-plus-noise ratio (SINR). Proactive EMI cancellation schemes that exploit the time-domain structure of interference and design RIS phase shifts to nullify it are necessary to harness the full potential of RIS [342] [343].

Finally, **deployment strategy**—the physical placement and configuration of the RIS—is a key system design parameter that significantly impacts secrecy performance. The optimal location balances the path losses of the BS-RIS and RIS-user links. Joint optimization of the RIS location and its passive beamforming has been shown to achieve higher secrecy rates compared to heuristic placement near the source or destination [344]. Moreover, concepts like **double-RIS or cooperative RIS** systems can provide additional spatial diversity and degrees of freedom, further enhancing reliability and secrecy, though at the cost of increased optimization and estimation complexity [345] [346].

In conclusion, RIS technology provides a powerful and flexible toolkit for enhancing PLS in industrial wireless networks. By progressing from passive to active and STAR-RIS architectures, and by developing robust algorithms to tackle practical challenges like CSI acquisition, HWIs, and EMI, RIS-enabled smart radio environments promise to be a cornerstone for securing the demanding and dynamic communications of future smart factories and critical infrastructure.

**Table: Comparison of approaches in 5.1 Reconfigurable Intelligent Surfaces (RIS) for Secure Beamforming and Environment Control**

| Aspect | Passive RIS | Active RIS | STAR-RIS |
| :--- | :--- | :--- | :--- |
| **Core Function** | Reflects signals with controllable phase shift (and potentially amplitude). | Reflects and amplifies signals using integrated reflection-type amplifiers. | Simultaneously transmits and reflects signals, providing 360° coverage. |
| **Key Advantage for PLS** | Creates favorable signal conditions for legitimate receivers while degrading channel for eavesdroppers via beamforming. | Counters the "double fading" effect, leading to substantially higher secrecy rates for a given power budget. | Serves users on both sides of the surface, valuable for complex industrial settings with scattered devices. |
| **Main Limitation/Challenge** | Suffers from "double fading" effect, limiting secrecy gain, especially with a weak direct link. | Introduces own power consumption, amplified thermal noise, and requires robust beamforming under new constraints. | Introduces challenges like managing mutual interference between sides and addressing "full-space mutual eavesdropping." |
| **Typical Optimization Algorithms** | Alternating optimization (AO), semidefinite relaxation (SDR), majorization-minimization (MM), successive convex approximation (SCA). | Algorithms to manage joint optimization of transmit beamforming and RIS reflection/amplification matrix under power and noise constraints. | Joint optimization of partition strategy (ES/MS), phase shifts, and transmit beamforming, often using AO, SDR, MM, or SCA. |
| **Key Reference(s)** | [331] | [334], [82], [335] | [332], [336], [337], [338], [40] |


### 5.2 Non-Orthogonal Multiple Access (NOMA) for Secrecy Rate Optimization

Non-Orthogonal Multiple Access (NOMA) has emerged as a cornerstone technology for enhancing spectral efficiency in 5G and beyond networks by allowing multiple users to share the same time-frequency resource block through superposition coding at the transmitter and successive interference cancellation (SIC) at the receiver [347]. Beyond its spectral gains, NOMA presents unique opportunities and challenges for physical layer security (PLS). The inherent structure of superimposed signals can be strategically engineered to enhance secrecy, particularly against external eavesdroppers and, more critically, internal threats from untrusted users within the NOMA cluster. This subsection delves into the core principles of leveraging NOMA for secrecy rate optimization, covering power allocation strategies, the handling of untrusted users, and the synergistic integration with Reconfigurable Intelligent Surfaces (RIS).

The fundamental mechanism for secrecy in NOMA lies in the intelligent management of inter-user interference. In a downlink scenario with two users—a strong user (near user) and a weak user (far user)—the base station superimposes their signals with different power levels. The weak user, experiencing a poorer channel, is typically allocated more power to ensure its message can be decoded by treating the strong user's signal as noise. The strong user, with a better channel, first decodes and subtracts the weak user's signal via SIC before decoding its own. From a secrecy perspective, this structure can be advantageous. The message intended for the weak user is broadcast at high power, making it relatively easy for an eavesdropper to intercept. However, the strong user's message is embedded within a signal where it appears as a lower-power component beneath the dominant weak user's signal. This superposition can act as a form of interference, obscuring the strong user's confidential data from an eavesdropper with a channel quality inferior to that of the strong legitimate user [348]. The core optimization problem, therefore, involves allocating power between users to maximize a secrecy metric, such as the secrecy sum rate (SSR) or the individual secrecy rate, while satisfying quality of service (QoS) constraints for all legitimate users [349]. Research has derived closed-form expressions for optimal power allocation policies that maximize the SSR, demonstrating that NOMA can achieve a significant secrecy rate improvement over conventional Orthogonal Multiple Access (OMA) by effectively utilizing the power domain [349].

A critical and more challenging scenario arises when NOMA users are *untrusted*, meaning each user is a potential eavesdropper for the other's message. This is a realistic model for many industrial IoT applications where devices may not be fully trusted. In such cases, the standard SIC decoding order creates a inherent security vulnerability: the strong user must decode the weak user's message to perform SIC, thereby having full access to it. To address this, researchers have investigated secure decoding orders and power allocation schemes that can ensure a positive secrecy rate for both users. This involves a delicate balance where the power allocation must be constrained such that a user can decode the interference (for SIC) but cannot achieve a rate for the other user's message that exceeds its own channel capacity to decode its intended message, thereby ensuring confidentiality [92]. Analytical expressions for secrecy outage probability (SOP) under imperfect SIC conditions have been derived for downlink untrusted NOMA systems, providing crucial insights into the fundamental limits of secure communication in such adversarial environments [93][350]. Furthermore, fairness-aware designs aim to maximize the minimum secrecy rate between untrusted users or minimize the maximum SOP, ensuring equitable security performance across the network [97].

The integration of NOMA with Reconfigurable Intelligent Surfaces (RIS) unlocks a new dimension for secrecy enhancement. An RIS, with its array of tunable passive elements, can dynamically shape the wireless propagation environment. When combined with NOMA, the RIS can be optimized to create highly favorable channel conditions for legitimate users while degrading the channel towards potential eavesdroppers. The interplay between NOMA and RIS configuration is nuanced. RIS configurations can be static (fixed phase shifts for a transmission block) or dynamic (phase shifts can change multiple times within a block). From an information-theoretic perspective, the dynamic RIS configuration is capacity-achieving for RIS-aided single-antenna NOMA networks, as it can adapt to the superimposed signal structure in real-time [351]. The primary role of the RIS in secure NOMA is to enhance the disparity between the channel gains of legitimate users and eavesdroppers. By carefully optimizing the phase shifts, the RIS can strengthen the channel of the weak NOMA user, ensuring successful SIC at the strong user and improving the overall signal-to-interference-plus-noise ratio (SINR) for both. Simultaneously, it can create destructive interference at the location of an eavesdropper. For scenarios with both internal (untrusted near user) and external eavesdroppers, joint beamforming and power allocation schemes have been proposed. These schemes may incorporate artificial noise (AN) beamforming via the RIS to jam eavesdroppers without affecting legitimate receivers, significantly improving the system's secrecy performance [352]. Recent advancements also consider active RIS (ARIS) elements, which include amplification, to overcome the "double path-loss" attenuation of passive RIS and have shown superior SOP performance compared to passive RIS-assisted NOMA or OMA systems [89].

The performance gains of NOMA for PLS are evident when compared to OMA. Analytical and simulation results consistently show that NOMA can achieve a higher secrecy sum rate, lower secrecy outage probability, and better energy efficiency under a wide range of conditions [353][354]. This superiority is particularly pronounced in scenarios requiring massive connectivity and low latency, such as in IoT networks. For short-packet communications—essential for ultra-reliable low-latency communications (URLLC) in industry—NOMA has been shown to achieve a higher effective throughput than OMA under the same finite blocklength constraint, or to meet the same throughput target with lower latency [355][356]. However, the benefits are contingent on careful system design. User pairing is a critical factor; pairing users with highly divergent channel gains typically yields greater NOMA gains. Furthermore, the derived "NOMA dominant condition" specifies when NOMA is guaranteed to provide spectral efficiency gains over OMA for each individual user in a cluster, which directly informs secure user selection strategies [347]. In conclusion, NOMA serves as a powerful framework for PLS, transforming multiuser interference from a liability into a tool for secrecy. Through optimized power allocation, innovative decoding strategies for untrusted scenarios, and synergistic integration with RIS, NOMA-based systems can provide robust, spectrally-efficient secure communications tailored for the demanding environments of future industrial networks.

**Table: Comparison of approaches in 5.2 Non-Orthogonal Multiple Access (NOMA) for Secrecy Rate Optimization**

| Aspect | Method 1: Power Allocation for Secrecy Rate Optimization | Method 2: Secure Decoding for Untrusted Users | Method 3: RIS-NOMA Integration for Secrecy Enhancement |
| :--- | :--- | :--- | :--- |
| **Core Idea** | Allocate power between NOMA users to maximize a secrecy metric (e.g., Secrecy Sum Rate) while satisfying QoS constraints. The inherent interference from superposition coding can obscure confidential data from eavesdroppers. | Design secure decoding orders and constrained power allocation to ensure positive secrecy rates for all users within a NOMA cluster where each user is a potential eavesdropper for the others. | Use a Reconfigurable Intelligent Surface (RIS) to dynamically shape the wireless environment, enhancing the channel for legitimate NOMA users and degrading it for eavesdroppers, often combined with beamforming and artificial noise. |
| **Key Techniques** | Optimal power allocation policies, closed-form expressions for Secrecy Sum Rate (SSR) maximization, QoS-aware power allocation bounds. | Secure SIC decoding order strategies, power allocation constraints to limit inter-user eavesdropping, minimization of maximum secrecy outage probability (SOP) for fairness. | Joint optimization of RIS phase shifts, beamforming, and power allocation; use of active RIS (ARIS) to overcome double path-loss; artificial noise (AN) beamforming via RIS. |
| **Primary Security Challenge Addressed** | External eavesdroppers and the interception of the strong user's message. | Internal eavesdropping from untrusted users within the same NOMA cluster. | Both external eavesdroppers and internal (untrusted) users, focusing on enhancing the channel gain disparity. |
| **Typical Performance Metrics** | Secrecy Sum Rate (SSR), individual secrecy rate, secrecy outage probability (SOP). | Secrecy outage probability (SOP) (often under imperfect SIC), minimum secrecy rate, fairness (min-max SOP). | Secrecy outage probability (SOP), secrecy system throughput, ergodic secrecy rate. |
| **Key Reference(s)** | [349], [348] | [92], [93], [97] | [351], [352], [89] |


### 5.3 Terahertz (THz) and Visible Light Communication (VLC) for Inherent Security

The exploration of the high-frequency spectrum, encompassing Terahertz (THz) and Visible Light Communication (VLC), presents a paradigm shift for physical layer security (PLS) in industrial settings. These technologies offer inherent physical properties that can be harnessed to create confidential communication channels, but they also introduce unique vulnerabilities that require specialized countermeasures.

**Terahertz (THz) Communications: Exploiting Directivity and Near-Field Phenomena**
THz band communications (0.1-10 THz) are a cornerstone for 6G, promising ultra-high data rates. From a security perspective, the most significant attribute is the inherent high directivity required to overcome severe path loss. This is typically achieved through ultra-massive antenna arrays, creating pencil-thin beams that naturally confine signals in the angular domain, making eavesdropping outside the main lobe challenging [357]. However, this angular security is compromised if an eavesdropper resides within the same beam sector as the legitimate receiver. This scenario, known as the "range security" problem, is particularly critical in industrial environments where devices may be densely packed. Traditional far-field beamforming fails in this case, as it cannot distinguish between users at different distances within the same angular direction. To address this, research is pivoting towards exploiting the near-field region of large antenna arrays. In the near-field, the electromagnetic wavefront is spherical, and the channel gain becomes dependent on both angle and distance. Novel antenna architectures, such as widely-spaced arrays, are being proposed to engineer this spherical wavefront, enabling beamfocusing that can create secure zones at specific locations, thereby providing both angular and range security [357]. This concept of "wavefront engineering," including the use of specialized beams like Bessel or Airy beams, is seen as key to realizing efficient and secure THz links by creating focused spots of high signal strength exclusively at the intended receiver's location [358]. Furthermore, the concept of "absolute security" has been proposed for high-frequency links, leveraging the spatial minima of broadband, high-gain antenna patterns at different frequencies. The union of these nulls across a frequency band can define a physical region where an eavesdropper is guaranteed to fail to decode, regardless of computational power or noise, offering a powerful, physics-based security guarantee [359]. Despite these advantages, THz links are highly susceptible to blockage and intermittent connectivity. Here, Reconfigurable Intelligent Surfaces (RIS) play a dual role: they can provide an alternative non-line-of-sight (NLOS) path to maintain connectivity and can be optimized to enhance PLS. For instance, RIS can be configured to maximize the secrecy spectral efficiency over a geographical area, providing a secure communication zone without needing instantaneous knowledge of the eavesdropper's position [331]. The integration of sensing and communication at THz bands also opens avenues for enhanced situational awareness, allowing the system to dynamically map the environment and adjust secure transmission parameters in real-time [360].

**Visible Light Communication (VLC) / LiFi: Confinement and Controllability**
VLC, and its networked version LiFi, utilize the visible light spectrum (400-800 THz) for data transmission. Its most celebrated inherent security feature is signal confinement; light does not penetrate opaque walls, physically containing the communication within a room. This is often summarized as "What You See Is What You Send" (WYSIWYS) [361]. However, this does not equate to perfect security. Any device within the illuminated area is a potential eavesdropper. The broadcast nature of the downlink from lighting fixtures (LEDs) means all users in the coverage cell receive the same signal. Therefore, PLS techniques are essential to ensure confidentiality among co-located users. The optical channel has unique constraints, such as intensity modulation and direct detection (IM/DD), and strict average and peak optical power limits dictated by illumination requirements and LED nonlinearity. Research has derived closed-form bounds for the secrecy capacity under these constraints, providing fundamental limits for secure VLC system design [362]. To enhance security, techniques like Artificial Noise (AN) are adapted for VLC. However, the clipping distortion introduced when constraining signals to the LED's linear dynamic range must be carefully incorporated into the AN design to avoid degrading the legitimate channel [223]. Innovative hardware-based approaches have also been explored, such as using gold nanoparticle (GNP) plates to manipulate circularly polarized light, creating unique channel fingerprints that can be exploited to increase the secrecy rate around the legitimate receiver [363]. A significant challenge for VLC is its reliance on line-of-sight (LOS), making it vulnerable to blockage. This is where RIS (often termed Intelligent Reflecting Surfaces or IRS in optical contexts) becomes a transformative technology for LiFi. RIS can dynamically reconfigure light paths, mitigating blockages and providing NLOS connectivity [364]. From a security standpoint, RIS can be optimized to perform secure beamforming. By intelligently adjusting the phases of reflected light waves, an RIS can maximize the signal strength at the legitimate receiver while minimizing it at an eavesdropper's location, even when the eavesdropper has a more favorable direct channel [101]. Furthermore, RIS can enable novel jamming schemes. For example, a full-duplex legitimate receiver can transmit jamming signals, with an RIS (including advanced Simultaneous Transmitting and Reflecting RIS - STAR-RIS) focusing this jamming interference precisely onto the eavesdropper while canceling self-interference at the receiver [40]. The integration of RIS with Non-Orthogonal Multiple Access (NOMA) in VLC systems is another promising direction, where the RIS is used to manipulate channel gains between users to maximize the secrecy capacity of the system [365].

**Hybrid Systems and Emerging Challenges**
Recognizing the complementary strengths and weaknesses of RF (including THz) and VLC, hybrid systems are a major research trend. RF provides robustness to blockage and wider coverage, while VLC offers high bandwidth and inherent spatial confinement. These systems can be designed to leverage the security of VLC for downlink in sensitive areas while using RF for uplink or backup, optimizing quality-of-service and security jointly [366]. For ultimate reliability and security, aggregated RF/VLC systems, where a user is served simultaneously by both links, are being investigated [367]. However, the integration also introduces new attack vectors; for instance, adding RF links to a VLC network can broaden the attack surface due to RF's broadcast nature, requiring careful cross-layer security designs [368]. Key challenges for both THz and VLC security include practical hardware impairments (e.g., phase noise in RIS, LED nonlinearity), the difficulty of obtaining perfect channel state information (CSI) for eavesdroppers, and the need for low-complexity, real-time optimization algorithms to configure RIS elements and beamforming vectors in dynamic industrial environments. As these technologies mature towards 6G, their unique physical characteristics will continue to provide a fertile ground for developing robust, inherent, and physics-augmented security solutions for industrial wireless networks.

**Table: Comparison of approaches in 5.3 Terahertz (THz) and Visible Light Communication (VLC) for Inherent Security**

| Technology / Approach | Key Security Mechanism / Concept | Advantages / Strengths | Limitations / Challenges | Reference(s) |
| :--- | :--- | :--- | :--- | :--- |
| Terahertz (THz) Communications | Exploiting high directivity and near-field beamfocusing (e.g., with widely-spaced arrays) for angular and range security. | Inherent angular confinement via pencil-thin beams; Near-field beamfocusing creates secure zones at specific locations; Potential for "absolute security" via spatial nulls across frequencies. | Vulnerable to eavesdroppers within the same beam sector (range security problem); Highly susceptible to blockage and intermittent connectivity. | [357], [358], [359] |
| Terahertz (THz) Communications | Integration of Reconfigurable Intelligent Surfaces (RIS) for PLS and blockage mitigation. | RIS can provide secure NLOS paths and optimize secrecy spectral efficiency over an area without needing eavesdropper's instantaneous location. | Practical hardware impairments (e.g., phase noise); Need for real-time optimization in dynamic environments. | [331], [360] |
| Visible Light Communication (VLC) / LiFi | Exploiting inherent signal confinement (WYSIWYS - "What You See Is What You Send"). | Physical containment within illuminated rooms; High bandwidth; Immunity to RF interference. | Broadcast nature within the room allows co-located eavesdropping; Reliant on line-of-sight, vulnerable to blockage. | [361] |
| Visible Light Communication (VLC) / LiFi | Adapted PLS techniques (e.g., Secrecy Capacity analysis, Artificial Noise) under optical constraints (IM/DD, power limits). | Provides fundamental performance limits for secure design; AN can enhance confidentiality among co-located users. | Clipping distortion from LED nonlinearity must be incorporated into AN design; Strict optical power constraints. | [362], [223] |
| Visible Light Communication (VLC) / LiFi | Hardware-based security using Gold Nanoparticle (GNP) plates. | Manipulates circularly polarized light to create unique channel fingerprints, increasing secrecy rate around the legitimate receiver. | Requires specialized hardware; Performance dependent on specific setup and environment. | [363] |
| Visible Light Communication (VLC) / LiFi | RIS (IRS) for secure beamforming and blockage mitigation. | RIS can dynamically reconfigure light paths to maximize signal at legitimate receiver and minimize it at eavesdropper; Enables novel jamming schemes (e.g., with STAR-RIS). | Difficulty obtaining perfect CSI for eavesdroppers; Hardware impairments and phase noise. | [364], [101], [40], [365] |
| Hybrid RF/VLC Systems | Leveraging complementary strengths: VLC for secure downlink, RF for robust uplink/coverage. | Optimizes QoS and security jointly; Aggregated systems improve reliability and energy efficiency. | Integration broadens attack surface (e.g., RF's broadcast nature); Requires careful cross-layer security design. | [366], [367], [368] |


### 5.4 Emerging Paradigms: Active RIS, STAR-RIS, and Intelligent Surfaces

While conventional passive RISs have demonstrated significant potential for enhancing physical layer security (PLS) by manipulating the wireless propagation environment, their inherent limitations—most notably the "double-fading" attenuation and restricted half-space coverage—have spurred the development of advanced metasurface architectures. These emerging paradigms, including Active RIS, Simultaneously Transmitting and Reflecting RIS (STAR-RIS), and intelligent computational surfaces, offer transformative capabilities for securing industrial wireless networks by providing amplified signal control, full-space coverage, and integrated sensing and processing.

**Active RIS** addresses the fundamental performance bottleneck of passive RISs: the multiplicative path loss experienced on the cascaded transmitter-RIS-receiver link. By integrating low-cost amplifiers (e.g., negative resistance components) into each reflecting element, an Active RIS can not only apply a phase shift but also amplify the impinging signal [334]. This active amplification directly counteracts the double-fading effect, enabling a strengthened reflected link without requiring an impractically large number of passive elements. For PLS, this capability is crucial. As noted in [369], passive RISs often achieve only marginal secrecy gains in scenarios with strong direct links between legitimate transceivers due to this fading. In contrast, an Active RIS can effectively reshape the signal-to-interference-plus-noise ratio (SINR) landscape. For instance, in a secure transmission scenario, the Active RIS can be optimized to amplify the signal towards the legitimate receiver while simultaneously minimizing the signal leakage towards an eavesdropper. Joint optimization of the transmit beamforming at the base station and the reflective coefficient matrix (now containing both phase and controllable amplitude) at the Active RIS can significantly maximize the secrecy rate, as explored in [82] and [333]. However, this gain comes with new challenges, including managing the amplified thermal noise introduced by the active components, increased power consumption, and more complex beamforming design that must balance signal enhancement with noise minimization [335].

**Simultaneously Transmitting and Reflecting RIS (STAR-RIS)** represents a paradigm shift from coverage extension to coverage creation. A conventional reflective-only RIS serves users located on the same side as its incident signal. A STAR-RIS, however, partitions its elements to simultaneously reflect signals to users on one side and transmit signals to users on the opposite side, thereby providing 360-degree full-space coverage [370]. This unique property unlocks novel security mechanisms, particularly for industrial settings with complex geometries. A STAR-RIS can be deployed to create secure zones. For example, it can transmit confidential information to legitimate receivers located in a "safe" zone (e.g., inside a secure control room) while reflecting jamming signals or nulls towards potential eavesdroppers in an "unsafe" zone (e.g., a public area) [331]. This enables spatial secrecy without precise knowledge of the eavesdropper's instantaneous location. Furthermore, STAR-RIS is exceptionally suited for enabling secure full-duplex (FD) systems. A friendly FD monitor can use a STAR-RIS to reflect a suspicious transmission to a suspicious receiver (to maintain the communication link for surveillance) while simultaneously transmitting a jamming signal from the monitor to the same receiver to degrade its reception, all coordinated through the STAR-RIS's coefficients [371]. This facilitates proactive eavesdropping for security monitoring. The co-design of transmission and reflection beamforming under coupled or independent phase-shift models is a core research challenge, often tackled via alternating optimization and semi-definite relaxation, to maximize metrics like the eavesdropping non-outage probability or the covert communication rate [337].

Beyond signal manipulation, the convergence of wireless communication and sensing/computing is leading to the concept of **Intelligent Surfaces with Integrated Capabilities**. The **Hybrid RIS (HRIS)** incorporates sensing elements alongside reflective ones, allowing the surface to sense a portion of the impinging signal while reflecting the rest [372]. This localized sensing capability can be leveraged for low-overhead channel estimation, localization of users or potential threats, and even physical-layer authentication, making the RIS an intelligent node rather than a purely passive configurator. Extending this idea further, the **Reconfigurable Intelligent Computational Surface (RICS)** envisions a metasurface with a dual-layer structure: a reconfigurable beamforming layer for wave manipulation and an intelligence computation layer based on metamaterials for performing analog, wave-based computations directly on the received signals [373]. An RICS could, for instance, perform in-situ spectral analysis to detect jamming patterns or execute basic encryption operations at the speed of light, thereby offloading processing tasks from digital units and reducing latency for time-critical industrial security applications.

The evolution of RIS architectures also includes **Beyond Diagonal RIS (BD-RIS)**, which moves away from the traditional diagonal phase shift matrix model by introducing interconnections between scattering elements [374]. This allows for more sophisticated manipulation of both the magnitude and phase of signals, providing greater flexibility in shaping wavefronts for security purposes, such as creating more precise spatial nulls towards eavesdroppers. Furthermore, the concept of **Absorptive RIS (ARIS)** offers a middle ground between passive and active RIS by being able to absorb part of the incident signal energy, thereby providing a degree of amplitude control without active amplification [375]. This can be highly effective for interference mitigation in shared spectrum scenarios, such as ensuring that a communication system does not interfere with a co-located radar, thereby preserving the security and integrity of both systems.

In summary, the evolution from passive RIS to these advanced intelligent surfaces marks a transition from simply reconfiguring the environment to embedding intelligence, amplification, and multi-functional capabilities directly into the wireless infrastructure. For industrial physical-layer security, Active RIS overcomes fundamental attenuation limits to boost secure links, STAR-RIS enables geometric security policies and covert operations, while HRIS and RICS pave the way for autonomous, self-configuring secure networks that integrate sensing and processing. As these technologies mature, their co-design with communication protocols and security algorithms will be pivotal in realizing robust, efficient, and intelligent security frameworks for future industrial Internet of Things (IIoT) and cyber-physical systems.

**Table: Comparison of approaches in 5.4 Emerging Paradigms: Active RIS, STAR-RIS, and Intelligent Surfaces**

| RIS Architecture | Key Principle / Mechanism | Primary Advantages for PLS | Key Challenges / Limitations | Reference(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Active RIS** | Integrates low-cost amplifiers (e.g., negative resistance components) into each reflecting element to apply phase shift and amplify the impinging signal. | Directly counteracts the "double-fading" attenuation, enabling a strengthened reflected link. Can reshape the SINR landscape to amplify signal towards legitimate receiver while minimizing leakage to eavesdropper, significantly boosting secrecy rate. | Introduces amplified thermal noise from active components, increased power consumption, and more complex beamforming design that must balance signal enhancement with noise minimization. | [334], [369], [82], [333], [335] |
| **STAR-RIS (Simultaneously Transmitting and Reflecting RIS)** | Partitions elements to simultaneously reflect signals to one side and transmit signals to the opposite side, providing 360-degree full-space coverage. | Enables creation of secure zones (e.g., transmit confidential info to a safe zone while reflecting jamming signals to an unsafe zone). Facilitates spatial secrecy without precise eavesdropper location. Suited for secure full-duplex systems and proactive eavesdropping. | Co-design of transmission and reflection beamforming under coupled or independent phase-shift models is complex. Optimization (e.g., via alternating optimization, semi-definite relaxation) is required to maximize metrics like eavesdropping non-outage probability. | [370], [331], [371], [337] |
| **Intelligent Surfaces with Integrated Capabilities (HRIS & RICS)** | **Hybrid RIS (HRIS):** Incorporates sensing elements alongside reflective ones to sense a portion of the impinging signal while reflecting the rest.<br>**Reconfigurable Intelligent Computational Surface (RICS):** Features a dual-layer structure with a reconfigurable beamforming layer and an intelligence computation layer for analog, wave-based computations. | Enables low-overhead channel estimation, localization of users/threats, and physical-layer authentication. RICS can perform in-situ spectral analysis to detect jamming or execute basic encryption at light speed, reducing latency for time-critical security. | Transforms RIS from a passive configurator to an intelligent node, requiring integration of sensing/computing hardware and algorithms. Design and control complexity increases. | [372], [373] |
| **Beyond Diagonal RIS (BD-RIS)** | Moves beyond the traditional diagonal phase shift matrix model by introducing interconnections between scattering elements, allowing sophisticated manipulation of both signal magnitude and phase. | Provides greater flexibility in shaping wavefronts for security, such as creating more precise spatial nulls towards eavesdroppers. | More complex hardware architecture and control mechanisms required compared to conventional diagonal RIS. | [374] |
| **Absorptive RIS (ARIS)** | Capable of absorbing part of the incident signal energy, providing a degree of amplitude control without active amplification. | Effective for interference mitigation in shared spectrum (e.g., ensuring communication does not interfere with co-located radar), thereby preserving security and integrity of both systems. Offers a compromise between passive and active RIS in complexity and power. | Provides amplitude control but not signal amplification, so performance gain may be limited compared to active RIS in some scenarios. | [375] |


## 6 PLS for Specific Industrial Applications and Systems

This section surveys the application and tailoring of PLS techniques to critical industrial domains. It covers secure communication for the Industrial Internet of Things (IIoT) and wireless sensor networks, security for Unmanned Aerial Vehicle (UAV) networks, and the protection of Cyber-Physical Systems (CPS), industrial control networks, and in-vehicle networks.

### 6.1 Secure Communication for Industrial Internet of Things (IIoT) and Wireless Sensor Networks (WSNs)

The pervasive deployment of resource-constrained Industrial Internet of Things (IIoT) devices and Wireless Sensor Networks (WSNs) in smart factories, environmental monitoring, and process automation introduces formidable security challenges. Traditional cryptographic protocols are often computationally prohibitive for these low-power, low-memory endpoints, creating a critical need for lightweight, efficient, and robust security solutions. Physical Layer Security (PLS) emerges as a vital complementary paradigm, exploiting the inherent properties of the wireless medium and hardware to provide foundational security services tailored for constrained environments.

**Lightweight Authentication Mechanisms** are paramount for establishing trust in IIoT ecosystems. Radio Frequency Fingerprinting (RFF) has gained significant traction as a non-cryptographic, device-specific authentication method. It leverages unique, unintentional hardware imperfections introduced during manufacturing—manifested in signal features like I/Q offset, phase noise, and spectral regrowth—to create a device "fingerprint." Recent advances heavily utilize Deep Learning (DL) to extract and classify these complex features from raw signal data, achieving high identification accuracy [16]. However, a major challenge for DL-based RFF is domain adaptation; models trained under specific channel conditions, times, or locations often degrade when deployed elsewhere. Novel feature representations, such as the Double-Sided Envelope Power Spectrum (EPS), have been proposed to capture hardware impairments while suppressing irrelevant domain information, significantly improving cross-domain robustness [301]. Beyond transient signal features, function modeling approaches like FID aim to learn the mathematical expression of a device's physical-layer process. This model, which is independent of transmitted data, serves as a channel-robust fingerprint resilient to replay attacks [376]. For an even more hardware-centric approach, Physical Unclonable Functions (PUFs) exploit nanoscale manufacturing variations to generate device-unique, tamper-evident responses to challenges. Silicon-based PUFs, such as SRAM PUFs, provide a lightweight source of entropy for key generation and device identity directly on the chip [377]. Emerging memory technologies like Resistive RAM (ReRAM) are also being explored for constructing multi-state PUFs to enhance authentication in software-defined networks [378]. To address scalability in massive machine-type communication (mMTC) scenarios, flexible group authentication schemes (GAS) and fast, scalable protocols leveraging fog computing have been proposed to authenticate numerous devices simultaneously with minimal overhead [379][380].

**Secret Key Generation (SKG) from Shared Randomness** offers a lightweight alternative to traditional key distribution. By exploiting the reciprocity and randomness of the wireless channel between two legitimate parties, symmetric encryption keys can be generated from measured Channel State Information (CSI). This is particularly promising for private 5G/6G industrial networks where low-latency, secure session establishment is required [381]. The practical implementation of full SKG protocols, including advantage distillation, information reconciliation, and privacy amplification, has been demonstrated in real-world settings, even under adversarial eavesdropping attempts [382]. To improve reliability in volatile channels, reconciliation techniques using error-correcting codes like polar codes can be applied to pre-process channel measurements before hypothesis testing for authentication [307]. Furthermore, the integration of SKG with other PLS primitives, such as PUFs, into multi-factor authentication protocols enhances security for delay-sensitive applications [383]. The environment itself can be engineered to aid key generation; Reconfigurable Intelligent Surfaces (RIS) can dynamically customize channel characteristics to increase entropy and boost the key generation rate in otherwise static industrial settings [327].

**Secure Data Aggregation and Communication** is essential for preserving bandwidth and energy in dense WSNs. PLS principles are applied to protect data integrity and confidentiality during in-network processing. Lightweight, decentralized data obfuscation strategies for privacy-preserving aggregation, which minimize communication overhead and leverage efficient synchronous transmission protocols, are being developed for low-power IoT systems [384]. At the modulation level, physical-layer encryption (PLE) schemes, such as those derived from standardized lightweight stream ciphers, can encrypt data between the channel coding and modulation blocks, providing a generic confidentiality solution adaptable to various IoT protocols [385]. For securing broadcast or multicast communications in industrial settings, artificial noise and friendly jamming techniques can be strategically deployed to degrade the signal at potential eavesdropper locations while maintaining quality at legitimate receivers [41].

**Integration with Fog and Edge Computing Architectures** addresses scalability and latency challenges. Moving authentication and key management functions from a distant cloud to network edge nodes (e.g., fog servers, gateways) significantly reduces communication latency and confines attack surfaces [379]. These edge nodes can run machine learning models for AI-enhanced security, such as adaptive RF fingerprinting or intrusion detection, offloading complex computations from end-devices [26][386]. Blockchain technology can be integrated at the edge to provide decentralized, tamper-resistant ledgers for access control and key management without the prohibitive overhead of proof-of-work, using lightweight consensus algorithms like Proof-of-Authentication (PoAh) [387]. Software-Defined Perimeter (SDP) frameworks deployed in Multi-access Edge Computing (MEC) can create dynamic, identity-centric perimeters, authorizing only authenticated devices at the edge to access core cloud services [388].

Despite promising advances, significant **challenges** persist. The extreme heterogeneity of IIoT devices—from legacy brownfield systems with no inherent security to modern greenfield sensors—complicates the uniform deployment of PLS solutions. Developing realistic, standardized security testbeds that holistically incorporate this heterogeneity is crucial for evaluating solutions [27]. The energy budget of battery-powered or energy-harvesting nodes remains a stringent constraint, necessitating continuous optimization of the security-performance-energy trade-off. Furthermore, the dynamic and often harsh industrial radio environment, with multipath fading and interference, can impact the reliability of channel-dependent techniques like SKG and RFF. Finally, achieving end-to-end security requires seamless cross-layer integration, where PLS primitives are effectively combined with lightweight upper-layer cryptographic protocols [115] and secure system administration frameworks [389] to build a comprehensive defense-in-depth strategy for the industrial wireless edge.

**Table: Comparison of approaches in 6.1 Secure Communication for Industrial Internet of Things (IIoT) and Wireless Sensor Networks (WSNs)**

| Method / Approach | Core Idea / Mechanism | Key Strengths / Advantages | Key Challenges / Limitations | Primary Application Context | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Radio Frequency Fingerprinting (RFF) with Deep Learning | Leverages unique hardware imperfections from manufacturing (e.g., I/Q offset, phase noise) to create a device fingerprint. Uses Deep Learning (DL) to extract and classify complex features from raw signal data. | High identification accuracy; non-cryptographic and device-specific. | Domain adaptation: models degrade under different channel conditions, times, or locations. | Device authentication in IIoT/WSNs. | [16] |
| Double-Sided Envelope Power Spectrum (EPS) for RFF | A novel IQ data representation designed to capture hardware impairments while suppressing irrelevant domain information, improving cross-domain robustness for DL models. | Significantly improves robustness and generalizability across domains (e.g., cross-day, cross-location). | Effectiveness contingent on the quality of signal capture and representation. | Enhancing domain adaptation for DL-based RF fingerprinting. | [301] |
| Function Modeling-based Identification (FID) | Learns the mathematical expression (function model) of a device's physical-layer process, which is independent of transmitted data, to serve as a channel-robust fingerprint. | Data-independent and resilient to replay attacks; channel-robust; high reported accuracy (>99%). | Requires modeling and separating channel effects; computational cost of model training. | Trusted identification of low-end IoT devices resilient to channel variations and replay. | [376] |
| Physical Unclonable Functions (PUFs) | Exploits nanoscale manufacturing variations to generate device-unique, tamper-evident responses to challenges. | Lightweight source of entropy for key generation and identity; tamper-evident; hardware-centric. | Reliability issues (e.g., environmental variations); potential vulnerability to modeling attacks. | Lightweight device authentication and key generation on constrained embedded devices. | [377] |
| ReRAM-based Multi-state PUFs | Uses inherent randomness in Resistive RAM (ReRAM) nanomaterials to construct digital PUFs with multiple states for authentication. | Enhances authentication security; suitable for embedding in IoT devices; multi-state approach may improve error tolerance. | Novel technology; long-term reliability and practical deployment challenges in varied environments. | Enhancing authentication security in software-defined wireless networks (SDWN). | [378] |
| Secret Key Generation (SKG) from Channel State Information (CSI) | Exploits reciprocity and randomness of the wireless channel between two parties to generate symmetric encryption keys from measured CSI. | Lightweight alternative to key distribution; information-theoretic security; promising for low-latency sessions. | Reliability in volatile channels; dependent on channel randomness and reciprocity. | Secure session establishment in private 5G/6G industrial networks. | [381] |
| SKG with Information Reconciliation (e.g., Polar Codes) | Applies error-correcting codes like polar codes (Slepian-Wolf reconciliation) to pre-process channel measurements before hypothesis testing for authentication. | Improves reliability and authentication performance in low SNR scenarios by reconciling channel measurements. | Adds complexity to the SKG protocol; requires coordination between parties. | Enhancing the precision and consistency of physical layer authentication. | [307] |
| Multi-factor Authentication (PUF + SKG + Localization) | Combines PUFs, proximity estimation (localization), and SKG from wireless fading coefficients into a fast, privacy-preserving protocol. | Enhanced security through multiple factors; designed for short blocklength, delay-constrained applications. | Integration complexity; performance trade-offs between factors. | Fast, low-latency mutual authentication for delay-sensitive applications. | [383] |
| Reconfigurable Intelligent Surface (RIS)-aided PLS | Uses RIS to dynamically customize wireless channel characteristics to increase entropy for SKG or to direct signals/jamming for security. | Can boost key generation rate in static environments; enhances secrecy capacity and jamming effectiveness. | RIS reconfiguration speed, deployment optimization, and channel estimation challenges. | Improving PLS (SKG, anti-eavesdropping) in static industrial or indoor environments. | [327] |
| Lightweight Privacy-Preserving Data Aggregation (LiPI) | Employs decentralized, collaborative data obfuscation strategies and synchronous transmission protocols to protect data during in-network aggregation. | Minimizes communication overhead and energy consumption; no trusted third party required. | Security reliant on the obfuscation strategy and node cooperation. | Privacy-preserving data aggregation in low-power, dense WSNs/IoT systems. | [384] |
| Generic Physical-Layer Encryption (Grain-128PLE) | A lightweight stream cipher placed between channel coding and modulation blocks to encrypt data, providing a protocol-agnostic confidentiality solution. | Generic solution adaptable to various IoT protocols; derived from a NIST-evaluated lightweight cipher. | Adds processing step at the physical layer; security depends on the underlying cipher. | Providing data confidentiality at the physical layer for diverse IoT networks. | [385] |
| Friendly Jamming & Artificial Noise | Strategically deploys jamming signals or artificial noise to degrade signal quality at potential eavesdropper locations while maintaining it at legitimate receivers. | Effectively enhances secrecy capacity; can be network-controlled. | Requires knowledge of eavesdropper location/region; may cause interference if not carefully managed. | Securing broadcast/multicast communications in industrial settings. | [41] |
| Fog/Edge-based Authentication & Key Management | Moves authentication and key management functions from the cloud to network edge nodes (fog servers, gateways) to reduce latency and attack surface. | Reduces communication latency; confines attack surface; enables scalability. | Security of the edge nodes themselves; requires trust in the edge infrastructure. | Fast and scalable authentication for large-scale IoT deployments (e.g., smart living). | [379] |
| AI-enhanced Adaptive RF Fingerprinting | Leverages AI (machine learning) at the edge for adaptive selection and tuning of RF fingerprinting techniques to suit challenging RF environments. | Improves accuracy and flexibility of device authentication over dynamic conditions. | Requires computational resources at the edge; depends on quality of training data and models. | Adaptive and accurate IIoT device authentication in heterogeneous environments. | [26] |
| Blockchain with Lightweight Consensus (PoAh) | Integrates blockchain at the edge with lightweight consensus algorithms like Proof-of-Authentication (PoAh) for decentralized, tamper-resistant access control and key management. | Provides decentralization and immutability without the high overhead of proof-of-work. | Latency and storage overhead on constrained devices; scalability of the blockchain. | Decentralized security management for large-scale IoT frameworks. | [387] |
| Software-Defined Perimeter (SDP) in MEC | Deploys SDP frameworks in Multi-access Edge Computing (MEC) to create dynamic, identity-centric perimeters, authorizing only authenticated edge devices to access core services. | Enhances security by hiding core services; reduces attack surface. | Adds complexity to network architecture and device onboarding. | Hierarchical security for cellular-connected IoT devices in MEC environments. | [388] |


### 6.2 Security for Unmanned Aerial Vehicle (UAV) Networks in Industrial Settings

The integration of Unmanned Aerial Vehicles (UAVs) into industrial wireless networks offers transformative potential for applications such as remote monitoring, precision agriculture, logistics, and emergency response. Their high mobility, on-demand deployment, and ability to establish dominant line-of-sight (LoS) links are significant advantages. However, these very characteristics—particularly the broadcast nature of air-to-ground channels—introduce severe security vulnerabilities, making UAV communications highly susceptible to eavesdropping and jamming attacks. Consequently, Physical Layer Security (PLS) has emerged as a critical, lightweight complement to cryptographic methods for safeguarding UAV-assisted industrial communications. The research in this domain focuses on exploiting the unique degrees of freedom offered by UAVs, such as controllable mobility and flexible positioning, to proactively enhance secrecy performance.

A cornerstone of UAV-PLS is the joint optimization of the UAV's trajectory and transmit power to maximize secrecy rates against ground-based eavesdroppers. Static optimization is often insufficient; instead, the UAV's mobility is leveraged as a dynamic resource. By intelligently planning its flight path, a UAV can position itself to create favorable channel conditions for the legitimate receiver while simultaneously degrading the channel to potential eavesdroppers. This is formulated as a non-convex optimization problem maximizing the average secrecy rate over a mission period. As demonstrated in [64] and [390], sophisticated algorithms based on alternating optimization, block coordinate descent, and successive convex approximation (SCA) are employed to iteratively optimize the trajectory and power allocation. These approaches can secure communications even in challenging scenarios where the legitimate channel is initially inferior to the eavesdropping channel. The optimization framework is extended to robust designs that account for imperfect knowledge of eavesdropper locations, as seen in [391] and [392], ensuring performance guarantees under location uncertainty.

Beyond acting as information transmitters, UAVs are effectively deployed as dynamic security-enhancing agents. Two prominent roles are mobile friendly jammers and mobile relays. As a jammer, a UAV can fly close to a suspected eavesdropper region and transmit artificial noise (AN) to deliberately interfere with the eavesdropper's reception without critically harming the legitimate link. The work in [393] shows that jointly optimizing the jammer UAV's trajectory and jamming power significantly outperforms static jamming. For coverage extension in obstructed industrial environments, UAVs serve as mobile decode-and-forward (DF) or amplify-and-forward (AF) relays. Security in such relaying systems is paramount, especially with untrusted relays or external eavesdroppers. Research like [127] and [394] co-designs the relay's trajectory, transmit power, and communication scheduling (e.g., blocklength for short packets) to maximize secrecy throughput or energy efficiency, ensuring reliable and secure delivery for latency-sensitive industrial IoT data.

Resilience against active jamming attacks is another critical dimension. UAV networks are vulnerable to both ground-based and intelligent mobile jammers. Defensive strategies involve designing intelligent flight paths that avoid jammer-rich zones or optimize communication parameters in real-time. Studies such as [395] and [396] employ reinforcement learning (RL) frameworks, enabling UAVs to learn optimal anti-jamming trajectories through interaction with the environment. The UAV learns to adapt its path, potentially using higher SINR thresholds or virtual jamming models, to complete data collection missions from distributed IoT nodes despite adversarial interference. Furthermore, integrated sensing and communication frameworks, as proposed in [397], allow a UAV to use its own jamming signals for dual purposes: degrading an eavesdropper's channel and simultaneously sensing/estimating the eavesdropper's state for predictive trajectory planning and resource allocation.

The security challenges escalate in multi-UAV systems, such as coordinated swarms or fleets deployed for complex industrial tasks. These systems face unique cyber-physical security threats where attacks on communication links can lead to physical mission failure, including collisions or loss of control. PLS techniques are adapted for swarm coordination and secure swarm-to-swarm or swarm-to-ground communications. Cooperative strategies are essential, such as using a subset of UAVs as distributed jammers or forming virtual antenna arrays for collaborative beamforming. For instance, [126] analyzes the secrecy outage probability for a swarm performing cooperative jamming and energy harvesting. [398] and [128] investigate using UAV swarms to construct distributed beamforming patterns that maximize signal strength towards legitimate receivers while minimizing sidelobe leakage towards colluding eavesdroppers, formulated as a multi-objective optimization problem. The scalability, coordination overhead, and consensus in decentralized swarm security remain key research challenges.

Emerging technologies are being integrated to further bolster UAV-PLS. Reconfigurable Intelligent Surfaces (RIS) mounted on UAVs or deployed in the environment can dynamically reshape the wireless propagation landscape. [399] and [63] show that jointly optimizing the UAV's trajectory and the RIS's phase shifts can significantly improve secrecy rates, even under imperfect channel state information. For next-generation industrial networks, the confluence of UAVs with terahertz (THz) communications and non-orthogonal multiple access (NOMA) is explored. [74] investigates covert communication in THz bands using a UAV-mounted RIS, while [400] examines secrecy in UAV-based NOMA systems through protected zone optimization. Finally, to address the holistic security of UAV networks, cross-layer approaches incorporating blockchain for secure coordination and data integrity are proposed, as discussed in [116] and [401], which provide decentralized trust and resilience against spoofing and data tampering in multi-provider swarm operations.

**Table: Comparison of approaches in 6.2 Security for Unmanned Aerial Vehicle (UAV) Networks in Industrial Settings**

| Method / Role | Key Idea / Strategy | Optimization Variables / Techniques | Key Findings / Performance | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **UAV as Secure Transmitter** | Jointly optimize UAV's trajectory and transmit power to maximize secrecy rates against ground eavesdroppers by exploiting controllable mobility. | Trajectory, transmit power; Alternating optimization, block coordinate descent, successive convex approximation (SCA). | Enables secure communication even when the legitimate channel is initially inferior to the eavesdropping channel. | [64], [390] |
| **Robust Secure Transmitter Design** | Extends trajectory/power optimization to account for imperfect knowledge of eavesdropper locations, ensuring performance under uncertainty. | Robust trajectory, transmit power; Techniques to handle location uncertainty (e.g., worst-case optimization). | Provides performance guarantees and enhances secrecy rates despite imperfect eavesdropper location information. | [391], [392] |
| **UAV as Mobile Friendly Jammer** | Deploy UAV as a mobile jammer flying near suspected eavesdropper regions to transmit artificial noise (AN), degrading eavesdropper's reception. | Jammer trajectory, jamming power; Joint optimization using block coordinate descent and SCA. | Significantly outperforms static jamming in improving the average secrecy rate of the ground wiretap channel. | [393] |
| **UAV as Mobile Relay** | Use UAV as a mobile decode-and-forward (DF) or amplify-and-forward (AF) relay for coverage extension, with security against untrusted relays/eavesdroppers. | Relay trajectory, transmit power, communication scheduling (e.g., blocklength); Joint resource optimization and 3D trajectory design. | Maximizes secrecy throughput or secrecy energy efficiency for reliable, secure delivery of latency-sensitive IoT data. | [127], [394] |
| **Anti-Jamming & Resilient Path Planning** | Design intelligent flight paths and communication parameters to counteract active jamming attacks from ground or mobile jammers. | Anti-jamming trajectory, communication parameters; Reinforcement learning (RL) frameworks (e.g., Dueling Double Deep Q-Network). | Enables UAVs to learn optimal trajectories to complete data collection missions despite adversarial jamming interference. | [395], [396] |
| **Integrated Sensing & Communication (ISAC)** | Use UAV's jamming signals for dual purposes: degrading eavesdropper's channel and simultaneously sensing/estimating eavesdropper's state for predictive planning. | UAV trajectory, resource allocation, sensing parameters; Extended Kalman filtering, robust optimization. | Improves secure communication performance by integrating sensing for state estimation and predictive resource allocation. | [397] |
| **Multi-UAV Swarm & Cooperative Security** | Employ UAV swarms for cooperative strategies like distributed jamming or forming virtual antenna arrays for collaborative beamforming against colluding eavesdroppers. | Swarm trajectory, cooperative jamming/beamforming power, user association; Multi-objective optimization, swarm intelligence algorithms. | Enhances secrecy performance (e.g., reduces secrecy outage probability) and counters colluding eavesdroppers through distributed beamforming. | [126], [398], [128] |
| **UAV with Reconfigurable Intelligent Surfaces (RIS)** | Mount RIS on UAVs or deploy in environment to dynamically reshape propagation; jointly optimize UAV trajectory and RIS phase shifts. | UAV trajectory, RIS phase shifts, transmit power; Alternating optimization, fractional programming, SCA. | Significantly improves secrecy rates, even under imperfect channel state information, compared to benchmarks without RIS. | [399], [63] |
| **UAV with Emerging Tech (THz, NOMA)** | Integrate UAVs with terahertz communications and non-orthogonal multiple access (NOMA) for enhanced spectral efficiency and security. | Protected zone optimization, trajectory, power allocation, user scheduling; Block successive convex approximation. | Investigates covert communication in THz bands and optimizes secrecy in NOMA systems through protected zone shape optimization. | [74], [400] |
| **Cross-Layer & Blockchain Integration** | Incorporate blockchain for secure coordination, data integrity, and decentralized trust in multi-UAV systems to resist spoofing and tampering. | Consortium blockchain architecture, hybrid consensus protocols (e.g., DPOS-PBFT), smart contracts. | Provides decentralized trust and resilience against cyber-attacks, enabling secure multi-provider swarm operations with scalability. | [116], [401] |


### 6.3 Protection of Industrial Control Systems (ICS), SCADA, and Critical Infrastructure

The convergence of Information Technology (IT) and Operational Technology (OT) networks, driven by the imperatives of Industry 4.0, has fundamentally transformed Industrial Control Systems (ICS), Supervisory Control and Data Acquisition (SCADA) networks, and other critical infrastructure. This integration, while enabling unprecedented efficiency and remote management, has dramatically expanded the attack surface, rendering the traditional "security by obscurity" principle of air-gapping obsolete [402]. Consequently, these cyber-physical systems (CPS) have become high-value targets for sophisticated adversaries, with attacks capable of causing catastrophic physical damage, environmental harm, and threats to human safety [403]. In this high-stakes environment, Physical Layer Security (PLS) emerges not as a replacement for, but as a vital complement to, cryptographic and network-level defenses. PLS techniques offer a unique advantage by exploiting the inherent randomness and physical properties of the wireless channel—the very medium that increasingly connects sensors, actuators, and controllers—to enhance resilience, detection, and protection at the foundational level of communication.

The threat landscape for ICS is distinct and multifaceted. Adversaries often aim to manipulate the physical process by compromising the integrity of sensor data or control commands. **False Data Injection (FDI) attacks** are a primary concern, where an attacker injects malicious measurements into the system to deceive operators or control algorithms, potentially driving the physical process into a hazardous state without triggering conventional alarms [404]. More insidious are **stealthy deception attacks**, which hijack communication channels (e.g., between Human-Machine Interfaces (HMIs) and Programmable Logic Controllers (PLCs)) to present a coherent but entirely fake view of the industrial process to the operator, prompting harmful manual interventions [168]. Furthermore, **protocol-specific attacks** exploit vulnerabilities in legacy industrial protocols like Modbus, DNP3, or PROFINET, which often lack basic authentication and encryption [9]. **Jamming and Denial-of-Service (DoS) attacks** at the physical layer can disrupt critical telemetry, leading to loss of visibility and control [405]. PLS provides a foundational countermeasure against these threats by focusing on securing the wireless data-in-transit before it is interpreted as a protocol message.

A core application of PLS in ICS is enhancing **anomaly detection at the physical layer**. Traditional intrusion detection systems (IDS) often analyze network metadata or protocol semantics. PLS-augmented detection incorporates the unique "fingerprint" of the communication channel itself. Techniques like **RF fingerprinting** leverage hardware imperfections in transmitters (PLCs, RTUs) to create a unique identifier for each device. This allows for physical-layer authentication, distinguishing between a legitimate field device and an impersonator, even if cryptographic keys are stolen. More broadly, machine learning models can be trained to learn the normal behavioral "invariants" of the cyber-physical process by jointly analyzing time-series data from both cyber (network traffic patterns) and physical (sensor readings, actuator states) domains [406]. This **cyber-physical intrusion detection** approach is more robust, as it can identify attacks that appear normal in the cyber domain but cause deviations in the physical process, and vice-versa [407]. For instance, an FDI attack might pass network checks but would violate the learned physical constraints of the system, such as mass-balance equations in a water treatment plant [408].

PLS also directly contributes to the **resilience of control loops**. Wireless control loops are vulnerable to eavesdropping and active interference. PLS techniques like **friendly jamming** and **artificial noise** can be strategically deployed to degrade the signal quality at potential eavesdropper locations while preserving link quality for the legitimate controller-actuator or sensor-controller pair. In the context of ICS, this could involve using auxiliary nodes or even unmanned aerial vehicles (UAVs) to dynamically create jamming zones around critical wireless links in a plant. Furthermore, **physical-layer secret key generation (PL-SKG)** offers a lightweight alternative to complex key management infrastructure for resource-constrained field devices. By exploiting the reciprocal and random nature of the wireless channel between, for example, a sensor and its controller, both parties can generate identical secret bits from measured Channel State Information (CSI). These keys can then be used for lightweight encryption or authentication of subsequent commands and measurements, providing a layer of security that is inherently tied to the physical location of the devices, making remote replication by an attacker extremely difficult.

The role of **Reconfigurable Intelligent Surfaces (RIS)** is particularly promising for securing industrial wireless deployments. RIS panels can be installed in factory halls or across critical infrastructure sites to intelligently reshape the wireless environment. For ICS security, an RIS can be optimized to perform **secure beamforming**, focusing signal energy precisely towards intended PLCs or sensors while creating deep signal nulls in directions where eavesdroppers might be located. This is crucial for protecting wireless SCADA communications in environments where directional antennas are impractical. RIS can also dynamically alter the channel to enhance the entropy and randomness for PL-SKG protocols [409]. Moreover, in the face of jamming attacks, an RIS can be reconfigured to reflect signals along non-jammed paths, thereby maintaining control loop connectivity.

Finally, PLS must be integrated into a holistic **resilience modeling and design** philosophy for CPS. Security cannot be an afterthought; it must be co-designed with the control logic and physical process. This involves using formal methods and digital twins to model attack paths and assess the cyber-physical risk of different threat vectors [403] [410]. PLS parameters, such as jamming power or beamforming strategies, become part of this optimization, aiming to guarantee safety constraints even under attack [411]. The goal shifts from merely preventing breaches to ensuring the system can **absorb, adapt, and recover** from adversarial actions—maintaining core operational functionality through techniques like event-triggered control, moving target defense (which can include dynamically changing physical layer parameters), and graceful degradation [412].

In conclusion, the protection of ICS, SCADA, and critical infrastructure demands a defense-in-depth strategy where PLS forms the essential first line of defense at the communication frontier. By leveraging the physical properties of the wireless medium for authentication, confidentiality, and intrusion detection, PLS addresses threats that are specific to the cyber-physical nexus. As industrial networks continue to evolve towards 5G/6G-enabled, ultra-reliable low-latency communication (URLLC), the integration of PLS with AI-driven security operations and quantum-resistant cryptography will be paramount in building the resilient and secure industrial ecosystems of the future.

**Table: Comparison of approaches in 6.3 Protection of Industrial Control Systems (ICS), SCADA, and Critical Infrastructure**

| Method / Technique | Primary Application / Goal | Key Mechanism / Approach | Reference |
| :--- | :--- | :--- | :--- |
| RF Fingerprinting | Physical-layer authentication & device identification | Leverages hardware imperfections in transmitters (PLCs, RTUs) to create a unique device identifier. | [39] |
| Cyber-Physical Intrusion Detection | Anomaly detection by fusing cyber and physical data | Machine learning models trained to learn normal behavioral "invariants" by jointly analyzing time-series network traffic and sensor/actuator data. | [406], [407] |
| Friendly Jamming & Artificial Noise | Resilience of wireless control loops against eavesdropping | Strategically degrades signal quality at potential eavesdropper locations while preserving link quality for legitimate pairs. | [41] |
| Physical-Layer Secret Key Generation (PL-SKG) | Lightweight encryption/authentication for field devices | Exploits the reciprocal, random nature of the wireless channel (via Channel State Information) to generate identical secret bits between two parties. | [39] |
| Reconfigurable Intelligent Surfaces (RIS) for Secure Beamforming | Protecting wireless SCADA communications | RIS panels reshape the wireless environment to focus signal energy towards intended receivers and create nulls towards eavesdroppers. | [409] |
| Integrated Cyber-Physical Risk Assessment | Resilience modeling and design for CPS | Formal methods and digital twins to model attack paths and assess the cyber-physical risk of different threat vectors. | [403], [410] |
| Event-Triggered Control & Moving Target Defense (MTD) | Ensuring system can absorb, adapt, and recover from attacks | Techniques like event-triggered control and dynamically changing physical layer parameters to maintain core functionality under attack. | [412], [413] |


### 6.4 Secure In-Vehicle and Intra-Vehicle Networks

The security of automotive and transportation systems, particularly within the context of industrial logistics and smart manufacturing, is paramount due to the safety-critical nature of their operations. These systems operate across two primary domains: the internal, constrained in-vehicle networks (IVNs) and the external, dynamic vehicle-to-everything (V2X) communications. Physical Layer Security (PLS) offers a suite of techniques uniquely suited to address the stringent latency, bandwidth, and computational constraints of these environments, providing robust defenses against a growing landscape of cyber threats.

Within the vehicle, the Controller Area Network (CAN) bus remains the de facto standard for communication between Electronic Control Units (ECUs). Its design prioritizes reliability and real-time performance but inherently lacks authentication, encryption, and sender identification, making it vulnerable to spoofing, replay, and injection attacks [414]. A primary PLS-based defense is **physical-layer intrusion detection and ECU fingerprinting**. This approach exploits the unique, hardware-induced imperfections in the analog signals transmitted by each ECU. Variations in clock skew, rise/fall times, and signal voltage levels, caused by manufacturing tolerances in oscillators and transceivers, create a distinctive "fingerprint" for each transmitter [415]. By deploying a monitoring node that analyzes these physical signal characteristics—both in time and frequency domains—an intrusion detection system (IDS) can differentiate between legitimate ECUs and an attacker spoofing a message ID. For instance, methods have been developed to identify ECUs using inimitable characteristics of signals, achieving high accuracy in detecting compromised nodes [416]. The robustness of such signal characteristic-based identification over a vehicle's lifetime, accounting for temperature variations and aging, has been a focus of recent research, with strategies like adaptive model updates significantly improving long-term accuracy [417]. More advanced fingerprinting schemes, such as **two-point voltage fingerprinting**, measure voltages at two different locations on the bus to construct a more resilient profile, raising the bar against sophisticated attackers trying to mimic a single-point voltage signature [418]. Furthermore, **covert channel-based authentication** ingeniously repurposes the concept of covert channels for defense. Techniques like TACAN (Transmitter Authentication in CAN) embed authentication information within the timing (inter-arrival times) or the least significant bits of normal CAN messages, enabling a trusted monitor to verify senders without modifying the protocol or adding traffic overhead [419]. Similarly, CANTO explores the use of optimized traffic flows to establish a time-covert cryptographic authentication channel, extracting several bits of authentication data per frame [420].

Beyond fingerprinting, **deep learning-based anomaly detection** at the physical and data link layers represents a powerful PLS-adjacent technique. Since CAN message encodings are often proprietary, models are trained to learn the normal "shape" or temporal patterns of CAN traffic, flagging deviations indicative of an attack. These methods can operate on raw bit-level data, arbitration ID sequences, or, more effectively, on decoded signal-level data when a database is available [421] [422]. Models such as Gated Recurrent Unit (GRU) autoencoders, Generative Adversarial Networks (GANs), and Transformer-based architectures (e.g., CAN-BERT) have shown high efficacy in detecting both known and unknown attack patterns by learning the complex dependencies in CAN data streams [423] [424] [425]. However, these data-driven IDS models are themselves vulnerable to adversarial examples, necessitating research into adversarial attack defending systems specifically designed for in-vehicle networks [426].

Expanding the scope to the external environment, **securing V2X communications** is critical for coordinated logistics, fleet management, and autonomous transportation systems. V2X links, including vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I), are inherently wireless and broadcast in nature, making them susceptible to eavesdropping, jamming, and message injection attacks [427]. PLS techniques are vital here. For C-V2X and future 5G NR V2X systems, the physical layer can be leveraged for **lightweight authentication and integrity protection**. One promising approach is **hybrid PLS-ML authentication**, where the location or mobility pattern of a vehicle, estimated through time-of-arrival or angle-of-arrival measurements, serves as a dynamic fingerprint. Machine learning models track legitimate vehicle trajectories, and significant deviations in the claimed versus estimated position can flag a malicious transmitter [428]. Furthermore, the integration of sensing and communication (ISAC) in 6G V2X systems opens new avenues for **Secure-ISAC**, where sensing capabilities can be used to detect and characterize eavesdroppers or jammers, informing proactive security measures like beamforming nulls towards threats [429]. The use of **Reconfigurable Intelligent Surfaces (RIS)** has also been proposed to enhance PLS in V2V scenarios. By intelligently configuring RIS elements, the signal quality at legitimate receivers can be improved while degrading it at potential eavesdroppers, thereby improving secrecy metrics like the secrecy outage probability [430].

Finally, the overarching challenge is the **integration of these PLS techniques into practical, deployable systems**. This involves overcoming constraints such as the limited payload size in CAN frames, the real-time latency requirements of safety-critical functions, and the need for low-overhead key management. Lightweight authentication protocols and frameworks like LASAN (Lightweight Authentication for Secure Automotive Networks) aim to provide full lifecycle authentication within these constraints [431]. Hardware-based solutions, such as FPGA-based IDS-ECU architectures or the use of Physically Unclonable Functions (PUFs) for key generation, offer pathways to efficient, integrated security [432] [433]. As automotive architectures evolve towards centralized compute and zonal designs with mixed networks (CAN, Automotive Ethernet), PLS and cross-layer security frameworks will be essential to provide a unified security posture across diverse in-vehicle technologies [434].

**Table: Comparison of approaches in 6.4 Secure In-Vehicle and Intra-Vehicle Networks**

| Domain | Method / Technique | Core Idea / Mechanism | Key Findings / Performance | Reference |
| :--- | :--- | :--- | :--- | :--- |
| In-Vehicle Networks (IVN) | Physical-layer intrusion detection and ECU fingerprinting | Exploits unique hardware-induced imperfections in analog signals (clock skew, rise/fall times, voltage levels) to create a distinctive fingerprint for each transmitter. | Achieves high accuracy in differentiating legitimate ECUs from attackers. Robustness over vehicle lifetime improved with adaptive model updates. | [415], [416], [417] |
| In-Vehicle Networks (IVN) | Two-point voltage fingerprinting | Measures voltages at two different locations on the bus to construct a more resilient ECU profile against sophisticated mimicry attacks. | Achieves an overall F1-score over 99.4%, raising the bar for attackers trying to mimic single-point voltage signatures. | [418] |
| In-Vehicle Networks (IVN) | Covert channel-based authentication (e.g., TACAN, CANTO) | Embeds authentication information within the timing (inter-arrival times) or the least significant bits of normal CAN messages without modifying the protocol or adding traffic overhead. | TACAN demonstrates feasibility with low bit error ratios. CANTO extracts 4–5 bits of authentication data per frame under optimized traffic flows. | [419], [420] |
| In-Vehicle Networks (IVN) | Deep learning-based anomaly detection (e.g., GRU autoencoders, GANs, Transformers) | Models learn the normal "shape" or temporal patterns of CAN traffic (raw bits, ID sequences, or decoded signals) to flag deviations indicative of attacks. | Models like INDRA (GRU autoencoder), GIDS (GAN), and CAN-BERT (Transformer) show high efficacy in detecting known and unknown attack patterns. | [423], [424], [425] |
| In-Vehicle Networks (IVN) | Adversarial attack defending systems | Defends data-driven IDS models (e.g., LSTM-based) against adversarial examples designed to fool them. | Proposed AADS achieves over 99% accuracy for detecting adversarial attacks against an LSTM-based model. | [426] |
| Vehicle-to-Everything (V2X) | Hybrid PLS-ML authentication | Uses vehicle location/mobility pattern (estimated via time-of-arrival/angle-of-arrival) as a dynamic fingerprint. ML models track legitimate trajectories to flag malicious transmitters. | Outperforms baseline schemes (e.g., angle-of-arrival based) significantly in terms of missed detections. | [428] |
| Vehicle-to-Everything (V2X) | Secure-ISAC (Integrated Sensing and Communication) | Leverages sensing capabilities in 6G V2X systems to detect and characterize eavesdroppers/jammers, informing proactive security measures like beamforming nulls. | Proposed as a future direction to address interference coupling and enhance confidentiality in ISAC-enabled V2X systems. | [429] |
| Vehicle-to-Everything (V2X) | Dual RIS-aided V2V NOMA communications | Uses dual Reconfigurable Intelligent Surfaces (RIS) to intelligently configure signal propagation, improving quality at legitimate receivers while degrading it at eavesdroppers. | Analytical models show dual RIS can significantly improve secrecy metrics like secrecy outage probability for secure V2V communication. | [430] |
| Integration & Frameworks | Lightweight authentication protocols (e.g., LASAN) | Provides full lifecycle authentication for in-vehicle networks while complying with real-time and low computational resource constraints. | LASAN protocols are analyzed for security properties and evaluated for timing requirements, showing compliance with automotive constraints. | [431] |
| Integration & Frameworks | Hardware-based solutions (FPGA-based IDS-ECU, PUFs) | Integrates IDS functionality with ECU tasks on efficient hardware (FPGA) or uses Physically Unclonable Functions (PUFs) for low-overhead key generation. | FPGA-based architecture achieves state-of-the-art accuracy with low latency and power consumption. PUF-based framework drastically reduces the number of authentication frames required. | [432], [433] |
| Integration & Frameworks | Cross-layer security for evolving architectures (e.g., NDN) | Provides a foundational security infrastructure (e.g., via digital signatures) to bridge diverse link-layer protocols (CAN, Automotive Ethernet) in centralized/zonal architectures. | Proof-of-concept demonstrates NDN can provide secure, high-speed bridging between protocols and prevent injection, DoS, and replay attacks. | [434] |


### 6.5 PLS for Smart Manufacturing and Industry 4.0 Automation

The transformation of industrial production into smart manufacturing and Industry 4.0 automation hinges on the deep integration of Cyber-Physical Systems (CPS), the Industrial Internet of Things (IIoT), and collaborative robotics. This paradigm shift introduces stringent communication requirements—ultra-reliable low-latency communication (URLLC), precise time synchronization, and deterministic data delivery—to support real-time process control, coordination of Automated Guided Vehicles (AGVs), and safe human-robot collaboration. While wired Time-Sensitive Networking (TSN) is becoming the backbone for deterministic Ethernet, the need for flexibility, mobility, and reconfigurability is driving the adoption of wireless technologies like 5G, WiFi 6/7, and WirelessHART. However, this wireless integration significantly expands the attack surface. Traditional cryptographic security, while essential, can introduce latency and computational overhead incompatible with tight control loops and resource-constrained sensors. Furthermore, as demonstrated in [435], even encrypted traffic can leak sensitive operational patterns through side-channel analysis. Therefore, Physical Layer Security (PLS) emerges as a critical complementary line of defense, exploiting the inherent randomness and properties of the wireless channel to provide lightweight, low-latency security primitives that are uniquely suited to the smart factory environment.

A primary application of PLS in smart manufacturing is securing wireless extensions of TSN and deterministic networks. As highlighted in [436] and [1], achieving microsecond-level time synchronization over wireless links (e.g., via IEEE 802.1AS) is foundational for coordinated operations. PLS techniques can protect these synchronization protocols from targeted jamming or manipulation attacks that could desynchronize an entire production line. For instance, friendly jamming or directional modulation can be employed to secure the transmission of timing reference signals, ensuring that only legitimate controllers and devices can accurately recover the synchronization clock. In cell-free massive MIMO systems envisioned for factory floors [437], PLS principles like secure beamforming and artificial noise injection can be integrated into the resource allocation algorithms. By optimizing beamforming vectors to maximize signal strength at intended actuator locations while minimizing leakage towards potential eavesdropper regions—possibly near the factory perimeter or in maintenance areas—secrecy rates for control commands can be enhanced without adding protocol latency.

Collaborative robots (cobots) and mobile AGVs represent another critical domain where PLS is vital. These entities operate in close proximity, exchanging real-time coordination data and sensor feeds. The wireless channels for AGV cooperation, as studied in [438], are susceptible to eavesdropping, which could reveal logistics patterns, or jamming, which could cause collisions. PLS offers proactive countermeasures. Physical-layer authentication using RF fingerprinting can ensure that control commands originate from a legitimate factory controller and not a rogue device introduced into the network. For AGV platoons, secret key generation from shared wireless channel characteristics can facilitate lightweight, frequent key updates for encrypting coordination messages, preserving confidentiality with minimal overhead. Furthermore, in tightly-coupled wireless systems for robotic teams [439], the broadcast nature of the medium, while efficient, is a vulnerability. PLS techniques like null-steering beamforming can ensure that broadcast commands are intelligibly received only by the intended robotic group, creating spatial secrecy zones within the factory.

Ensuring data integrity and availability for real-time process control is paramount. Here, PLS intersects with intrusion detection and resilience. Jamming attacks pose a direct threat to availability. While higher-layer protocols may use frequency hopping (as in WirelessHART), PLS can provide additional resilience. Machine learning-based jamming pattern recognition at the physical layer can enable faster detection and mitigation, informing the network controller to switch resources. Moreover, the integration of Reconfigurable Intelligent Surfaces (RIS) into industrial settings offers a revolutionary PLS tool [409]. An RIS can be strategically deployed to actively shape the factory radio environment. It can enhance signal strength towards a blocked sensor behind machinery (improving reliability) while simultaneously creating deep signal nulls towards a window or vent—a potential eavesdropper location—thereby improving secrecy. This dynamic control over propagation is ideal for adapting to the changing landscape of a flexible production line.

Finally, the integration of PLS with industrial protocols and deterministic network management presents both a challenge and an opportunity. Proprietary industrial protocols, often lacking security [440], can benefit from a PLS underlay that provides a baseline of confidentiality without modifying legacy application code. In software-defined industrial networks [441], [442], the centralized controller has a global view of the network. This enables *network-controlled physical-layer security*, as suggested in [41], where the SDN controller can orchestrate PLS strategies—like instructing specific access points to emit friendly jamming or configuring RIS phase shifts—based on real-time threat intelligence and traffic flow requirements. This co-design of network control and physical-layer security is a promising direction for holistic smart factory protection. In essence, PLS does not replace cryptographic security in Industry 4.0 but rather fortifies it, providing an adaptive, low-overhead shield that operates in harmony with the stringent timing and reliability constraints of automated industrial systems, from the shop floor to the mobile robotic fleet.

**Table: Comparison of approaches in 6.5 PLS for Smart Manufacturing and Industry 4.0 Automation**

| Method / Technique | Application / Use Case | Key Mechanism / Contribution | Reference |
| :--- | :--- | :--- | :--- |
| Physical Layer Security (PLS) | Securing wireless extensions of TSN and deterministic networks; protecting time synchronization protocols. | Exploits inherent randomness of wireless channel for lightweight, low-latency security; uses friendly jamming, directional modulation, secure beamforming, and artificial noise injection. | [1]; [437] |
| Physical-layer authentication using RF fingerprinting | Securing control commands for collaborative robots (cobots) and AGVs. | Ensures control commands originate from legitimate factory controllers by using unique RF characteristics as a fingerprint. | N/A (Concept described in text, not directly from a provided source paper) |
| Secret key generation from shared wireless channel characteristics | Securing coordination messages for AGV platoons. | Generates encryption keys from the shared physical channel properties, enabling lightweight, frequent key updates. | N/A (Concept described in text, not directly from a provided source paper) |
| Null-steering beamforming | Securing broadcast commands for tightly-coupled robotic teams. | Shapes wireless beams so broadcast commands are intelligibly received only by the intended robotic group, creating spatial secrecy zones. | [439] |
| Machine learning-based jamming pattern recognition | Intrusion detection and resilience for real-time process control. | Enables faster detection and mitigation of jamming attacks at the physical layer by recognizing attack patterns. | N/A (Concept described in text, not directly from a provided source paper) |
| Reconfigurable Intelligent Surfaces (RIS) | Enhancing signal reliability and secrecy in industrial IoT settings. | Actively shapes the radio environment to enhance signal strength towards legitimate devices and create signal nulls towards potential eavesdropper locations. | [409] |
| Network-controlled physical-layer security | Holistic smart factory protection via SDN. | SDN controller orchestrates PLS strategies (e.g., friendly jamming, RIS configuration) based on real-time threat intelligence and traffic flows. | [41]; [441]; [442] |


### 6.6 Testbeds, Experimental Validation, and Security Frameworks for Industrial PLS

The transition from theoretical models of Physical Layer Security (PLS) to robust, deployable solutions for industrial environments necessitates rigorous experimental validation and standardized security frameworks. This practical dimension is critical, as industrial systems impose unique constraints of real-time operation, legacy compatibility, and safety-critical consequences that are often abstracted away in analytical PLS studies. Consequently, a rich ecosystem of Industrial Control System (ICS) and Industrial Internet of Things (IIoT) testbeds has emerged, serving as the proving grounds for PLS techniques. These testbeds range from high-fidelity physical replicas of critical infrastructure, like chemical process reactors or water treatment plants [443], to scalable, virtualized environments built using containerization and simulation tools [444]. For instance, frameworks like MiniCPS provide toolkits for emulating network and control-layer interactions of CPS, enabling the safe investigation of attacks and defenses that bridge cyber and physical domains [445]. The maturity and credibility of such testbeds are paramount, leading to the development of assessment models like the ICS Cybersecurity Testbed Maturity Model (ICS-CTM2), which evaluates testbeds across domains such as architectural coverage, fidelity, and support for security experimentation [446]. Furthermore, the concept of Digital Twins (DTs) is gaining traction for security testing, as exemplified by EPICTWIN, a digital power twin that allows for the safe execution and study of cyber-attacks on smart grid configurations without risking physical infrastructure [447]. These DTs, especially when enhanced with blockchain for data integrity, can create trusted simulation environments for security validation [410].

Parallel to experimental platforms, structured methodologies for threat modeling and risk assessment are essential to guide the application and evaluation of PLS in industrial contexts. Traditional IT-centric risk models often fail to capture the physical impact and unique attack vectors of CPS, such as manipulation of sensor data or control logic to cause physical damage [448]. Integrated frameworks are therefore proposed to holistically assess cyber-physical risks. These include optimization-based frameworks that model attacker objectives—such as maximizing physical system failure time while avoiding detection—to identify worst-case attack strategies and system vulnerabilities [403]. Other approaches extend traditional safety engineering methods; for example, Cyber Layer of Protection Analysis (CLOPA) integrates security failures into the established safety risk assessment framework (LOPA), providing a quantitative method to evaluate the trade-offs between reliability and security in CPS design [449]. For IIoT ecosystems, specialized threat modeling frameworks are being developed to automate risk assessment, accounting for the convergence of IT and Operational Technology (OT) networks and the large-scale, heterogeneous nature of connected devices [450] [210]. These frameworks often utilize attack graphs to model lateral movement and prerequisite conditions, enabling heuristic approaches to select optimal countermeasures under budget constraints [451].

Despite these advances, a significant gap persists between the promise of theoretical PLS and its practical, standardized deployment in industry. Many PLS techniques, such as those leveraging Reconfigurable Intelligent Surfaces (RIS) for beamforming or artificial noise, are validated in controlled, idealized channel conditions that do not reflect the complex, reflective, and dynamic environments of factories or power plants. The practical integration of PLS with existing industrial communication protocols (e.g., PROFINET, Modbus) and legacy devices, which were designed without security considerations, remains a formidable challenge [9]. Furthermore, while security frameworks and architectural patterns are proposed—such as Defence-in-Depth (DiD) strategies combined with lightweight, end-to-end encryption for IIoT [15] or dual-MCU architectures for resilient PLC operation [452]—there is a lack of industry-wide standards specifying how and where PLS mechanisms should be incorporated. The validation of PLS-based intrusion detection systems (IDS) also faces practical hurdles, including the scarcity of comprehensive, well-labeled attack datasets that capture both network traffic and physical process behavior [453], and the difficulty in tuning these systems for real-world deployment where extensive malicious training data is hard to acquire [454]. Ultimately, bridging this gap requires closer collaboration between the PLS research community and industrial practitioners, a focus on developing PLS solutions that are compatible with industrial lifecycle and certification processes [455], and the continued evolution of high-fidelity, accessible testbeds that can demonstrate the tangible security benefits of PLS under realistic operational constraints.

**Table: Comparison of approaches in 6.6 Testbeds, Experimental Validation, and Security Frameworks for Industrial PLS**

| Method/Model Name | Primary Purpose/Function | Key Features/Approach | Reference |
| :--- | :--- | :--- | :--- |
| ICS/IIoT Testbeds (e.g., physical replicas) | Provide experimental platforms for validating PLS and security techniques in realistic industrial environments. | High-fidelity physical replicas of critical infrastructure (e.g., chemical reactors, water plants). | [443] |
| ICSSIM Framework | Build scalable, virtualized ICS security testbeds for safe investigation of attacks and defenses. | Framework for building customizable, reproducible, low-cost simulation testbeds using Docker containerization. | [444] |
| MiniCPS Toolkit | Enable security research on CPS networks by emulating network and control-layer interactions. | Lightweight real-time network emulation (builds on Mininet) with APIs for physical-layer interaction and industrial protocol simulation (Ethernet/IP, Modbus/TCP). | [445] |
| ICS Cybersecurity Testbed Maturity Model (ICS-CTM2) | Assess and compare the maturity and credibility of ICS testbeds. | Evaluates testbeds across domains like architectural coverage, fidelity, and support for security experimentation. | [446] |
| Digital Twins (e.g., EPICTWIN) | Enable safe cyber security testing, research, and education without risking physical infrastructure. | Digital replicas (twins) of physical systems (e.g., smart grid) for deploying attacks/countermeasures; can be enhanced with blockchain for data integrity. | [447], [410] |
| Optimization-based Cyber-Physical Risk Assessment Framework | Identify worst-case attack strategies and system vulnerabilities by modeling attacker objectives. | Integrates cyber and physical systems; models attacks aiming to maximize physical impact (failure time) while avoiding detection and respecting resource constraints. | [403] |
| Cyber Layer of Protection Analysis (CLOPA) | Integrate security failures into safety risk assessment for CPS design. | Extends the LOPA safety framework to include failures from cyber-attacks, providing a quantitative method to evaluate reliability-security trade-offs. | [449] |
| Model-Based Risk Assessment for CPS | Holistically assess cyber-physical risks by identifying physical threats to guide cyber attack scenario analysis. | Uses hybrid automaton for physical system modeling and network/data flow models for cyber system analysis, validated on real-world testbeds. | [448] |
| Specialized IIoT Threat Modeling Frameworks (e.g., TMAP) | Automate risk assessment for IIoT ecosystems, accounting for IT/OT convergence. | Utilize attack graphs to model lateral movement and prerequisite conditions for heuristic countermeasure selection under budget constraints. | [450], [210], [451] |
| Defence-in-Depth (DiD) with Lightweight Encryption | Provide end-to-end security for IIoT/Industry 4.0 networks. | Combines multi-layered DiD strategies with lightweight encryption algorithms (e.g., Attribute-Based Encryption, OSCORE) for E2E security. | [15] |
| Secure Dual-MCU Architecture | Ensure resilient communication and control for IIoT devices like PLCs under attack. | Uses a dual microcontroller unit (MCU) setup to separate and protect control functions from network communication, ensuring operational resilience. | [452] |


## 7 Cross-Layer Integration, Implementation, and Practical Challenges

This section examines the practical deployment of PLS, bridging theory and practice. It discusses the integration of PLS with higher-layer protocols and network architectures. It analyzes critical implementation challenges, including hardware imperfections, scalability, and the security vs. performance trade-offs. It also reviews experimental testbeds and prototype implementations.

### 7.1 Integration with Higher-Layer Protocols and Network Architectures

The efficacy of physical layer security (PLS) in industrial wireless networks is not determined in isolation but is profoundly shaped by its integration with the established protocol stacks governing medium access, routing, and transport. For resource-constrained Industrial Internet of Things (IIoT) devices, a purely additive security layer is often infeasible. Therefore, a synergistic, cross-layer approach is essential, where PLS mechanisms are embedded within or carefully coordinated with higher-layer protocol operations to enhance end-to-end security, manage overhead, and ensure interoperability.

At the Medium Access Control (MAC) layer, deterministic protocols like IEEE 802.15.4e Time Slotted Channel Hopping (TSCH) and the IETF 6TiSCH stack are foundational for industrial low-power wireless networks, providing reliability and low latency. Integrating PLS with these scheduled MACs presents unique opportunities and challenges. The time-slotted, channel-hopping nature of TSCH can be leveraged to enhance secrecy. For instance, the schedule itself can be designed to incorporate **friendly jamming** techniques, where specific slots or channels are allocated for transmitting artificial noise towards potential eavesdropper directions, as conceptualized in works like [41]. This jamming traffic must be meticulously scheduled to avoid interfering with legitimate communications, a task that can be optimized by the 6TiSCH scheduling function. Furthermore, the Enhanced Minimal Scheduling Function (EMSF) proposed in [456], which reduces control overhead and latency, could be extended to dynamically adjust schedules based on physical-layer security metrics, such as real-time estimations of eavesdropper presence or channel reciprocity for key generation. The integration of Software-Defined Networking (SDN) principles, as explored in [457], allows for centralized, intelligent orchestration where a controller can dynamically allocate "secure tracks" for sensitive data flows, applying PLS strategies like beamforming or artificial noise on a per-flow basis while isolating control overhead to prevent degradation of application performance.

The routing layer, particularly the Routing Protocol for Low-Power and Lossy Networks (RPL), is another critical integration point. RPL is the *de facto* standard for constructing routing topologies (DODAGs) in IIoT networks but is notoriously vulnerable to insider attacks like selective forwarding, sinkholes, and rank manipulation, as extensively documented in [458], [459], and [460]. PLS can complement cryptographic authentication in RPL by providing continuous, lightweight trust metrics. **Physical-layer authentication** and **RF fingerprinting** techniques, which identify devices based on unique hardware imperfections in their transmitted signals, can be used to verify the identity of neighboring nodes during parent selection and route maintenance, mitigating spoofing attacks. For example, a node could use RF fingerprinting to ensure that control messages like DIO or DAO advertisements are indeed from a legitimate neighbor and not from a malicious clone, addressing threats like the CloneID attack. Moreover, PLS-generated secret keys, derived from shared channel characteristics, can be used to secure RPL control messages more efficiently than traditional asymmetric cryptography. The **Chained Secure Mode (CSM)** framework proposed in [461] and extended to 6LoWPAN in [462] exemplifies this integration. It uses network coding principles to create a chain of trust along the routing path, providing immediate-sender authentication for fragments and control packets, thereby defending against buffer-reservation and replay attacks at the adaptation layer. This demonstrates how a PLS-inspired construct can be woven directly into the routing protocol's operation to enhance resilience.

Integration with transport and application layer protocols is crucial for achieving end-to-end security semantics. Lightweight protocols like the Constrained Application Protocol (CoAP) are standard in IoT. Traditionally, CoAP relies on Datagram Transport Layer Security (DTLS) for security, but the session establishment and maintenance overhead can be prohibitive. PLS offers two complementary paths. First, PLS can **offload key establishment**. Protocols like Ephemeral Diffie-Hellman Over COSE (EDHOC), used to establish keys for Object Security for Constrained RESTful Environments (OSCORE), can be accelerated or made more robust by using physical-layer secret key generation (SKG) to seed or augment the key agreement process, as studied in works like [409]. Second, for ultra-constrained scenarios, **physical-layer encryption (PLE)** schemes like Grain-128PLE, proposed in [385], can provide a layer of confidentiality directly at the PHY, sitting between channel coding and modulation. This can be particularly valuable for protecting data in transit before it reaches a gateway that may terminate a DTLS session. The concept of blending security for storage and communication, as in [463], highlights a system-level view where cryptographic operations are minimized. PLS-generated keys could be the foundation for such blended security objects, reducing the need for redundant cryptographic primitives across layers.

Furthermore, the emergence of Information-Centric Networking (ICN) paradigms for IoT, as seen in [464] and [465], introduces a different architectural model where security is bound to content rather than connections. PLS integrates naturally here by securing the content at the point of wireless transmission. ICN's inherent stateful forwarding and caching can also interact with PLS; for instance, a cached data packet in an untrusted node could be re-encrypted using a locally generated PLS key when forwarded to the next hop, providing a form of link-layer security that aligns with ICN's hop-by-hop trust model. This is contrasted with traditional IP-based approaches in studies like [466], which show the robustness benefits of ICN's stateful data plane—a robustness that can be further hardened with PLS techniques against jamming or eavesdropping on wireless links.

However, successful integration is fraught with practical challenges. The primary concern is **overhead management**. PLS techniques like channel estimation for SKG or the transmission of artificial noise consume time, energy, and spectral resources. In tightly scheduled networks like 6TiSCH, these activities must compete for scarce time slots. Solutions like [467] highlight the need for co-design, where the scheduling function is aware of the energy and latency costs of security operations. **Interoperability** is another major hurdle. Industrial networks are heterogeneous, containing legacy devices that may not support newer PLS techniques. Protocols must be designed to gracefully degrade, such as RPL operating in its Unsecured Mode while PLS-capable nodes employ additional protections. Finally, **dynamic network conditions**—mobility, interference, and fluctuating traffic loads—require adaptive PLS. Reinforcement learning-based approaches for congestion-aware routing, as in [468], could be extended to also adapt PLS parameters, like jamming power or key generation rate, based on the perceived security threat level and available network resources. In conclusion, the true potential of PLS in industrial wireless communications is unlocked not as a standalone solution, but through its careful, co-designed integration with MAC, routing, and application protocols, creating a resilient, efficient, and holistic security fabric for the critical IIoT ecosystem.

**Table: Comparison of approaches in 7.1 Integration with Higher-Layer Protocols and Network Architectures**

| Layer / Protocol | Integration Point / PLS Technique | Key Concept / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| MAC (IEEE 802.15.4e TSCH / 6TiSCH) | Friendly Jamming | Scheduling artificial noise in specific slots/channels towards eavesdropper directions, orchestrated by SDN. | [41] |
| MAC (IEEE 802.15.4e TSCH / 6TiSCH) | Dynamic Schedule Adjustment | Extending scheduling functions (e.g., EMSF) to adjust schedules based on real-time PLS metrics like eavesdropper presence. | [456] |
| MAC (IEEE 802.15.4e TSCH / 6TiSCH) | SDN Orchestration & Layer-2 Slicing | Using SDN to centrally allocate secure "tracks" for sensitive flows, applying PLS per-flow and isolating control overhead. | [457] |
| Routing (RPL) | Physical-Layer Authentication & RF Fingerprinting | Using unique hardware RF fingerprints to verify neighbor identity during parent selection, mitigating spoofing (e.g., CloneID). | [458], [459], [460] |
| Routing (RPL) & Adaptation (6LoWPAN) | Chained Secure Mode (CSM) | Using network coding to create a chain of trust for immediate-sender authentication of fragments/control packets, defending against buffer-reservation attacks. | [461], [462] |
| Transport/Application (CoAP/OSCORE) | Key Establishment Offload | Using physical-layer secret key generation (SKG) to seed/augment key agreement protocols like EDHOC for OSCORE. | [409] |
| Physical Layer | Physical-Layer Encryption (PLE) | Implementing encryption (e.g., Grain-128PLE) between channel coding and modulation for link-layer confidentiality. | [385] |
| Application (Storage & Communication) | Blended Security | Using PLS-generated keys as a foundation for blended security objects that unify secure storage and communication, minimizing crypto overhead. | [463] |
| Network Architecture (ICN) | Content-Centric PLS | Securing content at the point of wireless transmission; using ICN's stateful forwarding to enable hop-by-hop re-encryption with PLS keys. | [464], [465], [466] |
| Cross-Layer (Scheduling & Routing) | Co-Design for Overhead Management | Co-designing scheduling and routing functions to balance control packet distribution and manage energy/latency costs of PLS operations. | [467] |
| Cross-Layer (Routing) | Adaptive PLS via Reinforcement Learning | Extending reinforcement learning-based congestion-aware routing to adapt PLS parameters (jamming power, key gen rate) based on threat level and resources. | [468] |


### 7.2 Convergence with Software-Defined Networking (SDN) and Time-Sensitive Networking (TSN)

The convergence of Software-Defined Networking (SDN) and Time-Sensitive Networking (TSN) with physical layer security (PLS) represents a paradigm shift towards programmable, deterministic, and secure industrial wireless communications. SDN’s architectural principle of decoupling the control plane from the data plane provides a centralized, global view of the network, enabling the orchestration of sophisticated PLS mechanisms that were previously difficult to coordinate in a distributed manner. This programmability allows for the implementation of *network-controlled physical-layer security*, where the SDN controller can dynamically optimize security parameters based on real-time network state and threat intelligence. For instance, the controller can execute intelligent access point (AP) selection algorithms and coordinate *friendly jamming* strategies across multiple nodes to maximize secrecy capacity, as explored in [41]. By treating jamming sources and beamforming parameters as programmable network resources, the SDN controller can solve optimization problems to allocate artificial noise precisely, degrading eavesdropper channels while minimizing interference to legitimate users. This centralized control is particularly potent in complex industrial environments with multiple potential eavesdroppers and dynamic channel conditions, moving PLS from a static, link-by-link approach to an adaptive, network-wide security service.

The stringent requirements of industrial applications, however, demand more than just adaptive security; they require guaranteed performance bounds on latency and reliability. This is where TSN, a set of IEEE 802.1 standards that extend Ethernet for deterministic real-time communication, becomes critical. TSN provides mechanisms like scheduled traffic (IEEE 802.1Qbv) and frame replication and elimination for reliability (FRER, IEEE 802.1CB) to ensure packets are delivered within a bounded latency and with extremely high reliability [469]. Integrating PLS with TSN creates the foundation for *secure ultra-reliable low-latency communications (URLLC)*. The challenge lies in ensuring that security enhancements, such as cryptographic processing or the introduction of friendly jamming signals, do not violate the deterministic timing guarantees. Architectural designs for this integration, such as Time-Sensitive Software-Defined Networking (TSSDN) for in-vehicle networks [442], demonstrate how control flows can be mapped to ensure SDN programmability without imposing delay penalties on time-critical TSN traffic. The SDN controller, aware of the TSN schedule (Gate Control Lists), can compute and deploy secure paths and PLS configurations during network planning or reconfiguration phases, ensuring that security policies are enforced within the strict temporal constraints of the industrial control loop.

A key technical challenge in this convergence is achieving and maintaining precise time synchronization, which is fundamental for both TSN's scheduled operations and certain PLS techniques like coordinated jamming. As highlighted in [470], mission-critical industrial automation may require device-level synchronization with jitter as low as 1 microsecond. The SDN control plane can play a vital role in managing and distributing synchronization protocols, but the wireless medium introduces variability. Therefore, PLS-TSN integration must employ robust synchronization mechanisms that are resilient to jamming and other attacks targeting timing protocols. Furthermore, the reconfiguration of security parameters or network paths must be executed in a manner that preserves state consistency and does not introduce transient violations of latency or reliability. The use of a *synchronous transaction model* for network reconfigurations, as evaluated in [471], ensures that updates to forwarding rules and security policies are applied atomically across all switches, maintaining deterministic behavior for time-sensitive flows during changes.

The advent of *programmable data planes*, exemplified by languages like P4, further amplifies the potential of this convergence. Moving beyond simple packet forwarding, programmable switches can execute in-network algorithms for security monitoring, lightweight encryption, or physical-layer key distillation at line rate. This enables *intra-cellular optimization* and other in-network processing that can drastically reduce latency by bypassing the core network for localized industrial communication, as proposed in [472]. For PLS, programmable data planes can implement fast reaction mechanisms, such as instantly activating pre-computed backup paths with specific beamforming or jamming settings upon detecting a potential eavesdropping threat or link failure, a concept akin to accelerating recovery in [473]. This fusion of data plane programmability with SDN control and TSN determinism allows for the creation of highly adaptive yet predictable industrial networks. Security functions become deeply embedded in the network fabric, capable of responding to threats at the speed of the data plane while being governed by the holistic, policy-driven intelligence of the control plane, all within the rigid temporal framework guaranteed by TSN, thereby realizing the vision of secure, ultra-reliable, and low-latency wireless industrial communications.

**Table: Comparison of approaches in 7.2 Convergence with Software-Defined Networking (SDN) and Time-Sensitive Networking (TSN)**

| Aspect | SDN & PLS Integration | TSN & Deterministic Guarantees | Programmable Data Planes (e.g., P4) |
| :--- | :--- | :--- | :--- |
| **Core Concept** | SDN's centralized control enables orchestration of network-wide physical-layer security (PLS) mechanisms, such as intelligent AP selection and coordinated friendly jamming. | TSN standards (e.g., IEEE 802.1Qbv, 802.1CB) provide deterministic latency and ultra-high reliability for time-critical industrial traffic. | Programmable switches execute in-network algorithms (e.g., security monitoring, key distillation) at line rate, enabling low-latency, localized processing. |
| **Primary Benefit** | Enables adaptive, network-controlled PLS, moving from static, link-by-link security to a dynamic, optimized service based on real-time network state. | Provides the foundation for secure Ultra-Reliable Low-Latency Communications (URLLC) by guaranteeing strict performance bounds. | Drastically reduces latency via intra-cellular optimization and enables fast reaction mechanisms (e.g., instant path switching) for security and recovery. |
| **Key Challenge** | Coordinating security mechanisms (e.g., jamming) without violating the network's performance or creating new vulnerabilities from the centralized control plane. | Ensuring that security enhancements (e.g., crypto, jamming) do not violate the deterministic timing and reliability guarantees of TSN schedules. | Designing and verifying correct, secure in-network programs and ensuring state consistency during reconfigurations. |
| **Integration/Synergy** | The SDN controller can compute and deploy secure paths and PLS configurations in alignment with the TSN schedule (Gate Control Lists) during planning phases. | Architectural designs like Time-Sensitive Software-Defined Networking (TSSDN) map control flows to maintain SDN programmability without penalizing TSN traffic latency. | Fuses data plane programmability with SDN control and TSN determinism, embedding security functions into the network fabric for adaptive yet predictable operations. |
| **Supporting Reference** | [41] | [469]; [442] | [472]; [473] |
| **Cross-Cutting Theme** | **Time Synchronization**: Critical for both coordinated jamming (PLS) and TSN schedules. Requires robust, attack-resilient mechanisms as highlighted in [470]. | **Consistent Reconfiguration**: Updates to security and forwarding rules must preserve deterministic behavior. A *synchronous transaction model* can ensure atomic updates, as in [471]. | **In-Network Processing**: Enables localized decision-making and action, reducing dependency on the core network and controller, thus supporting both low latency and security responsiveness. |


### 7.3 Hardware Imperfections, Channel Estimation Errors, and Real-World Constraints

The theoretical performance of physical layer security (PLS) techniques, often derived under ideal assumptions of perfect hardware and instantaneous, flawless channel knowledge, faces significant degradation when confronted with the non-idealities of real-world industrial deployments. A critical gap exists between the promise of information-theoretic security and its practical realization, primarily due to hardware imperfections, imperfect channel state information (CSI), and quantized signal processing. These constraints introduce irreducible error floors, create complex performance-security trade-offs, and necessitate the development of robust design methodologies.

**Hardware Imperfections** constitute a fundamental challenge, as transceivers and passive components inevitably deviate from their ideal models. In reconfigurable intelligent surface (RIS)-aided systems, which are pivotal for enhancing PLS, phase noise and discrete phase shifting introduce significant errors. Research in [474] demonstrates that while increasing the number of RIS elements improves secrecy outage probability (SOP), the gain diminishes due to these phase errors. Notably, random discrete phase shifting can match or even outperform imperfect coherent phase shifting in terms of the probability of non-zero secrecy capacity, offering a lower-complexity alternative. Beyond RIS, transceiver hardware impairments (HWI)—such as amplifier non-linearities, in-phase/quadrature (I/Q) imbalance, and oscillator phase noise—distort transmitted and received signals. The work in [475] reveals that HWI leads to non-zero lower bounds on outage probability and symbol error rate in the high signal-to-noise ratio (SNR) regime, a stark contrast to the asymptotically zero error achievable with ideal hardware. This "ceiling effect" is further analyzed in [199], which shows that residual hardware impairments (RHIs) have a more severe negative impact on reliability (outage probability) than channel estimation errors, though they can paradoxically improve security (intercept probability) by degrading the eavesdropper's channel as well. Similarly, [476] confirms that I/Q mismatches limit reliability but can enhance security performance. The cumulative effect of these imperfections is severe, as shown in [477], where the joint impact of transceiver HWI, RIS phase noise, and imperfect CSI creates an irreducible mean-square-error floor.

**Imperfect Channel State Information** is arguably the most pervasive constraint. PLS techniques like beamforming, artificial noise (AN) generation, and RIS phase optimization are highly sensitive to the accuracy of CSI for both legitimate and eavesdropping links. In industrial settings, obtaining perfect CSI, especially for passive eavesdroppers, is impossible. Feedback delays, estimation errors, and limited pilot resources lead to outdated and inaccurate CSI. The survey [478] comprehensively outlines this challenge and various mitigation strategies. The impact is quantifiable: [193] derives explicit secrecy outage capacity expressions for AF and DF relaying under imperfect legitimate CSI and no eavesdropper CSI, showing clear performance penalties. [479] quantifies the degradation in SOP due to using outdated eavesdropper CSI in sensor scheduling, highlighting a key vulnerability. The problem is exacerbated in systems with stringent latency requirements; [160] investigates the joint reliability-security trade-off for short packets, where the finite blocklength limits the resources available for accurate channel estimation. Robust design is therefore essential. [340] formulates a robust beamforming problem that minimizes transmit power subject to an outage probability constraint, using statistical CSI error models and semidefinite programming to ensure performance guarantees. [480] leverages extreme value theory to design precoders that compensate for channel estimation error uncertainty with minimal power, ensuring reliability for ultra-reliable low-latency communications.

**Quantized Signal Processing and Real-World System Constraints** further limit performance. Practical systems employ digital-to-analog converters, analog-to-digital converters, and low-resolution phase shifters with finite precision. [481] addresses the fronthaul load problem by using few-bit vector quantization for CSI, showing that exploiting spatial correlation can maintain estimation accuracy under severe bit constraints. Similarly, phase shifts in RIS are often constrained to discrete values from a finite set. The study [482] establishes that rotated phase-shift keying is capacity-achieving for channels with phase-quantized outputs, providing a fundamental limit for such systems. Furthermore, protocols themselves impose constraints. Experimental analysis in [483] demonstrates that control channel structures in 4G LTE have varying resilience to targeted interference, with cell-specific reference signals being particularly vulnerable. This underscores that PLS must be evaluated within the specific framing and resource allocation rules of the deployed wireless standard.

To combat these challenges, **robust optimization frameworks and cross-layer techniques** are paramount. The core approach involves designing PLS schemes that explicitly account for imperfection models during optimization. This often leads to complex, non-convex problems solved via iterative algorithms like alternating optimization, majorization-minimization, and semidefinite relaxation, as seen in [477] and [484]. A key insight is the need to balance resource allocation. For instance, [180] shows that joint relay and jammer selection improves effective secrecy throughput but is more sensitive to feedback delays than traditional best relay selection, indicating a trade-off between performance gain and robustness. Similarly, [485] proposes a novel scheme that intentionally sacrifices some CSI acquisition to reduce pilot overhead, then uses rate splitting to manage the resulting interference, ultimately improving net throughput. The performance-security trade-off is also evident in power allocation. [199] identifies a trade-off where parameters that improve reliability (e.g., reducing AN power) can degrade security, and vice versa. Ultimately, as summarized in [91], system design must ensure that the number of low-cost RIS elements or base station antennas scales appropriately to counteract the performance loss from HWI and imperfect CSI, preserving a positive ergodic secrecy rate.

In conclusion, bridging the gap between PLS theory and industrial practice requires a paradigm shift towards robust, imperfection-aware design. The idealized assumptions of perfect hardware and CSI must be abandoned in favor of statistical models that capture phase errors, hardware non-linearities, estimation inaccuracies, and quantization effects. Future research must continue to develop low-complexity robust algorithms, explore the integration of machine learning for adaptive compensation of these imperfections, and validate proposed schemes through real-world experimental testbeds that fully embody these challenging constraints.

**Table: Comparison of approaches in 7.3 Hardware Imperfections, Channel Estimation Errors, and Real-World Constraints**

| Challenge Category | Specific Issue / Imperfection | Key Finding / Impact | Mitigation Strategy / Design Insight | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Hardware Imperfections | Phase noise & discrete phase shifting in RIS | Increasing RIS elements improves SOP, but gains diminish due to phase errors. Random discrete phase shifting can match/outperform imperfect coherent shifting for PNZ with lower complexity. | Use random discrete phase shifting as a lower-complexity alternative to imperfect coherent phase shifting. | [474] |
| Hardware Imperfections | Transceiver Hardware Impairments (HWI) | HWI leads to non-zero lower bounds on outage probability and SER in high SNR, creating a "ceiling effect" unlike ideal hardware. | Design must account for irreducible error floors in high SNR regimes. | [475] |
| Hardware Imperfections | Residual Hardware Impairments (RHIs) | RHIs have a more severe negative impact on reliability (outage probability) than channel estimation errors, but can paradoxically improve security (intercept probability) by degrading the eavesdropper's channel. | Recognize the reliability-security trade-off; parameters improving one may degrade the other. | [199] |
| Hardware Imperfections | I/Q Imbalance | I/Q mismatches limit reliability but can enhance security performance. | Consider hardware imperfections as a double-edged sword in system design. | [476] |
| Hardware Imperfections | Joint HWI, RIS phase noise, and imperfect CSI | The joint impact creates an irreducible mean-square-error floor. | Robust beamforming design is essential to mitigate cumulative imperfections. | [477] |
| Imperfect Channel State Information | General imperfect CSI for PLS techniques | PLS techniques like beamforming, AN, and RIS optimization are highly sensitive to CSI accuracy. Obtaining perfect CSI, especially for eavesdroppers, is impossible. | Employ robust design and mitigation strategies outlined in surveys. | [478] |
| Imperfect Channel State Information | Imperfect legitimate CSI & no eavesdropper CSI in MIMO relaying | Derives explicit secrecy outage capacity expressions, showing clear performance penalties for AF and DF relaying. | Quantify performance loss under practical CSI assumptions. | [193] |
| Imperfect Channel State Information | Outdated eavesdropper CSI in sensor scheduling | Quantifies degradation in SOP due to using outdated CSI, highlighting a key vulnerability. | Scheduling schemes must account for CSI aging. | [479] |
| Imperfect Channel State Information | Finite blocklength limits in URLLC | The joint reliability-security trade-off for short packets is investigated, where finite blocklength limits resources for accurate channel estimation. | Optimize resource allocation under short packet constraints; counter-intuitively allocating fewer resources can enhance performance. | [160] |
| Imperfect Channel State Information | Statistical CSI error models for robust design | Formulates a robust beamforming problem minimizing transmit power subject to an outage probability constraint using SDP. | Use statistical error models and convex optimization for performance guarantees. | [340] |
| Imperfect Channel State Information | Channel estimation error uncertainty in URLLC | Leverages extreme value theory to design precoders that compensate for error uncertainty with minimal power. | Apply statistical extreme value theory for robust, low-power precoding. | [480] |
| Quantized Signal Processing | Few-bit vector quantization for CSI in cell-free massive MIMO | Exploiting spatial correlation can maintain CSI estimation accuracy under severe fronthaul bit constraints. | Use spatial correlation to improve efficiency of quantized CSI feedback. | [481] |
| Quantized Signal Processing | Discrete phase shifts in RIS / phase-quantized outputs | Rotated phase-shift keying is capacity-achieving for channels with phase-quantized outputs, providing a fundamental limit. | Use optimal modulation schemes (rotated PSK) for quantized systems. | [482] |
| Quantized Signal Processing | Protocol-specific constraints (e.g., 4G LTE control channels) | Control channel structures have varying resilience to targeted interference, with cell-specific reference signals being particularly vulnerable. | PLS evaluation must consider specific framing and resource allocation rules of the deployed standard. | [483] |
| Robust Optimization & Cross-Layer Techniques | Joint relay and jammer selection (JRJS) with feedback delays | JRJS improves effective secrecy throughput but is more sensitive to feedback delays than traditional best relay selection. | Trade-off exists between performance gain and robustness to CSI delays. | [180] |
| Robust Optimization & Cross-Layer Techniques | Sacrificing CSI for reduced pilot overhead | Proposes sacrificing some CSI acquisition to reduce overhead, then using rate splitting to manage resulting interference, improving net throughput. | Balance CSI accuracy with overhead; use interference-aware techniques like rate splitting. | [485] |
| Robust Optimization & Cross-Layer Techniques | Scaling of low-cost RIS elements/antennas | System design must ensure the number of RIS elements or BS antennas scales appropriately to counteract performance loss from HWI and imperfect CSI. | Scale system dimensions (antennas, RIS elements) to preserve a positive ergodic secrecy rate. | [91] |


### 7.4 Scalability, Overhead, and Performance Trade-offs in Large-Scale Deployments

The transition from theoretical physical layer security (PLS) schemes to their practical deployment in large-scale Industrial Internet of Things (IIoT) environments introduces a complex web of scalability challenges, signaling overhead, and critical performance trade-offs. While PLS techniques like artificial noise (AN) beamforming, reconfigurable intelligent surface (RIS) optimization, and physical-layer key generation (PLKG) offer promising low-latency security, their resource demands can become prohibitive when scaled to thousands of resource-constrained devices. The core challenge lies in managing the inherent tension between the intensity of security measures and the stringent performance metrics—throughput, latency, reliability, and energy efficiency—mandated by industrial applications.

A primary scalability bottleneck is the control signaling and coordination overhead required for dynamic PLS. Techniques like optimal friendly jamming and transmit power allocation in RIS-assisted secure communication or joint precoding and phase shift design for secret key generation necessitate frequent channel state information (CSI) acquisition and configuration updates. In a massive IIoT deployment with sporadic traffic, such as those using NarrowBand IoT or LoRaWAN [486] [487], the energy and bandwidth cost of continuously estimating channels for thousands of devices and configuring hundreds of RIS elements can erode the net system efficiency. This overhead is exacerbated in cell-free massive MIMO systems supporting URLLC, where rigorous resource allocation algorithms must solve non-convex optimization problems to jointly optimize pilot and payload power under finite blocklength constraints [437]. The computational complexity of these centralized algorithms may not scale linearly with the number of access points and devices.

This directly leads to the critical trade-off between security intensity and network performance. Allocating more power to artificial noise to degrade an eavesdropper's channel inherently reduces the power available for the legitimate data signal, potentially lowering the achievable data rate and increasing the secrecy outage probability for devices at the cell edge. Similarly, increasing the rate of PLKG to enhance secrecy requires more channel probing packets, consuming bandwidth and energy that could be used for data transmission, and increasing the collision probability in shared media. Studies on cross-layer optimization for battery-powered IoT devices highlight that reliability constraints and non-ideal hardware significantly reduce the energy-optimal range of communication [488]. A security-driven increase in transmit power or retransmissions to meet a target secrecy outage probability can drastically shorten network lifetime, conflicting with the durability goals of IIoT deployments [489].

Furthermore, the quest for ultra-reliability and low latency (URLLC) in critical industrial control loops often clashes with the procedural delays of PLS. Secure short-packet transmissions, essential for IIoT, are particularly sensitive to these trade-offs. Proactive Hybrid Automatic Repeat reQuest (HARQ) with feedback prediction can improve energy efficiency, but its gains are sensitive to the processing delay of the prediction mechanism itself [490]. In a tightly synchronized 6TiSCH network, the additional latency from executing PLKG protocols or computing secure beamforming weights could violate the deterministic deadlines required for control packet delivery [491]. The need for distributed and low-latency scheduling to support network dynamics, as explored in [492], is complicated by the additional computational burden of security algorithms at each node.

Scalability also concerns the efficient utilization of spectral and energy resources. In heterogeneous networks with coexisting Human-to-Human (H2H) and critical Machine-to-Machine (M2M) traffic, introducing PLS mechanisms like simultaneous wireless information and power transfer (SWIPT) for energy harvesting adds a new dimension to resource allocation [493]. The multi-agent deep reinforcement learning approach needed to manage spectrum, power, and power-splitting ratios must now also account for secrecy rate constraints, increasing the state-action space and training complexity. Similarly, in ultra-dense networks, joint device association, computation offloading, and resource allocation to minimize network-wide energy consumption [494] becomes even more challenging when security constraints dictate that certain offloading paths or resource blocks must be avoided to prevent eavesdropping.

Finally, the management overhead extends to the lifecycle of the IIoT system. Reliable firmware updates over large-scale mesh networks are a routine but critical operation for maintaining security [495]. The process of securely distributing new cryptographic keys or PLS algorithm parameters to a vast fleet of devices must itself be scalable and not overwhelm the network. The performance investigation in such scenarios, measuring join time and throughput, provides essential insight into how the network behaves under this massive control plane load. Moreover, achieving resiliency at the IoT edge often requires leveraging multi-communication networks (e.g., LPWAN and Wi-Fi) [496]. Integrating PLS across these heterogeneous interfaces, each with different bandwidth, latency, and power characteristics, requires a unified yet lightweight security management framework that can operate within the mixed-criticality QoS requirements of diverse IIoT applications.

In conclusion, the successful large-scale adoption of PLS in industry hinges on developing adaptive and lightweight mechanisms that explicitly optimize the trade-off surface between security intensity and performance overhead. This necessitates cross-layer designs where security parameters are dynamically tuned based on real-time channel conditions, traffic criticality, and device energy state. Machine learning, particularly distributed reinforcement learning as seen in [497] and [498], offers a promising pathway for devices to autonomously learn near-optimal security policies with minimal signaling overhead. Furthermore, leveraging lightweight authentication like RF fingerprinting and efficient key generation from one-bit quantized CSI [499] can reduce procedural complexity. Ultimately, the scalability of PLS will be determined by its ability to seamlessly integrate into the resource-constrained, latency-sensitive, and ultra-reliable fabric of future industrial wireless systems without becoming the bottleneck it aims to protect against.

**Table: Comparison of approaches in 7.4 Scalability, Overhead, and Performance Trade-offs in Large-Scale Deployments**

| Method/Model | Key Idea | Advantages | Limitations/Challenges | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Artificial Noise (AN) Beamforming | Adds artificially generated noise to degrade eavesdropper's channel while preserving legitimate signal. | Promising low-latency security; effective in degrading eavesdropper's channel. | Reduces power available for data signal, lowering data rate and increasing secrecy outage probability; resource-intensive for scaling. | [203] |
| Reconfigurable Intelligent Surface (RIS) Optimization | Dynamically configures wireless propagation environment via software-controlled metasurfaces to enhance security. | Can create favorable signal paths for legitimate users and nulls for eavesdroppers; low power consumption. | Requires frequent CSI acquisition and configuration updates; high coordination overhead in massive deployments; complex joint precoding and phase shift design. | [437] |
| Physical-Layer Key Generation (PLKG) | Generates secret keys from shared wireless channel characteristics (e.g., CSI). | Offers low-latency, lightweight security; suitable for resource-constrained devices. | Requires frequent channel probing, consuming bandwidth and energy; increases collision probability in shared media; procedural delays can violate URLLC deadlines. | [499] |
| Simultaneous Wireless Information and Power Transfer (SWIPT) | Enables devices to harvest energy and decode information from the same RF signal. | Improves energy sustainability for battery-powered IoT devices; supports energy-constrained networks. | Complicates resource allocation; multi-agent DRL needed to manage spectrum, power, and power-splitting ratios increases state-action space and training complexity. | [493] |
| Distributed Reinforcement Learning (e.g., DISNETS, MALoRa) | Uses multi-agent RL frameworks for autonomous, distributed resource allocation and security policy optimization. | Reduces signaling overhead; enables devices to learn near-optimal policies; improves scalability and energy efficiency. | Training complexity; requires careful design of reward functions and state spaces; performance sensitive to network dynamics and sporadic traffic. | [497], [498] |
| Lightweight Authentication (e.g., RF Fingerprinting) | Uses unique hardware imperfections or channel features for device authentication. | Reduces procedural complexity and latency; low computational overhead. | Accuracy can be affected by channel conditions and hardware variability; may require initial profiling phase. | [499] |
| Cross-Layer Optimization (e.g., for link parameters) | Jointly optimizes parameters across PHY and MAC layers (modulation, SNR, payload size, retransmissions) under constraints. | Improves energy efficiency and reliability trade-off; tailored to hardware non-idealities and application requirements. | Increased design complexity; optimal solutions may be non-convex and computationally heavy; requires accurate channel and hardware models. | [488] |
| Proactive HARQ with Feedback Prediction | Predicts ACK/NACK feedback to preemptively schedule retransmissions, reducing latency. | Improves energy efficiency and reliability for stringent latency budgets (e.g., 1-2 ms). | Gains sensitive to the processing delay of the prediction mechanism itself; adds implementation complexity. | [490] |


### 7.5 Experimental Testbeds, Prototype Implementations, and Security Validation

The transition of Physical Layer Security (PLS) from theoretical constructs to deployable solutions in industrial environments necessitates rigorous experimental validation. This process relies on specialized testbeds, prototype implementations, and comprehensive security assessment methodologies that bridge the gap between simulation and real-world deployment. Software-Defined Radio (SDR) platforms are foundational to this effort, offering the flexibility to prototype and test novel PLS waveforms and protocols. For instance, the Universal Software Radio Peripheral (USRP) platform has been used to implement time-slotted wireless systems for Industrial IoT, demonstrating that with careful synchronization and a "Just-in-Time" scheduling algorithm, SDRs can achieve the low latency and tight synchrony required for control applications like automated guided vehicles [500]. Similarly, SDRs are instrumental in vulnerability analysis, enabling researchers to develop protocol-aware interference waveforms to stress-test systems like 4G LTE, revealing that control channels such as Cell-Specific Reference signals are particularly susceptible to targeted jamming [483]. Tools like RFquack further lower the barrier to entry by combining the determinism of embedded RF frontends with software flexibility, creating a uniform toolkit for protocol security analysis that has been used to discover vulnerabilities in industrial RF devices [501].

For large-scale, repeatable, and high-fidelity experimentation, FPGA-based wireless network emulators represent the state of the art. The Colosseum emulator allows for real-time, hardware-in-the-loop emulation of complex scenarios with dozens of nodes. Frameworks like eSWORD integrate into Colosseum to enable safe, controlled, and large-scale studies of jamming attacks and countermeasures, providing patterns of throughput and signal degradation that closely match real-world over-the-air experiments [102]. The accuracy of such emulations is paramount, addressed by toolchains like CaST, which generate realistic mobile channel scenarios from ray-tracing models and use containerized SDR-based sounders to validate the emulated channel impulse responses with high precision on platforms like Colosseum [502]. These emulation capabilities are also critical for evaluating next-generation architectures like Open Radio Access Networks (Open RAN), where the security and performance impact of encrypting critical interfaces can be quantitatively assessed in full-stack, compliant implementations [503].

On the device and endpoint security side, Hardware-assisted Trusted Execution Environments (TEEs) have become a key platform for prototyping secure services. ARM TrustZone, widely available in industrial and IoT-grade processors, is frequently leveraged through open-source frameworks like OP-TEE. Researchers have used OP-TEE to implement and evaluate secure services, such as key-value stores, on common hardware like Raspberry Pi, assessing the performance and usability trade-offs for IoT applications [504]. The practicality of using TEEs for critical industrial components like Programmable Logic Controllers (PLCs) has been explored through proof-of-concept designs, evaluating performance and resource consumption in real-world ICS configurations [505]. Beyond TrustZone, innovative TEE designs are being prototyped on other hardware. BYOTee leverages the programmable logic of FPGAs to allow users to build customized, attested enclaves with a configurable hardware Trusted Computing Base (TCB) [506]. Similarly, TEEOD utilizes the programmable logic in heterogeneous SoCs to create physically isolated secure execution environments [507].

Security validation of these prototypes requires methodologies that go beyond functional testing. For PLS algorithms, particularly secret key generation (SKG), real-world eavesdropping challenges have been proposed to rigorously test security claims. One seminal work implemented a full SKG chain in indoor environments with a passive eavesdropper and publicly released the eavesdropper's dataset, ciphertexts, and software, inviting the community to attempt to break the system—a practice mirroring cryptographic challenges [382]. Performance benchmarking is equally critical, especially for resource-constrained environments. Tools like iperfTZ are developed specifically to uncover network performance bottlenecks in TrustZone-based trusted applications, providing essential data on throughput and energy consumption for edge deployments [508]. For TEEs themselves, benchmarking suites like SGXGauge provide a diverse set of workloads (e.g., blockchain, secure ML) to characterize performance overheads related to memory paging and interactions with the OS [509]. Furthermore, continuous monitoring frameworks like TEEMon are essential for diagnosing performance bottlenecks (e.g., excessive system calls) in TEE-based applications during runtime in production-like settings [510].

Finally, assessing full PLS protocol stacks in constrained environments is a significant challenge. This involves integrating PLS primitives with higher-layer security protocols. For example, research has combined lightweight protocols like OSCORE and EDHOC for end-to-end security in CoAP-based IoT, with implementations tailored for microcontrollers both with and without TrustZone-M, evaluating their RAM/FLASH footprint and energy consumption [511]. Similarly, holistic approaches integrate TEEs with standard communication middleware, such as implementing a fully attested MQTT broker within Intel SGX using WebAssembly to ensure portable and trustworthy distributed communication [512]. These integrative efforts highlight the cross-layer coordination required to move PLS from a link-level enhancement to a component of a comprehensive, practical security architecture for industrial wireless systems.

**Table: Comparison of approaches in 7.5 Experimental Testbeds, Prototype Implementations, and Security Validation**

| Category | Method / Tool / Framework | Primary Purpose / Contribution | Key Findings / Capabilities | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **SDR Prototyping & Vulnerability Analysis** | Universal Software Radio Peripheral (USRP) with custom scheduling | Prototyping time-slotted wireless IoT networks with low latency and tight synchrony | Achieved synchronization within ±0.05µs (90% of slots) and end-to-end latency down to 3.75ms, suitable for AGV control. | [500] |
| **SDR Prototyping & Vulnerability Analysis** | Open-source SDR tools for LTE PHY layer analysis | Vulnerability analysis and testing of 4G LTE under targeted interference | Identified Cell-Specific Reference signals (CRS) as most susceptible to protocol-aware jamming. | [483] |
| **SDR Prototyping & Vulnerability Analysis** | RFquack toolkit | Universal hardware-software toolkit for wireless protocol security analysis | Combines determinism of embedded RF frontends with software flexibility; used to discover 11 vulnerabilities in industrial RF devices. | [501] |
| **Large-Scale Network Emulation** | eSWORD framework integrated with Colosseum emulator | Safe, controlled, large-scale study of jamming attacks and countermeasures | Emulated jamming patterns in throughput and SNR degradation closely match real-world over-the-air experiments. | [102] |
| **Large-Scale Network Emulation** | CaST toolchain for Colosseum | Creating and characterizing realistic wireless network emulation scenarios | Achieves ≤20 ns accuracy in Channel Impulse Response tap delays and 0.5 dB accuracy in tap gains. | [502] |
| **Large-Scale Network Emulation** | Full-stack O-RAN implementation in Colosseum | Assessing security/performance impact of encrypting Open RAN interfaces | Provides quantitative insights into latency and throughput reduction from encrypting E2 and Open Fronthaul interfaces. | [503] |
| **Trusted Execution Environments (TEEs)** | OP-TEE framework on ARM TrustZone (e.g., Raspberry Pi) | Implementing and evaluating secure services (e.g., key-value store) for IoT | Assesses performance and usability trade-offs for IoT applications using common hardware. | [504] |
| **Trusted Execution Environments (TEEs)** | OP-TEE and OpenPLC proof-of-concept | Exploring practicality of ARM TrustZone TEE for securing Programmable Logic Controllers (PLCs) | Evaluates performance and resource consumption in real-world Industrial Control System configurations. | [505] |
| **Trusted Execution Environments (TEEs)** | BYOTee framework using FPGAs | Building customizable, attested enclaves with configurable hardware TCB | Allows users to create enclaves with customized hardware TCBs using commodity FPGAs. | [506] |
| **Trusted Execution Environments (TEEs)** | TEEOD design using FPGA programmable logic | Creating physically isolated secure execution environments on heterogeneous SoCs | Prototype can host multiple enclaves with physically isolated, on-chip execution. | [507] |
| **Security Validation & Benchmarking** | Full SKG chain implementation with public challenge dataset | Rigorous real-world testing of Secret Key Generation (SKG) security under eavesdropping | Released eavesdropper dataset and ciphertexts to invite community to break the system, mirroring cryptographic challenges. | [382] |
| **Security Validation & Benchmarking** | iperfTZ tool | Uncovering network performance bottlenecks for TrustZone-based trusted applications | Provides data on throughput and energy consumption trade-offs for edge deployments. | [508] |
| **Security Validation & Benchmarking** | SGXGauge benchmark suite | Comprehensive performance characterization for Intel SGX TEEs | Contains diverse workloads (blockchain, secure ML) to characterize overheads related to paging and OS interaction. | [509] |
| **Security Validation & Benchmarking** | TEEMon framework | Continuous performance monitoring and bottleneck diagnosis for TEE-based applications | Identifies causes of performance bottlenecks (e.g., excessive system calls) during runtime with 5-17% overhead. | [510] |
| **Integrated Protocol Stacks** | uOSCORE/uEDHOC libraries (with/without TEE) | Implementing end-to-end security (OSCORE & EDHOC) for CoAP-based IoT on constrained devices | Evaluates RAM/FLASH footprint and energy consumption on microcontrollers with and without TrustZone-M. | [511] |
| **Integrated Protocol Stacks** | WebAssembly-based broker in Intel SGX | Implementing a fully attested MQTT broker for portable, trustworthy distributed communication | Demonstrates a holistic approach integrating TEEs with standard middleware (MQTT, TLS). | [512] |


### 7.6 Cross-Layer Security Frameworks and Blockchain Integration

While physical layer security (PLS) provides a foundational, information-theoretic barrier against eavesdropping and jamming, its practical efficacy in complex industrial environments is significantly amplified when integrated into a holistic, cross-layer security architecture. These advanced frameworks unify PLS mechanisms with higher-layer cryptographic protocols, distributed trust systems, and hardware-rooted security to create resilient, end-to-end protection for industrial wireless networks. A key synergy exists between PLS and lightweight cryptographic protocols designed for resource-constrained Industrial Internet of Things (IIoT) devices. Traditional transport-layer security (TLS) is often too heavy for such devices and requires proxies to terminate secure channels, breaking end-to-end security. Protocols like Object Security for Constrained RESTful Environments (OSCORE) and Ephemeral Diffie-Hellman Over COSE (EDHOC), standardized by the IETF, offer a solution by providing application-layer security for CoAP messages. The integration point is potent: PLS can be used to generate the secret symmetric keys required by OSCORE. For instance, channel state information (CSI)-based key generation, potentially assisted by a Reconfigurable Intelligent Surface (RIS) to enhance randomness and key generation rate, can feed directly into the EDHOC key exchange protocol. This creates a hybrid key establishment where the initial cryptographic keys are derived from the physical properties of the wireless channel, adding an extra layer of security rooted in the communication medium itself. Research into implementing these protocols on microcontrollers with Trusted Execution Environments (TEEs), such as those featuring ARM TrustZone-M, demonstrates a further cross-layer hardening. By isolating the cryptographic operations and keys within a TEE, vulnerabilities in the application or operating system cannot compromise the key material, even if the key originated from a PLS process [511].

Beyond cryptographic integration, blockchain technology emerges as a powerful tool for establishing decentralized trust and auditability in industrial networks, particularly when managing network infrastructure itself. In Software-Defined Networking (SDN) for industrial settings, blockchain can secure critical control-plane functions. An intent-driven security SDN (IS2N) can leverage a blockchain middle-layer to immutably store network-level snapshots, device registration records, and OpenFlow messages, ensuring the integrity and non-repudiation of network commands and preventing malicious tampering with network policies [513]. This blockchain-backed transparency is crucial for collaborative security paradigms. For example, in Collaborative Intrusion Detection Systems (CIDS), where multiple IDS nodes share detection rules and alerts, a blockchain can serve as a tamper-resistant ledger to record shared rules, node reputation scores, and trust relationships. This prevents malicious nodes from poisoning the collaborative knowledge base and enables a decentralized trust mechanism, moving beyond the assumption of always-honest participants [514]. Similarly, blockchain can underpin federated learning (FL) systems in IIoT, where it provides a secure, immutable record for global model updates, participant contributions, and aggregation results, preventing model tampering and ensuring auditability [515].

The most robust cross-layer frameworks incorporate hardware-rooted trust via TEEs like Intel SGX or ARM TrustZone to protect the most sensitive operations. This is especially critical for industrial control logic and secure firmware updates. A TEE can create an isolated enclave to execute a Programmable Logic Controller's (PLC) control application, ensuring its integrity and confidentiality even if the host operating system is compromised. Proof-of-concept implementations using open-source TEE operating systems like OP-TEE demonstrate the feasibility of shielding PLC logic execution, though challenges remain regarding real-time performance and resource consumption on industrial-grade hardware [505]. For firmware updates, a TEE can perform secure attestation, verifying the authenticity and integrity of new firmware images before they are flashed onto a device. This process can be further anchored in a blockchain, where the hash of the authorized firmware is stored immutably. The TEE on the device can query the blockchain to verify the firmware signature against the recorded hash, creating a decentralized and verifiable update mechanism resistant to man-in-the-middle attacks. This concept of a hardware root of trust is extended in solutions like the Cryptographic Trust Center chip, which provides uniform cryptographic key management for grid-edge devices, integrating directly with blockchain-based transactive energy platforms to verify message provenance [516].

However, the integration of these technologies is not without profound challenges and subtle pitfalls. Combining TEEs with blockchains, for instance, introduces unique attack vectors. A naive implementation of a TEE-backed smart contract for confidential industrial data processing can be vulnerable to rollback attacks if the underlying blockchain uses a non-final consensus protocol (like Proof-of-Work), where chain reorganizations can revert transactions and cause inconsistent state inside the TEE [517]. Furthermore, the confidentiality guarantees of a TEE can be jeopardized if the blockchain's consensus can be manipulated to produce forged blocks containing malicious inputs to the enclave, as highlighted in the design of Ekiden [518]. These insights necessitate careful architectural choices, such as the "execute-order-validate" separation in Hyperledger Fabric or the use of TEEs only with finality-based consensus. Similarly, while blockchain provides transparency and immutability, it does not inherently guarantee the trustworthiness of data at its origin—a sensor reading fed into a blockchain can be accurate or maliciously fabricated. Cross-layer frameworks must therefore incorporate data trust modules at the physical/edge layer, perhaps using PLS-based authentication or anomaly detection, to assess the credibility of source data before it is committed to the ledger [519].

In conclusion, the future of industrial wireless security lies not in isolated layer-specific solutions but in coherent cross-layer frameworks. These architectures strategically combine the physical-layer robustness of PLS, the agility and end-to-end security of lightweight cryptography, the decentralized trust and auditability of blockchain, and the hardware-enforced isolation of TEEs. Such an integrated approach addresses the full spectrum of threats—from over-the-air eavesdropping to compromised network controllers and malicious firmware—ensuring confidentiality, integrity, and availability for the most demanding industrial control and IoT applications. The ongoing research challenge is to standardize interfaces, manage the complexity of these hybrid systems, and continuously address the novel security implications that arise from their interaction, as systematically explored in studies on TEE-assisted smart contracts [520] and the lessons learned from existing blockchain-TEE applications [521].

**Table: Comparison of approaches in 7.6 Cross-Layer Security Frameworks and Blockchain Integration**

| Method/Model | Key Idea/Mechanism | Application Context | Reference |
| :--- | :--- | :--- | :--- |
| Integration of PLS with Lightweight Cryptography (OSCORE/EDHOC) | Uses physical layer properties (e.g., CSI-based key generation, potentially RIS-assisted) to generate secret keys for application-layer security protocols (OSCORE, EDHOC), enabling end-to-end security for constrained IIoT devices. | Secure communication for resource-constrained Industrial Internet of Things (IIoT) devices, replacing heavy TLS. | [511] |
| Blockchain for SDN Security (IS2N) | Leverages a blockchain middle-layer to immutably store network snapshots, device registrations, and control messages (e.g., OpenFlow), ensuring integrity and non-repudiation of network commands in Software-Defined Networking. | Securing control-plane functions and intent-driven security management in industrial Software-Defined Networks (SDN). | [513] |
| Blockchain for Collaborative Intrusion Detection (CIDS) | Uses a blockchain as a tamper-resistant ledger to record shared detection rules, node reputation scores, and trust relationships, enabling decentralized trust and preventing poisoning of the collaborative knowledge base. | Establishing trust and auditability in Collaborative Intrusion Detection Systems (CIDS) for IoT/industrial networks. | [514] |
| Blockchain-based Federated Learning (FL) | Employs blockchain to provide a secure, immutable record for global model updates, participant contributions, and aggregation results in Federated Learning, preventing model tampering and ensuring auditability. | Secure and verifiable model aggregation in Federated Learning systems for Industrial IoT (IIoT). | [515] |
| TEE for Securing Programmable Logic Controllers (PLCs) | Uses a Trusted Execution Environment (TEE) like ARM TrustZone to create an isolated enclave for executing a PLC's control application, ensuring its integrity and confidentiality even if the host OS is compromised. | Protecting control logic execution on industrial Programmable Logic Controllers (PLCs) against strong adversaries. | [505] |
| Hardware Root of Trust with Blockchain (Cryptographic Trust Center) | Integrates a hardware security chip (Cryptographic Trust Center) for uniform key management with a blockchain platform to verify message provenance, creating a decentralized and verifiable security mechanism. | Secure key management and message provenance verification for grid-edge devices in transactive energy platforms. | [516] |
| TEE-Blockchain Integration Pitfalls & Solutions | Highlights challenges like rollback attacks in TEE-backed smart contracts on blockchains with non-final consensus, proposing architectural mitigations like "execute-order-validate" separation or use with finality-based consensus. | Designing secure hybrid systems combining Trusted Execution Environments (TEEs) and blockchains for confidential smart contracts. | [517], [518], [520], [521] |
| Cross-Layer Data Trust Architecture | Proposes a layered architecture incorporating data trust modules at the physical/edge layer to assess the credibility of source data before it is committed to a blockchain, addressing the blockchain's inability to guarantee data origin trustworthiness. | Ensuring end-to-end trust in blockchain-based IoT applications by evaluating sensor data trustworthiness. | [519] |


## 8 Emerging Trends, Open Challenges, and Future Directions

This concluding section identifies persistent open research challenges, including scalability for massive IoT, robustness under imperfect CSI and intelligent adversarial attacks, and standardization. It outlines future trends such as AI/ML-driven adaptive PLS


## References
[1] A Look Inside 5G Standards to Support Time Synchronization for Smart   Manufacturing

[2] Design of a 5G Ready and Reliable Architecture for the Smart Factory of   the Future

[3] Enhanced Sliding Window Superposition Coding for Industrial Automation

[4] Integration of 5G with TSN as Prerequisite for a Highly Flexible Future   Industrial Automation  Time Synchronization based on IEEE 802.1AS

[5] Application and network layers design for wireless sensor network to   supervise chemical active product warehouse

[6] Cyber Security in Smart Manufacturing (Threats, Landscapes Challenges)

[7] Security Solutions for Local Wireless Networks in Control Applications   based on Physical Layer Security

[8] Avoiding the Internet of Insecure Industrial Things

[9] Vulnerabilities and Attacks Against Industrial Control Systems and   Critical Infrastructures

[10] Key Factors of Wireless Real-Time Networks -- From Dependability to   Timeliness

[11] A Survey of Machine and Deep Learning Methods for Internet of Things   (IoT) Security

[12] Real-time Cooperative Communication for Automation over Wireless

[13] Fast Authentication and Progressive Authorization in Large-Scale IoT    How to Leverage AI for Security Enhancement 

[14] Grand Challenges for Embedded Security Research in a Connected World

[15] Securing IIoT using Defence-in-Depth  Towards an End-to-End Secure   Industry 4.0

[16] Machine Learning Methods for Device Identification Using Wireless   Fingerprinting

[17] Testbed for Functional Safety-Relevant Wireless Communication Based on   IO-Link Wireless and 5G

[18] 6G Underlayer Network Concepts for Ultra Reliable and Low Latency   Communication in Manufacturing

[19] Towards Industry 5.0  Intelligent Reflecting Surface (IRS) in Smart   Manufacturing

[20] Fading in reflective and heavily shadowed industrial environments with   large arrays

[21] Autonomous Interference Mapping for Industrial IoT Networks over   Unlicensed Bands

[22] Performance Analysis of a Mission-Critical Portable LTE System in   Targeted RF Interference

[23] Towards Ultra-Reliable Low-Latency Communications  Typical Scenarios,   Possible Solutions, and Open Issues

[24] Resource Allocation for Secure URLLC in Mission-Critical IoT Scenario

[25] Machine Learning for Massive Industrial Internet of Things

[26] Towards Adaptive RF Fingerprint-based Authentication of IIoT devices

[27] Developing a Security Testbed for Industrial Internet of Things

[28] Reconfigurable Intelligent Surfaces in Challenging Environments    Underwater, Underground, Industrial and Disaster

[29] Secure Short-Packet Communications at the Physical Layer for 5G and   Beyond

[30] A Survey of Physical Layer Security Techniques for 5G Wireless Networks   and Challenges Ahead

[31] Cyber-Physical Defense in the Quantum Era

[32] Securing Wireless Communications of the Internet of Things from the   Physical Layer, An Overview

[33] Physical Layer Security  Authentication, Integrity and Confidentiality

[34] Physical Layer Security for Ultra-Reliable and Low-Latency   Communications

[35] Physical Layer Secret Key Agreement Using One-Bit Quantization and   Low-Density Parity-Check Codes

[36] A Survey of Optimization Approaches for Wireless Physical Layer Security

[37] Wireless Physical-Layer Identification  Modeling and Validation

[38] On the Use of CSI for the Generation of RF Fingerprints and Secret Keys

[39] Physical Layer Security -- from Theory to Practice

[40] STAR-RIS-Assisted-Full-Duplex Jamming Design for Secure Wireless   Communications System

[41] Network-Controlled Physical-Layer Security  Enhancing Secrecy Through   Friendly Jamming

[42] Reconfigurable Intelligent Surfaces for Wireless Communications    Overview of Hardware Designs, Channel Models, and Estimation Techniques

[43] Wi-Fi Meets ML  A Survey on Improving IEEE 802.11 Performance with   Machine Learning

[44] Wireless Environment as a Service Enabled by Reconfigurable Intelligent   Surfaces  The RISE-6G Perspective

[45] Smart Wireless Environments Enabled by RISs  Deployment Scenarios and   Two Key Challenges

[46] A Comprehensive Survey on Radio Frequency (RF) Fingerprinting    Traditional Approaches, Deep Learning, and Open Challenges

[47] References in Wikipedia  The Editors' Perspective

[48] A Survey on Text Simplification

[49] Achievable Secrecy Rates of an Energy Harvesting Device

[50] Fast and energy-efficient technique for jammed region mapping in   wireless sensor networks

[51] Secure Outage Analysis for RIS-Aided MISO Systems with Randomly Located   Eavesdroppers

[52] Secrecy Outage Analysis over Correlated Composite Nakagami-$m$ Gamma   Fading Channels

[53] Secrecy Performance Analysis of RIS Assisted Ambient Backscatter   Communication Networks

[54] Energy Efficiency Scheme with Cellular Partition Zooming for Massive   MIMO Systems

[55] On Secure Computation Over the Binary Modulo-2 Adder Multiple-Access   Wiretap Channel

[56] Secret key generation from Gaussian sources using lattice hashing

[57] Quantifying AI Vulnerabilities  A Synthesis of Complexity, Dynamical   Systems, and Game Theory

[58] Ensuring High-Quality Randomness in Cryptographic Key Generation

[59] Nonlinear RF Fingerprints Authentication for OFDM Wireless Devices based   on Demodulated Symbols

[60] Cyber Risk at the Edge  Current and future trends on Cyber Risk   Analytics and Artificial Intelligence in the Industrial Internet of Things   and Industry 4.0 Supply Chains

[61] On Robustness of Massive MIMO Systems Against Passive Eavesdropping   under Antenna Selection

[62] Eavesdropping with Intelligent Reflective Surfaces  Near-Optimal   Configuration Cycling

[63] Robust Secure UAV Communications with the Aid of Reconfigurable   Intelligent Surfaces

[64] Securing UAV Communications Via Trajectory Optimization

[65] Deep Learning-based Physical-Layer Secret Key Generation for FDD Systems

[66] Secure Short-Packet Transmission with Aerial Relaying  Blocklength and   Trajectory Co-Design

[67] Insider-Attacks on Physical-Layer Group Secret-Key Generation in   Wireless Networks

[68] Augmented Digital Twin for Identification of Most Critical Cyberattacks   in Industrial Systems

[69] Formal Verification of Cyber-Physical Systems using Theorem Proving   (Invited Paper)

[70] Large-Scale MIMO Relaying Techniques for Physical Layer Security  AF or   DF 

[71] Self-Controlled Jamming Resilient Design Using Physical Layer Secret   Keys

[72] Wireless Powered Cooperative Jamming for Secrecy Multi-AF Relaying   Networks

[73] Optimal Friendly Jamming and Transmit Power Allocation in RIS-assisted   Secure Communication

[74] Aerial Intelligent Reflecting Surface Enabled Terahertz Covert   Communications in Beyond-5G Internet of Things

[75] Directional Modulation  A Secure Solution to 5G and Beyond Mobile   Networks

[76] Artificial-Noise-Aided Secure Channel with a Full-duplex Source

[77] Beamforming for Secure Communication via Untrusted Relay Nodes Using   Artificial Noise

[78] Artificial Noise Revisited

[79] Reconfigurable Intelligent Surface Enabled Over-the-Air Uplink   Non-orthogonal Multiple Access

[80] Stochastic Geometry Modeling and Analysis for THz-mmWave Hybrid IoT   Networks

[81] Beamforming Design for RIS-Aided THz Wideband Communication Systems

[82] Active Reconfigurable Intelligent Surface Aided Secure Transmission

[83] Wireless Communications Through Reconfigurable Intelligent Surfaces

[84] Technology Trends for Massive MIMO towards 6G

[85] Securing the Skies  An IRS-Assisted AoI-Aware Secure Multi-UAV System   with Efficient Task Offloading

[86] Secrecy of Opportunistic User Scheduling in RIS-Aided Systems  A   Comparison with NOMA Scheduling

[87] Reconfigurable Intelligent Surface for Physical Layer Key Generation    Constructive or Destructive 

[88] Joint Precoding and Phase Shift Design in Reconfigurable Intelligent   Surfaces-Assisted Secret Key Generation

[89] Secure Communication of Active RIS Assisted NOMA Networks

[90] Jamming Pattern Recognition over Multi-Channel Networks  A Deep Learning   Approach

[91] Spatially Correlated RIS-Aided Secure Massive MIMO Under CSI and   Hardware Imperfections

[92] Decoding Orders and Power Allocation for Untrusted NOMA  A Secrecy   Perspective

[93] Secrecy Outage Probability Analysis for Downlink NOMA with Imperfect SIC   at Untrusted Users

[94] Optimal User Load and Energy Efficiency in User-Centric Cell-Free   Wireless Networks

[95] Science based AI model certification for untrained operational   environments with application in traffic state estimation

[96] Beamforming Design and Power Allocation for Secure Transmission with   NOMA

[97] Secrecy Fairness Aware NOMA for Untrusted Users

[98] On Secrecy Performance of RIS-Assisted MISO Systems over Rician Channels   with Spatially Random Eavesdroppers

[99] Precoder Design and Power Allocation for Downlink MIMO-NOMA via   Simultaneous Triangularization

[100] An overview of visible light communication systems

[101] Leveraging IRS Induced Time Delay for Enhanced Physical Layer Security   in VLC Systems

[102] ESWORD  Implementation of Wireless Jamming Attacks in a Real-World   Emulated Network

[103] Proactive Eavesdropping via Cognitive Jamming in Fading Channels

[104] Energy Efficient Computing Systems  Architectures, Abstractions and   Modeling to Techniques and Standards

[105] Smart Channel State Information Pre-processing for Joint Authentication   and Secret Key Distillation

[106] Waveform-Defined Security  A Low-Cost Framework for Secure   Communications

[107] Towards Intelligent Context-Aware 6G Security

[108] Physical-Layer Authentication Using Channel State Information and   Machine Learning

[109] Perfectly Secure Key Agreement Over a Full Duplex Wireless Channel

[110] Let's shake on it  Extracting secure shared keys from Wi-Fi CSI

[111] QPLEX  Realizing the Integration of Quantum Computing into Combinatorial   Optimization Software

[112] Quantum-Resistant Cryptography

[113] Exploring Quantum-Enhanced Machine Learning for Computer Vision    Applications and Insights on Noisy Intermediate-Scale Quantum Devices

[114] Physics Informed Neural Networks for Phase Locked Loop Transient   Stability Assessment

[115] Lightweight Cryptography for IoT  A State-of-the-Art

[116] Blockchain-Based Security Architecture for Unmanned Aerial Vehicles in   B5G 6G Services and Beyond  A Comprehensive Approach

[117] Open-Set RF Fingerprinting via Improved Prototype Learning

[118] From Hardware Fingerprint to Access Token  Enhancing the Authentication   on IoT Devices

[119] Radio Frequency Fingerprint Identification Based on Denoising   Autoencoders

[120] SignCRF  Scalable Channel-agnostic Data-driven Radio Authentication   System

[121] A new Definition and Classification of Physical Unclonable Functions

[122] Overview of RIS-Enabled Secure Transmission in 6G Wireless Networks

[123] The Impact of Side Information on Physical Layer Security under   Correlated Fading Channels

[124] Joint Trajectory and Resource Allocation Design for Energy-Efficient   Secure UAV Communication Systems

[125] UAV Trajectory and Multi-User Beamforming Optimization for Clustered   Users Against Passive Eavesdropping Attacks With Unknown CSI

[126] Secure Swarm UAV-assisted Communications with Cooperative Friendly   Jamming

[127] Secure Short-Packet Communications via UAV-Enabled Mobile Relaying    Joint Resource Optimization and 3D Trajectory Design

[128] Two-Way Aerial Secure Communications via Distributed Collaborative   Beamforming under Eavesdropper Collusion

[129] Structural Credit Assignment with Coordinated Exploration

[130] UAV-Assisted Attack Prevention, Detection, and Recovery of 5G Networks

[131] Tasks People Prompt  A Taxonomy of LLM Downstream Tasks in Software   Verification and Falsification Approaches

[132] Optimal Downlink Training Sequence for Massive MIMO Secret-Key   Generation

[133] Anomaly Detection Dataset for Industrial Control Systems

[134] Safe Model-Based Reinforcement Learning for Systems with Parametric   Uncertainties

[135] Deep Reinforcement Learning for Cybersecurity Threat Detection and   Protection  A Review

[136] 5G Non-Public Network for Industrial IoT  Operation Models

[137] Fractional Barrier Lyapunov Functions with Application to Learning   Control

[138] Cybersecurity in Critical Infrastructures  A Post-Quantum Cryptography   Perspective

[139] Railgun  streaming windows for mission critical systems

[140] Large language models in 6G security  challenges and opportunities

[141] Zero-touch realization of Pervasive Artificial Intelligence-as-a-service   in 6G networks

[142] Joint Precoding and Artificial Noise Design for MU-MIMO Wiretap Channels

[143] Making existing software quantum safe  a case study on IBM Db2

[144] Securing Bluetooth Low Energy  A Literature Review

[145] Millimetre-waves to Terahertz SISO and MIMO Continuous Variable Quantum   Key Distribution

[146] Some i-Mark games

[147] X- problem of value three

[148] Polynomial-Time, Semantically-Secure Encryption Achieving the Secrecy   Capacity

[149] Secrecy Analysis of Physical Layer over $κ-μ$ Shadowed Fading   Scenarios

[150] Security Performance Analysis of Physical Layer over Fisher-Snedecor   $\mathcal{F}$ Fading Channels

[151] Performance Analysis of Physical Layer Security over Fluctuating   Beckmann Fading Channels

[152] Secrecy Performance of α-κ-μ Shadowed Fading Channel

[153] Some Discussions on PHY Security in DF Relay

[154] Secure Outage Analysis of FSO Communications Over Arbitrarily Correlated   Málaga Turbulence Channels

[155] A Simple Evaluation for the Secrecy Outage Probability Over   Generalized-K Fading Channels

[156] Secrecy Performance of Body-Centric Communications over Alternate Rician   Shadowed Fading Channels

[157] The Conditional Information Leakage Given Eavesdropper's Received   Signals in Wiretap Channels

[158] A Model for Adversarial Wiretap Channel

[159] Optimization of Code Rates in SISOME Wiretap Channels

[160] Trade Reliability for Security  Leakage-Failure Probability Minimization   for Machine-Type Communications in URLLC

[161] On the Information Leakage Performance of Secure Finite Blocklength   Transmissions over Rayleigh Fading Channels

[162] Physical-Layer Security in the Finite Blocklength Regime over Fading   Channels

[163] Wiretap Channels  Nonasymptotic Fundamental Limits

[164] Almost universal codes for MIMO wiretap channels

[165] Achieving Secrecy Capacity of the Wiretap Channel and Broadcast Channel   with a Confidential Component

[166] Short Blocklength Wiretap Channel Codes via Deep Learning  Design and   Performance Evaluation

[167] Improving Secrecy with Nearly Collinear Main and Wiretap Channels via a   Cooperative Jamming Relay

[168] Stealthy Deception Attacks Against SCADA Systems

[169] Synthesis of Sensor Deception Attacks at the Supervisory Layer of   Cyber-Physical Systems

[170] Seeing is Believing  A Federated Learning Based Prototype to Detect   Wireless Injection Attacks

[171] Secure Relaying in Non-Orthogonal Multiple Access  Trusted and Untrusted   Scenarios

[172] Active Linkability Attacks

[173] Explainable and Transferable Adversarial Attack for ML-Based Network   Intrusion Detectors

[174] Can't Boil This Frog  Robustness of Online-Trained Autoencoder-Based   Anomaly Detectors to Adversarial Poisoning Attacks

[175] Snooping Attacks on Deep Reinforcement Learning

[176] A Secure and Trusted Mechanism for Industrial IoT Network using   Blockchain

[177] An Analytics Framework for Heuristic Inference Attacks against   Industrial Control Systems

[178] Security versus Reliability Analysis of Opportunistic Relaying

[179] Relay Selection for Wireless Communications Against Eavesdropping  A   Security-Reliability Tradeoff Perspective

[180] Joint Relay and Jammer Selection Improves the Physical Layer Security in   the Face of CSI Feedback Delays

[181] Achieving Covertness and Secrecy  A New Paradigm for Secure Wireless   Communication

[182] On the Analysis of AoI-Reliability Tradeoff in Heterogeneous IIoT   Networks

[183] Scheduling Observers Over a Shared Channel with Hard Delivery Deadlines

[184] Scheduling with Probabilistic Per-Packet Real-Time Guarantee for URLLC

[185] Resource Allocation for Secure Multi-User Downlink MISO-URLLC Systems

[186] Resource Allocation for Cell-free Massive MIMO-enabled URLLC Downlink   Systems

[187] Physical Layer Security-Aware Routing and Performance Tradeoffs in Ad   Hoc Networks

[188] Dependability-Aware Routing and Scheduling for Time-Sensitive Networking

[189] Delay Performance of MISO Wireless Communications

[190] Improving Network Availability of Ultra-Reliable and Low-Latency   Communications with Multi-Connectivity

[191] Cross-layer Optimization for Ultra-reliable and Low-latency Radio Access   Networks

[192] Linear shrinkage receiver for slow fading channels under imperfect   channel state information

[193] On the Secrecy Outage Capacity of Physical Layer Security in Large-Scale   MIMO Relaying Systems with Imperfect CSI

[194] Secrecy Analysis for MISO Broadcast Systems with Regularized   Zero-Forcing Precoding

[195] Erasure Broadcast Channels with Intermittent Feedback

[196] A Unified Framework for Multi-Hop Wireless Relaying with Hardware   Impairments

[197] A New Look at Dual-Hop Relaying  Performance Limits with Hardware   Impairments

[198] Performance Analysis of I Q Imbalance with Hardware Impairments over   Fox's H-Fading Channels

[199] Hardware Impaired Ambient Backscatter NOMA Systems  Reliability and   Security

[200] Power-Efficient and Secure WPCNs with Hardware Impairments and   Non-Linear EH Circuit

[201] Bounds on the Secrecy Outage Probability for Dependent Fading Channels

[202] Effect of Correlation between Information and Energy Links in Secure   Wireless Powered Communications

[203] Performance Analysis of Finite Blocklength Transmissions Over Wiretap   Fading Channels  An Average Information Leakage Perspective

[204] Reliability-Latency-Rate Tradeoff in Low-Latency Communications with   Finite-Blocklength Coding

[205] Outage-Constrained Robust Beamforming for Intelligent Reflecting Surface   Aided Wireless Communication

[206] Sensing-Throughput Tradeoff for Interweave Cognitive Radio System  A   Deployment-Centric Viewpoint

[207] Performance Analysis of Underlay Cognitive Radio Systems    Estimation-Throughput Tradeoff

[208] Uncharted Territory  Energy Attacks in the Battery-less Internet of   Things

[209] Learning-Aided Physical Layer Attacks Against Multicarrier   Communications in IoT

[210] TMAP  A Threat Modeling and Attack Path Analysis Framework for   Industrial IoT Systems (A Case Study of IoM and IoP)

[211] A Proactive Decoy Selection Scheme for Cyber Deception using MITRE   ATT&CK

[212] When Attackers Meet AI  Learning-empowered Attacks in Cooperative   Spectrum Sensing

[213] Optimal Power Allocation for Artificial Noise under Imperfect CSI   against Spatially Random Eavesdroppers

[214] Constructive Interference Based Secure Precoding  A New Dimension in   Physical Layer Security

[215] Two High-Performance Amplitude Beamforming Schemes for Secure Precise   Communication and Jamming with Phase Alignment

[216] Secure Precise Wireless Transmission with   Random-Subcarrier-Selection-based Directional Modulation Transmit Antenna   Array

[217] Energy-efficient Alternating Iterative Secure Structure of Maximizing   Secrecy Rate for Directional Modulation Networks

[218] Secure Massive MIMO Communication with Low-resolution DACs

[219] Exploiting Full-duplex Receivers for Achieving Secret Communications in   Multiuser MISO Networks

[220] Secrecy Energy Efficiency of MIMOME Wiretap Channels with Full-Duplex   Jamming

[221] The Sound and the Fury  Hiding Communications in Noisy Wireless Networks   with Interference Uncertainty

[222] Multi-Antenna Jamming in Covert Communication

[223] On the Design of Artificial Noise for Physical Layer Security in Visible   Light Communication Channels with Clipping

[224] On the Role of Artificial Noise in Training and Data Transmission for   Secret Communications

[225] Secure M-PSK Communication via Directional Modulation

[226] Two Low-complexity Efficient Beamformers for IRS-and-UAV-aided   Directional Modulation Networks

[227] Secure Directional Modulation to Enhance Physical Layer Security in IoT   Networks

[228] On Secrecy Rate of the Generalized Artificial-Noise Assisted Secure   Beamforming for Wiretap Channels

[229] Artificial-Noise-Aided Secure Transmission with Directional Modulation   based on Random Frequency Diverse Arrays

[230] Two Practical Random-Subcarrier-Selection Methods for Secure Precise   Wireless Transmission

[231] Two Efficient Beamformers for Secure Precise Jamming and Communication   with Phase Alignment

[232] Defining Spatial Security Outage Probability for Exposure Region Based   Beamforming

[233] Robust Secure Transmission of Using Main-Lobe-Integration Based Leakage   Beaforming in Directional Modulation MU-MIMO Systems

[234] Active Eavesdropper Mitigation via Orthogonal Channel Estimation

[235] Enhanced Secrecy Rate Maximization for Directional Modulation Networks   via IRS

[236] Joint Power Allocation and Beamforming for Active IRS-aided Directional   Modulation Network

[237] Optimal Power Allocation for Secure Directional Modulation Networks with   a Full-duplex UAV User

[238] Alternating Iterative Secure Structure between Beamforming and Power   Allocation for UAV-aided Directional Modulation Networks

[239] Pseudo-random Phase Precoded Spatial Modulation

[240] A Deep-learning-based Joint Inference for Secure Spatial Modulation   Receiver

[241] Index Modulation Based Coordinate Interleaved Orthogonal Design for   Secure Communications

[242] OFDM-Based Optical Spatial Modulation

[243] Non-Orthogonal Waveforms in Secure Communications

[244] Index Modulation Pattern Design for Non-Orthogonal Multicarrier Signal   Waveforms

[245] Secure Short-Packet Communications for Mission-Critical IoT Applications

[246] Reliable and Secure Short-Packet Communications

[247] Physical Layer Security for RF Satellite Channels in the Finite-length   Regime

[248] Non-Orthogonal Multiplexing in the FBL Regime Enhances Physical Layer   Security with Deception

[249] Transmit Filter and Artificial Noise Design for Secure MIMO-OFDM Systems

[250] Hybrid Spatio-Temporal Artificial Noise Design for Secure MIMOME-OFDM   Systems

[251] Capacity-based Spatial Modulation Constellation and Pre-scaling Design

[252] Mitigating Smart Jammers in Multi-User MIMO

[253] Mitigating Smart Jammers in MU-MIMO via Joint Channel Estimation and   Data Detection

[254] Low-complexity and High-performance Receive Beamforming for Secure   Directional Modulation Networks against an Eavesdropping-enabled Full-duplex   Attacker

[255] Universal MIMO Jammer Mitigation via Secret Temporal Subspace Embeddings

[256] Resilient-By-Design Framework for MIMO-OFDM Communications under Smart   Jamming

[257] Jamming Modulation  An Active Anti-Jamming Scheme

[258]  Borrowing Arrows with Thatched Boats   The Art of Defeating Reactive   Jammers in IoT Networks

[259] DeepFake  Deep Dueling-based Deception Strategy to Defeat Reactive   Jammers

[260] Deep Learning for Launching and Mitigating Wireless Jamming Attacks

[261]  Jam Me If You Can''  Defeating Jammer with Deep Dueling Neural Network   Architecture and Ambient Backscattering Augmented Communications

[262] Towards an AI-Driven Universal Anti-Jamming Solution with Convolutional   Interference Cancellation Network

[263] IRS-based Wireless Jamming Attacks  When Jammers can Attack without   Power

[264] Low-Latency Communication using Delay-Aware Relays Against Reactive   Adversaries

[265] Deep Learning Based Joint Beamforming Design in IRS-Assisted Secure   Communications

[266] Truly Intelligent Reflecting Surface-Aided Secure Communication Using   Deep Learning

[267] Robust Beamforming for RIS-aided Communications  Gradient-based Manifold   Meta Learning

[268] Online RIS Configuration Learning for Arbitrary Large Numbers of $1$-Bit   Phase Resolution Elements

[269] Defeating Proactive Jammers Using Deep Reinforcement Learning for   Resource-Constrained IoT Networks

[270] Learning-based Intelligent Surface Configuration, User Selection,   Channel Allocation, and Modulation Adaptation for Jamming-resisting Multiuser   OFDMA Systems

[271] Online Robust Policy Learning in the Presence of Unknown Adversaries

[272] Learning to Cope with Adversarial Attacks

[273] Autoencoder-based Communications with Reconfigurable Intelligent   Surfaces

[274] Waveform Learning for Reduced Out-of-Band Emissions Under a Nonlinear   Power Amplifier

[275] Adversarial Attacks on Deep-Learning Based Radio Signal Classification

[276] Evaluating Adversarial Evasion Attacks in the Context of Wireless   Communications

[277] Channel-Aware Adversarial Attacks Against Deep Learning-Based Wireless   Signal Classifiers

[278] Adversarial Robustness of Distilled and Pruned Deep Learning-based   Wireless Classifiers

[279] Frequency-based Automated Modulation Classification in the Presence of   Adversaries

[280] A Simple Framework to Enhance the Adversarial Robustness of Deep   Learning-based Intrusion Detection System

[281] Intelligent Reflecting Surface-Assisted Wireless Key Generation for   Low-Entropy Environments

[282] Physical Layer Secret Key Generation with Kalman Filter Detrending

[283] A formal definition and a new security mechanism of physical unclonable   functions

[284] A Proof of Concept SRAM-based Physically Unclonable Function (PUF) Key   Generation Mechanism for IoT Devices

[285] Ring Oscillator and its application as Physical Unclonable Function   (PUF) for Password Management

[286] A Secret Key Generation Scheme for Internet of Things using   Ternary-States ReRAM-based Physical Unclonable Functions

[287] Detecting Recycled Commodity SoCs  Exploiting Aging-Induced SRAM PUF   Unreliability

[288] Using Convolutional Codes for Key Extraction in SRAM Physical Unclonable   Functions

[289] A Robust SRAM-PUF Key Generation Scheme Based on Polar Codes

[290] Lightweight (Reverse) Fuzzy Extractor with Multiple Referenced PUF   Responses

[291] Exploiting PUF Models for Error Free Response Generation

[292] CycPUF  Cyclic Physical Unclonable Function

[293] Set-based Obfuscation for Strong PUFs against Machine Learning Attacks

[294] PUF-Phenotype  A Robust and Noise-Resilient Approach to Aid   Intra-Group-based Authentication with DRAM-PUFs Using Machine Learning

[295] TREVERSE  Trial-and-Error Lightweight Secure Reverse Authentication with   Simulatable PUFs

[296] Physical Unclonable Function-based Key Sharing for IoT Security

[297] Pre-print  Radio Identity Verification-based IoT Security Using RF-DNA   Fingerprints and SVM

[298] Radio Frequency Fingerprint Identification for LoRa Using Spectrogram   and CNN

[299] Uncovering the Portability Limitation of Deep Learning-Based Wireless   Device Fingerprints

[300] The Day-After-Tomorrow  On the Performance of Radio Fingerprinting over   Time

[301] EPS  Distinguishable IQ Data Representation for Domain-Adaptation   Learning of Device Fingerprints

[302] Disentangled Representation Learning for RF Fingerprint Extraction under   Unknown Channel Statistics

[303] Semi-Supervised RF Fingerprinting with Consistency-Based Regularization

[304] Federated Radio Frequency Fingerprinting with Model Transfer and   Adaptation

[305] White-Box Adversarial Attacks on Deep Learning-Based Radio Frequency   Fingerprint Identification

[306] Penetrating RF Fingerprinting-based Authentication with a Generative   Adversarial Attack

[307] Physical Layer Authentication Using Information Reconciliation

[308] Authenticating On-Body IoT Devices  An Adversarial Learning Approach

[309] Towards Motion Invariant Authentication for On-Body IoT Devices

[310] Preventing Identity Attacks in RFID Backscatter Communication Systems  A   Physical-Layer Approach

[311] Access-based Lightweight Physical Layer Authentication for the Internet   of Things Devices

[312] Device Authentication Codes based on RF Fingerprinting using Deep   Learning

[313] The Wyner Variational Autoencoder for Unsupervised Multi-Layer Wireless   Fingerprinting

[314] Post Quantum Cryptography  Techniques, Challenges, Standardization, and   Directions for Future Research

[315] Sapphire  A Configurable Crypto-Processor for Post-Quantum Lattice-based   Protocols

[316] FIPS Compliant Quantum Secure Communication using Quantum Permutation   Pad

[317] Post-Quantum Cryptographic Hardware Primitives

[318] SPHINCS$^+$ post-quantum digital signature scheme with Streebog hash   function

[319] FROG  Forward-Secure Post-Quantum Signature

[320] Identifying Research Challenges in Post Quantum Cryptography Migration   and Cryptographic Agility

[321] A Lightweight Authentication Protocol against Modeling Attacks based on   a Novel LFSR-APUF

[322] PhenoAuth  A Novel PUF-Phenotype-based Authentication Protocol for IoT   Devices

[323] Authenticated Secret Key Generation in Delay Constrained Wireless   Systems

[324] Fusing Keys for Secret Communications  Towards Information-Theoretic   Security

[325] Graph Layer Security  Encrypting Information via Common Networked   Physics

[326] Securing IoT Communication using Physical Sensor Data -- Graph Layer   Security with Federated Multi-Agent Deep Reinforcement Learning

[327] When Physical Layer Key Generation Meets RIS  Opportunities, Challenges,   and Road Ahead

[328] RIS-Assisted Wireless Link Signatures for Specific Emitter   Identification

[329] On the RIS Manipulating Attack and Its Countermeasures in Physical-layer   Key Generation

[330] Explainable Adversarial Learning Framework on Physical Layer Secret Keys   Combating Malicious Reconfigurable Intelligent Surface

[331] Spatial Secrecy Spectral Efficiency Optimization Enabled by   Reconfigurable Intelligent Surfaces

[332] STAR-RIS Aided Secure MIMO Communication Systems

[333] RIS-Assisted Green Secure Communications  Active RIS or Passive RIS 

[334] Active Reconfigurable Intelligent Surface Aided Wireless Communications

[335] Beamforming Optimization for Active RIS-Aided Multiuser Communications   With Hardware Impairments

[336] Security Enhancement for Coupled Phase-Shift STAR-RIS Networks

[337] Simultaneously Transmitting and Reflecting RIS (STAR-RIS) Assisted   Multi-Antenna Covert Communications  Analysis and Optimization

[338] Two-Timescale Design for STAR-RIS Aided NOMA Systems

[339] RIS-Assisted Wireless Communications  Long-Term versus Short-Term Phase   Shift Designs

[340] Robust Transmission Design for RIS-Aided Communications with Both   Transceiver Hardware Impairments and Imperfect CSI

[341] Max-Min SINR Analysis of STAR-RIS Assisted Massive MIMO Systems with   Hardware Impairments

[342] Electromagnetic Interference Cancellation for RIS-Assisted   Communications

[343] Electromagnetic Interference in RIS-Aided Communications

[344] Joint Reconfigurable Intelligent Surface Location and Passive   Beamforming Optimization for Maximizing the Secrecy-Rate

[345] Cooperative RIS and STAR-RIS assisted mMIMO Communication  Analysis and   Optimization

[346] Double-RIS Aided Multi-user MIMO Communications  Common Reflection   Pattern and Joint Beamforming Design

[347] Non-Orthogonal Multiple Access (NOMA) in Cellular Uplink and Downlink    Challenges and Enabling Techniques

[348] Secure Transmission to the Strong User with Optimal Power Allocation in   NOMA

[349] Secrecy Sum Rate Maximization in Non-Orthogonal Multiple Access

[350] Secrecy Outage Probability Analysis for Downlink Untrusted NOMA Under   Practical SIC Error

[351] Reconfigurable Intelligent Surface (RIS) Aided Multi-User Networks    Interplay Between NOMA and RIS

[352] Improving Physical Layer Security for Reconfigurable Intelligent Surface   aided NOMA 6G Networks

[353] On the Secrecy Rate of Downlink NOMA in Underlay Spectrum Sharing with   Imperfect CSI

[354] Energy-Efficient Transmission Design in Non-Orthogonal Multiple Access

[355] Short-Packet Communications in Non-Orthogonal Multiple Access Systems

[356] Short-Packet Downlink Transmission with Non-Orthogonal Multiple Access

[357] On Multiple-Antenna Techniques for Physical-Layer Range Security in the   Terahertz Band

[358] Wavefront Engineering  Realizing Efficient Terahertz Band Communications   in 6G and Beyond

[359] Absolute Security in High-Frequency Wireless Links

[360] Joint Sensing and Communication for Situational Awareness in Wireless   THz Systems

[361] The feasibility of launching physical layer attacks in visible light   communication networks

[362] Physical-layer Security for Indoor Visible Light Communications  Secrecy   Capacity Analysis

[363] Exploiting Gold Nanoparticles for Secure Visible Light Communications

[364] LiFi Through Reconfigurable Intelligent Surfaces  A New Frontier for 6G 

[365] Intelligent Reflecting Surfaces for Enhanced Physical Layer Security in   NOMA VLC Systems

[366] Hybrid RF VLC Systems under QoS Constraints

[367] Energy-Efficient Resource Allocation for Aggregated RF VLC Systems

[368] Physical Layer Security in Cooperative NOMA Hybrid VLC RF Systems

[369] Active RIS vs. Passive RIS  Which Will Prevail in 6G 

[370] Simultaneously Transmitting And Reflecting (STAR) RIS for 6G    Fundamentals, Recent Advances, and Future Directions

[371] Wireless Information Surveillance via STAR-RIS

[372] Hybrid Reconfigurable Intelligent Metasurfaces  Enabling Simultaneous   Tunable Reflections and Sensing for 6G Wireless Communications

[373] Reconfigurable Intelligent Computational Surfaces  When Wave Propagation   Control Meets Computing

[374] Reconfigurable Intelligent Surfaces 2.0  Beyond Diagonal Phase Shift   Matrices

[375] Applications of Absorptive Reconfigurable Intelligent Surfaces in   Interference Mitigation and Physical Layer Security

[376] FID  Function Modeling-based Data-Independent and Channel-Robust   Physical-Layer Identification

[377] PUF for the Commons  Enhancing Embedded Security on the OS Level

[378] A ReRAM Physically Unclonable Function (ReRAM PUF)-based Approach to   Enhance Authentication Security in Software Defined Wireless Networks

[379] A Fast and Scalable Authentication Scheme in IoT for Smart Living

[380] A Flexible and Lightweight Group Authentication Scheme

[381] Physical Layer Security in a Private 5G Network for Industrial and   Mobility Application

[382] A SKG Security Challenge  Indoor SKG Under an On-The-Shoulder   Eavesdropping Attack

[383] Multi-factor Physical Layer Security Authentication in Short Blocklength   Communication

[384] LiPI  Lightweight Privacy-Preserving Data Aggregation in IoT

[385] Grain-128PLE  Generic Physical-Layer Encryption for IoT Networks

[386] Network Intrusion Detection System in a Light Bulb

[387] PoAh  A Novel Consensus Algorithm for Fast Scalable Private Blockchain   for Large-scale IoT Frameworks

[388] Five-Layers SDP-Based Hierarchical Security Paradigm for Multi-access   Edge Computing

[389] Public Key Reinforced Blockchain Platform for Fog-IoT Network System   Administration

[390] Secure UAV-to-Ground MIMO Communications  Joint Transceiver and Location   Optimization

[391] Robust Trajectory and Transmit Power Design for Secure UAV   Communications

[392] UAV-Aided Jamming for Secure Ground Communication with Unknown   Eavesdropper Location

[393] UAV-Enabled Cooperative Jamming for Improving Secrecy of Ground Wiretap   Channel

[394] Secrecy Energy Efficiency Maximization for UAV-Enabled Mobile Relaying

[395] Resilient Path Planning for UAVs in Data Collection under Adversarial   Attacks

[396] Robust and Decentralized Reinforcement Learning for UAV Path Planning in   IoT Networks

[397] Integrated Sensing, Navigation, and Communication for Secure UAV   Networks with a Mobile Eavesdropper

[398] UAV Swarm-enabled Collaborative Secure Relay Communications with   Time-domain Colluding Eavesdropper

[399] Intelligent Reflecting Surface Aided Secure UAV Communications

[400] Enhancing Physical Layer Security for NOMA Transmission in mmWave Drone   Networks

[401] Blockchain-Enhanced UAV Networks for Post-Disaster Communication  A   Decentralized Flocking Approach

[402] Cybersecurity of Industrial Cyber-Physical Systems  A Review

[403] An Integrated Cyber-Physical Risk Assessment Framework for Worst-Case   Attacks in Industrial Control Systems

[404] A Deep Learning-based Framework for Conducting Stealthy Attacks in   Industrial Control Systems

[405] Modelling Load-Changing Attacks in Cyber-Physical Systems

[406] A Data-Centric Approach to Generate Invariants for a Smart Grid Using   Machine Learning

[407] Assessment of Cyber-Physical Intrusion Detection and Classification for   Industrial Control Systems

[408] Investigation of Cyber Attacks on a Water Distribution System

[409] Reconfigurable Intelligent Surface for Physical Layer Security in   6G-IoT  Designs, Issues, and Advances

[410] Towards Situational Aware Cyber-Physical Systems  A Security-Enhancing   Use Case of Blockchain-based Digital Twins

[411] A Compositional Approach to Safety-Critical Resilient Control for   Systems with Coupled Dynamics

[412] Cyber-Resilience Approaches for Cyber-Physical Systems

[413] Enhanced Cyber-Physical Security Using Attack-resistant Cyber Nodes and   Event-triggered Moving Target Defence

[414] State-of-the-Art Survey on In-Vehicle Network Communication (CAN-Bus)   Security and Vulnerabilities

[415] Linking Received Packet to the Transmitter Through   Physical-Fingerprinting of Controller Area Network

[416] Identifying ECUs Using Inimitable Characteristics of Signals in   Controller Area Networks

[417] On the Robustness of Signal Characteristic-Based Sender Identification

[418] Two-Point Voltage Fingerprinting  Increasing Detectability of ECU   Masquerading Attacks

[419] TACAN  Transmitter Authentication through Covert Channels in Controller   Area Networks

[420] CANTO -- Covert AutheNtication with Timing channels over Optimized   traffic flows for CAN

[421] Exploiting the Shape of CAN Data for In-Vehicle Intrusion Detection

[422] X-CANIDS  Signal-Aware Explainable Intrusion Detection System for   Controller Area Network-Based In-Vehicle Network

[423] INDRA  Intrusion Detection using Recurrent Autoencoders in Automotive   Embedded Systems

[424] GIDS  GAN based Intrusion Detection System for In-Vehicle Network

[425] CAN-BERT do it  Controller Area Network Intrusion Detection System based   on BERT Language Model

[426] An Adversarial Attack Defending System for Securing In-Vehicle Networks

[427] Cyber Security Challenges and Solutions for V2X Communications  A Survey

[428] Hybrid PLS-ML Authentication Scheme for V2I Communication Networks

[429] Secure-ISAC  Secure V2X Communication  An Integrated Sensing and   Communication Perspective

[430] Physical Layer Security Performance of Dual RIS-aided V2V NOMA   Communications

[431] Security in Automotive Networks  Lightweight Authentication and   Authorization

[432] A Lightweight FPGA-based IDS-ECU Architecture for Automotive CAN

[433] Fortifying Vehicular Security Through Low Overhead Physically Unclonable   Functions

[434] Securing Automotive Architectures with Named Data Networking

[435] Can You Still See Me   Reconstructing Robot Operations Over End-to-End   Encrypted Channels

[436] Integration of IEEE 802.1AS-based Time Synchronization in IEEE 802.11 as   an Enabler for Novel Industrial Use Cases

[437] Resource Allocation for Uplink Cell-Free Massive MIMO enabled URLLC in a   Smart Factory

[438] Evaluation of NR-Sidelink for Cooperative Industrial AGVs

[439] Coordinated Broadcast-based Request-Reply and Group Management for   Tightly-Coupled Wireless Systems

[440] PropFuzz -- An IT-Security Fuzzing Framework for Proprietary ICS   Protocols

[441] SDN4CoRE  A Simulation Model for Software-Defined Networking for   Communication over Real-Time Ethernet

[442] Secure Time-Sensitive Software-Defined Networking in Vehicles

[443] A Survey on Industrial Control System Testbeds and Datasets for Security   Research

[444] ICSSIM-A Framework for Building Industrial Control Systems Security   Simulation Testbeds

[445] MiniCPS  A toolkit for security research on CPS Networks

[446] ICS-CTM2  Industrial Control System Cybersecurity Testbed Maturity Model

[447] EPICTWIN  An Electric Power Digital Twin for Cyber Security Testing,   Research and Education

[448] Model-Based Risk Assessment for Cyber Physical Systems Security

[449] Cyber LOPA  An Integrated Approach for the Design of Dependable and   Secure Cyber Physical Systems

[450] Security of IT OT Convergence  Design and Implementation Challenges

[451] Heuristic Approach Towards Countermeasure Selection using Attack Graphs

[452] A Secure Dual-MCU Architecture for Robust Communication of IIoT Devices

[453] On the Elements of Datasets for Cyber Physical Systems Security

[454] Deployment Challenges of Industrial Intrusion Detection Systems

[455] System Security Assurance  A Systematic Literature Review

[456] Enhanced Minimal Scheduling Function for IEEE802.15.4e TSCH Networks

[457] Isolating SDN Control Traffic with Layer-2 Slicing in 6TiSCH Industrial   IoT Networks

[458] Secure IoT Routing  Selective Forwarding Attacks and Trust-based   Defenses in RPL Network

[459] SoS-RPL  Securing Internet of Things Against Sinkhole Attack Using RPL   Protocol-Based Node Rating and Ranking Mechanism

[460] The DAO Induction Attack Against the RPL-based Internet of Things

[461] Securing RPL using Network Coding  The Chained Secure Mode (CSM)

[462] Integrating 6LoWPAN Security with RPL Using The Chained Secure Mode   Framework

[463] BLEND  Efficient and blended IoT data storage and communication with   application layer security

[464] A Case for Time Slotted Channel Hopping for ICN in the IoT

[465] COPSS-lite  Lightweight ICN Based Pub Sub for IoT Environments

[466] IoT Content Object Security with OSCORE and NDN  A First Experimental   Comparison

[467] A Novel Energy-Efficient Cross-Layer Design for Scheduling and Routing   in 6TiSCH Networks

[468] Congestion-Aware Routing in Dynamic IoT Networks  A Reinforcement   Learning Approach

[469] Ensuring Reliable and Predictable Behavior of IEEE 802.1CB Frame   Replication and Elimination

[470] Over-the-Air Time Synchronization for URLLC  Requirements, Challenges   and Possible Enablers

[471] Simulation-based Evaluation of a Synchronous Transaction Model for   Time-Sensitive Software-Defined Networks

[472] Achieving Ultra-Reliable Low-Latency Communication (URLLC) in   Next-Generation Cellular Networks with Programmable Data Planes

[473] Supercharge me  Boost Router Convergence with SDN

[474] On the Impacts of Phase Shifting Design and Eavesdropping Uncertainty on   Secrecy Metrics of RIS-aided Systems

[475] Two-Way Relaying under the Presence of Relay Transceiver Hardware   Impairments

[476] I Q Imbalance Aware Nonlinear Wireless-Powered Relaying of B5G Networks    Security and Reliability Analysis

[477] RIS-Aided MIMO Systems with Hardware Impairments  Robust Beamforming   Design and Analysis

[478] Wireless Physical Layer Security with Imperfect Channel State   Information  A Survey

[479] Secrecy Outage for Wireless Sensor Networks

[480] Extreme Value Theory-based Robust Minimum-Power Precoding for URLLC

[481] Few-Bit CSI Acquisition for Centralized Cell-Free Massive MIMO with   Spatial Correlation

[482] Is Phase Shift Keying Optimal for Channels with Phase-Quantized Output 

[483] LTE PHY Layer Vulnerability Analysis and Testing Using Open-Source SDR   Tools

[484] Secure Massive RIS aided Multicast with Uncertain CSI  Energy-Efficiency   Maximization via Accelerated First-Order Algorithms

[485] Sacrificing CSI for a Greater Good  RIS-enabled Opportunistic Rate   Splitting

[486] NarrowBand IoT Data Transmission Procedures for Massive Machine Type   Communications

[487] Future Industrial Applications  Exploring LPWAN-Driven IoT Protocols

[488] Energy-Reliability Aware Link Optimization for Battery-Powered IoT   Devices with Non-Ideal Power Amplifiers

[489] Optimized Resource Provisioning and Operation Control for Low-power   Wide-area IoT Networks

[490] Feedback Prediction for Proactive HARQ in the Context of Industrial   Internet of Things

[491] Enhancing End-to-End Determinism and Reliability in 6TiSCH networks with   disjoint leaf-based MPLS-like tunnels

[492] Real-Time Control over Wireless Networks

[493] Multi-Agent Deep Reinforcement Learning Based Resource Management in   SWIPT Enabled Cellular Networks with H2H M2M Co-Existence

[494] Joint Device Association, Resource Allocation and Computation Offloading   in Ultra-Dense Multi-Device and Multi-Task IoT Networks

[495] Reliable IoT Firmware Updates  A Large-scale Mesh Network Performance   Investigation

[496] Resilient Edge  Can we achieve Network Resiliency at the IoT Edge using   LPWAN and WiFi 

[497] A Distributed Neural Linear Thompson Sampling Framework to Achieve URLLC   in Industrial IoT

[498] Multiagent Reinforcement Learning with an Attention Mechanism for   Improving Energy Efficiency in LoRa Networks

[499] Physical Layer Authentication for Non-coherent Massive SIMO-Based   Industrial IoT Communications

[500] Design and Implementation of Time-Sensitive Wireless IoT Networks on   Software-Defined Radio

[501] RFQuack  A Universal Hardware-Software Toolkit for Wireless Protocol   (Security) Analysis and Research

[502] CaST  A Toolchain for Creating and Characterizing Realistic Wireless   Network Emulation Scenarios

[503] Securing O-RAN Open Interfaces

[504] Developing Secure Services for IoT with OP-TEE  A First Look at   Performance and Usability

[505] On Practicality of Using ARM TrustZone Trusted Execution Environment for   Securing Programmable Logic Controllers

[506] BYOTee  Towards Building Your Own Trusted Execution Environments Using   FPGA

[507] Towards a Trusted Execution Environment via Reconfigurable FPGA

[508] iperfTZ  Understanding Network Bottlenecks for TrustZone-based Trusted   Applications

[509] A Comprehensive Benchmark Suite for Intel SGX

[510] TEEMon  A continuous performance monitoring framework for TEEs

[511] The Cost of OSCORE and EDHOC for Constrained Devices

[512] A Holistic Approach for Trustworthy Distributed Systems with WebAssembly   and TEEs

[513] IS2N  Intent-Driven Security Software-Defined Network with Blockchain

[514] On Blockchain Architectures for Trust-Based Collaborative Intrusion   Detection

[515] Blockchain-based Federated Learning with Secure Aggregation in Trusted   Execution Environment for Internet-of-Things

[516] Integrating Hardware Security into a Blockchain-Based Transactive Energy   Platform

[517] Blockchain and Trusted Computing  Problems, Pitfalls, and a Solution for   Hyperledger Fabric

[518] Ekiden  A Platform for Confidentiality-Preserving, Trustworthy, and   Performant Smart Contract Execution

[519] A Trust Architecture for Blockchain in IoT

[520] SoK  TEE-assisted Confidential Smart Contract

[521] Lessons Learned from Blockchain Applications of Trusted Execution   Environments and Implications for Future Research


