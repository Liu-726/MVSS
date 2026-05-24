# A Comprehensive Survey of Blockchain and Artificial Intelligence for 6G Wireless Communications: Synergies, Architectures, and Applications

## 1 Introduction to the 6G Vision and the Imperative for Blockchain-AI Integration

This section introduces the key drivers, stringent performance requirements (e.g., Tbps rates, μs latency, ubiquitous intelligence), and transformative use cases (e.g., holographic telepresence, pervasive IoT, autonomous systems) of 6G networks. It establishes the core challenges in scalability, security, trust, and resource management that necessitate the synergistic convergence of Blockchain and Artificial Intelligence (AI) as foundational enablers for a decentralized, intelligent, and trustworthy network ecosystem.

### 1.1 The 6G Vision: Drivers, Requirements, and Transformative Use Cases

The anticipated sixth generation (6G) of wireless communication is envisioned not merely as an incremental enhancement of 5G but as a foundational paradigm shift, poised to catalyze a comprehensive digital and societal revolution [1]. It aims to transcend the traditional goal of enhanced mobile broadband, evolving into an intelligent, integrated digital infrastructure that seamlessly fuses the physical, digital, and human worlds [2]. This transformation is driven by the convergence of several powerful trends, including the explosive growth of the Internet of Everything (IoE), the demand for immersive human-machine interactions, and the imperative for autonomous, intelligent systems across all sectors of society and industry [3]. At the heart of this vision lies the concept of pervasive artificial intelligence (AI), where intelligence becomes a native, ubiquitous service embedded throughout the network, from the core to the extreme edge and end devices [4]. This shift from "connected things" to "connected intelligence" mandates a network that is not only a communication conduit but also a distributed sensing, computing, and reasoning platform [5].

To realize this ambitious vision, 6G networks must satisfy a set of extraordinarily stringent and multi-dimensional Key Performance Indicators (KPIs) that far exceed the capabilities of current systems. The overarching target is to achieve "extreme connectivity" and "hyper-connectivity," ensuring no constraints on data rate, coverage, or computing [6]. Specific quantitative goals include peak data rates reaching terabits-per-second (Tbps) to support bandwidth-intensive applications like holographic streaming [7]. Latency must be pushed to microsecond ($\mu$s) levels to enable real-time tactile feedback and control loops for mission-critical services [8]. Reliability must approach "seven-nines" (99.99999%) or higher for ultra-reliable low-latency communication (URLLC) in industrial and vehicular settings [9]. Furthermore, connection density must scale to support massive deployments, with projections of over 10 million devices per square kilometer for ubiquitous IoE [10]. Simultaneously, the network must be energy-sustainable, leveraging technologies like wireless power transfer and intelligent resource management to support "zero-energy" devices and reduce the overall carbon footprint [11]. These KPIs collectively define a performance envelope that is orders of magnitude more demanding than 5G, necessitating radical innovations in architecture, spectrum, and underlying technologies.

The transformative potential of 6G is most vividly illustrated through its enabling use cases, which promise to redefine human experience, industrial productivity, and societal infrastructure. A primary driver is the creation of truly **immersive communications**, blending extended reality (XR), holography, and haptics to deliver lifelike, interactive experiences [12]. This enables applications such as holographic telepresence for remote collaboration, immersive virtual classrooms, and tactile-enabled remote surgery, where the fidelity of sensory feedback is paramount [13]. Closely related is the development of the **Metaverse**, a persistent, shared virtual universe that converges physical and cyber worlds [14]. The Metaverse demands seamless, low-latency synchronization between digital twins and their physical counterparts, supported by massive, concurrent user interactions and real-time rendering of complex 3D environments [15].

In the physical world, 6G is critical for the full realization of **autonomous systems and intelligent transportation**. Vehicle-to-everything (V2X) communications will evolve to support cooperative perception, high-precision navigation, and real-time collective decision-making among connected and autonomous vehicles, requiring ultra-reliable, low-latency links [16]. Similarly, the **Industrial Internet of Things (IIoT)** will transition to ultra-reliable and deterministic wireless networks for advanced manufacturing (Industry 4.0/5.0), where sub-millisecond latency and perfect synchronization are needed for closed-loop control of robotic arms and collaborative machines [9]. Furthermore, 6G will enable **pervasive sensing and intelligence**, where the network itself becomes a distributed sensor for environmental monitoring, health diagnostics, and smart city management, integrating communication and sensing functions [17]. These use cases—from the deeply immersive and virtual to the critically physical and autonomous—collectively paint a picture of a future where 6G serves as the indispensable nervous system for a hyper-connected, intelligent world. However, achieving this vision introduces unprecedented complexity in network management, security, resource orchestration, and trust, creating a compelling imperative for the synergistic integration of blockchain and artificial intelligence as foundational enabling technologies.

**Table: Comparison of approaches in 1.1 The 6G Vision: Drivers, Requirements, and Transformative Use Cases**

| Aspect | Key Points / Features | Reference |
| :--- | :--- | :--- |
| **Vision & Paradigm Shift** | 6G is a foundational paradigm shift, not just an incremental enhancement of 5G. It aims to be an intelligent, integrated digital infrastructure fusing physical, digital, and human worlds, driven by IoE growth, immersive interactions, and autonomous systems. | [1], [2], [3] |
| **Core Concept: Pervasive AI** | Intelligence becomes a native, ubiquitous service embedded throughout the network, from core to edge. This shifts the focus from "connected things" to "connected intelligence," making the network a distributed sensing, computing, and reasoning platform. | [4], [5] |
| **Key Performance Indicators (KPIs)** | Targets "extreme/hyper-connectivity" with no constraints on data rate, coverage, or computing. Specific goals include Tbps peak data rates, microsecond latency, "seven-nines" reliability, connection density >10M devices/km², and energy sustainability for "zero-energy" devices. | [6], [7], [8], [9], [10], [11] |
| **Use Case: Immersive Communications & Metaverse** | Enables truly immersive experiences via XR, holography, and haptics (e.g., holographic telepresence, remote surgery). The Metaverse is a persistent, shared virtual universe converging physical and cyber worlds, requiring low-latency synchronization of digital twins and real-time 3D rendering. | [12], [13], [14], [15] |
| **Use Case: Autonomous Systems & IIoT** | Critical for full autonomous system realization. Enables advanced V2X for cooperative perception and decision-making in autonomous driving. Supports ultra-reliable, deterministic wireless for Industry 4.0/5.0 with sub-millisecond latency for closed-loop robotic control. | [16], [9] |
| **Use Case: Pervasive Sensing & Intelligence** | The network itself becomes a distributed sensor for environmental monitoring, health diagnostics, and smart city management, integrating communication and sensing functions. | [17] |
| **Enabling Technologies Synergy** | Achieving the 6G vision introduces unprecedented complexity in management, security, and orchestration, creating a compelling imperative for the synergistic integration of blockchain and artificial intelligence as foundational technologies. | (Implied by the concluding statement; specific references for blockchain integration include [18] and for AI integration, numerous papers above.) |


### 1.2 Core Challenges in 6G: Scalability, Security, Trust, and Resource Management

The ambitious vision for 6G—encompassing hyper-connectivity, ubiquitous intelligence, and the integration of physical and digital worlds—introduces a set of profound and interconnected challenges that existing network paradigms are ill-equipped to handle. These challenges stem from the unprecedented scale, heterogeneity, and performance demands of envisioned applications, ranging from massive-scale Internet of Things (IoT) and immersive extended reality to mission-critical cyber-physical systems. Four core challenges emerge as critical bottlenecks: scalability, security, trust, and resource management. Successfully addressing these is not merely an incremental improvement but a fundamental prerequisite for realizing the 6G promise.

First, the **scalability challenge** is multifaceted, driven by the sheer density and diversity of connected entities. 6G networks are expected to support a hyper-dense fabric of billions of heterogeneous devices, from simple sensors to autonomous vehicles and aerial platforms, all requiring seamless connectivity [6]. This massive scale is compounded by the network slicing paradigm, where numerous logical, end-to-end network slices with stringent and diverse performance requirements must be instantiated, managed, and orchestrated simultaneously [19]. The traditional centralized or cloud-centric architectures face insurmountable bottlenecks in control signaling, state synchronization, and data aggregation under such conditions. Furthermore, the integration of non-terrestrial networks (NTNs)—including satellites, high-altitude platforms (HAPs), and unmanned aerial vehicles (UAVs)—extends the network into three dimensions, adding another layer of topological and management complexity [20] [21]. This integrated space-air-ground network must scale not just in terms of device count but also in geographical coverage and service variety, demanding fundamentally new decentralized and self-organizing architectural principles.

Second, the **security challenge** in 6G is dramatically amplified. The vastly expanded attack surface includes the pervasive deployment of AI/ML models, a multitude of vulnerable IoT endpoints, softwarized network functions, and an open multi-vendor, multi-domain ecosystem [22] [23]. The automation of critical processes, while necessary for efficiency, also introduces new vectors for sophisticated AI-powered attacks, such as adversarial machine learning, data poisoning in federated learning systems, and model stealing [24] [25]. The stringent latency requirements for applications like tactile internet and autonomous systems often conflict with the computational overhead of traditional cryptographic security protocols. Moreover, the inherent openness and resource constraints of many 6G devices make them susceptible to physical layer attacks, jamming, and spoofing [26]. Consequently, 6G security must evolve from static, perimeter-based models to adaptive, context-aware, and pervasive frameworks that provide security guarantees across the entire protocol stack, including the physical layer [27] [28].

Closely related is the third core challenge: **decentralized trust**. In a 6G ecosystem populated by autonomous agents, devices from myriad manufacturers, and data from distributed sources, establishing and maintaining trust is paramount. The conventional model of trust anchored in centralized authorities (e.g., certificate authorities) becomes a single point of failure and a scalability bottleneck. Applications like vehicle-to-everything (V2X) communication, collaborative robotics, and federated learning require devices to trust data, models, and commands from peers without relying on a central arbiter [16]. The issue of data provenance and integrity is critical; for AI models trained on distributed data, verifying the authenticity and quality of contributed data is essential to prevent poisoning attacks and ensure reliable outcomes [25]. Furthermore, in multi-stakeholder scenarios like smart cities or integrated satellite-terrestrial networks, different administrative domains must collaborate, necessitating transparent and auditable trust mechanisms that do not require mutual pre-established agreements [29]. This calls for a paradigm shift towards decentralized trust models that can autonomously verify identities, actions, and data history.

Finally, the **resource management challenge** reaches new levels of complexity in 6G. The network's goal evolves from merely allocating communication bandwidth to orchestrating a unified pool of heterogeneous resources spanning sensing, communication, computation, and storage—often termed a "compute-communication-sensing" convergence [30] [31]. This must be done in real-time to meet the ultra-low latency (potentially sub-millisecond) and ultra-high reliability (e.g., 99.99999%) targets for services like industrial automation and remote surgery [32]. The dynamic and unpredictable nature of wireless channels, coupled with the mobility of users and network nodes (like UAVs), makes static optimization impossible. Moreover, the vision of "zero-touch" network and service management demands fully automated decision-making cycles that can perceive the network state, analyze it, and execute optimal resource allocation policies without human intervention [33] [34]. This necessitates intelligent, predictive, and adaptive resource orchestration frameworks that can simultaneously satisfy the conflicting Key Performance Indicators (KPIs) of numerous network slices and applications across the edge-cloud continuum [35] [36].

In summary, the 6G vision precipitates a perfect storm of challenges: scaling to universal connectivity, securing an open and intelligent ecosystem, establishing trust among autonomous entities, and dynamically managing a unified fabric of resources with extreme efficiency. These challenges are deeply interwoven; for instance, scalable management requires automation (AI), which itself must be secure and trustworthy. Addressing them in isolation with legacy approaches is futile. This creates a powerful imperative for a synergistic integration of two disruptive technological paradigms: Blockchain and Artificial Intelligence. Blockchain offers foundational properties of decentralization, immutability, transparency, and automated trust—directly tackling the trust and security challenges while enabling new decentralized scaling models. Artificial Intelligence provides the cognitive engine for predictive optimization, real-time adaptation, and intelligent automation—essential for scalable and zero-touch resource management. Their confluence, therefore, is not merely beneficial but is increasingly viewed as a cornerstone for architecting resilient, efficient, and trustworthy 6G systems [37] [38].

### 1.3 The Imperative for a Foundational Shift: From Centralized to Decentralized and Intelligent Networks

The envisioned landscape of sixth-generation (6G) wireless communications represents a radical departure from its predecessors, promising not merely incremental improvements but a fundamental transformation towards an "Internet of Intelligence" [39]. This future network is characterized by hyper-flexible, ubiquitous connectivity supporting a vast, heterogeneous ecosystem of intelligent agents, immersive experiences like the Metaverse, and mission-critical applications such as remote surgery and autonomous vehicle fleets [40]. To realize this vision, 6G must meet unprecedented and often conflicting Key Performance Indicators (KPIs): terabit-per-second data rates, microsecond-scale latency, near-perfect reliability, global three-dimensional coverage, and massive-scale connectivity for billions of devices and sensors [7]. Crucially, these performance targets must be achieved while ensuring stringent security, user privacy, energy efficiency, and operational autonomy. It is increasingly evident that the traditional, centralized, and predominantly model-based architectural paradigms that underpinned 4G and 5G networks are fundamentally ill-suited to meet these multifaceted 6G demands. This inadequacy necessitates a foundational shift towards a new architectural ethos built upon two synergistic pillars: native artificial intelligence (AI) for autonomous optimization and decentralized frameworks, epitomized by blockchain, for security, trust, and efficient resource orchestration.

The limitations of centralized architectures are manifold and become critical in the 6G context. First, the sheer scale and heterogeneity of the network—encompassing terrestrial, aerial, and non-terrestrial nodes—render centralized control and management prohibitively complex, slow, and vulnerable to single points of failure [41]. The core-to-edge data haul for centralized AI processing creates intolerable latency for real-time applications and congests backhaul links with massive data flows from ubiquitous sensors and devices [42]. Second, traditional model-based optimization, reliant on precise mathematical formulations of wireless channels and user behavior, struggles with the "unknown unknowns" of 6G's dynamic environment. The network will be too complex, too fast-changing, and too intertwined with human and machine intent for purely analytical solutions to manage efficiently [43]. This complexity is further exacerbated by the need for zero-touch network operation and management to reduce human intervention and operational costs, a goal that cannot be achieved without embedding intelligence directly into the network fabric [33].

Consequently, the infusion of **native AI** emerges as a non-negotiable imperative. AI is no longer merely an application running on the network but the core mechanism for its operation. It transforms the network from a static infrastructure into a self-evolving, cognitive system. AI-driven techniques, such as deep reinforcement learning and federated learning, are essential for real-time, adaptive resource allocation, predictive network slicing, and automated root cause analysis (RCA) in a system of immense scale [44]. Native intelligence enables the network to learn from experience, predict traffic patterns and failures, and autonomously reconfigure itself to maintain optimal performance and quality of experience (QoE) for diverse, customized services [45]. This shift from "connected things" to "connected intelligence" is central to the 6G roadmap [4].

However, the pervasive deployment of AI itself introduces profound new challenges, primarily concerning **trust, security, and data governance**. Centralized AI models trained on aggregated user data pose severe privacy risks and create attractive targets for cyber-attacks [22]. The "black-box" nature of complex AI models, such as deep neural networks, erodes trust, especially when they control safety-critical processes. How can one trust an AI model managing autonomous vehicle coordination or a surgical robot without understanding its decision-making logic? [46]. Furthermore, in a multi-stakeholder environment involving multiple service providers, enterprises, and users, establishing verifiable trust and enabling transparent, auditable transactions for resource sharing (e.g., spectrum, compute, data) becomes paramount [18].

This is where the second pillar, **decentralization through blockchain and Distributed Ledger Technology (DLT)**, becomes foundational. Blockchain addresses the core trust deficits of centralized systems by providing a transparent, immutable, and cryptographically secure ledger for recording transactions and states without a central authority. Its intrinsic properties of decentralization, auditability, and non-repudiation are directly aligned with 6G's security and operational needs [37]. For instance, blockchain can create tamper-proof logs for network slice leasing, automate service level agreement (SLA) verification via smart contracts, and establish decentralized identity management for the massive Internet of Things (IoT) ecosystem, preventing spoofing and unauthorized access [47]. Crucially, blockchain provides the ideal trust anchor for decentralized AI paradigms like Federated Learning (FL). It can securely coordinate participating devices, aggregate model updates in a verifiable manner, and incentivize data contribution while preserving local data privacy [48]. The convergence thus creates a virtuous cycle: AI provides the intelligence for autonomous, efficient network operations, while blockchain provides the trusted, secure, and transparent framework within which this intelligence can operate and collaborate.

Therefore, the convergence of AI and blockchain is not a mere technological augmentation but a **foundational architectural shift** essential for 6G. It moves the network from a centralized, inflexible, and opaque paradigm to a decentralized, intelligent, and trustworthy ecosystem. AI injects the cognitive capability needed for autonomy and adaptation at scale, while blockchain embeds the trust, security, and coordination mechanisms required for a secure and collaborative multi-party system. This synergistic integration is poised to tackle 6G's most daunting challenges, from managing ultra-dense, cell-free radio access networks and orchestrating integrated sensing, communication, and computing resources, to securing the extended reality (XR) experiences of the Metaverse and ensuring the safety of autonomous cyber-physical systems [49]. As research progresses, this dual foundation will enable 6G to fulfill its promise as a resilient, efficient, and intelligent platform that seamlessly blends the physical and digital worlds for the benefit of society.

### 1.4 Synergistic Convergence: Blockchain and AI as Complementary Enablers

The envisioned 6G wireless ecosystem promises a hyper-connected, intelligent, and immersive digital universe, integrating massive-scale Internet of Things (IoT), pervasive edge intelligence, and mission-critical applications from autonomous systems to the metaverse. This paradigm shift, however, introduces profound challenges in trust, security, privacy, scalability, and efficient resource orchestration within inherently decentralized and heterogeneous networks. Addressing these challenges requires more than incremental improvements; it demands a foundational rethinking of system architecture. This survey posits that the synergistic convergence of Blockchain and Artificial Intelligence (AI) provides a transformative framework to meet these imperatives. Rather than operating in isolation, these two disruptive technologies function as complementary enablers, each mitigating the core limitations of the other to unlock the full potential of 6G.

Blockchain technology offers the essential trust and coordination layer required for secure and transparent AI operations in a decentralized 6G environment. At its core, blockchain establishes a shared, immutable version of the truth between participants that do not inherently trust one another [50]. This property is critical for collaborative AI paradigms like Federated Learning (FL), where multiple devices or edge nodes train a global model without sharing raw data. While FL enhances privacy, it remains vulnerable to security threats such as model tampering by a malicious central server or poisoning attacks from compromised clients. By integrating FL with blockchain, the training process can be decentralized and secured. Smart contracts can automate and enforce the rules of model aggregation and participant incentive mechanisms in a transparent manner [51]. The immutable ledger provides an auditable trail of all model updates, contributions, and transactions, enabling the detection of anomalies and ensuring that only verified updates are incorporated into the global model [52]. This creates a "trustless" environment where security does not rely on a single entity but is mathematically enforced by the network's consensus, aligning perfectly with the decentralized ethos of 6G edge networks.

Furthermore, blockchain empowers secure and equitable data and AI marketplaces, which are pivotal for the data-driven intelligence of 6G. In traditional settings, data silos and privacy concerns stifle innovation. Blockchain, combined with cryptographic techniques like zero-knowledge proofs (ZKPs), enables privacy-preserving data sharing and computation. For instance, ZKPs can allow a participant to prove the validity of their locally trained model update or data quality without revealing the underlying private data, a technique explored in frameworks like zkDFL [53]. This facilitates verifiable and privacy-conscious collaboration. Moreover, blockchain can manage digital assets representing data or AI models, such as Non-Fungible Tokens (NFTs), to create transparent trading environments. As demonstrated in a Decentralized Energy Marketplace, NFTs can represent unique energy profiles, enabling secure and automated peer-to-peer trading managed by smart contracts [54]. This model can be extended to 6G for trading sensor data, computational resources, or AI model inferences, ensuring data owners retain ownership and are fairly compensated [55]. Thus, blockchain provides the decentralized trust, auditability, and micro-transaction capability necessary to operationalize distributed AI at scale.

Conversely, AI injects much-needed intelligence and adaptability into blockchain systems, overcoming their inherent performance bottlenecks and enhancing their functionality for 6G's dynamic demands. Traditional blockchain consensus mechanisms, like Proof-of-Work (PoW), are notoriously resource-intensive and lack utility beyond securing the ledger. AI offers revolutionary alternatives. Consensus can be reimagined as a useful computational task. For example, Proof-of-Useful-Work (PoUW) schemes can direct the mining effort towards training machine learning models, thereby contributing valuable AI computation to the network instead of solving cryptographic puzzles [56]. Similarly, AI can optimize consensus itself; deep reinforcement learning agents can model blockchain growth as a Markov decision process to make optimal verification decisions, potentially sparing computational resources [57]. AI-driven consensus algorithms like AICons aim to improve energy efficiency and fairness by utilizing all participants' local ML models to select validators and evaluate contributions based on model accuracy, energy use, and bandwidth [58].

Beyond consensus, AI is crucial for managing the blockchain lifecycle within 6G's complex network conditions. Machine learning models can predict transaction confirmation times by analyzing network congestion and gas fees, allowing for dynamic fee adjustment and improved user experience [59]. AI is also vital for security and maintenance, enabling the detection of malicious smart contract code, fraudulent DeFi transactions, and anomalous network behavior [60] [61]. For resource-constrained IoT devices at the 6G edge, AI can facilitate lightweight, adaptive blockchain architectures. It can optimize sharding strategies, manage cross-chain interoperability intelligently, and implement smart intrusion detection systems at network gateways [47] [62]. In essence, AI transforms blockchain from a relatively static ledger into a dynamic, self-optimizing, and intelligent network component capable of meeting the low-latency, high-throughput, and adaptive requirements of 6G applications.

This bidirectional synergy creates a powerful virtuous cycle for 6G. Blockchain provides the secure, transparent, and decentralized foundation upon which trustworthy collaborative AI can be built. In turn, AI enhances the scalability, efficiency, and intelligence of the blockchain infrastructure itself. This convergence is not merely additive but multiplicative, enabling novel capabilities such as decentralized autonomous organizations (DAOs) for network governance, verifiable and privacy-preserving semantic communication, and robust digital twin ecosystems for smart cities and industrial IoT. As we move towards a 6G world characterized by cyber-physical-social integration, this fusion of decentralized trust and collective intelligence becomes not just advantageous but imperative. The following sections of this survey will delve into the technical architectures, specific mechanisms, and groundbreaking use cases where this Blockchain-AI synergy is actively shaping the future of wireless communications, from securing federated learning at the edge to enabling the transparent and intelligent fabric of the metaverse.

**Table: Comparison of approaches in 1.4 Synergistic Convergence: Blockchain and AI as Complementary Enablers**

| Method/Model | Key Idea/Contribution | Reference |
|--------------|----------------------|-----------|
| Federated Learning (FL) with Blockchain | Integrates FL with blockchain to decentralize and secure the training process. Smart contracts automate model aggregation and incentives, while the immutable ledger provides an auditable trail for anomaly detection. | [51], [52] |
| zkDFL | A decentralized federated learning framework that uses zero-knowledge proofs (ZKPs) to allow participants to prove the validity of their model updates without revealing private data. | [53] |
| Proof-of-Useful-Work (PoUW) | A consensus mechanism that directs mining effort towards training machine learning models, contributing useful AI computation instead of solving cryptographic puzzles. | [56] |
| AI-driven Blockchain Consensus (AICons) | An AI-enabled consensus algorithm that utilizes all participants' local ML models to select validators and evaluate contributions based on model accuracy, energy use, and bandwidth to improve energy efficiency and fairness. | [58] |
| Machine Learning for Transaction Confirmation Time Prediction | Uses ML models to predict Ethereum transaction confirmation times by analyzing network congestion and gas fees, enabling dynamic fee adjustment. | [59] |
| AI for Blockchain Security & Maintenance | Employs AI/ML for detecting malicious smart contract code, fraudulent DeFi transactions, and anomalous network behavior. | [60], [61] |
| AI-optimized Lightweight Blockchain Architectures | Uses AI to optimize sharding strategies, manage cross-chain interoperability, and implement smart intrusion detection for resource-constrained IoT devices at the edge. | [47], [62] |
| Blockchain-based Data/AI Marketplace with NFTs | Uses Non-Fungible Tokens (NFTs) to represent unique digital assets (e.g., data, AI models, energy profiles) enabling secure, transparent peer-to-peer trading managed by smart contracts. | [54], [55] |
| Reinforcement Learning for Blockchain Consensus | Models blockchain growth as a Markov decision process, using a deep reinforcement learning agent to make optimal verification decisions, potentially sparing computational resources. | [57] |



### Roadmap and Taxonomy

The following taxonomy tree outlines the structure of this survey:


```plaintext
A Survey of Blockchain and Artificial Intelligence for 6G Wireless Communications
|----Section 1: Integration of Blockchain and AI in 6G Wireless Networks
|     |----Subsection 1.1: Blockchain for AI Systems
|     |     |----Blockchain consensus mechanisms: [63][64][65]
|     |     |----Sharding techniques: [66][67][68]
|     |     |----Decentralized ledger frameworks: [69][70][71]
|     |     |----Privacy-enhancing tools: [72][53][73]
|     |----Subsection 1.2: AI Integration in Blockchain
|     |     |----AI-driven ledger optimization: [74][75][76]
|     |     |----Federated learning frameworks: [77][78][79]
|     |     |----Zero-knowledge proofs for security: [53][80][81]
|     |     |----Blockchain scalability enhancements: [82][83][23]
|     |----Subsection 1.3: Blockchain and AI Use Cases
|     |     |----IoT frameworks: [84][85][86]
|     |     |----Healthcare innovations: [87][88][89]
|     |     |----Autonomous vehicles: [90][91][92]
|     |     |----Smart city deployments: [93][94][95]

|----Section 2: Artificial Intelligence Applications in 6G Wireless Networks
|     |----Subsection 2.1: AI Techniques for Optimization
|     |     |----Reinforcement learning: [96][97][98]
|     |     |----Dynamic resource allocation: [9][99][100]
|     |     |----Generative AI for semantic communication: [101][102][103]
|     |     |----Task-oriented AI frameworks: [31][104][105]
|     |----Subsection 2.2: AI for Privacy and Security
|     |     |----Explainable AI for security: [46][106][107]
|     |     |----Privacy-preserving federated learning: [79][108][53]
|     |     |----Defense against adversaries: [109][110][111]
|     |     |----Trust mechanisms in AI: [112][56][113]
|     |----Subsection 2.3: AI in Semantic Communications
|     |     |----Semantic-aware systems: [114][93][15]
|     |     |----Integration of AI-generated models: [101][115][116]
|     |     |----Knowledge transfer frameworks: [117][118][119]

|----Section 3: Synergies Between Blockchain and AI for 6G
|     |----Subsection 3.1: Combined Blockchain-AI Frameworks
|     |     |----Blockchain-enabled AI trust: [53][106][120]
|     |     |----Federated learning on blockchain: [121][78][108]
|     |     |----Generative AI with blockchain: [101][122][123]
|     |----Subsection 3.2: Privacy and Security Advancements
|     |     |----Zero-knowledge proofs: [53][124][72]
|     |     |----Blockchain-enhanced AI security: [125][126][85]
|     |     |----Fine-grained data control: [53][127][128]
|     |----Subsection 3.3: Applications in Emerging Technologies
|     |     |----Edge computing integration: [129][85][130]
|     |     |----Healthcare systems for IoT: [131][89][132]
|     |     |----Metaverse solutions: [133][79][125]
|     |     |----Smart city frameworks: [134][120][94]
```


## 2 Foundational Technologies: A Primer on Blockchain and AI for 6G

This section provides a technical primer on the core components of both technologies tailored for wireless environments. For Blockchain, it covers architectures (public, private, consortium), consensus mechanisms (PoW, PoS, DAG-based), scalability solutions (sharding, sidechains), and smart contracts. For AI, it reviews key paradigms including Deep Learning, Reinforcement Learning (single/multi-agent), Federated Learning, and Generative AI, focusing on their inherent properties and initial applications in network optimization and security.

### 2.1 Core Blockchain Architectures and Mechanisms for Decentralized 6G

The foundational role of blockchain in 6G networks stems from its ability to provide decentralized trust, data integrity, and automated contract execution. However, the diverse and stringent requirements of 6G use cases—ranging from ultra-reliable low-latency communications (URLLC) for industrial IoT to massive-scale public sensor networks—demand careful selection and adaptation of blockchain architectures and consensus mechanisms. The core blockchain paradigms—public, private, and consortium—offer distinct trade-offs in decentralization, access control, and performance, making them suitable for different 6G operational scenarios.

Public blockchains, characterized by permissionless participation and full decentralization, are inherently transparent and censorship-resistant. While this model aligns with the vision of a fully open and user-centric 6G ecosystem, its classical implementations face significant challenges. The high energy consumption of Proof-of-Work (PoW) consensus, as highlighted in [135], and potential scalability bottlenecks make vanilla public blockchains less suitable for latency-sensitive or resource-constrained 6G applications like autonomous vehicle coordination or dense IoT deployments. Nevertheless, for certain public 6G services requiring maximal auditability and trust among unrelated parties—such as transparent spectrum auctioning or public data marketplaces—innovations in energy-efficient public ledgers remain relevant.

In contrast, private and consortium blockchains, which are permissioned, offer a more pragmatic fit for many 6G network scenarios. A private blockchain, governed by a single entity (e.g., a mobile network operator), provides high throughput, low latency, and strict privacy, making it ideal for internal network management, such as automating SLA verification between network slices or securing device firmware updates within a private industrial network. The consortium blockchain, governed by a pre-selected group of organizations, strikes a balance between decentralization and control. This architecture is particularly promising for multi-stakeholder 6G environments, such as secure infrastructure sharing among competing operators [136], federated data marketplaces for smart cities [137], or cross-domain trust management. The performance assessment in [38] confirms that a properly configured consortium blockchain can meet the performance and scalability requirements of fine-grained 6G scenarios.

The performance and security of any blockchain are fundamentally dictated by its consensus mechanism. For 6G integration, the trade-offs between security, latency, energy efficiency, and scalability are paramount. Proof-of-Work (PoW), while securing major cryptocurrencies, is notoriously energy-intensive and slow, creating a misalignment with 6G's green and low-latency goals. Proposals like Evolved-Proof-of-Work (E-PoW) aim to salvage this situation by repurposing mining computations for useful AI training tasks, connecting block mining with AI learning in 6G systems [138]. Proof-of-Stake (PoS) and its variants dramatically reduce energy consumption by selecting validators based on their staked economic value rather than computational work. However, PoS introduces different concerns, such as potential centralization of wealth and vulnerability to long-range attacks, which are critical considerations for 6G's security fabric [139].

For consortium and private blockchains underpinning 6G services, Byzantine Fault Tolerance (BFT) consensus protocols are often preferred. Practical Byzantine Fault Tolerance (PBFT) and its derivatives provide high throughput and finality with low latency, which is crucial for real-time 6G applications. However, their performance is highly sensitive to network conditions. Studies like [140] and [141] rigorously analyze PBFT in non-ideal wireless channels, considering path loss and fading for mmWave and THz signals—key 6G enablers. They identify an "active distance" beyond which consensus reliability plummets, providing vital design guidelines for deploying wireless blockchain networks. RAFT, a crash-fault-tolerant protocol, offers simpler and more efficient consensus for environments where malicious nodes are not the primary concern, such as within a trusted operator's domain.

Emerging consensus models are being tailored specifically for the 6G and IoT landscape. Proof-of-Reputation (PoR) leverages the historical behavior of nodes to select leaders, integrating trust management directly into the consensus layer, which is vital for evaluating the continuous trustworthiness of devices in a dynamic 6G network [142] [143]. Lightweight alternatives like Proof-of-Authentication (PoAh) replace computational puzzles with cryptographic authentication, making them suitable for resource-constrained IoT devices at the 6G edge [144]. Furthermore, Directed Acyclic Graph (DAG)-based structures, such as Tangle, offer a promising alternative to linear blockchains by allowing parallel transaction processing, potentially increasing scalability and reducing fees for micro-transactions in massive IoT environments [145] [146].

The wireless nature of 6G itself introduces unique challenges and opportunities for consensus design. The instability of wireless links directly impacts consensus reliability, as messages may be delayed or lost. Innovative solutions like Symbiotic Blockchain Consensus (SBC) leverage cognitive backscatter communications to create mutualistic transmission relationships between nodes, improving consensus success rates and reducing energy consumption in wireless PBFT and RAFT networks [147]. Ultimately, the choice of blockchain architecture and consensus is not one-size-fits-all but must be context-aware, aligning with the specific trust model, performance requirements, and physical layer realities of the target 6G application scenario.

**Table: Comparison of approaches in 2.1 Core Blockchain Architectures and Mechanisms for Decentralized 6G**

| Blockchain Paradigm/Consensus Mechanism | Key Characteristics | Suitable 6G Use Cases / Scenarios | Performance & Security Considerations (from Source Papers) | Reference(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Public Blockchain** (e.g., with PoW) | Permissionless, fully decentralized, transparent, censorship-resistant. | Transparent spectrum auctioning, public data marketplaces (requiring maximal auditability among unrelated parties). | High energy consumption (PoW), potential scalability bottlenecks, less suitable for latency-sensitive/resource-constrained apps. PoW energy footprint exceeds PoS-based systems by orders of magnitude. | [135], [137] |
| **Private Blockchain** | Permissioned, governed by a single entity (e.g., MNO), high throughput, low latency, strict privacy. | Internal network management (e.g., automating SLA verification between network slices), securing device firmware updates within a private industrial network. | Offers high performance (throughput, latency) suitable for internal, trusted domains. Performance evaluation shows it can complete federation procedures faster than public blockchains. | [148] |
| **Consortium Blockchain** | Permissioned, governed by a pre-selected group of organizations, balances decentralization and control. | Multi-stakeholder environments: secure infrastructure sharing among operators, federated data marketplaces for smart cities, cross-domain trust management. | A properly configured consortium blockchain can meet the performance and scalability requirements of fine-grained 6G scenarios. Enables accountable and transparent network sharing. | [38], [136], [137] |
| **Proof-of-Work (PoW)** | Validators compete via computational puzzles; high security but energy-intensive. | Legacy public blockchain applications. Proposals like E-PoW aim to repurpose mining for useful tasks (e.g., AI training). | Notoriously energy-intensive and slow, misaligned with 6G's green/low-latency goals. E-PoW can salvage computing power from mining for AI training. Provides strongest formal security guarantees among permissionless mechanisms. | [135], [138], [139] |
| **Proof-of-Stake (PoS) & Variants** | Validators selected based on staked economic value; dramatically reduces energy consumption. | Energy-efficient public or consortium ledgers. | Introduces concerns like potential centralization of wealth and vulnerability to long-range attacks. Can achieve security guarantees similar to PoW with hybrid approaches. | [139] |
| **Byzantine Fault Tolerance (BFT)** (e.g., PBFT) | High throughput, finality with low latency, suitable for permissioned networks. | Real-time 6G applications within consortium/private blockchains (e.g., secure IoT device data protection). | Performance highly sensitive to network conditions. In non-ideal wireless channels (mmWave/THz), consensus reliability plummets beyond an "active distance". | [140], [141], [149] |
| **RAFT** | Crash-fault-tolerant protocol, simpler and more efficient than BFT. | Environments within a trusted operator's domain where malicious nodes are not the primary concern. | Offers simpler consensus. Performance in wireless networks is also affected by channel conditions and has its own "active distance". | [140] |
| **Proof-of-Reputation (PoR)** | Leverages historical node behavior to select leaders, integrates trust management. | Dynamic 6G networks for continuous trustworthiness evaluation of devices, blockchain-based MEC systems. | An alternative consensus mechanism where nodes with highest reputation form the consensus group. Critical for trustworthy 6G networks via blockchain-based Trust and Reputation Management. | [142], [143], [150] |
| **Proof-of-Authentication (PoAh)** | Replaces computational puzzles with cryptographic authentication. | Resource-constrained IoT devices at the 6G edge, private/permissioned blockchains for large-scale IoT. | A lightweight consensus algorithm suitable for resource-constrained devices, offering low latency (e.g., ~3 secs on Raspberry Pi). | [144] |
| **DAG-based (e.g., Tangle, StakeDag)** | Directed Acyclic Graph structure allows parallel transaction processing. | Massive IoT environments for micro-transactions, scalable trustless systems. | Can overcome high resource consumption and low throughput of linear blockchains. Performance and security (e.g., double-spending attack probability) are impacted by network load. StakeDag combines PoS with DAG for leaderless asynchronous BFT. | [145], [146] |
| **Symbiotic Blockchain Consensus (SBC)** | Leverages cognitive backscatter communications for mutualistic transmission between nodes. | Wireless PBFT and RAFT networks in 6G to combat link instability and high energy consumption. | Increases consensus success rate and reduces energy consumption in wireless networks by creating symbiotic relationships between nodes. | [147] |


### 2.2 Scalability and Performance Enhancements for Blockchain in 6G

The stringent performance requirements of 6G networks—envisioning ultra-low latency, massive device connectivity, and multi-gigabit throughput—pose a fundamental challenge for the direct integration of traditional blockchain architectures. The inherent limitations of sequential block processing, full network replication, and consensus-intensive validation create significant bottlenecks in transaction throughput and confirmation latency. To bridge this gap and enable blockchain to serve as a trustworthy substrate for 6G applications like massive IoT, real-time edge intelligence, and the metaverse, a new generation of scalability and performance enhancements is critical. These advancements primarily revolve around three interconnected paradigms: sharding, layer-2 solutions and sidechains, and novel ledger structures like Directed Acyclic Graphs (DAGs).

Sharding stands as the most prominent on-chain scaling technique, directly attacking the scalability trilemma by partitioning the network's workload. The core principle involves dividing the entire network of nodes into smaller, parallel committees called shards, each responsible for processing a distinct subset of transactions and maintaining a portion of the global state. This parallelization promises near-linear throughput scaling with the number of shards. Research such as [66] provides a foundational framework, demonstrating how sharding can be applied to general blockchain workloads beyond cryptocurrencies. Sharding can be implemented across different dimensions: network sharding divides validator nodes, transaction sharding allocates transactions to shards (often via account address hashing), and state sharding partitions the global ledger storage, as explored in [151]. However, sharding introduces profound security and complexity challenges. A primary concern is the reduced security threshold within a single shard, making it vulnerable to takeover if an adversary concentrates power. Protocols like [152] and [153] aim to bolster shard security to resist up to half of the participants being malicious. Furthermore, cross-shard transactions, which require coordination between multiple shards, become a critical performance bottleneck and a source of new attack vectors. Simple two-phase commit protocols can lock assets and increase latency. Innovative solutions like [68] propose buffer mechanisms and optimized communication for atomic cross-shard processing, while [154] introduces architectures that obviate intra-shard consensus to reduce overhead. Security analyses also reveal novel threats in sharded ecosystems, such as front-running attacks that manipulate transaction ordering across shards, as detailed in [67], and denial-of-service attacks that target specific shards through hash-based transaction flooding, discussed in [155]. The formal foundations and trade-offs of sharding are systematically analyzed in works like [156] and [157].

Complementing on-chain sharding, Layer-2 (L2) scaling solutions and sidechains operate on the principle of moving the bulk of transaction processing off the main blockchain (Layer-1), thereby alleviating its congestion. These protocols batch numerous transactions into a single, periodically settled proof on the main chain. Sidechains are independent blockchains with their own consensus rules, connected to the main chain via two-way pegs, enabling asset transfer. Layer-2 solutions, such as state channels, rollups, and plasma, offer varying trade-offs between security, generality, and withdrawal delays. As surveyed in [158], solutions like the Lightning Network (for payment channels) or optimistic/zk-rollups allow for high-frequency, low-latency, and low-cost transactions ideal for 6G micro-payments and IoT data exchanges. Frameworks like [159] propose enhancements to existing L2 payment networks to mitigate specific inefficiencies. The core value proposition for 6G is that these solutions can leverage the high-speed, low-latency device-to-device (D2D) communication fabrics of 6G to establish and manage off-chain channels or sidechain consensus, while the main blockchain provides ultimate security and settlement guarantees with less frequent interaction.

A radical departure from the linear chain-of-blocks paradigm is found in Directed Acyclic Graph (DAG)-based ledger structures. In a DAG, each new transaction or block references multiple previous ones, forming a graph where transactions can be added concurrently without waiting for a single canonical chain to progress. This intrinsic parallelism offers the potential for very high throughput and fast initial confirmation, making DAGs particularly attractive for high-volume, asynchronous 6G environments like IoT sensor networks. The IOTA Tangle is a seminal example, and its behavior under dynamic loads is analyzed in [145]. However, DAGs face unique challenges in achieving consensus on a total transaction order and preventing conflicts. Protocols like [64] address transaction inclusion collisions to improve throughput, while [71] and [160] propose consensus mechanisms to achieve fast confirmation with security guarantees. Security analyses, such as [161], reveal that deviations from honest transaction selection strategies can undermine throughput and decentralization. Furthermore, DAGs must be resilient to specific attacks like parasite chain attacks, as studied in [162]. For resource-constrained 6G endpoints, lightweight DAG variants are essential, such as the two-layer architecture in [163] which minimizes on-device storage, or [164] designed for mobile D2D ecosystems.

The convergence of these scalability techniques with 6G network capabilities creates a powerful synergy. Sharding can map naturally onto network slicing in 6G, where a slice could manage a specific blockchain shard. The ultra-reliable low-latency communication (URLLC) features of 6G can drastically reduce cross-shard messaging delays. DAG-based ledgers can flourish in dense mesh networks enabled by 6G's advanced D2D communication. Moreover, edge computing resources in the 6G architecture can host Layer-2 processing or function as lightweight validators for shards or DAG tips, as conceptualized in frameworks like [165]. Ultimately, the scalability enhancements for blockchain are not merely incremental improvements but foundational re-architectings necessary to transform blockchain from a potential bottleneck into a seamless, high-performance trust layer capable of underpinning the demanding and decentralized applications envisioned for the 6G era.

**Table: Comparison of approaches in 2.2 Scalability and Performance Enhancements for Blockchain in 6G**

| Method/Paradigm | Core Principle & Mechanism | Key Challenges & Limitations | Proposed Solutions & Protocols (from Source Papers) | Synergy with 6G Networks |
| :--- | :--- | :--- | :--- | :--- |
| **Sharding** | Partitions the network into parallel committees (shards), each processing a distinct subset of transactions and maintaining a portion of the global state. Enables near-linear throughput scaling. | Reduced security per shard (single-shard takeover risk); complexity of cross-shard transactions (coordination bottleneck, new attack vectors like front-running and DoS). | [66]; [151]; [152]; [153]; [68]; [154]; [67]; [155]; [156]; [157] | Can map naturally onto 6G network slicing. Ultra-reliable low-latency communication (URLLC) can drastically reduce cross-shard messaging delays. |
| **Layer-2 Solutions & Sidechains** | Moves bulk transaction processing off the main chain (Layer-1). Batches transactions into a single, periodically settled proof on the main chain. Includes sidechains, state channels, rollups, and plasma. | Security vs. generality vs. withdrawal delay trade-offs; potential trust assumptions or high computational requirements for proving correctness. | [158]; [159] | Can leverage 6G's high-speed, low-latency D2D communication for establishing/managing off-chain channels or sidechain consensus. Main chain provides ultimate security with less frequent interaction. |
| **DAG-based Ledgers** | Uses a Directed Acyclic Graph structure where new transactions/blocks reference multiple previous ones, enabling concurrent addition and intrinsic parallelism. | Achieving consensus on total transaction order; preventing conflicts (double-spends); vulnerability to specific attacks (e.g., parasite chains, incentive attacks). | [145]; [64]; [71]; [160]; [161]; [162]; [163]; [164] | Can flourish in dense mesh networks enabled by 6G's advanced D2D communication. Lightweight DAG variants are suitable for resource-constrained 6G endpoints. |


### 2.3 Smart Contracts and Decentralized Automation

At the core of blockchain's operational value for 6G networks lies the concept of smart contracts—self-executing, tamper-proof programs that encode the terms of an agreement directly into code [166]. These autonomous agents provide the foundational mechanism for decentralized automation, enabling trustless and transparent coordination between network entities without requiring a central authority. For the dynamic, heterogeneous, and ultra-dense 6G ecosystem, smart contracts offer a paradigm shift from manual, paper-based agreements and centralized orchestration to automated, verifiable, and efficient digital workflows. Their primary role is to stipulate and enforce the rules of interaction between mutually distrusting parties, such as mobile network operators, infrastructure providers, service tenants, and end-users, by making contractual conditions accurately available on the blockchain [167].

A critical application in 6G is the automation of dynamic resource trading and infrastructure sharing. The vision of network-as-a-service and dense small-cell-as-a-service demands fine-grained, real-time trading of bandwidth, compute, and storage resources. Smart contracts can automate these roaming and sharing agreements, as demonstrated by systems like Bandcoin, which uses smart contracts to automate mobile network bandwidth roaming agreements between operators [168]. Similarly, for small-cell-as-a-service, smart contracts can implement simple but effective Service Level Agreements (SLAs) between individual small cell providers and mobile operators, enabling a decentralized marketplace for network infrastructure [169]. This automation reduces administrative overhead, minimizes settlement times, and enables new business models where any entity can become a micro-provider.

Furthermore, smart contracts are pivotal for automated SLA enforcement and decentralized orchestration in zero-touch network management. Future 6G applications, such as remote surgery and connected vehicles, require SLAs that are dynamic, flexible, and automatically enforceable [170]. A smart contract can continuously monitor Key Performance Indicators (KPIs) fed by oracles or integrated sensors, and autonomously execute actions—such as issuing penalties, triggering compensation, or reallocating resources—when SLA thresholds are breached. This creates a transparent and accountable framework for service assurance. Architectures like BEAT propose end-to-end automated, transparent, and accountable network sharing by leveraging blockchain and smart contracts to manage and enforce SLAs with minimal human intervention [136].

However, deploying smart contracts in high-performance 6G environments is fraught with significant challenges. A primary constraint is the inherent limit of on-chain computation. Executing complex logic directly on a blockchain is expensive in terms of transaction fees (gas) and latency, as every node in the network must redundantly process the contract [171]. This is prohibitive for real-time network decisions requiring millisecond-level responses. Solutions to this scalability-privacy trilemma are actively being researched. One promising direction is the design of scalable and privacy-preserving on/off-chain smart contracts, where only the minimal necessary logic and state hashes are stored on-chain, while the bulk of computation and sensitive data is handled off-chain among the participating parties [172]. Techniques like optimistic execution, where results are assumed correct and only disputed executions are verified on-chain, can also drastically reduce overhead [173].

Security and correctness present another monumental challenge. Smart contracts, once deployed, are immutable, making post-deployment bug fixes impossible without sophisticated upgradeability patterns [174]. Vulnerabilities can lead to catastrophic financial losses and network disruptions. Therefore, ensuring contract security is paramount. This has spurred extensive research into vulnerability detection using formal verification, symbolic execution (e.g., [175]), fuzzing, and deep learning [176]. Automated repair tools are also emerging to fix common vulnerabilities in smart contracts before deployment [177]. For 6G, where contracts will manage critical infrastructure, building secure design models using formal methods from the outset is essential [178].

To overcome the limitations of traditional smart contracts in handling complex, data-driven logic required for 6G optimization, the emerging concept of AI-enabled or verifiable smart contracts is gaining traction. These are contracts whose logic or verification process is augmented or generated by Artificial Intelligence. A key innovation is the use of AI, particularly machine learning models, to make decisions within or for the contract. For instance, a contract governing radio resource allocation could integrate a lightweight reinforcement learning agent to make optimal slicing decisions. The challenge lies in verifiably executing such AI models on-chain in a trustless manner. Projects like Agatha address this by enabling verifiable off-chain execution of complex Deep Neural Network (DNN) computations, where the integrity of the AI's output is proven on-chain without requiring all nodes to re-run the entire model [179]. This bridges the gap between the expressive power of AI and the trust guarantees of blockchain.

Moreover, the fusion of Explainable AI (XAI) with smart contracts can enhance transparency and trust in automated network decisions. An AI-driven smart contract managing RAN slicing could use XAI techniques to generate auditable justifications for its resource allocation decisions, which are then recorded on the ledger [180]. This meets the stringent need for trustworthiness in critical 6G services. The future of decentralized automation in 6G thus lies in hybrid architectures that leverage the trust anchor of blockchain-based smart contracts for settlement and enforcement, while orchestrating complex, AI-driven optimization and real-time control in off-chain, high-performance edge computing environments. This symbiotic relationship positions smart contracts not merely as simple payment scripts, but as the critical governance and coordination layer for a truly decentralized, automated, and intelligent 6G network.

**Table: Comparison of approaches in 2.3 Smart Contracts and Decentralized Automation**

| Method/Concept | Key Idea | Application in 6G Context | Key Challenge Addressed | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Smart Contracts (General) | Self-executing, tamper-proof programs that encode agreement terms into code, enabling trustless coordination. | Foundational mechanism for decentralized automation, shifting from manual agreements to automated digital workflows. | Ensuring conditions (e.g., time) are accurately available on-chain for correct execution. | [166], [167] |
| Bandcoin | Uses smart contracts to automate mobile network bandwidth roaming agreements between operators. | Automation of dynamic resource trading and infrastructure sharing for network-as-a-service models. | Improving transaction performance for efficient, fine-grained roaming agreements. | [168] |
| Smart Contract SLAs for Small-Cell-as-a-Service | Implements simple but effective SLAs between small cell providers and mobile operators via smart contracts. | Enables a decentralized marketplace for network infrastructure (e.g., dense small-cell-as-a-service). | Creating scalable and legally sound agreements for micro-providers. | [169] |
| BEAT Architecture | Blockchain-enabled accountable and transparent network sharing architecture using smart contracts to manage/enforce SLAs. | Automated, transparent, and accountable end-to-end network sharing with minimal human intervention. | Difficulties in negotiating, monitoring, and enforcing SLAs in shared infrastructure. | [136] |
| Lazy Contracts | Alleviates high gas costs by secure and trustless off-chain execution, with on-chain state hashes and dispute resolution. | Reduces cost and latency for smart contract execution in high-performance 6G environments. | High on-chain computation costs (gas) and latency prohibitive for real-time decisions. | [171] |
| Scalable & Privacy-preserving On/Off-chain Design | Splits contract logic; minimal necessary data on-chain, bulk computation & sensitive data handled off-chain. | Enables complex, data-driven logic for 6G optimization while preserving scalability and privacy. | Scalability-privacy trilemma of executing complex logic directly on-chain. | [172] |
| OV (Validity-based Optimistic Smart Contracts) | Supports optimistic execution where results are assumed correct; only disputed executions are verified on-chain. | Drastically reduces overhead for smart contract execution, suitable for concurrent processing. | Overhead of redundant on-chain execution by all network nodes. | [173] |
| Smart Contract Vulnerability Detection & Repair | Uses formal verification, symbolic execution, fuzzing, deep learning for detection; automated tools for repair. | Ensuring security and correctness of contracts managing critical 6G infrastructure. | Immutability of deployed contracts and catastrophic risks from vulnerabilities. | [176], [177], [175] |
| Formal Secure Design Models | Building executable secure design models for smart contracts using formal methods (e.g., TLA+). | Essential for designing secure contracts for critical 6G infrastructure from the outset. | Design flaws leading to vulnerabilities like reentrancy, unpredictable state. | [178] |
| Agatha (AI-enabled Smart Contracts) | Enables verifiable off-chain execution of complex DNN computations; integrity of AI output proven on-chain. | Allows integration of AI/ML models (e.g., for RAN slicing) into smart contracts in a trustless manner. | Verifiable execution of complex, data-driven AI logic on-chain with high trust guarantees. | [179] |
| Explanation-Guided Deep RL (XRL) | Combines eXplainable AI (XAI) with DRL to generate auditable justifications for AI decisions recorded on-chain. | Enhances transparency and trust in AI-driven smart contracts for critical 6G services (e.g., RAN slicing). | Opaqueness of black-box AI decision-making in critical, automated network management. | [180] |


### 2.4 Foundational AI Paradigms for Network Intelligence

The realization of intelligent, self-optimizing 6G networks is fundamentally predicated on the effective deployment of advanced artificial intelligence and machine learning (AI/ML) paradigms. These paradigms provide the cognitive engine for the network, enabling it to learn from vast amounts of data, adapt to dynamic conditions, and make autonomous decisions. Among the plethora of ML techniques, three foundational paradigms stand out as particularly critical for 6G: Deep Learning (DL) for complex pattern recognition and prediction, Reinforcement Learning (RL) for sequential decision-making in uncertain environments, and Federated Learning (FL) as a privacy-preserving framework for distributed intelligence. These paradigms are not merely academic concepts but are being actively integrated into the core fabric of next-generation wireless system design, addressing challenges from the physical layer to network orchestration.

Deep Learning, characterized by multi-layered artificial neural networks, has revolutionized the ability to model and infer from high-dimensional, non-linear data. In the context of 6G, DL serves as a powerful tool for tasks that require sophisticated pattern recognition and predictive analytics. A primary application is in radio resource management (RRM), where DL models can learn complex mappings between network states (e.g., channel conditions, traffic load, user distribution) and optimal resource allocation strategies. For instance, supervised DL models can be trained on datasets generated by traditional optimization algorithms or simulations to predict optimal sub-band and power allocation in multi-cell networks, achieving high accuracy and significantly reducing online computational overhead [181]. Beyond resource allocation, DL is instrumental in traffic forecasting, which is essential for proactive network scaling and load balancing. Models can analyze historical base station data to predict future traffic patterns, enabling intelligent infrastructure planning [182]. Furthermore, DL is pivotal for physical layer enhancements, such as implicit channel learning, where models are trained directly on channel-corrupted datasets to perform tasks like modulation classification or beam prediction without explicit channel estimation, thereby improving robustness and reducing signaling overhead [183]. The advent of specialized architectures like Transformers, with their self-attention mechanisms, is also pushing the boundaries in areas like massive MIMO processing and semantic communication, offering superior representation capabilities for complex wireless signals [184].

While DL excels at perception and prediction, Reinforcement Learning provides the framework for action and control. RL agents learn optimal policies by interacting with their environment, receiving rewards or penalties for their actions, making it ideally suited for sequential decision-making problems in highly dynamic and stochastic wireless networks. Single-agent Deep RL (DRL) has been successfully applied to problems like dynamic spectrum access, power control, and user association, where an agent learns to maximize a long-term reward, such as network throughput or energy efficiency [35]. However, the distributed and heterogeneous nature of 6G networks—comprising numerous base stations, edge servers, and user equipment—often necessitates a multi-agent perspective. Multi-Agent Reinforcement Learning (MARL) enables multiple distributed entities to learn collaborative or competitive policies. This is particularly valuable in Open RAN (O-RAN) architectures and for managing resources in dense, interference-limited scenarios like in-X subnetworks. MARL frameworks allow distributed agents (e.g., gNodeBs) to make localized decisions based on partial observations while coordinating implicitly or explicitly to optimize a global network objective, such as fair resource utilization or minimizing inter-subnetwork interference [96], [185]. The tutorial by [186] further elaborates on the mathematical frameworks and potential applications of MARL in 6G domains like mobile edge computing and UAV networks.

A paramount concern in distributing intelligence across 6G's edge is data privacy and the communication overhead associated with centralized data aggregation. Federated Learning directly addresses this by enabling collaborative model training across a massive number of distributed devices without exchanging raw data. In a typical FL framework, a central server coordinates the process by distributing a global model to edge devices (clients). Each client trains the model locally on its private dataset and sends only the model updates (e.g., gradients or weights) back to the server, which then aggregates them to improve the global model. This paradigm is foundational for privacy-preserving network intelligence. Its applications in 6G are vast, ranging from collaborative traffic prediction across multiple base stations [187] and RF fingerprinting for localization [188] to distributed intrusion detection [189]. FL is considered a key enabler for "ubiquitous AI" in 6G, allowing data-driven solutions to scale across heterogeneous devices while adhering to stringent data sovereignty regulations [190]. However, vanilla FL faces challenges in wireless environments, including statistical heterogeneity (non-IID data), communication efficiency, and security against malicious clients. This has spurred advanced variants like Hierarchical FL (HFL) to reduce node failures [97], Split Federated Learning (SFL) to accommodate resource-constrained devices by splitting the model between clients and servers [191], and Federated DRL (F-DRL) to train reinforcement learning policies in a distributed manner [192].

In summary, Deep Learning, Reinforcement Learning (and its multi-agent extension), and Federated Learning constitute the foundational AI triad for 6G network intelligence. DL provides the perceptual and predictive capabilities, RL offers the decision-making engine for adaptive control, and FL furnishes the privacy-preserving, scalable framework for distributed learning. Their initial and ongoing integration is already demonstrating significant potential in revolutionizing classic wireless problems like radio resource management, traffic prediction, and physical layer processing. As 6G research progresses, the convergence and joint optimization of these paradigms—such as using FL to distribute the training of a MARL system for network slicing or employing DL within RL agents for better state representation—will be crucial in building truly autonomous, efficient, and trustworthy wireless ecosystems.

**Table: Comparison of approaches in 2.4 Foundational AI Paradigms for Network Intelligence**

| Paradigm | Key Characteristics | Primary Applications in 6G (as per text) | Key Challenges / Advanced Variants | Reference(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Learning (DL)** | Multi-layered artificial neural networks for complex pattern recognition and predictive analytics from high-dimensional, non-linear data. | Radio Resource Management (RRM), Traffic Forecasting, Physical Layer enhancements (e.g., implicit channel learning, modulation classification, beam prediction). | Specialized architectures like Transformers for massive MIMO and semantic communication. | [181], [182], [183], [184] |
| **Reinforcement Learning (RL) / Deep RL (DRL)** | Framework for sequential decision-making; agents learn optimal policies by interacting with the environment to maximize long-term reward. | Dynamic Spectrum Access, Power Control, User Association, Resource Management in dynamic/stochastic environments. | Single-agent DRL; Multi-Agent RL (MARL) for distributed, collaborative decision-making in O-RAN and dense subnetworks. | [35], [96], [185], [186] |
| **Federated Learning (FL)** | Privacy-preserving, distributed learning framework; collaborative model training across devices without exchanging raw data, only model updates. | Collaborative Traffic Prediction, RF Fingerprinting for Localization, Distributed Intrusion Detection, enabling "ubiquitous AI". | Statistical heterogeneity (non-IID data), communication efficiency, security against malicious clients. Variants: Hierarchical FL (HFL), Split Federated Learning (SFL), Federated DRL (F-DRL). | [187], [188], [189], [190], [97], [191], [192] |


### 2.5 Advanced AI Models: Generative AI and Goal-Oriented Learning

The evolution towards 6G networks is fundamentally intertwined with a paradigm shift from data-centric connectivity to intelligence-native operation. This transition necessitates moving beyond traditional discriminative AI models towards more sophisticated, creative, and purpose-driven AI frameworks. Two pivotal classes of advanced AI models—Generative AI (GenAI) and Goal-Oriented Learning—are poised to be the cornerstone of this transformation, enabling networks that are not only efficient but also context-aware, adaptive, and capable of understanding intent.

Generative AI represents a monumental leap from models that analyze and classify existing data to those that can synthesize novel, high-quality data and content. In the 6G context, GenAI's role is multifaceted. A primary application is in **synthetic data generation** for training robust machine learning models. Real-world network data, especially for rare events like extreme network congestion or novel security threats, is often scarce, costly, or privacy-sensitive. GenAI models, such as Generative Adversarial Networks (GANs) and Diffusion Models, can learn the underlying distribution of real network data (e.g., traffic patterns, channel conditions, user behavior) and generate realistic, annotated synthetic datasets [193]. This capability is crucial for training AI agents in simulation environments like **Digital Twins**, allowing for stress-testing and optimization of network policies without risking live operations [194]. Furthermore, GenAI is instrumental in **optimizing network configurations**. By modeling the complex, high-dimensional relationship between network parameters (e.g., beamforming vectors, resource block allocation, slicing policies) and performance outcomes, generative models can propose novel, high-performing configurations that might not be discovered through conventional optimization or reinforcement learning alone [195]. This leads to more efficient use of spectrum and energy resources, a critical requirement for sustainable 6G.

Perhaps the most transformative application of GenAI in 6G is in enabling **semantic and goal-oriented communications**. Classical communication, governed by Shannon's theorem, focuses on the accurate transmission of bits. In contrast, semantic communication aims to convey the *meaning* or *intent* behind the data [196]. GenAI models are perfectly suited for this task. They can act as powerful semantic encoders and decoders, extracting and reconstructing the semantic essence of information—be it an image, a sensor reading, or a command. For instance, instead of transmitting every pixel of a high-resolution video feed from an autonomous vehicle, a GenAI-powered semantic encoder could extract and transmit only a compact, structured representation of the scene's critical elements (e.g., "pedestrian crossing 50m ahead, red traffic light") [197]. The receiver, equipped with a complementary GenAI model, can then reconstruct a plausible scene or directly feed the semantic information to the vehicle's control system. This approach, known as **deep joint source and channel coding (JSCC)**, dramatically reduces bandwidth requirements and is more robust to channel impairments, as the system prioritizes preserving meaning over bit-level accuracy [197]. The concept extends to the provisioning of **AI-Generated Content (AIGC)** services over wireless links, where generative models at the edge create personalized media, which can then be efficiently transmitted using semantic compression techniques [198].

Closely related to semantic communication is the paradigm of **Goal-Oriented and Task-Oriented Communications**. Here, the AI model's design and the communication process itself are intrinsically tied to the successful accomplishment of a specific downstream task or goal, rather than the faithful reproduction of transmitted data [31]. This represents a shift from "communicating data" to "communicating for action." In a 6G ecosystem supporting massive IoT and autonomous systems, the ultimate goal may be object detection, collaborative decision-making, or completing a federated learning round—not merely exchanging raw sensor readings. Goal-oriented AI frameworks, therefore, involve the **co-design of sensing, communication, computation, and machine learning models** in an integrated loop [199]. For example, in a multi-agent robotic system, the communication protocol between agents can be *emergent* and learned, optimizing the information exchange specifically for the collaborative task at hand, such as swarm formation or area coverage [200]. The AI models governing these agents are trained with a loss function that directly reflects the task's success metric (e.g., minimization of task completion time, maximization of detection accuracy), incentivizing them to learn what information is truly relevant to transmit. This approach is highly efficient, as it inherently filters out irrelevant data, conserving precious wireless resources like energy and bandwidth [201]. Advanced techniques, such as **neuro-symbolic AI**, further enhance this by combining deep learning with symbolic reasoning, allowing the system to learn and communicate based on causal structures and knowledge graphs, leading to more interpretable and robust goal-oriented behaviors [202].

The synergy between Generative AI and Goal-Oriented Learning is particularly powerful. GenAI can model complex environments and user intents, providing the rich, contextual understanding needed for goal formulation. Conversely, goal-oriented frameworks provide the necessary constraints and objectives to guide the generative process, ensuring that the synthesized data or communications are not just realistic but also *effective* for the intended purpose. Together, these advanced AI models are dismantling the traditional silos between communication, computation, and intelligence. They are paving the way for 6G networks that are inherently intelligent—capable of understanding context, generating solutions, and efficiently marshaling all network resources (sensing, communication, computation) towards the achievement of complex, user-defined goals. This intelligence-native vision positions 6G not merely as a faster pipe, but as an active, cognitive fabric that underpins the future of immersive digital experiences, autonomous systems, and a truly connected intelligent world [4].

**Table: Comparison of approaches in 2.5 Advanced AI Models: Generative AI and Goal-Oriented Learning**

| AI Model Category | Key Capabilities & Role in 6G | Primary Applications / Use Cases | Key Enabling Techniques / Frameworks | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Generative AI (GenAI) | Synthesizes novel, high-quality data; acts as semantic encoder/decoder; models complex environments and user intents. | Synthetic data generation for training; Network configuration optimization; Semantic & goal-oriented communications; AI-Generated Content (AIGC) provisioning. | Generative Adversarial Networks (GANs); Diffusion Models; Deep Joint Source and Channel Coding (JSCC); Digital Twins. | [193]; [194]; [195]; [197]; [198] |
| Goal-Oriented / Task-Oriented Learning | Co-designs sensing, communication, computation, and ML; optimizes information exchange for specific downstream tasks; prioritizes task success over data fidelity. | Multi-agent collaborative tasks (e.g., swarm robotics); Federated learning; Edge inference; Intent-based semantic communication. | Integrated Sensing-Communication-Computation (ISCC); Emergent communication protocols; Neuro-symbolic AI; Generative Flow Networks (GFlowNets). | [31]; [199]; [200]; [201]; [202] |
| Semantic Communication | Aims to convey the *meaning* or *intent* behind data; prioritizes preserving semantics over bit-level accuracy. | Efficient image/video transmission; Low-bandwidth command & control; Semantic-aware network resource allocation. | Deep Joint Source and Channel Coding (JSCC); Knowledge Base (KB) integration; Semantic encoders/decoders. | [196]; [197]; [203]; [204] |


### 2.6 Privacy-Preserving and Trustworthy AI Mechanisms

The vision for 6G networks extends far beyond enhanced connectivity, aiming to create an intelligent, autonomous, and ubiquitous fabric that supports critical applications from autonomous systems to personalized healthcare. This hyper-connected reality, however, raises profound concerns regarding data privacy, model security, and the trustworthiness of automated decisions. To address these challenges, the 6G ecosystem must be underpinned by robust **Privacy-Preserving and Trustworthy AI Mechanisms**. These mechanisms are not mere add-ons but foundational requirements to ensure ethical compliance, user adoption, and the reliable operation of network services.

At the forefront of privacy preservation is **Federated Learning (FL)**, a distributed machine learning paradigm that has emerged as a cornerstone for 6G intelligence. FL enables model training across a massive number of heterogeneous devices—such as user equipment, IoT sensors, and edge servers—without requiring raw data to leave their local storage. This fundamental shift from centralized data collection to decentralized model updating directly mitigates privacy risks associated with data transmission and storage. The core privacy promise of FL is that only model updates (e.g., gradients or parameters), not the sensitive training data itself, are shared with a central aggregator or amongst peers. This framework is particularly vital for 6G use cases like smart healthcare, where patient data from IoMT devices must remain confidential [113], and for intelligent vehicular networks where driving patterns are protected [205].

However, basic FL has inherent limitations. The shared model updates can still leak information about the underlying training data through inference attacks. To fortify FL, advanced cryptographic and statistical techniques are integrated. **Secure Aggregation** protocols allow the central server to compute the sum of client updates without being able to inspect any individual update, thereby preventing the server from learning information from a single client. This is often achieved through multi-party computation or homomorphic encryption. **Differential Privacy (DP)**, another pivotal technology, provides a rigorous mathematical guarantee of privacy. By carefully calibrated noise to the local model updates before they are shared, DP ensures that the participation of any single data point in the training set cannot be reliably inferred from the output, thus protecting against membership inference attacks [206]. The integration of **Local Differential Privacy (LDP)** within FL frameworks further empowers clients to sanitize their updates locally before any aggregation, offering a stronger client-side privacy guarantee [205]. Research continues to optimize the trade-off between the privacy budget (epsilon in DP) and model utility, which is crucial for maintaining high performance in 6G applications.

While privacy-preserving techniques shield the data, the opaque nature of complex AI models, especially deep neural networks, creates a "black box" problem that erodes trust. For 6G networks managing mission-critical services—such as zero-touch network slicing, resource allocation for ultra-reliable low-latency communication (URLLC), or collision avoidance in autonomous driving—understanding *why* an AI model made a specific decision is non-negotiable. This is the domain of **Explainable AI (XAI)**. XAI encompasses a suite of methods designed to make the outputs of AI systems understandable to human stakeholders, including network engineers, regulators, and end-users. By providing insights into model behavior, XAI enhances transparency, facilitates debugging, ensures compliance with regulations, and ultimately builds trust in automated systems [46].

XAI techniques can be categorized as *post-hoc* or *ante-hoc*. Post-hoc methods, such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations), analyze a trained model to generate explanations for individual predictions. For instance, in a network intrusion detection system, an XAI method can highlight which features of the network traffic (e.g., packet size, source port) were most influential in flagging an activity as malicious [207]. Ante-hoc, or intrinsically interpretable, models are designed to be transparent from the start, such as decision trees or linear models with constraints. In the 6G context, explanation-guided learning frameworks are being developed where the XAI process is embedded directly into the training loop. For example, an **Explanation-Guided Federated Learning (EGFL)** scheme uses explanations to ensure model predictions are fair and aligned with network policies, quantitatively validating faithfulness via metrics like comprehensiveness score [131]. Similarly, **Turbo Explainable Federated Learning (TEFL)** employs an iterative closed-loop between a resource allocator and an explainer to achieve transparent and SLA-aware service management [208].

The confluence of privacy preservation and explainability is essential for **Trustworthy AI**. Trustworthiness encompasses fairness (mitigating bias), robustness (resilience against adversarial attacks), accountability, and transparency. XAI plays a critical role in auditing AI models for bias and ensuring their decisions are justifiable, which is a core pillar of responsible AI deployment [209]. For instance, in a federated learning scenario for RAN slicing, XAI can help identify if the global model is unfairly allocating resources against slices from specific geographic areas or device types, enabling corrective measures [106]. Furthermore, understanding model behavior is the first step in defending it; XAI can help uncover model vulnerabilities and spurious correlations that adversaries might exploit [210].

Nevertheless, achieving both strong privacy and high-fidelity explainability presents a nuanced trade-off. Privacy mechanisms like differential privacy inherently obscure the precise relationship between inputs and outputs, which can dampen or distort the explanations generated by XAI methods [206]. Conversely, certain XAI outputs could inadvertently leak information about the model or training data, creating a new attack surface for model extraction or inference attacks [211]. Therefore, a balanced, integrated design is paramount. Future research directions include developing privacy-aware XAI techniques that provide meaningful explanations while respecting privacy guarantees, and creating formal frameworks to quantify and manage the privacy-explainability-utility trilemma. As 6G evolves towards a native AI platform, these privacy-preserving and trustworthy AI mechanisms will be indispensable in building a secure, ethical, and human-centric network that is not only intelligent but also reliable and accountable.

**Table: Comparison of approaches in 2.6 Privacy-Preserving and Trustworthy AI Mechanisms**

| Method/Model | Core Objective | Key Techniques/Mechanisms | Primary Application/Use-Case in 6G | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Federated Learning (FL) | Enable distributed model training without sharing raw data to preserve privacy. | Decentralized model updates (gradients/parameters), local training on heterogeneous devices (UE, IoT sensors, edge servers). | Smart healthcare (IoMT data confidentiality), intelligent vehicular networks (protecting driving patterns). | [113], [205] |
| Secure Aggregation (within FL) | Prevent the central server from inspecting individual client updates to enhance privacy. | Multi-party computation, homomorphic encryption. | Fortifying FL frameworks against inference attacks on shared model updates. | [212], [48] |
| Differential Privacy (DP) / Local Differential Privacy (LDP) | Provide a rigorous mathematical guarantee that the participation of any single data point cannot be inferred. | Adding carefully calibrated noise to model updates (DP) or sanitizing updates locally before sharing (LDP). | Protecting against membership inference attacks in FL; strengthening client-side privacy in vehicular networks and other edge intelligence scenarios. | [206], [205] |
| Explainable AI (XAI) - Post-hoc (e.g., SHAP, LIME) | Make the outputs of complex AI models understandable to human stakeholders to build trust and transparency. | Analyzing a trained model to generate explanations for individual predictions (e.g., feature importance). | Network intrusion detection (highlighting influential traffic features), auditing AI models for bias and compliance. | [207], [46] |
| Explanation-Guided Federated Learning (EGFL) | Integrate XAI directly into the FL training loop to ensure model predictions are fair, transparent, and policy-aligned. | Using explanations (e.g., via Jensen-Shannon divergence) as a constraint or guide during federated training. | Transparent and fair resource allocation for 6G RAN slicing, quantitatively validating explanation faithfulness. | [131] |
| Turbo Explainable Federated Learning (TEFL) | Achieve transparent and SLA-aware service management through an iterative closed-loop between a resource allocator and an explainer. | Exchanging soft feature attributions and predictions in a closed loop; using attribution-based confidence metrics as constraints. | Trustworthy zero-touch network slicing management at the RAN-Edge under non-IID data. | [208] |


## 3 AI for Optimizing 6G Network Intelligence and Performance

This section surveys the application of AI as a standalone enabler for enhancing 6G network operations. Topics include AI-driven radio resource management, dynamic network slicing, intelligent beamforming and massive MIMO optimization, predictive traffic management, and the optimization of emerging paradigms like semantic/goal-oriented communications and Integrated Sensing and Communication (ISAC). The role of AI in Open RAN (O-RAN) and network automation is also discussed.

### 3.1 AI-Driven Radio Resource Management and Network Slicing

The realization of 6G's vision for ultra-reliable, low-latency, and massive-scale connectivity hinges on the ability to dynamically and intelligently manage the radio access network (RAN) and its resources. The inherent complexity, high-dimensional state spaces, and stringent, diverse service requirements render traditional optimization models and rule-based controllers inadequate. Consequently, Artificial Intelligence (AI), and particularly Deep Reinforcement Learning (DRL), has emerged as the cornerstone for enabling zero-touch, autonomous, and continuous radio resource management (RRM) and network slicing. DRL agents learn optimal control policies through continuous interaction with the network environment, making them exceptionally suited for the stochastic and non-stationary nature of wireless systems. This paradigm is fundamental to creating self-organizing networks that can meet the exacting demands of enhanced Mobile Broadband (eMBB), Ultra-Reliable Low Latency Communications (URLLC), and massive Machine-Type Communications (mMTC) slices in 6G.

A primary application of DRL is in dynamic RAN slicing, which involves partitioning physical radio resources into logically isolated virtual networks. Research demonstrates the efficacy of DRL in optimizing slice performance across multiple time scales and architectural paradigms. For instance, within the Open RAN (O-RAN) framework, solutions employ DRL-based xApps in the near-real-time RAN Intelligent Controller (RIC) to perform fine-grained resource allocation. Studies like [213] and [214] showcase hierarchical DRL agents managing inter-slice and intra-slice resources, dynamically borrowing unused bandwidth from underutilized slices to boost the throughput of others, thereby improving peak data rates for eMBB and reducing transmission times for URLLC traffic. The O-RAN architecture's programmability is explicitly leveraged to support such AI-driven, multi-time scale management [213]. Furthermore, the integration of Mobile Edge Computing (MEC) with network slicing for applications like the Internet of Vehicles (IoV) is effectively managed by DRL agents that jointly handle channel/power allocation, slice selection, and user grouping, demonstrating robustness under varying network conditions [215].

To address the scalability challenges of centralized controllers in large-scale networks with numerous slices, federated and multi-agent DRL (MARL) architectures are proposed. These distribute the intelligence across the network. [216] introduces a federated DRL approach with traffic-aware local decision agents placed in the RAN, forming specialized clusters that reduce communication overhead and react swiftly to user mobility. Similarly, MARL frameworks are designed for inter-cell coordination, where each base station acts as an agent. To enhance cooperation among these agents, advanced neural architectures like Graph Attention Networks (GAT) are integrated with DRL, allowing agents to better understand spatial-temporal dependencies and inter-cell interference, leading to more efficient inter-slice resource management [217]. The challenge of poor transferability of DRL models across different network environments is addressed by transfer learning (TL). As explored in [218], a TL-aided DIRP algorithm first trains a centralized "generalist" model, which is then transferred and fine-tuned by distributed agents, significantly improving sample efficiency, convergence rate, and model reproducibility compared to training from scratch.

The ultimate goal of these AI-driven mechanisms is the realization of zero-touch network and service management (ZSM), where the network self-configures, self-optimizes, and self-heals with minimal human intervention. This requires continuous, farsighted control that optimizes long-term performance metrics. Actor-Critic-based DRL methods, which combine value-based and policy-based learning, are particularly effective for this continuous control. Novel frameworks like the collaborative statistical Actor-Critic (CS-AC) are proposed for scalable slice performance management under statistical Service Level Agreements (SLAs), optimizing for metrics like latency percentiles [219]. Other works, such as [220] and [221], propose advanced Actor-Critic variants (e.g., TDSAC, D-TD3) to minimize a multi-objective cost function encompassing energy consumption, virtual network function (VNF) instantiation costs, and latency, enabling the central unit to autonomously reconfigure computing resources.

Beyond algorithm design, significant research focuses on the practical challenges of deploying DRL in real networks. Slow convergence and performance instability upon deployment are major hurdles. Techniques to accelerate and safe-guard learning are critical. [222] proposes a hybrid TL approach combining policy reuse and distillation to provide safe and accelerated convergence for DRL-based O-RAN slicing controllers. Similarly, leveraging forecasting of traffic demands can significantly enhance DRL agent convergence, as shown in [223], where a forecasting-aided DRL approach improves initial reward and convergence rates. For even greater practicality, offline RL is introduced as a paradigm where agents learn near-optimal policies from pre-collected, potentially sub-optimal datasets, eliminating the need for risky and lengthy online interactions during deployment [224]. Furthermore, the push towards edge intelligence is demonstrated by frameworks like [225], which enables the training and deployment of DRL power control agents directly on GPU-embedded software-defined radios, proving the feasibility of on-device AI for distributed RRM.

Finally, the management of resources extends beyond the radio spectrum to a holistic, end-to-end scope encompassing transport and computational resources at the edge. DRL frameworks are designed for this integrated challenge. [226] proposes a decentralized DRL method for orchestrating end-to-end resources (radio, transport, computing) to meet slice SLAs dynamically. In computation offloading scenarios for MEC, DRL optimizes joint resource allocation and task scheduling to minimize system energy consumption [227]. The problem of efficiently embedding the chain of VNFs that constitute a network slice onto a physical substrate is also tackled using DRL, where an agent learns to maximize the number of accommodated slices by observing network states and requested slice graphs [228]. In summary, AI-driven RRM and network slicing represent a transformative shift towards autonomous, efficient, and adaptive 6G networks. Through advanced DRL, MARL, and complementary AI techniques, these systems can dynamically orchestrate multi-dimensional resources across the RAN, edge, and core to instantiate and maintain performance-isolated slices, paving the way for true zero-touch operation and the support of tomorrow's most demanding digital services.

**Table: Comparison of approaches in 3.1 AI-Driven Radio Resource Management and Network Slicing**

| Method/Model Category | Key Idea/Approach | Application Context | Reference |
| :--- | :--- | :--- | :--- |
| Hierarchical DRL in O-RAN | Employs DRL-based xApps in near-RT RIC for fine-grained resource allocation; hierarchical agents manage inter-slice and intra-slice resources, dynamically borrowing unused bandwidth. | Dynamic RAN slicing in O-RAN framework for eMBB, URLLC, mMTC slices. | [213] |
| DRL for Midhaul Resource Allocation | Applies RL to dynamically allocate unused bandwidth from underutilized slices to improve throughput for eMBB and reduce transmission time for URLLC. | Network slicing resource allocation in O-RAN midhaul. | [214] |
| Federated DRL (FDRL) with Traffic-Aware Agents | Proposes a federated DRL approach with traffic-aware local decision agents placed in the RAN, forming specialized clusters to reduce overhead and react to mobility. | Scalable and distributed 6G RAN slicing orchestration. | [216] |
| MARL with Graph Attention Networks (GAT) | Integrates GAT with DRL in a multi-agent framework to help agents understand spatial-temporal dependencies and inter-cell interference for inter-slice resource management. | Slicing resource management in dense cellular networks. | [217] |
| Transfer Learning-aided Multi-Agent DRL (TL-DIRP) | Uses TL to first train a centralized "generalist" model, then transfers and fine-tunes it for distributed agents to improve sample efficiency and convergence. | Inter-cell network slicing optimization. | [218] |
| DRL for MEC-enabled IoV Slicing | Uses a model-free DRL approach (DQL) to jointly solve channel/power allocation, slice selection, and user grouping in MEC-enabled IoV networks. | Network slicing with MEC for the Internet of Vehicles (IoV). | [215] |
| Collaborative Statistical Actor-Critic (CS-AC) | A model-free DRL framework for scalable, farsighted slice performance management under statistical SLAs, optimizing for metrics like latency percentiles. | 6G network slicing control with MEC and mMIMO. | [219] |
| Advanced Actor-Critic (TDSAC, D-TD3) | Employs advanced Actor-Critic variants (e.g., TDSAC, D-TD3) to minimize a multi-objective cost function (energy, VNF cost, latency) for autonomous resource reconfiguration. | Zero-touch joint resource and energy control in network slicing. | [220], [221] |
| Hybrid Transfer Learning for Safe DRL | Proposes a hybrid TL approach combining policy reuse and distillation to provide safe and accelerated convergence for DRL-based O-RAN slicing controllers. | Safe and accelerated DRL for O-RAN slicing. | [222] |
| Forecasting-aided DRL | Leverages forecasting of traffic demands to enhance DRL agent convergence, improving initial reward and convergence rates. | Improving DRL convergence in O-RAN slicing. | [223] |
| Offline Reinforcement Learning | Introduces offline RL to learn near-optimal policies from pre-collected datasets, eliminating the need for risky online interactions during deployment. | Advancing RAN slicing with offline learning from datasets. | [224] |
| Edge Deployment of DRL (MR-iNet Gym) | Enables training and deployment of DRL power control agents directly on GPU-embedded software-defined radios, proving on-device AI feasibility. | Edge deployment of DRL for distributed RRM on SDRs. | [225] |
| Decentralized DRL for End-to-End Slicing (EdgeSlice) | Proposes a decentralized DRL method to orchestrate end-to-end resources (radio, transport, computing) to meet slice SLAs dynamically. | Slicing wireless edge computing networks. | [226] |
| DRL for Computation Offloading & Resource Allocation | Utilizes DRL to design an optimal computation offloading and resource allocation strategy for minimizing system energy consumption in MEC. | Energy-efficient computation offloading and resource allocation in 5G Beyond. | [227] |
| DRL for VNF Embedding (Deep Allocation Agent) | Uses a DRL agent (Deep Allocation Agent) to learn to maximize the number of accommodated slices by observing network states and requested slice graphs for VNF embedding. | Efficient embedding of VNFs in 5G network slicing. | [228] |


### 3.2 AI for Physical Layer and RAN Optimization: Beamforming, MIMO, and O-RAN

The optimization of the physical layer and the Radio Access Network (RAN) represents one of the most impactful applications of artificial intelligence (AI) in 6G systems. The inherent complexity of massive MIMO, millimeter-wave (mmWave), and Terahertz (THz) communications, characterized by high-dimensional channel matrices, dynamic blockage, and stringent latency requirements, makes traditional optimization methods inadequate. AI, particularly deep learning (DL) and reinforcement learning (RL), offers a paradigm shift by learning optimal control policies directly from data, enabling real-time adaptation to the rapidly changing wireless environment. For instance, AI is pivotal for intelligent beamforming, where algorithms must rapidly compute optimal precoding vectors for dozens to hundreds of antenna elements. Deep neural networks can learn to map partial or outdated channel state information (CSI) to near-optimal beamforming vectors, drastically reducing computational latency compared to iterative convex optimization solvers [229]. This is especially critical for mmWave/THz systems where beam alignment must be maintained despite user mobility and blockages. Furthermore, AI models are being developed for channel prediction, modulation and coding scheme (MCS) adaptation, and signal detection, moving beyond model-based assumptions to data-driven solutions that can handle real-world hardware impairments and non-linearities [230] [231].

The architectural embodiment of this AI-driven control is the Open RAN (O-RAN) framework, which institutionalizes intelligence through programmable, data-driven closed loops. O-RAN's disaggregated architecture, with its open interfaces, allows AI/ML models to be hosted as applications (xApps and rApps) on RAN Intelligent Controllers (RICs). The near-real-time RIC (Near-RT RIC), operating with control loops between 10ms and 1s, is the primary platform for xApps that perform fine-grained RAN optimization. These xApps consume a rich stream of Key Performance Measurements (KPMs) via the E2 interface and exert control by configuring RAN parameters. Use cases are diverse and impactful: **Traffic Steering (TS) xApps** use RL to dynamically manage handovers and cell associations, optimizing for throughput, load balancing, or energy efficiency. Studies show RL-based TS xApps can improve cluster-aggregated throughput by 18-24% over traditional heuristic policies [232] [233]. **Resource Allocation xApps** leverage multi-agent RL to manage scheduling, interference coordination, and slice resource partitioning in real-time, adapting to heterogeneous traffic demands [234] [235]. **Spectrum Sharing xApps**, like ChARM, employ neural networks to analyze raw I/Q samples and infer spectrum context (e.g., detecting Wi-Fi interference), enabling reactive frequency switching to adhere to dynamic spectrum access policies [236].

However, integrating AI into the RAN's critical path introduces significant new challenges that must be addressed for reliable deployment. A primary concern is the **testing and validation** of AI models. The performance of an xApp trained in a simulated environment may degrade severely in the real world due to the "sim2real" gap—discrepancies in channel models, traffic patterns, and hardware behavior [237]. This necessitates robust AI testing frameworks that can automatically and intelligently explore an AI model's decision space under realistic, varied conditions, assessing not only performance but also vulnerability to adversarial inputs [238]. Platforms like Colosseum, which functions as a large-scale **Open RAN Digital Twin**, are essential for this purpose, providing a high-fidelity, hardware-in-the-loop environment for training, testing, and validating xApps at scale before live deployment [239] [240].

Another critical challenge is **AI misconfiguration and conflict management**. In a multi-vendor O-RAN ecosystem, multiple independent xApps may simultaneously attempt to control overlapping RAN parameters (e.g., transmit power, handover thresholds), leading to conflicts that degrade overall network performance [241] [242]. For example, a throughput-maximizing xApp might conflict with an energy-saving xApp. Standardized Conflict Management Systems (CMS) are therefore required. Proposed solutions employ game-theoretic frameworks or hierarchical RL to orchestrate xApps, ensuring their collective actions align with higher-level operator intents (e.g., maximizing a weighted combination of throughput and energy efficiency) without destructive interference [243]. Furthermore, the **security of AI components** themselves is paramount. xApps are vulnerable to adversarial machine learning attacks, where subtly perturbed input data (KPMs or spectrograms) can cause misclassification and erroneous control decisions, potentially crashing network performance [244] [245]. Defensive techniques like adversarial training and model distillation are being explored to harden xApps.

Finally, the pursuit of extreme latency and efficiency is pushing intelligence deeper into the RAN. The concept of **distributed applications (dApps)** extends the O-RAN control plane by embedding lightweight AI inference engines directly within Distributed Units (DUs) or even Radio Units (RUs). This enables ultra-fast control loops (sub-millisecond) for PHY-layer functions like link adaptation and beam selection, which are beyond the reach of the Near-RT RIC [246] [247]. Similarly, neuromorphic processing for RIS control, as seen in NeuroRIS, promises nanosecond-order reconfiguration by leveraging event-driven spiking neural networks, showcasing the fusion of novel AI hardware with wireless infrastructure [248]. In summary, AI is fundamentally transforming physical layer and RAN optimization from a static, model-based exercise into a dynamic, data-driven, and adaptive process. The O-RAN architecture provides the essential framework for this integration, but realizing its full potential requires concerted research into robust AI testing, secure and conflict-free operation, and the co-design of AI algorithms with network infrastructure to meet 6G's extreme performance targets.

**Table: Comparison of approaches in 3.2 AI for Physical Layer and RAN Optimization: Beamforming, MIMO, and O-RAN**

| Method/Model | Application Area | Key Idea/Approach | Reference |
| :--- | :--- | :--- | :--- |
| Deep Neural Networks for Beamforming | Physical Layer (Beamforming) | Maps partial/outdated CSI to near-optimal beamforming vectors, reducing computational latency vs. iterative solvers. | [229] |
| RL-based Traffic Steering (TS) xApps | O-RAN (Traffic Steering) | Uses RL to dynamically manage handovers and cell associations to optimize throughput, load balancing, or energy efficiency. | [232], [233] |
| Multi-agent RL for Resource Allocation xApps | O-RAN (Resource Allocation) | Leverages multi-agent RL to manage scheduling, interference coordination, and slice resource partitioning in real-time. | [234], [235] |
| ChARM (Spectrum Sharing xApp) | O-RAN (Spectrum Sharing) | Employs neural networks to analyze raw I/Q samples and infer spectrum context (e.g., Wi-Fi interference) for reactive frequency switching. | [236] |
| Game-Theoretic Conflict Management | O-RAN (Conflict Management) | Proposes a Conflict Management System (CMS) using cooperative bargain game theory (e.g., Nash Social Welfare) to find optimal configurations for conflicting xApp parameters. | [241] |
| Hierarchical RL for Intent-driven Orchestration | O-RAN (Orchestration) | Uses hierarchical RL to orchestrate multiple xApps/rApps according to high-level operator intents (e.g., weighted KPI optimization). | [243] |
| Adversarial Training & Model Distillation | O-RAN (AI Security) | Explores defensive techniques like adversarial training and model distillation to harden xApps against adversarial ML attacks. | [245] |
| Distributed Applications (dApps) | O-RAN (Real-time Control) | Embeds lightweight AI inference engines directly within DUs/RUs for ultra-fast control loops (sub-millisecond) for PHY-layer functions. | [246] |
| Neuromorphic Processing (NeuroRIS) | RIS Control | Uses event-driven spiking neural networks on neuromorphic processors for nanosecond-order RIS reconfiguration, enabling real-time adaptation. | [248] |


### 3.3 AI for Emerging Communication Paradigms: Semantic, Goal-Oriented, and Integrated Sensing & Communication (ISAC)

The evolution towards 6G necessitates a fundamental rethinking of communication paradigms, moving beyond the traditional Shannon-centric focus on reliable bit transmission towards systems that understand intent, context, and goals. Artificial Intelligence serves as the indispensable core enabler for these emerging paradigms, including semantic and goal-oriented communications, AI-generated content, and Integrated Sensing and Communication (ISAC). By embedding intelligence across the network stack, AI transforms communication from a mere data pipe into a dynamic, context-aware, and purpose-driven fabric for intelligent applications.

Semantic communication represents a paradigm shift where the meaning or semantics of information, rather than its precise bit-level representation, becomes the primary unit of exchange. AI, particularly deep learning models, is pivotal in realizing this vision. Deep neural networks, such as autoencoders, are trained to extract and compress semantic features from source data (e.g., images, text) at the transmitter and reconstruct semantically consistent content at the receiver [249]. This approach can drastically reduce bandwidth requirements while preserving the information necessary for the downstream task, as demonstrated in applications like image classification where semantic communication can achieve significant accuracy gains over traditional methods [250]. The challenge lies in developing robust models that can extract invariant semantic representations resilient to channel corruptions and domain shifts. Furthermore, the concept of a "semantic language" and knowledge-driven networks is emerging, where AI facilitates reasoning over transmitted semantics, moving networks from data-driven to knowledge-driven operation [251].

Closely related is the paradigm of goal-oriented or task-oriented communication, which optimizes the entire transmission process for the successful execution of a specific task at the receiver, such as accurate inference, control, or collaboration. Here, AI is used to design communication strategies that minimize the use of resources (bandwidth, energy, latency) while maximizing task performance. This often involves end-to-end joint optimization of sensing, compression, transmission, and inference using techniques like deep reinforcement learning (DRL). For instance, in multi-agent systems for autonomous collaboration, AI can learn emergent communication protocols that are more efficient than hard-coded schemes for task execution [200]. Frameworks for task-oriented integrated sensing, computation, and communication (ISCC) leverage AI to co-design these three coupled processes, ensuring that the transmitted information is precisely what is needed for the edge AI task at hand, be it federated learning or real-time inference [104].

Generative AI (GAI) is revolutionizing content creation and delivery, giving rise to the concept of AI-Generated Everything (AIGX). In wireless networks, GAI models like Generative Adversarial Networks (GANs), diffusion models, and large language models (LLMs) can be deployed at the edge to create, adapt, and personalize immersive content (e.g., for extended reality, metaverse, or digital twins) on demand [101]. This integration significantly alleviates bandwidth pressure, as only concise semantic prompts or latent vectors need to be transmitted instead of raw high-fidelity media streams. Semantic communication frameworks empowered by generative AI (GAI-SCN) are proposed to synergistically combine efficient semantic extraction with high-quality content generation [252]. For example, a unified framework integrating semantic communication and AI-generated content has been proposed for the Metaverse, optimizing resource allocation for semantic extraction, content generation, and graphic rendering to enhance user immersion [115].

Integrated Sensing and Communication (ISAC) is a cornerstone 6G technology that unifies sensing (e.g., radar, localization) and communication functionalities using shared hardware, spectrum, and signal processing. AI is critical for managing the inherent trade-offs and achieving joint optimization in ISAC systems. The dynamic and uncertain radio environment, especially in high-mobility scenarios like autonomous vehicles, makes classical optimization intractable. Machine learning, particularly DRL, enables ISAC systems to adaptively configure waveform parameters, beamforming, and resource allocation to balance sensing accuracy (e.g., target detection resolution) and communication performance (e.g., data rate) in real-time [253]. Furthermore, AI facilitates the fusion and interpretation of massive sensing data. For instance, ISAC-driven digital twins for intelligent machine networks use AI to structurally store sensing information and optimize communication, networking, and control schemes [254]. The interplay between ISAC and other AI-empowered technologies like Reconfigurable Intelligent Surfaces (RIS) is also being explored, where AI orchestrates the smart propagation environment to enhance both sensing and communication performance simultaneously [255].

The applications of these AI-driven paradigms are vast and transformative. In the Internet of Things (IoT) and autonomous systems, semantic and goal-oriented communications enable efficient collaboration among swarms of drones or autonomous vehicles, where only critical state and intent information is exchanged [256]. ISAC provides autonomous vehicles with simultaneous high-resolution environmental mapping and ultra-reliable vehicle-to-everything (V2X) links, a capability fundamental to safe navigation. For immersive experiences and the Internet of Senses (IoS), generative semantic communications can deliver personalized, multi-sensory content with minimal latency and bandwidth, enabling flawless telepresence [257]. Ultimately, the convergence of these AI-powered paradigms—semantic understanding, goal-driven efficiency, generative content, and integrated sensing—is paving the way for a truly intelligent, context-aware, and resource-optimal 6G ecosystem that seamlessly supports the future of connected intelligence.

**Table: Comparison of approaches in 3.3 AI for Emerging Communication Paradigms: Semantic, Goal-Oriented, and Integrated Sensing & Communication (ISAC)**

| Paradigm / Technology | Core AI Enabler(s) | Key Concept / Objective | Primary Applications / Use Cases | Reference(s) |
| :--- | :--- | :--- | :--- | :--- |
| Semantic Communication | Deep Learning (e.g., Autoencoders, Deep Generative Models) | Focuses on transmitting the meaning (semantics) of information rather than exact bits, aiming for bandwidth reduction and task-specific information preservation. | Image classification, surface defect detection, immersive media, Metaverse content delivery. | [249], [250], [251] |
| Goal/Task-Oriented Communication | Deep Reinforcement Learning (DRL), End-to-end joint optimization | Optimizes the entire transmission process (sensing, compression, transmission, inference) for the successful execution of a specific downstream task, minimizing resource use. | Multi-agent autonomous collaboration (e.g., drones, vehicles), federated learning, real-time edge AI inference. | [200], [104] |
| Generative AI (GAI) / AI-Generated Everything (AIGX) | Generative Adversarial Networks (GANs), Diffusion Models, Large Language Models (LLMs) | Creates, adapts, and personalizes immersive content on-demand at the network edge, reducing bandwidth by transmitting prompts/latent vectors instead of raw media. | Extended Reality (XR), Metaverse, digital twins, personalized immersive experiences for the Internet of Senses (IoS). | [101], [252], [115] |
| Integrated Sensing and Communication (ISAC) | Machine Learning, Deep Reinforcement Learning (DRL) | Unifies sensing (e.g., radar, localization) and communication using shared hardware/spectrum; AI manages trade-offs and enables joint, adaptive optimization. | Autonomous vehicles (simultaneous mapping and V2X), intelligent machine networks, digital twins, smart propagation environments with RIS. | [253], [254], [255] |


### 3.4 AI-Powered Network Automation, Digital Twins, and Edge Intelligence

The realization of fully autonomous, self-optimizing 6G networks hinges on advanced AI frameworks that manage the entire network lifecycle, from planning and deployment to operation and optimization. This vision of AI-native networks embeds intelligence as a fundamental, pervasive layer, moving beyond reactive automation to proactive and predictive management. A cornerstone of this approach is the application of Machine Learning Operations (MLOps) principles to network functions, ensuring the continuous integration, deployment, monitoring, and retraining of AI models that govern network behavior. Exemplifying this, the concept of **SliceOps** is proposed as a systematic, standalone slice natively embedded within the 6G architecture [19]. SliceOps is tasked with gathering and managing the complete AI lifecycle, providing AI-as-a-Service to other network slices. By integrating eXplainable AI (XAI) with MLOps, it employs explanation-guided reinforcement learning (XRL) to ensure the transparency, trustworthiness, and interpretability of AI-driven decisions, such as latency-aware radio resource allocation, thereby addressing the critical "black-box" problem in autonomous network slicing ecosystems.

Complementing AI-native operations, **Digital Twins (DTs)** emerge as a transformative paradigm for network modeling, simulation, and experience-driven management. A DT creates a high-fidelity, synchronized virtual representation of physical network entities, dynamics, and services. This virtual replica serves as a safe, on-demand sandbox for data generation, AI model training, policy testing, and "what-if" analysis without risking the live network. The interplay between AI and DT is symbiotic: AI algorithms, particularly Deep Reinforcement Learning (DRL), are essential for building accurate, adaptive twin models and for optimizing decisions within them, while the DT provides the rich, synthetic data and simulation environment necessary for efficient and scalable AI training [258]. For instance, DTs can simulate the complex state variation of network slicing environments, allowing DRL agents to pre-verify and optimize slice optimization strategies extensively before deployment, significantly improving final performance and scalability [259]. In vehicular networks, two-tier digital twins capture networking features of vehicles and edge servers to drive a scalable, two-stage computing resource allocation scheme that dynamically adapts to service demands and mobility [260]. Furthermore, DTs enable meta-learning frameworks for intelligent network management functions, where a high-tier meta-learner captures general features from the DT, and low-tier models are quickly customized for local networks, facilitating rapid adaptation to non-stationary conditions [261].

The efficient execution of these AI-driven automation and twin models demands a fundamental shift in computational architecture from centralized clouds to the network periphery, giving rise to **Edge Intelligence (Edge AI)**. Edge AI distributes intelligence by deploying model inference and training capabilities closer to data sources and end-users, which is critical for meeting the ultra-low latency, high bandwidth efficiency, and privacy preservation requirements of 6G applications [42]. Architectures for edge AI focus on efficient AI service provisioning, which involves novel resource pooling methods to jointly manage service data and network resources for AI workloads [262]. A key challenge is supporting **multi-tenancy**—concurrent execution of multiple latency-sensitive Deep Learning applications on resource-constrained edge servers. Frameworks like **Edge-MultiAI** address memory contention by leveraging model compression (e.g., quantization) and intelligent, predictive model swapping heuristics to maximize the number of warm-start inferences and the degree of multi-tenancy without compromising accuracy [263]. Similarly, investigations into concurrent model executions and dynamic model placements on edge AI accelerators show throughput improvements of up to 3.8x, highlighting the potential for flexible multi-service deployment [264].

For model training at the edge, **Federated Edge Learning (FEEL)** has become the predominant privacy-preserving distributed learning paradigm. FEEL coordinates global model training across numerous edge devices without centralizing raw data. Optimizing FEEL requires joint communication and computation resource management (C²RM), especially in heterogeneous environments with devices employing CPU-GPU heterogeneous computing. Efficient C²RM frameworks manage bandwidth allocation, workload partitioning between CPU/GPU, speed scaling, and time division to minimize overall energy consumption while maintaining learning efficiency [265]. Furthermore, continuous learning and model updates at the edge are essential for adapting to changing data distributions. Frameworks like **Deep-Edge** provide load- and interference-aware, fault-tolerant resource management for distributed model re-training across heterogeneous edge devices, carefully balancing update tasks with co-located latency-critical applications [266]. Beyond federated learning, distributed inference techniques such as **DEFER** partition large DNN models across multiple edge nodes in a pipeline, significantly increasing throughput and reducing per-device energy consumption compared to single-device inference [267].

The operational complexity of distributed edge intelligence necessitates robust management and orchestration frameworks. **Edge-as-a-Service (EaaS)** is envisioned as a service-oriented framework that manages large-scale, geo-distributed edge resources to enable edge autonomy, collaboration, and elasticity, facilitating ubiquitous computation and intelligence [268]. Supporting this, **AIOps** platforms are being adapted for edge environments, using machine learning for anomaly detection and operational analytics directly on edge devices to manage the increased infrastructure complexity [269]. Ensuring reliability, frameworks like **DeepFT** employ self-supervised deep surrogate models to proactively predict and diagnose faults, optimizing task scheduling and migration to avoid system overloads and QoS violations in volatile edge settings [270]. Ultimately, the convergence of AI-native automation, digital twins, and edge intelligence forms a powerful triad for 6G. AI and MLOps provide the brains for autonomous control, digital twins offer a virtual playground for safe development and optimization, and edge computing supplies the distributed, responsive nervous system to execute intelligence where it is most needed, paving the way for truly zero-touch, self-evolving future networks.

**Table: Comparison of approaches in 3.4 AI-Powered Network Automation, Digital Twins, and Edge Intelligence**

| Concept / Framework | Core Function / Purpose | Key Techniques / Enablers | Reference |
| :--- | :--- | :--- | :--- |
| SliceOps | A systematic, standalone slice embedded in 6G to manage the complete AI lifecycle, providing AI-as-a-Service to other network slices. | MLOps, eXplainable AI (XAI), explanation-guided reinforcement learning (XRL) for transparency and trust. | [19] |
| Digital Twins (DTs) | Creates a high-fidelity virtual replica of the physical network for simulation, data generation, AI training, and safe policy testing. | Symbiotic interplay with AI (e.g., DRL for model building), meta-learning frameworks for intelligent network management. | [258], [259], [260], [261] |
| Edge Intelligence (Edge AI) | Distributes AI model inference and training to the network periphery to meet ultra-low latency, bandwidth efficiency, and privacy requirements of 6G. | Efficient AI service provisioning, multi-tenancy support, model compression, predictive model swapping. | [42], [262], [263], [264] |
| Federated Edge Learning (FEEL) | A privacy-preserving distributed learning paradigm coordinating global model training across edge devices without centralizing raw data. | Joint communication and computation resource management (C²RM), CPU-GPU heterogeneous computing optimization. | [265] |
| Deep-Edge | A framework for efficient, distributed deep learning model updates (re-training) on heterogeneous edge devices. | Load- and interference-aware, fault-tolerant resource management for distributed training. | [266] |
| DEFER | A framework for distributed edge inference, partitioning large DNN models across multiple edge nodes in a pipeline. | Model partitioning across a dispatcher and multiple compute nodes connected in series. | [267] |
| Edge-as-a-Service (EaaS) | A service-oriented framework to manage large-scale, geo-distributed edge resources enabling edge autonomy, collaboration, and elasticity. | Management of cross-node edge resources for ubiquitous computation and intelligence. | [268] |
| AIOps for Edge | Adaptation of AIOps platforms for edge environments, using ML for anomaly detection and operational analytics on edge devices. | Machine learning for anomaly detection directly on resource-constrained edge devices. | [269] |
| DeepFT | A fault-tolerant edge computing framework using a self-supervised deep surrogate model to proactively predict and diagnose faults. | Self-supervised deep surrogate model for fault prediction, optimizing task scheduling and migration. | [270] |


## 4 Blockchain for Securing, Decentralizing, and Establishing Trust in 6G

This section explores the role of Blockchain in addressing fundamental 6G challenges related to security, privacy, and decentralization. It covers decentralized identity and access management, secure data provenance and sharing, tamper-resistant logging for network slices and transactions, resilient IoT management, and the use of smart contracts for automated service level agreements (SLAs) and resource trading in multi-stakeholder environments.

### 4.1 Decentralized Identity, Authentication, and Access Management for 6G Devices and Services

The envisioned 6G ecosystem is characterized by an unprecedented convergence of heterogeneous entities, including massive Internet of Things (IoT) devices, autonomous network slices, edge computing resources, and human users, operating across multiple administrative domains. This hyper-connected, multi-stakeholder environment renders traditional, centralized identity and access management (IAM) paradigms obsolete due to their inherent single points of failure, scalability bottlenecks, and vulnerability to large-scale data breaches. Blockchain technology emerges as a foundational enabler for a new paradigm of decentralized, user-centric, and tamper-proof IAM, which is critical for establishing trustless interactions and securing the 6G fabric.

At the core of this transformation are Decentralized Identifiers (DIDs) and the Self-Sovereign Identity (SSI) model. DIDs are a new type of identifier that enables verifiable, decentralized digital identity, independent of any centralized registry, identity provider, or certificate authority. A DID, along with its associated DID Document containing public keys and service endpoints, can be anchored on a blockchain, providing a globally resolvable, immutable root of trust. This directly addresses the cross-domain interoperability and trust challenges in 6G, as network functions and devices from different providers can authenticate each other without relying on a common, centralized PKI. As highlighted in [271] and [272], the application of DIDs extends beyond individuals to encompass IoT devices, network functions, and edge resources, forming a universal identity layer for the 6G service-based architecture. This shift from centralized certificates to DIDs and Verifiable Credentials (VCs) reduces complexity and the risk of single points of failure, laying the groundwork for more trustful collaboration in multi-party networks [273].

The SSI principle, empowered by blockchain and DIDs, returns control of identity data to the entity itself—whether a user or a device. In this model, credentials (e.g., attestations of device integrity, network slice permissions, or user attributes) are issued by trusted entities (issuers) as cryptographically signed VCs and held securely by the identity owner (holder). The holder can then present these credentials, or selective proofs derived from them, to verifiers (relying parties) to gain access to services. The blockchain acts as a neutral, tamper-proof registry for public DIDs and schemas, while the sensitive credential data remains off-chain under the holder's control. This architecture is explored in various designs, from generic frameworks [274] to domain-specific implementations for IoT [275] and healthcare [276]. It ensures privacy through minimal disclosure, mitigates the risks of massive centralized data repositories, and provides a robust, user-centric foundation for 6G's privacy regulations.

Complementing decentralized identity, blockchain enables fine-grained, dynamic, and tamper-proof access control mechanisms essential for 6G's resource-constrained and dynamic environments. Smart contracts codify access policies, automating authorization decisions and permission propagation in a transparent and auditable manner. For instance, capability-based access control models can be implemented where access tokens are issued and managed via smart contracts, allowing devices to be their own masters for resource control without a centralized authority [277]. Similarly, attribute-based access control (ABAC) policies can be enforced on-chain, where smart contracts validate the attributes (proven via VCs) of a requesting entity against predefined rules [278]. This is particularly powerful for complex, multi-tenant scenarios like smart cities or industrial IoT, where fine-grained permissions for data and physical access must be managed across organizational boundaries [279] [280].

The integration of blockchain for authentication and access management directly mitigates critical threats in 6G. It eliminates the single point of failure inherent in centralized authentication servers and PKI, distributing trust across a network of consensus nodes. The immutability of the ledger provides a definitive, auditable trail of all identity-related events and access attempts, enhancing non-repudiation and forensic capabilities [281]. Furthermore, advanced cryptographic techniques, often integrated with these blockchain systems, enhance privacy. Zero-Knowledge Proofs (ZKPs) allow entities to prove they possess certain credentials or attributes without revealing the underlying data, enabling privacy-preserving authentication [282]. Homomorphic encryption and anonymous auditing protocols can further safeguard sensitive interactions within blockchain-based IoT environments [127].

For the massive scale of 6G IoT, performance-aware designs are crucial. Lightweight consensus protocols like Proof-of-Authentication (PoAh) are proposed to replace resource-intensive mechanisms, making blockchain viable for resource-constrained devices [144]. Hierarchical or federated blockchain architectures, such as those employing multiple permissioned ledgers for domains federated by a public ledger, address scalability and privacy concerns while maintaining security guarantees [137]. In vehicular networks, hierarchical blockchain combined with fog computing can achieve efficient and stable identity authentication with low communication overhead [283].

In conclusion, blockchain technology provides the essential pillars for decentralizing trust in 6G. By anchoring DIDs and enabling SSI, it establishes a universal, user-centric identity layer. Through smart contract-enforced policies, it facilitates fine-grained, auditable access control across multi-domain ecosystems. These capabilities collectively address the core security requirements of 6G—confidentiality, integrity, authentication, and availability—while specifically mitigating the risks of centralized architectures. As 6G evolves towards a collaborative network of networks, blockchain-based decentralized IAM will be indispensable for enabling secure, privacy-preserving, and trustless interactions among its myriad heterogeneous entities.

**Table: Comparison of approaches in 4.1 Decentralized Identity, Authentication, and Access Management for 6G Devices and Services**

| Method/Model/Concept | Key Idea/Mechanism | Application Domain/Use Case | Reference |
| :--- | :--- | :--- | :--- |
| Decentralized Identifiers (DIDs) & Self-Sovereign Identity (SSI) | A new type of identifier enabling verifiable, decentralized digital identity, independent of centralized authorities. DIDs anchored on a blockchain provide a globally resolvable, immutable root of trust. The SSI model returns control of identity data to the entity (user/device). | Universal identity layer for 6G service-based architecture; cross-domain authentication for IoT devices, network functions, and edge resources. | [271], [272], [274], [275], [276] |
| Smart Contract-based Capability Access Control (BlendCAC) | A blockchain-enabled decentralized capability-based access control system. Smart contracts manage the registration, propagation, and revocation of capability tokens, allowing devices to be their own masters for resource control. | Fine-grained access control for IoT systems (e.g., Smart Grid, Smart Cities), enabling decentralized authorization without a central server. | [277] |
| Smart Contract-based Attribute-Based Access Control (ABAC) with Reputation | Attribute-based access control policies enforced via smart contracts. The contracts validate attributes (proven via Verifiable Credentials) of a requesting entity. Can be enhanced with a reputation assessment to deter malicious nodes. | Complex, multi-tenant IoT scenarios (e.g., smart cities, industrial IoT) requiring fine-grained, dynamic permission management across boundaries. | [278], [279], [280] |
| Federated/Hierarchical Blockchain Architecture (Fed-DDM) | A framework using multiple permissioned blockchains (intra-ledgers) for different domains, federated by a public blockchain (inter-ledger). Uses efficient BFT consensus within domains and a scalable PoW consensus for cross-domain operations. | Scalable and privacy-preserving decentralized data marketplaces for large-scale IoT in smart cities; addresses scalability and privacy while maintaining security. | [137] |
| Proof-of-Authentication (PoAh) Consensus | A novel lightweight consensus algorithm that replaces resource-intensive Proof-of-Work with a cryptographic authentication mechanism, making blockchain viable for resource-constrained devices. | Fast, scalable private blockchain for large-scale IoT frameworks (e.g., smart cities, environmental monitoring). | [144] |
| Hierarchical Blockchain with Fog Computing (ESIA) | Combines hierarchical blockchain with vehicular fog computing to group vehicles efficiently. Employs a bottom-up consensus process (B2UHChain) to achieve low communication overhead and high stability. | Efficient and stable identity authentication for the Internet of Vehicles (IoV), improving scalability and reducing latency. | [283] |
| Zero-Knowledge Proofs (ZKPs) for Privacy-Preserving Authentication (ZKBID) | Uses Zero-Knowledge Proofs to allow entities to prove possession of credentials or attributes without revealing the underlying data. ZKBID specifically links blockchain accounts to authenticated users in a one-to-one, anonymous yet accountable manner. | Accountable anonymous blockchain accounts for Web 3.0 decentralized identity; privacy-preserving authentication in blockchain systems. | [282] |
| Anonymous Auditing with Advanced Cryptography | Integrates privacy-enhancing tools and anonymous auditing methods, including advanced cryptographic techniques like homomorphic encryption, to secure blockchain-based IoT environments without compromising user privacy. | Enhancing security and privacy in blockchain-based IoT systems via anonymized auditing of transactions. | [127] |


### 4.2 Secure Data Provenance, Integrity, and Trusted Sharing

The foundational properties of blockchain—immutability, transparency, and cryptographic auditability—provide a paradigm shift for managing data in 6G ecosystems. In a network characterized by hyper-connectivity, massive IoT deployments, and decentralized intelligence, ensuring the provenance, integrity, and trusted sharing of data is paramount. Blockchain technology addresses these needs by creating an indelible, chronological record of data creation, access, and modification, thereby establishing a single source of truth that is verifiable by all authorized participants without reliance on a central authority. This capability is critical for 6G applications ranging from autonomous supply chains and smart city infrastructure to federated learning across network edges, where data authenticity directly impacts system safety, efficiency, and regulatory compliance.

A primary application is the creation of secure and transparent **data marketplaces** for IoT and 6G-generated data streams. Traditional centralized marketplaces suffer from single points of failure, lack of transparency in pricing and data usage, and minimal control for data owners. Blockchain-based frameworks like **Fed-DDM** propose a hierarchical, federated ledger architecture to enable scalable and interoperable data exchanges. By dividing participants into permissioned domains with private intra-ledgers and federating them via a public inter-ledger, such models balance scalability with the security and auditability required for large-scale IoT data trading [137]. Similarly, solutions like **BlockMarkchain** focus on creating a trustless marketplace where the validity of data can be disputed and adjudicated by a smart contract without the data itself being revealed on-chain, thus preserving privacy while ensuring contractual compliance [284]. For real-time trading from resource-constrained devices, frameworks incorporate energy-aware demand selection to ensure marketplace sustainability, using smart contracts to automate agreement frameworks and pricing models [285]. These decentralized marketplaces empower data owners with control and fair compensation, which is essential for incentivizing the high-quality data generation needed for 6G AI models.

Beyond commerce, blockchain's immutability is instrumental for **tamper-resistant logging and audit trails** across the 6G infrastructure. Network slice lifecycle management, resource allocation transactions, and access control events all require verifiable records to ensure operational integrity and facilitate post-incident forensic analysis. Systems like **BlockAudit** and **Harpocrates** demonstrate how blockchain can transform conventional audit logs. BlockAudit leverages a blockchain's design to create a scalable, tamper-proof system that defends against attacks exploiting root privileges or database vulnerabilities, thereby securing critical logs in enterprise and network systems [286] [287]. For highly sensitive operations, such as those on personal or health data, Harpocrates integrates zero-knowledge proofs with blockchain. This allows fine-grained data operations to be recorded immutably without leaking sensitive identifiers (e.g., user identity or data content), while still permitting the validity of the operations to be publicly verified [288]. This approach is vital for 6G networks handling sensitive user data while needing to comply with strict regulations like GDPR.

Establishing **verifiable data provenance and integrity** is another cornerstone, particularly for supply chains, scientific data, and AI training datasets in 6G. Provenance—the record of a data item's origin and journey—is key to assessing trustworthiness. Blockchain provides an immutable chain of custody. In supply chain management, frameworks like **PrivChain** use zero-knowledge range proofs to allow entities to prove certain attributes (e.g., a product was manufactured within an authorized region) without revealing the exact, sensitive location, thus protecting trade secrets while ensuring traceability [289]. For scientific and high-performance computing, **SciChain** introduces a blockchain with a tailored consensus protocol (Proof-of-Scalable-Traceability) to deliver immutable and autonomous data provenance services, ensuring that scientific data and its lineage are trustworthy and cannot be fabricated [290]. General models like **AUDITEM** further showcase automated data integrity verification using smart contracts and distributed file systems, providing business stakeholders with trustworthy and automated assurance of data authenticity [291].

However, implementing these solutions in 6G faces significant challenges. The inherent **tension between immutability and regulatory compliance** (e.g., GDPR's "right to be forgotten") requires novel technical approaches. Solutions like **Kovacs** address this by using one-time pseudonyms and protocols that allow data subjects to prove ownership and exercise their rights to rectify or delete personal data, even within a permissionless blockchain framework [292]. Other research explores **blockchain mutability** techniques, such as chameleon hashing, to allow authorized redactions or updates to on-chain data without breaking the chain's integrity, a necessary feature for dynamic IoT data in BIoT (Blockchain-IoT) ecosystems [293] [294]. **Scalability and performance** remain perennial hurdles. 6G networks will generate data at unprecedented volume and velocity. Lightweight blockchain architectures like **LSB** (Lightweight Scalable Blockchain) and **Microchain** propose tiered or hierarchical consensus protocols optimized for IoT constraints, reducing overhead and delay while maintaining security guarantees [295] [296]. Furthermore, **privacy-preserving techniques** must evolve. While hashing data provides integrity, it does not conceal patterns. Advanced cryptographic methods like zero-knowledge proofs (ZKPs), as used in Harpocrates and PrivChain, and differential privacy are being integrated to enable auditing and sharing without exposing the underlying sensitive information [297].

In conclusion, blockchain technology provides the essential bedrock for secure data provenance, integrity, and trusted sharing in 6G. By enabling decentralized data marketplaces, immutable audit logs, and verifiable provenance trails, it addresses critical trust deficits in complex, multi-stakeholder 6G environments. The convergence of these blockchain-based data assurance mechanisms with 6G's ultra-reliable, low-latency connectivity will unlock robust frameworks for everything from smart mobility and industrial automation to privacy-preserving collaborative AI, forming a trustworthy data foundation for the next generation of digital services.

**Table: Comparison of approaches in 4.2 Secure Data Provenance, Integrity, and Trusted Sharing**

| Model / Framework Name | Primary Purpose / Application | Key Technical Features / Innovations | Reference |
| :--- | :--- | :--- | :--- |
| Fed-DDM | Hierarchical decentralized data marketplace for IoT/6G data streams | Federated ledger architecture with permissioned domains (private intra-ledgers) and a public inter-ledger; uses BFT consensus for domains and scalable PoW for federation. | [137] |
| BlockMarkchain | Secure, trustless decentralized data marketplace | Dispute and adjudication of data validity via smart contracts without revealing data on-chain; constant load on blockchain. | [284] |
| Energy-aware Demand Selection and Allocation | Real-time IoT data trading from resource-constrained devices | Energy-aware demand selection and allocation; smart contracts automate agreement frameworks and pricing models. | [285] |
| BlockAudit | Secure and transparent tamper-proof audit logs | Leverages blockchain design for scalable, tamper-proof logs; defends against attacks exploiting root privileges or database vulnerabilities. | [286] |
| Harpocrates | Privacy-preserving and immutable audit log for sensitive data operations | Integrates zero-knowledge proofs with blockchain; records operations without leaking sensitive identifiers while allowing public verification. | [288] |
| PrivChain | Provenance and privacy preservation in blockchain-enabled supply chains | Uses zero-knowledge range proofs to prove attributes (e.g., authorized region) without revealing exact, sensitive location; includes incentive mechanism. | [289] |
| SciChain | Trustworthy scientific data provenance for HPC | Tailored consensus protocol (Proof-of-Scalable-Traceability) for immutable and autonomous data provenance services. | [290] |
| AUDITEM | Automated and efficient data integrity verification | Uses smart contracts and a distributed file system to store integrity verification attributes; includes a Data Integrity Verification Tool (DIVT). | [291] |
| Kovacs | Decentralized data exchange and usage logging for GDPR compliance in inverse transparency | Uses one-time pseudonyms and protocols allowing data subjects to prove ownership and exercise rights to rectify/delete personal data on permissionless blockchain. | [292] |
| LSB (Lightweight Scalable Blockchain) | Lightweight blockchain for IoT security and privacy | Tiered architecture; lightweight consensus, distributed trust, and throughput management optimized for IoT constraints. | [295] |
| Microchain | Light hierarchical consensus protocol for IoT systems | Hierarchical consensus protocol designed for scalability, storage, and privacy in IoT networks. | [296] |


### 4.3 Resilient and Trustworthy Management of Massive IoT and Network Slices

The envisioned 6G ecosystem will be characterized by an unprecedented scale of interconnected devices, forming massive Internet of Things (IoT) deployments, and by highly dynamic, logically isolated network slices catering to diverse vertical applications. Managing this complex, heterogeneous, and fluid environment demands a paradigm shift from centralized, trust-heavy models to decentralized, resilient, and trustworthy frameworks. Blockchain technology, with its core tenets of decentralization, immutability, and automated execution via smart contracts, emerges as a foundational enabler for such resilient management systems. It provides the necessary infrastructure for secure device lifecycle management, verifiable orchestration of network resources, and transparent enforcement of service agreements, thereby establishing a bedrock of trust across multi-stakeholder 6G operations.

For massive-scale IoT, blockchain addresses critical security and scalability challenges inherent in traditional centralized architectures. The initial onboarding and identity provisioning of billions of resource-constrained devices can be securely managed through decentralized registries. As highlighted in [298], blockchain and smart contracts can implement robust, token-based access control mechanisms, creating an immutable record of device identities and permissions. This eliminates single points of failure and prevents unauthorized access. Once deployed, continuous monitoring of device health and behavior is essential. Frameworks like the scalable architecture proposed in [299] leverage blockchain in conjunction with fog computing to decentralize monitoring tasks. IoT device states and telemetry data can be anchored on the blockchain, providing a tamper-proof audit trail. This immutability is crucial for forensic analysis and for building trust in the data reported by devices, as explored in [300], where device behavior analysis is secured within a blockchain and Trusted Execution Environment (TEE) framework. Furthermore, the critical process of delivering firmware and security updates to vast IoT networks is transformed by blockchain. Centralized update servers pose scalability and trust issues. Blockchain-based schemes, as discussed in [301], can create decentralized, incentivized delivery networks. Smart contracts can manage the commitment of vendors to pay distributors for verified updates, using cryptographic protocols like Zero-Knowledge Contingent Payment (ZKCP) to provide unforgeable proof-of-distribution. This ensures updates are delivered reliably and authentically, even in intermittently connected environments, a necessity underscored by investigations into reliable firmware roll-outs over large mesh networks [302]. To manage the sheer transaction volume, lightweight and scalable blockchain designs are paramount. Solutions such as tiered architectures [295], sharding techniques for IoT contexts [303], and hierarchical consensus protocols [304] are specifically engineered to reduce the computational, storage, and communication overhead on IoT devices, making blockchain integration feasible at scale.

Parallel to IoT device management, the dynamic lifecycle of network slices in 6G—encompassing instantiation, orchestration, runtime monitoring, and termination—requires automated and verifiable control mechanisms. Smart contracts are uniquely suited to codify the complex Service Level Agreements (SLAs) that define each slice's performance, security, and resource guarantees. As argued in [170], future SLAs must be dynamic, flexible, and automated to meet diverse application needs, with blockchain providing the immutable recording and auditing layer. Smart contracts can autonomously enforce these SLAs, triggering actions such as resource scaling, billing, or penalty application based on verifiable performance data. This automated enforcement addresses the trust gap identified in current practices, where reliance on service providers to acknowledge breaches is a vulnerability, as noted in [305]. The integration of oracles is vital for this model, as smart contracts operate in a closed blockchain environment. Oracles act as secure bridges, fetching real-world performance metrics (e.g., latency, throughput, packet loss) from the network and feeding them into the smart contract for evaluation. The integrity of this data is paramount, as corrupt oracles can lead to incorrect SLA assessments. Research into oracle security [306] and specific applications like [307] highlight methods to ensure the reliability and tamper-resistance of oracle-reported data, often through multiple attestations or TEEs. This creates a closed loop of measurement and enforcement: oracles supply verified performance data to the blockchain, smart contracts compare this data against SLA terms, and automatically execute agreed-upon actions. This mechanism not only ensures compliance but also enhances the resilience of the network slicing fabric itself. In a multi-tenant, multi-domain scenario, a localized failure or malicious action by one tenant or domain provider should not cascade. A decentralized ledger shared among stakeholders provides a single source of truth regarding slice states, resource allocations, and SLA statuses. Coordination for recovery or resource reallocation can be managed through pre-agreed smart contract logic, enabling rapid and trust-minimized responses to failures, moving towards the vision of self-healing networks.

In synthesis, blockchain technology provides the critical infrastructure for building resilient and trustworthy management systems for the massive IoT and dynamic network slicing paradigms of 6G. By decentralizing control, immutably logging transactions and states, and automating policy enforcement through tamper-proof smart contracts, it mitigates risks associated with central points of failure, opaque operations, and manual interventions. When integrated with secure oracles for real-world data and designed with scalability in mind through sharding, hierarchical consensus, and hybrid architectures, blockchain becomes a practical and powerful tool. It establishes a verifiable and automated governance layer that can manage the lifecycle of billions of devices and countless network slices, ensuring compliance, enhancing security, and fostering trust among all participants in the 6G value chain.

**Table: Comparison of approaches in 4.3 Resilient and Trustworthy Management of Massive IoT and Network Slices**

| Method/Model | Key Idea/Contribution | Reference |
| :--- | :--- | :--- |
| Token-based IoT Access Control | Uses blockchain and smart contracts to implement robust, token-based access control mechanisms for secure device onboarding and identity management. | [298] |
| Scalable IoT Monitoring Architecture | Leverages blockchain with fog computing to decentralize monitoring tasks, anchoring device states and telemetry on-chain for a tamper-proof audit trail. | [299] |
| Secure IoT Behavior Modeling | Secures device behavior analysis within a framework combining blockchain and Trusted Execution Environments (TEEs). | [300] |
| Decentralized IoT Software Update Delivery | Proposes a blockchain-based, incentivized delivery network for updates using smart contracts and Zero-Knowledge Contingent Payment (ZKCP) for proof-of-distribution. | [301] |
| Lightweight Scalable Blockchain (LSB) | Proposes a tiered blockchain architecture optimized for IoT, using lightweight consensus and cluster-based management to reduce overhead. | [295] |
| Scalable & Trustworthy Blockchain (STB) | Uses blockchain sharding and a peer-to-peer oracle network to achieve scalability, flexibility, and trustworthiness for IoT. | [303] |
| Hierarchical & Location-aware Consensus (LH-Raft) | A consensus protocol for IoT-blockchain apps that forms local groups based on node reputation and distance to improve scalability and reduce latency. | [304] |
| Autonomous SLA Architecture for 6G | Proposes an end-to-end layered SLA architecture using Distributed Ledger Technology (DLT) and smart contracts to make SLAs dynamic, automated, and transparent. | [170] |
| Blockchain-based SLA Compliance Assessment | Employs blockchain for assessing SLA compliance and enforcing consequences, moving beyond trust in service providers to acknowledge breaches. | [305] |
| Oracle Security & Data Integrity | Discusses oracle design, attacks, and mitigation strategies for feeding reliable real-world data (e.g., network performance) to smart contracts. | [306] |
| Data Integrity Verification for Network Slicing | Uses oracles and smart contracts to protect and verify the integrity of 5G network slice configurations. | [307] |


### 4.4 Smart Contracts for Automated Resource Trading and Service Orchestration

The inherent complexity and dynamism of 6G networks, characterized by ultra-dense deployments, heterogeneous resources, and a multitude of stakeholders—from mobile network operators and edge infrastructure providers to individual device owners—necessitate automated, transparent, and trust-minimized mechanisms for resource coordination. Smart contracts, as self-executing programs deployed on a blockchain, emerge as a foundational technology to automate complex, multi-party agreements, thereby enabling efficient decentralized marketplaces for trading communication, computation, and data resources without relying on centralized, potentially untrusted intermediaries.

A primary application is in **decentralized resource trading**, where smart contracts codify the rules for dynamic exchange. For spectrum sharing, projects like *Bandcoin* demonstrate how smart contracts can automate mobile network bandwidth roaming agreements between operators, service providers, and consumers, supporting advanced features like bulk purchases and auction mechanisms with significantly improved transaction performance [168]. Similarly, in multi-operator environments, consortium blockchains with specialized smart contracts, such as the Multi-Ops Spectrum Sharing (MOSS) contract, enforce truthful spectrum trading and punish malicious behavior without a central broker, enhancing privacy and fairness [308]. Beyond spectrum, smart contracts orchestrate markets for edge computing resources. Frameworks propose *futures-based* trading mechanisms where forward contracts between Mobile Edge Computing (MEC) servers (sellers) and resource consumers like UAVs or vehicles (buyers) are negotiated and executed automatically based on predicted supply, demand, and network conditions, reducing negotiation latency and trading failures compared to onsite spot markets [309] [310]. This concept extends to unifying futures and spot markets, where smart contracts manage overbooking and dynamic pricing to optimize resource utilization and social welfare [311]. For storage, decentralized storage networks (DSNs) leverage smart contracts to govern storage agreements between clients and providers, with incentive-compatible mechanisms that trigger verifiable proofs-of-storage only upon client challenge, reducing network overhead while ensuring honest behavior [312].

Closely related is the **automated fulfillment and enforcement of Service Level Agreements (SLAs)**, critical for the "as-a-Service" paradigm in 6G, including Network Slicing-as-a-Service (SlaaS) and Small-Cell-as-a-Service. Traditional SLAs are difficult to negotiate, monitor, and enforce transparently. Blockchain and smart contracts provide an immutable, auditable record of SLA terms and automated enforcement of penalties or rewards. Architectures like BEAT (Blockchain-Enabled Accountable and Transparent) utilize permissioned distributed ledgers and smart contracts to create transparent and accountable end-to-end frameworks for network and infrastructure sharing, automating compliance checks and settlements [136] [313]. For network slicing, smart contracts can encode the specific performance guarantees (e.g., latency, throughput, reliability) for each tenant slice. The autonomous monitoring of Key Performance Indicators (KPIs) against these contractual terms allows for real-time, trustless verification and automatic billing or compensation, which is essential for critical applications like remote surgery or connected vehicles [170]. This automation extends to the extreme edge, where smart contracts can implement simple yet effective SLAs between individual small cell providers (e.g., home or business users) and mobile operators, democratizing infrastructure sharing [169].

Furthermore, smart contracts are pivotal in creating **incentive mechanisms for resource sharing in device-centric networks**. As 6G evolves towards a paradigm where smart devices themselves become part of the network fabric, facilitating device-to-device (D2D) communications and opportunistic networking, incentivizing participation is crucial [314]. Smart contracts can manage micro-transactions and rewards for devices that relay data, share computational cycles, or provide caching storage. For instance, in proactive caching within hierarchical wireless networks, a blockchain-based smart contract constructs an autonomous content caching market. Cache helpers (e.g., edge nodes or user devices) adapt their strategies based on market statistics from the blockchain, with their truthful behavior financially enforced by the contract terms, creating a trustless cooperative ecosystem [315]. In socially trusted collaborative edge computing among small cell base stations (SBSs), payment-based incentive mechanisms implemented via smart contracts can ensure proportionally fair utility division, encouraging SBSs to form stable coalitions and share computation resources securely [316]. Similarly, for data trading in IoT, decentralized marketplaces use smart contracts to automatically enforce agreements between data providers and consumers, matching requirements and ensuring payment upon verified data delivery [317] [137]. This is particularly relevant for automotive data, where MEC-based architectures can use smart contracts to manage the lifecycle of data functions, processing vehicle data according to SLA policies and licensing terms for monetization [318].

The implementation of these smart contract systems must address significant challenges, including scalability, privacy, and secure oracle integration. Scalability is addressed through layered architectures (e.g., federated ledgers combining private intra-ledgers with a public inter-ledger) [137] and optimized consensus for permissioned settings [168]. Privacy concerns are mitigated by keeping sensitive data off-chain, storing only hashes or commitments on the blockchain, and using zero-knowledge proofs where necessary. Crucially, smart contracts require secure access to external data (oracles) to trigger execution based on real-world events like network performance metrics or SLA violations. Oracle networks and designs like the Practical Data Feed Service (PDFS) are essential to provide trustworthy, real-time data feeds to the blockchain without compromising security [319]. Moreover, the security of the smart contracts themselves is paramount, as vulnerabilities can lead to significant financial losses; thus, rigorous specification mining, formal verification, and auditing are required [320] [321].

In summary, smart contracts act as the automated governance layer for 6G's decentralized economy. By enabling trustless, programmable, and transparent agreements for resource trading, SLA management, and incentive distribution, they facilitate the efficient orchestration of a fragmented yet collaborative ecosystem. This automation reduces operational overhead, minimizes disputes, and unlocks new business models, from micro-leasing of device resources to dynamic multi-operator spectrum pools, forming the backbone of agile and economically sustainable 6G networks.

**Table: Comparison of approaches in 4.4 Smart Contracts for Automated Resource Trading and Service Orchestration**

| Application Category | Specific Use Case / Mechanism | Key Features / Benefits | Challenges Addressed | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Decentralized Resource Trading | Spectrum Sharing (e.g., Bandcoin) | Automates roaming agreements between operators, service providers, consumers; supports bulk purchases, auctions; improves transaction performance. | Manual, inefficient roaming agreements; lack of trust between parties. | [168] |
| Decentralized Resource Trading | Spectrum Sharing in Multi-Operator Networks (MOSS) | Consortium blockchain with smart contracts enforces truthful trading, punishes malicious behavior without a central broker; enhances privacy and fairness. | Identity privacy, data security, and trust in multi-operator spectrum sharing. | [308] |
| Decentralized Resource Trading | Futures-based Edge Computing Resource Trading (UAVs/Vehicles) | Forward contracts between MEC servers and buyers (UAVs/vehicles) based on predicted supply/demand/network conditions; reduces negotiation latency and trading failures. | Unpredictable trading latency, failure, and unfair pricing in onsite spot markets. | [309] [310] |
| Decentralized Resource Trading | Unifying Futures and Spot Markets with Overbooking | Smart contracts manage overbooking and dynamic pricing to optimize resource utilization and social welfare in mobile edge networks. | Underutilization of dynamic resources and excessive decision-making overhead in pure spot markets. | [311] |
| Decentralized Resource Trading | Decentralized Storage Networks (DSNs) | Smart contracts govern storage agreements; incentive-compatible mechanism triggers verifiable proofs-of-storage only upon client challenge, reducing network overhead. | Continuous verification cost and vulnerability to service-denying attacks in DSNs. | [312] |
| Automated SLA Fulfillment & Enforcement | Network/Infrastructure Sharing (BEAT) | Permissioned distributed ledger and smart contracts create transparent, accountable end-to-end frameworks for network sharing, automating compliance and settlements. | Difficulty in negotiating, monitoring, and enforcing traditional SLAs for infrastructure sharing. | [136] [313] |
| Automated SLA Fulfillment & Enforcement | Autonomous SLAs for Network Slicing | Smart contracts encode performance guarantees (latency, throughput); autonomous KPI monitoring enables real-time, trustless verification and automatic billing/compensation. | Lack of standardized, immutable, and auditable SLA recording for dynamic, critical 6G applications. | [170] |
| Automated SLA Fulfillment & Enforcement | Small-Cell-as-a-Service (SCaaS) | Smart contracts implement simple, effective SLAs between individual small cell providers (home/business users) and mobile operators. | Scalability and legal constraints in democratizing infrastructure sharing. | [169] |
| Incentive Mechanisms for Device-Centric Networks | Proactive Caching Market | Blockchain-based smart contracts create an autonomous content caching market; cache helpers adapt strategies based on market stats, with truthful behavior financially enforced. | Incentivizing cooperation and ensuring truthful behavior in decentralized caching. | [315] |
| Incentive Mechanisms for Device-Centric Networks | Socially Trusted Collaborative Edge Computing | Payment-based incentive mechanisms via smart contracts ensure proportionally fair utility division, encouraging SBSs to form stable coalitions and share resources. | Incentivizing resource sharing and managing security risks in ultra-dense small cell networks. | [316] |
| Incentive Mechanisms for Device-Centric Networks | Decentralized IoT Data Marketplaces | Smart contracts automatically enforce agreements between data providers and consumers, matching requirements and ensuring payment upon verified delivery. | Enabling scalable, interoperable, and secure data exchanges in large-scale IoT environments. | [317] [137] |
| Incentive Mechanisms for Device-Centric Networks | Automotive Data Monetization in MEC | MEC-based architecture uses smart contracts to manage the lifecycle of data functions, processing vehicle data per SLA policies and licensing terms. | Managing the value, privacy, and licensing of high-volume real-time vehicle data. | [318] |
| Implementation Challenges & Enablers | Scalability Solutions | Layered architectures (e.g., federated ledgers combining private intra-ledgers with a public inter-ledger) and optimized consensus for permissioned settings. | High resource demands, low throughput, and poor scalability of blockchains in large-scale systems. | [137] [168] |
| Implementation Challenges & Enablers | Oracle Services (e.g., PDFS) | Provides trustworthy, real-time external data feeds (e.g., network performance metrics) to smart contracts without compromising security. | The "oracle problem": secure access to reliable external data for smart contract execution. | [319] |
| Implementation Challenges & Enablers | Smart Contract Security | Rigorous specification mining, formal verification, and auditing are required to prevent vulnerabilities leading to financial losses. | Security vulnerabilities in smart contract code. | [320] [321] |


### 4.5 Privacy Preservation and Regulatory Compliance in Blockchain-Enabled 6G

The inherent transparency and immutability of blockchain, while foundational for trust and auditability in 6G networks, present significant challenges for data privacy and regulatory compliance. In a 6G ecosystem characterized by ubiquitous connectivity, massive IoT deployments, and pervasive AI-driven services, vast quantities of sensitive data—including personal identifiers, health records, financial transactions, and proprietary business information—will be generated and exchanged. Storing such data directly on a public, immutable ledger conflicts with core principles of data protection regulations like the EU's General Data Protection Regulation (GDPR), which enshrines rights to data erasure ("right to be forgotten"), rectification, and purpose limitation. This tension between blockchain's permanence and regulatory mandates for data minimization and deletion is a critical hurdle for adoption in regulated industries such as healthcare, finance, and smart city management [322]. Consequently, a suite of advanced privacy-enhancing techniques (PETs) and hybrid architectural models has emerged to reconcile blockchain's trust benefits with stringent privacy and compliance requirements.

Zero-Knowledge Proofs (ZKPs) have ascended as a cornerstone technology for privacy preservation in blockchain-enabled 6G systems. ZKPs allow a prover to cryptographically demonstrate the validity of a statement (e.g., "this transaction is correct," "I am over 18," "my credit score exceeds a threshold") to a verifier without revealing any underlying sensitive data. This capability is transformative for 6G applications. For instance, in decentralized identity management for network access, a user can prove their eligibility or credentials without exposing their full identity, enabling privacy-preserving authentication [323]. In supply chain traceability, a participant can prove a product's origin or compliance with storage conditions without disclosing sensitive supplier details or pricing information [289]. ZKPs also enable private smart contract execution and verifiable off-chain computations, where the correctness of a computation performed on private data can be attested to on-chain without leaking the inputs or internal state [324]. Advanced frameworks like zkSNARKs and zkSTARKs are being optimized for efficiency, making them increasingly viable for the low-latency, high-throughput demands of 6G networks [325]. The integration of ZKPs with federated learning, as seen in concepts like zkDFL, further illustrates their role in enabling verifiable, privacy-preserving collaborative AI model training across 6G edges [326].

To address the GDPR's right to erasure, cryptographic techniques and novel ledger structures are being explored. Chameleon hashes, which allow for controlled modification of blockchain data by holders of a trapdoor key, offer a pathway for authorized data redaction without breaking the chain's integrity [327]. Alternative architectures propose mechanisms like "context chains" or tree-based structures that isolate data belonging to specific entities or purposes, enabling the deletion of an entire context chain without affecting others in the network [328]. Furthermore, sophisticated key management and proxy re-encryption schemes can render encrypted on-chain data inaccessible upon revocation of access rights, achieving a functional equivalent to deletion [329]. For consent management, blockchain and smart contracts provide an immutable, transparent ledger for recording user consent preferences, data access requests, and data processing activities. Systems like OConsent and blockchain-based dynamic consent models give users auditable control over their data, allowing them to grant, modify, or revoke consent in a tamper-evident manner, which is crucial for demonstrating compliance [330] [331].

Hybrid on-chain/off-chain data storage models are essential architectural patterns for balancing auditability with privacy and scalability. In these models, the blockchain serves as an immutable, tamper-proof anchor for verification, while the bulk of sensitive data is stored off-chain in decentralized storage networks (e.g., IPFS), encrypted databases, or locally with data owners. Only cryptographic commitments (hashes), data provenance metadata, access control policies, and ZKPs are stored on-chain. This approach is exemplified in systems for electronic health records, where patient data remains in encrypted form off-chain, and the blockchain logs access events, consent states, and data lineage hashes, enabling auditability without exposing the clinical data [332] [333]. The Hybrid DLT concept extends this by using a public blockchain to render the history of private ledgers tamper-evident, without requiring the public chain to store the private data blocks themselves [334]. For IoT in 6G, this model allows lightweight devices to submit data hashes or ZKPs to the chain while keeping raw sensor data private, enabling secure data integrity verification and provenance tracking for applications like smart grids or industrial monitoring [291].

Selective disclosure and advanced encryption schemes further refine privacy controls. Stealth address protocols, such as those enhanced with homomorphic encryption (HE-DKSAP), generate unique, one-time addresses for each transaction, preventing the linkage of multiple transactions to a single recipient and enhancing transactional privacy on programmable blockchains [335]. Ring signatures and confidential transactions, as seen in proposals like Coloured Ring Confidential Transactions, obscure the sender, receiver, and amount in asset transfers, which is vital for financial privacy in 6G-enabled decentralized finance (DeFi) [336]. Differential privacy, a technique from statistical data analysis, is being integrated into blockchain query mechanisms and smart contracts to allow aggregate data analysis (e.g., for network optimization or market research) while providing mathematical guarantees against the re-identification of individuals from the released information [297] [337].

Finally, achieving regulatory compliance requires more than just technical mechanisms; it necessitates governance frameworks that align technical operations with legal obligations. Second-layer data governance models for permissioned blockchains are being developed to explicitly define roles, responsibilities, and processes for data controllers and processors, ensuring that privacy-by-design principles and regulatory requirements are embedded into the network's operational rules [338]. Frameworks like SeDe (Selective De-Anonymization) propose balanced models where privacy-preserving systems incorporate accountable governance structures, allowing for lawful de-anonymization under specific, auditable circumstances, such as investigating illicit activities, thereby addressing regulatory concerns about the potential misuse of absolute privacy [339]. In conclusion, for blockchain to be a viable trust anchor in the privacy-sensitive 6G era, it must evolve beyond its transparent roots. The convergence of advanced cryptography like ZKPs, hybrid data architectures, and embedded regulatory governance will be paramount in constructing blockchain systems that deliver both unwavering auditability and robust, compliant privacy protection.

**Table: Comparison of approaches in 4.5 Privacy Preservation and Regulatory Compliance in Blockchain-Enabled 6G**

| Method / Model / Technique | Core Mechanism / Approach | Primary Application / Use Case | Reference |
| :--- | :--- | :--- | :--- |
| Zero-Knowledge Proofs (ZKPs) | Cryptographic proof allowing a prover to demonstrate statement validity without revealing underlying data. | Decentralized identity management, supply chain traceability, private smart contract execution, verifiable off-chain computations, collaborative AI training. | [325], [289], [324], [326], [323] |
| Cryptographic Data Redaction (e.g., Chameleon Hashes) | Allows controlled modification/redaction of blockchain data using a trapdoor key without breaking chain integrity. | Enabling data deletion/modification to comply with GDPR's "right to be forgotten" on immutable ledgers. | [327] |
| Context/Tree-Based Ledger Structures | Tree-based structures (e.g., context chains) that isolate data by entity/purpose, enabling deletion of entire branches. | Enabling data deletion for specific entities or purposes in append-only blockchains. | [328] |
| Key Management & Proxy Re-Encryption | Sophisticated key management and proxy re-encryption schemes to render encrypted on-chain data inaccessible upon access revocation. | Achieving functional equivalent to data deletion for encrypted data on-chain (e.g., e-prescription management). | [329] |
| Blockchain-based Consent Management | Use of blockchain and smart contracts as an immutable, transparent ledger for recording user consent preferences and data access activities. | Providing users with auditable control over their data, allowing grant, modification, or revocation of consent (e.g., fitness data, general privacy management). | [330], [331] |
| Hybrid On-Chain/Off-Chain Storage | Blockchain stores cryptographic commitments (hashes), metadata, and access policies; bulk sensitive data stored off-chain in decentralized storage or encrypted databases. | Electronic Health Records (EHR) sharing, IoT data integrity verification, enabling auditability without exposing raw data. | [332], [333], [334], [291] |
| Stealth Address Protocols (e.g., HE-DKSAP) | Generates unique, one-time addresses for each transaction using techniques like homomorphic encryption to prevent transaction linkage. | Enhancing transactional privacy on programmable blockchains. | [335] |
| Ring Signatures & Confidential Transactions (e.g., Coloured Ring CT) | Obscures sender, receiver, and transaction amount using ring signatures and commitment schemes. | Financial privacy in decentralized finance (DeFi) and asset trading. | [336] |
| Differential Privacy Integration | Adds mathematical noise to query responses or smart contract outputs to prevent re-identification of individuals from aggregate data. | Private data sharing and aggregate analysis in Industrial IoT and blockchain query mechanisms. | [297], [337] |
| Second-Layer Data Governance Models | Governance frameworks defining roles, responsibilities, and processes for data controllers/processors on permissioned blockchains. | Aligning technical blockchain operations with legal obligations like GDPR, especially in multi-stakeholder environments (e.g., pandemic data sharing). | [338] |
| Selective De-Anonymization (SeDe) Frameworks | Balances privacy with regulatory compliance by allowing lawful, auditable de-anonymization under specific circumstances via threshold encryption and ZKPs. | Addressing regulatory concerns about misuse of absolute privacy in blockchain systems. | [339] |


### 4.6 Decentralized Trust and Reputation Management Systems

The envisioned 6G ecosystem, characterized by hyper-connectivity, massive IoT integration, and multi-stakeholder service provisioning, fundamentally challenges traditional, perimeter-based security models. Static authentication at the point of entry is insufficient for a dynamic network where authorized nodes can be compromised post-authentication or act selfishly, thereby impeding network reliability and resilience. To address this, Decentralized Trust and Reputation Management (DTRM) systems emerge as a critical paradigm, enabling the continuous, evidence-based evaluation of participant trustworthiness. Blockchain technology, with its inherent properties of decentralization, immutability, and transparency, provides an ideal foundational platform for such systems, fostering a verifiably trustworthy ecosystem without relying on a single central authority.

The core function of a blockchain-based DTRM is to quantify the trustworthiness of network entities—be they end-user devices, service providers, or infrastructure operators—based on their historical interactions and behaviors. This process involves the immutable recording of interaction evidence, such as service fulfillment records, data exchange logs, or feedback from resource consumers, onto a distributed ledger. Smart contracts then automate the computation of trust or reputation scores from this evidence according to predefined, transparent algorithms. For instance, in a resource-sharing marketplace for 6G, a blockchain can maintain reputation scores by evaluating a resource owner's adherence to Service Level Agreements (SLAs) and aggregating feedback from consumers, as discussed in [143]. This creates a self-reinforcing cycle where trustworthy behavior is incentivized and recorded, while malicious or unreliable actions are penalized and immutably documented, allowing the network to make informed, dynamic decisions about access and collaboration.

Several architectural innovations and frameworks illustrate the application of blockchain for DTRM in 6G-related scenarios. A common approach integrates Trust and Reputation Systems (TRS) directly into access control mechanisms. For example, one solution proposes a decentralized attribute-based access control system with an auxiliary TRS for IoT authorization, where trust scores progressively quantify node behavior and are incorporated into access policies to achieve dynamic and flexible control [340]. This ensures that access rights are not static but evolve with the entity's observed behavior. Similarly, other works design blockchain-based trust management for IoT access control, explicitly incorporating calculated reputation scores into attribute-based policies to create a self-adaptive system [341]. For supply chains—a critical 6G vertical—frameworks like TrustChain use a consortium blockchain to track interactions among participants and dynamically assign trust and reputation scores. Its novelty lies in evaluating both commodity quality and entity trustworthiness based on multiple observations, supporting product-specific reputations, and using smart contracts for automated, transparent score calculation [342]. Another supply-chain-focused solution, DeTRM, tackles data trust by correlating empirical data from adjacent sensor nodes to assess data authenticity before quantifying trustworthiness via smart contracts [343].

The integration of Artificial Intelligence (AI) with blockchain-based DTRM significantly enhances its capabilities, moving from simple rule-based scoring to intelligent, predictive, and adaptive trust assessment. AI models can analyze complex patterns in interaction data stored on the ledger to detect subtle malicious behaviors, predict future node reliability, and dynamically adjust trust metrics. For instance, generative adversarial learning has been proposed for intelligent trust management in 6G networks to optimize security and service quality [344]. Furthermore, frameworks like COBRA address the accuracy-privacy dilemma in trust assessment by encapsulating sensitive agent interactions within machine learning models. These models are then aggregated using a neural network to predict a trust score, preserving privacy while retaining context and demonstrating robustness against attacks like model injection [345]. For large-scale IoT systems, Trust2Vec leverages network embedding algorithms to navigate trust relationships and analyze latent network structures, enabling it to detect and mitigate large-scale collusion attacks (e.g., self-promoting, bad-mouthing) performed by hundreds of malicious devices [346].

Beyond specific frameworks, blockchain-based DTRM principles are being woven into the broader architectural fabric of 6G security. The concept of "Trust-as-a-Service" (TaaS) is proposed as a reputation-based framework for distributed multi-stakeholder environments, aligning with the zero-trust and zero-touch principles essential for 6G [347]. This is particularly relevant for decentralized marketplaces where selecting reliable third-party providers is crucial. The need for decentralized identity management in multi-stakeholder 6G networks also complements DTRM. By using Decentralized Identifiers (DIDs) and Verifiable Credentials, entities can establish and strengthen cross-domain trust relationships without centralized third parties, providing a foundational layer for reputation systems to build upon [348]. In the context of zero-trust architectures for 6G, blockchain can serve as an immutable database for storing and verifying access requests and user activities, enhancing security beyond the perimeter [349]. This integration is extended to Digital Twin (DT)-enabled 6G networks, where a decentralized zero-trust framework uses blockchain for authenticating DTs and communicated data, with AI providing intelligent threat detection across cooperating nodes [350].

Despite its promise, implementing blockchain-based DTRM in 6G faces significant challenges. The performance overhead of consensus mechanisms and on-chain storage must be minimized to meet 6G's ultra-low latency and high-throughput demands. Solutions like reputation-based sharding (e.g., RepChain) aim to improve throughput by leveraging node heterogeneity [351]. Privacy preservation is another critical concern; while the ledger is transparent, the sensitive data used for trust computation must be protected. Hybrid architectures using public blockchains for consensus with private sidechains or off-chain storage for sensitive attributes are a promising direction [340]. Furthermore, designing fair, attack-resistant, and economically sustainable reputation algorithms that cannot be easily gamed remains an open research area, as highlighted by work on intrinsic integrity-driven models [352]. Finally, the governance of these decentralized systems—ensuring they evolve transparently and accountably—is itself a complex challenge that requires careful design [353]. Overcoming these hurdles is essential for realizing DTRM systems that can underpin the secure, efficient, and trustworthy operation of the complex, open, and collaborative 6G network ecosystem.

**Table: Comparison of approaches in 4.6 Decentralized Trust and Reputation Management Systems**

| Method / Framework Name | Core Innovation / Focus | Application Context / Use Case | Reference |
| :--- | :--- | :--- | :--- |
| Blockchain-based DTRM for Resource Sharing | Quantifies reputation scores by evaluating SLA fulfillment and aggregating consumer feedback. | Resource-sharing marketplace in 6G networks. | [143] |
| Decentralized Attribute-Based Access Control with TRS | Integrates a Trust and Reputation System (TRS) into attribute-based access control for dynamic, flexible IoT authorization. | IoT authorization and access control. | [340] |
| Blockchain-based Trust Management for IoT Access Control | Incorporates calculated reputation scores into attribute-based policies for a self-adaptive system. | Decentralized IoT access control. | [341] |
| TrustChain | Uses a consortium blockchain to track interactions and assign dynamic trust/reputation scores, supporting product-specific reputations. | Supply chain management. | [342] |
| DeTRM | Correlates empirical data from adjacent sensor nodes to assess data authenticity before quantifying trustworthiness via smart contracts. | Blockchain-based supply chains. | [343] |
| Generative Adversarial Learning for Trust Management | Uses generative adversarial learning for intelligent trust management to optimize security and service quality. | 6G wireless networks. | [344] |
| COBRA | Encapsulates sensitive agent interactions in ML models, aggregated via a neural network to predict trust scores, preserving privacy and context. | Multi-agent systems (MAS) and IoT for reputation assessment. | [345] |
| Trust2Vec | Leverages network embedding algorithms to analyze latent trust structures and detect large-scale collusion attacks. | Large-scale IoT trust management. | [346] |
| Trust-as-a-Service (TaaS) | A reputation-based trust framework for distributed multi-stakeholder environments, aligning with zero-trust principles. | 5G/6G networks and distributed marketplaces. | [347] |
| Decentralized Identity Management with DIDs | Uses Decentralized Identifiers (DIDs) and Verifiable Credentials for cross-domain trust without centralized third parties. | Multi-stakeholder 6G networks. | [348] |
| Blockchain-based Zero Trust on the Edge | Uses blockchain as an immutable database for storing/verifying access requests and user activities. | Edge/IoT security and smart cities. | [349] |
| Decentralized Zero-Trust Framework for DT-based 6G | Integrates blockchain for authenticating Digital Twins (DTs) and communicated data, with AI for threat detection. | Digital Twin-enabled 6G networks. | [350] |
| RepChain | A reputation-based secure blockchain system using sharding to improve throughput by leveraging node heterogeneity. | General blockchain scalability and performance. | [351] |
| An Intrinsic Integrity-Driven Rating Model | Proposes an economically incentivized, integrity-driven reputation model for sustainable systems. | General reputation systems and oracles. | [352] |
| Defining Blockchain Governance Principles | Presents a comprehensive framework for blockchain governance, covering decentralization, incentives, accountability, etc. | Blockchain governance. | [353] |


## 5 Synergistic Integration: Blockchain-Empowered AI and AI-Enhanced Blockchain

This core section delves into the bidirectional synergy. It examines how Blockchain provides a decentralized, secure, and incentivized platform for AI operations, focusing on trustworthy Federated Learning (BlockFL), verifiable AI model marketplaces, and data provenance for training. Conversely, it explores how AI optimizes Blockchain performance, including AI-driven consensus mechanisms, intelligent sharding and resource management, and smart contract security analysis.

### 5.1 Blockchain as a Decentralized Trust Engine for AI Operations

The distributed and heterogeneous nature of 6G networks, encompassing massive IoT, edge intelligence, and semantic communications, necessitates a paradigm shift in how artificial intelligence (AI) operations are orchestrated and trusted. Centralized AI models, reliant on monolithic data silos and single points of control, present critical vulnerabilities including data privacy breaches, opaque decision-making, and susceptibility to systemic failure or manipulation. Blockchain technology emerges as a foundational decentralized trust engine, providing the immutable, transparent, and automated coordination layer required for secure and collaborative AI in the 6G era. Its core value proposition lies in establishing a verifiable and tamper-resistant record of the entire AI lifecycle, from data provenance and model training to inference execution and governance, thereby mitigating risks associated with central authority and fostering trust among mutually untrusted participants.

At the heart of this trust engine is the immutable ledger, which serves as a single source of truth for AI asset provenance. In collaborative environments, understanding the lineage of a machine learning model—its training data sources, the sequence of algorithms applied, and the contributors involved—is paramount for assessing its quality, fairness, and security. Systems like ProML explicitly leverage blockchain and smart contracts to empower distributed ML teams to jointly manage a single, tamper-proof source of truth about circulated ML assets' provenance [354]. This approach mitigates insider threats by eliminating reliance on a vulnerable central third party. Similarly, for AI-generated content (AIGC) and large language models (LLMs), blockchain can register datasets, licenses, and model checkpoints, creating an auditable trail that addresses copyright compliance and tracks iterative retraining processes [355]. This immutable logging extends to data workflows in smart manufacturing, where frameworks like SmartQC use distributed ledgers to provide data integrity and automate trust services within complex supply chains [356]. By anchoring AI operations to an immutable chain of evidence, blockchain provides the transparency needed for accountability and auditability, which are essential for high-stakes applications in healthcare, autonomous systems, and critical infrastructure.

Smart contracts are the executable component of this trust engine, automating and enforcing the rules of collaboration without intermediaries. They transform static ledgers into dynamic, programmable coordination platforms for distributed AI workflows. In federated learning (FL), smart contracts can orchestrate the entire training process: they can register participants, stipulate contribution rules, aggregate model updates via verified mechanisms, and—crucially—automate incentive distribution based on proven contribution quality. This is exemplified by designs that implement proof-of-contribution-based reward allocation, where smart contracts ensure project owners cannot evade payment and honest trainers are compensated fairly based on verifiable assessments of their input [357]. Platforms like BlockFLow further utilize Ethereum smart contracts to incentivize good behavior and penalize malicious actors in a fully decentralized, privacy-preserving FL system [358]. Beyond FL, smart contracts can encode service-level agreements for AI inference. The BRAIN platform, for instance, uses a two-phase smart contract mechanism where an inference committee commits and reveals results, with the smart contract executing the requested operation only upon consensus, thereby ensuring reliable and verifiable inference for large-scale models [359]. This automation extends to business contexts; languages like Daml are designed to capture the legal rules of multi-party workflows, with built-in authorization policies that enable secure composition and execution of complex business logic on-ledger [360].

This decentralized architecture fundamentally mitigates the risks of single points of failure and central authority manipulation that plague traditional AI systems. By distributing control across a network of nodes governed by consensus, no single entity can unilaterally alter the AI model's history, manipulate training data logs, or skew incentive distributions. This is particularly vital for decentralized autonomous organizations (DAOs) governing AI projects, where blockchain-based voting mechanisms, despite current challenges with power concentration, aim to democratize decision-making on protocol upgrades and resource allocation [361]. The decentralization also enhances resilience against attacks. A compromised central server in a conventional FL system could poison the global model or leak sensitive gradient information. In contrast, a blockchain-based FL system distributes the orchestration logic across the network. While not a panacea—as the consensus layer itself must be secured—it removes the singular, high-value target. Furthermore, integrating zero-knowledge proofs (ZKPs) with these smart contracts can enhance privacy by allowing participants to prove the correctness of their computations (e.g., a valid model update) without revealing the underlying private data, thus achieving a balance between verifiable trust and data confidentiality.

However, employing blockchain as a trust engine for AI is not without significant challenges that must be addressed for 6G integration. The deterministic nature of smart contracts, while ensuring consistency, clashes with the stochastic and often non-deterministic outputs of AI models, creating an "oracle problem" for feeding reliable off-chain data into on-chain logic [362]. Solutions like decentralized oracle networks with adaptive consensus algorithms are being developed to bridge this gap. Scalability and latency are paramount concerns for real-time 6G applications; the computational overhead of consensus and on-chain verification must be minimized through layer-2 solutions, efficient smart contract design, and hybrid architectures where only critical trust anchors are stored on-chain. Finally, the security of the trust engine itself is critical. Vulnerabilities in smart contract code, as highlighted by numerous studies on automated vulnerability detection and fixing, can lead to catastrophic financial and operational losses, undermining the very trust the system is meant to provide [363] [364]. Therefore, the development of formally verifiable smart contract languages and robust security auditing frameworks is a prerequisite for dependable AI operations.

In conclusion, blockchain technology provides an indispensable decentralized trust layer for AI in 6G networks. By offering immutable provenance tracking, automating complex, multi-party collaborations through smart contracts, and eliminating centralized chokepoints, it establishes the foundational trust required for scalable, secure, and transparent distributed intelligence. As 6G envisions a hyper-connected fabric of intelligent devices and services, the synergistic integration of blockchain's trust mechanisms with AI's cognitive capabilities will be crucial for realizing a resilient, accountable, and user-centric intelligent digital ecosystem.

**Table: Comparison of approaches in 5.1 Blockchain as a Decentralized Trust Engine for AI Operations**

| Method/Model Name | Key Idea/Approach | Application Context | Reference |
| :--- | :--- | :--- | :--- |
| ProML | Leverages blockchain and smart contracts to empower distributed ML teams to jointly manage a single, tamper-proof source of truth about ML assets' provenance. | Provenance management for machine learning software systems in distributed, untrusted environments. | [354] |
| Proof-of-Contribution-Based Design | Implements proof-of-contribution-based reward allocation via smart contracts to ensure fair compensation for trainers based on verifiable assessments of their input in collaborative ML. | Decentralized and collaborative machine learning/federated learning marketplaces. | [357] |
| BlockFLow | Utilizes Ethereum smart contracts to incentivize good behavior and penalize malicious actors in a fully decentralized, privacy-preserving federated learning system. | Accountable and privacy-preserving federated learning. | [358] |
| BRAIN | Uses a two-phase smart contract mechanism where an inference committee commits and reveals results, executing the operation only upon consensus for reliable inference of large-scale models. | Reliable inference and training of large-scale AI models. | [359] |
| Daml | A smart contract language designed to capture the legal rules of multi-party workflows with built-in authorization policies for secure composition and execution of complex business logic. | Securely automating real-world multi-party business workflows. | [360] |
| SmartQC | An extensible DLT-based framework that uses immutable ledgers for data integrity and smart contracts to automate trust services within complex data workflows. | Trusted data workflows in smart manufacturing and supply chains. | [356] |
| ACon² | Proposes an adaptive conformal consensus algorithm for decentralized oracle networks to provide provably correct off-chain data to smart contracts under distribution shift and Byzantine adversaries. | Solving the blockchain oracle problem for reliable data feeds in smart contracts. | [362] |
| SmartScan | An approach combining static and dynamic analysis to detect Denial of Service vulnerabilities (specifically unexpected revert) in Ethereum smart contracts. | Automated vulnerability detection in Ethereum smart contracts. | [363] |
| IBis | A blockchain-based framework with on-chain registries for datasets, licenses, and models to track provenance and ensure copyright compliance in AI model training workflows. | Copyright, provenance, and lineage tracking for AI-generated content and large language models. | [355] |


### 5.2 Trustworthy and Accountable Federated Learning (BlockFL)

The integration of blockchain with Federated Learning (FL) has emerged as a foundational paradigm, termed Blockchained Federated Learning (BlockFL or BCFL), to construct trustworthy, accountable, and decentralized training ecosystems. This synergy directly addresses the critical vulnerabilities of the traditional FL architecture, which relies on a central aggregator server. This centralization introduces a single point of failure, risks of model tampering, and a lack of transparency in the aggregation process and incentive distribution. By leveraging blockchain's inherent properties of decentralization, immutability, and consensus, BlockFL frameworks aim to create secure, auditable, and self-organizing collaborative intelligence networks suitable for 6G's distributed edge environments.

A primary architectural innovation in BlockFL is the replacement of the central server with a blockchain network, where smart contracts autonomously orchestrate the FL workflow. Frameworks like [365] and [366] exemplify this approach. Smart contracts define and enforce the rules for client registration, task publication, model update submission, and most importantly, the aggregation logic. This transforms the aggregation process from a black-box operation on a single server into a transparent, verifiable procedure recorded on an immutable ledger. The decentralized nature of this architecture inherently mitigates single-point-of-failure risks and deters malicious behavior from any single entity, as consensus among nodes is required to record each training round.

To ensure the integrity of the learning process against Byzantine clients—those who may submit poisoned or low-quality model updates—BlockFL systems incorporate sophisticated, blockchain-enabled robust aggregation and validation mechanisms. Simply decentralizing the aggregation is insufficient; the system must actively defend against malicious participants. Proposals such as [367] and [368] introduce peer-to-peer review and validation schemes. In these systems, a subset of participants acts as validators, checking the legitimacy of submitted model updates against a held-out validation dataset or through consensus metrics before they are approved for aggregation. Malicious updates are slashed, and the submitting client's reputation or stake is penalized. Conversely, [358] and [369] design mechanisms to fairly quantify and reward honest contributions, creating a self-reinforcing economic incentive for reliable participation. This combination of cryptographic verification, economic game theory, and decentralized consensus forms a robust defense against data poisoning and other adversarial attacks.

Beyond security, blockchain provides an elegant solution for decentralized model storage, versioning, and intellectual property (IP) protection. Instead of a central server holding the sole canonical version of the global model, each aggregated model can be stored as a transaction or within a block, creating a tamper-proof lineage of the model's evolution. This enables full auditability of the training process. Frameworks like [366] extend this concept by integrating model watermarking with blockchain to authenticate model ownership and provenance. Furthermore, the use of decentralized storage systems like the InterPlanetary File System (IPFS) in conjunction with blockchain, as seen in [365], addresses the storage overhead of large models while maintaining content-addressable, verifiable links on-chain.

However, the decentralization offered by blockchain introduces significant challenges, primarily concerning training efficiency, scalability, and consistency. A key issue is the problem of model staleness and ledger inconsistencies, thoroughly analyzed in [370] and [371]. In an asynchronous, consensus-driven blockchain, different clients may be training based on slightly different historical versions of the global model (due to blockchain forks or propagation delays). This breaks the synchronous round assumption of classic FL like FedAvg and can lead to training instability, slower convergence, and significant accuracy degradation—simulations show potential decreases of up to ~35%. Additionally, the act of recording every model update on-chain generates immense communication and storage overhead, creating a scalability bottleneck.

The research community has proposed several architectural and algorithmic innovations to navigate these trade-offs. To enhance scalability, sharding is a prominent solution. [372] and [62] propose partitioning the blockchain network into smaller shards, each managing a subset of clients or model parameters. This parallelizes consensus and validation, linearly improving transaction throughput. For communication efficiency, gradient compression techniques are vital. [373] demonstrates that compressing model updates before broadcasting can reduce communication traffic by 95-98% without compromising final accuracy. To address the inefficiencies of traditional Proof-of-Work (PoW) consensus, lightweight alternatives are essential for resource-constrained edge devices. [374] and frameworks utilizing Proof-of-Stake (PoS) or Practical Byzantine Fault Tolerance (PBFT) variants, such as [52], significantly reduce the computational and latency overhead of consensus, making on-device BlockFL feasible.

Privacy remains a paramount concern, even in BlockFL, as the blockchain's transparency can conflict with the need to protect model updates. Advanced cryptographic techniques are integrated to resolve this. [375] and [53] employ zero-knowledge proofs (ZKPs). These allow an aggregator (or smart contract) to prove the correctness of the aggregation computation without revealing the individual client inputs, thereby ensuring verifiability alongside privacy. Similarly, the use of local differential privacy, as in [358], adds calibrated noise to model updates before they are submitted, providing a rigorous privacy guarantee against inference attacks while still allowing for useful aggregation.

In conclusion, BlockFL represents a transformative architectural shift for building trustworthy AI in 6G networks. It replaces fragile, centralized trust with verifiable, decentralized protocols powered by blockchain and smart contracts. While successfully addressing core issues of security, accountability, and incentive alignment, it necessitates careful design to manage the inherent tensions between decentralization and efficiency. Future evolution will likely involve deeper co-design of lightweight, application-specific consensus mechanisms, advanced privacy-preserving cryptography like ZKPs and fully homomorphic encryption, and AI-driven optimization of the blockchain parameters themselves to dynamically adapt to network conditions and learning objectives, ultimately realizing robust and scalable collaborative intelligence at the edge.

**Table: Comparison of approaches in 5.2 Trustworthy and Accountable Federated Learning (BlockFL)**

| Method / Framework Name | Key Contribution / Focus | Reference |
| :--- | :--- | :--- |
| VeryFL | A blockchain-embedded FL framework for verifiable training, aggregation, and incentive distribution; includes model ownership authentication via blockchain and watermarking. | [366] |
| FLock | A decentralized FL system with a P2P review and reward/slash mechanism powered by smart contracts to detect and deter malicious clients. | [367] |
| VBFL (Robust Blockchained FL) | A blockchain-based FL framework with a decentralized validation mechanism for local models and a dedicated Proof-of-Stake consensus to protect legitimate updates. | [368] |
| BlockFLow | An accountable and privacy-preserving decentralized FL system using differential privacy, a novel auditing mechanism, and Ethereum smart contracts for incentives. | [358] |
| FAIR-BFL | A flexible BFL framework with modular design to dynamically adjust capabilities and a mechanism to quantify client contributions for fair incentive distribution. | [369] |
| ScaleSFL | A scalable BFL solution using sharding to separate off-chain FL components, improving validation performance linearly. | [372] |
| ChainFL | A two-layer blockchain-driven FL system using sharding in a subchain layer and a DAG-based mainchain for parallel, asynchronous cross-shard validation. | [62] |
| DAG-FL | An on-device FL framework using a Direct Acyclic Graph (DAG)-based blockchain to address device asynchrony and anomaly detection with low resource consumption. | [374] |
| BCFL (Fast BFL) | A fast BFL framework using gradient compression to reduce communication traffic by 95-98%, optimizing compression rate and block generation rate. | [373] |
| zkFL | A FL framework using zero-knowledge proofs (ZKPs) to allow an aggregator to prove the correctness of aggregation without revealing individual client inputs. | [375] |
| zkDFL | An efficient and privacy-preserving decentralized FL framework using ZKPs to allow a server to prove correct aggregation to clients via smart contracts. | [53] |


### 5.3 Verifiable AI Marketplaces and Provenance Management

The emergence of Machine Learning as a Service (MLaaS) and the growing value of high-quality datasets have created a demand for robust marketplaces where AI assets—models and data—can be traded, shared, and collaboratively developed. However, traditional centralized platforms face significant challenges, including lack of transparency in transactions, difficulties in proving ownership and contributions, and risks of intellectual property theft or misuse. Blockchain technology, with its inherent properties of decentralization, immutability, and transparency, provides a foundational architecture for building verifiable AI marketplaces and comprehensive provenance management systems, which are critical for fostering trust in multi-stakeholder 6G ecosystems.

A core function of these blockchain-empowered platforms is to establish indisputable proof of ownership and creation for AI models. Techniques like model watermarking can be integrated with blockchain to create a permanent, tamper-proof record of a model's origin. As explored in [376], such a platform can register a model's unique fingerprint (watermark) on-chain, allowing any party to verify its legitimate owner against the immutable ledger. This combats unauthorized use and model theft. Similarly, for datasets, platforms like [377] address intellectual property risks during data valuation by sanitizing datasets before sharing, limiting information transfer while still allowing accurate utility assessment, with blockchain potentially recording the licensing terms and access conditions.

Beyond simple ownership, modern AI development is often collaborative, involving multiple parties contributing data or compute resources. Fairly incentivizing such collaboration requires transparent mechanisms to evaluate and reward each participant's contribution. This is where concepts like Proof-of-Contribution and data valuation metrics come into play. The [357] proposes a marketplace that uses verifiable computations and zero-knowledge proofs to assess each trainer's contribution to the final model, ensuring rewards are allocated fairly and algorithmically via smart contracts. Another prominent method is the use of Shapley values from cooperative game theory to quantify data contributions. Frameworks like [378] and [379] utilize Data Shapley Values (DSV) to estimate the marginal value of each data owner's dataset to the trained model's performance. By executing these valuation algorithms within or anchored to a blockchain environment, the process becomes transparent and auditable, preventing a central broker from manipulating contributions. [380] specifically addresses this by proposing a blockchain-based FL framework that transparently evaluates contributions based on model updates, moving away from the assumption of a semi-trusted central server.

The architectural realization of these concepts leads to the creation of full-stack, decentralized AI marketplaces. [381] presents a marketplace that enforces a fair model-money swap, using a blockchain-empowered benchmarking process with trusted execution environments (TEEs) to transparently determine model prices based on authentic performance. [382] implements a secure data trading marketplace as a smart contract, ensuring model and data security against curious parties and providing resilience against malicious actors who may submit faulty data or evade payment. [383] envisions a blockchain-based marketplace where users can upload datasets, request model training, or query models, with nodes in the network providing computational resources, thereby democratizing access to AI resources. These platforms often leverage smart contracts to automate the entire workflow—from listing assets and escrowing payments to executing verification logic and distributing rewards—ensuring trustless and automated operations as seen in [384, 384].

Parallel to marketplaces for trading, managing the end-to-end provenance of ML assets is vital for auditability, reproducibility, and compliance, especially in regulated industries like healthcare and finance. Provenance tracking involves recording the complete lineage of an asset: its origin, all transformations, training cycles, contributors, and usage history. Blockchain serves as a decentralized ledger for this provenance data. [354] introduces a platform that allows distributed ML teams to jointly manage a single source of truth about ML assets' provenance using blockchain and smart contracts, mitigating insider threats. [385] designs a graph-based provenance model for AI assets within a value chain and implements it as a smart contract on a permissionless blockchain to solve challenges of trust, privacy, and fair remuneration. In scientific and high-performance computing contexts, [290] leverages blockchain to deliver immutable and autonomous data provenance services, ensuring the fidelity of scientific data lineage. For deployed systems, [386] proposes using verifiable credentials and a blockchain-recorded bill of materials (BOM) for models, creating a traceable supply chain that allows practitioners to scrutinize the qualities of all components used in an AI system.

The integration of these verifiable marketplaces and provenance systems within 6G networks is particularly potent. The ultra-reliable low-latency communication (URLLC) and massive connectivity of 6G can support the real-time, high-throughput data exchanges required for on-chain verification and micro-transactions in these marketplaces. Edge computing nodes in the 6G infrastructure can host lightweight blockchain clients or perform trusted model inference, bringing marketplace and verification functions closer to end-users and IoT devices. Furthermore, the synergy enhances security for 6G-native applications; for instance, a blockchain-based provenance system can track the lineage of AI models used for network slicing optimization or intrusion detection, ensuring they are trained on verified, unbiased data. As AI becomes more pervasive in managing 6G resources, having a transparent, auditable record of model development and data usage becomes not just beneficial but essential for operational integrity and regulatory compliance.

**Table: Comparison of approaches in 5.3 Verifiable AI Marketplaces and Provenance Management**

| Method / Model / Platform Name | Primary Purpose / Core Function | Key Techniques / Mechanisms | Reference |
| :--- | :--- | :--- | :--- |
| Tokenized Model | Decentralized model ownership verification and copyright protection | Model watermarking integrated with blockchain for immutable ownership records | [376] |
| IPProtect | Protecting intellectual property of visual datasets during data valuation | Dataset sanitization to limit information transfer while allowing utility assessment | [377] |
| Proof-of-Contribution-Based Design for Collaborative Machine Learning | Fair incentive allocation in collaborative/federated learning | Verifiable computations, zero-knowledge proofs for contribution assessment, smart contracts for rewards | [357] |
| Dealer | End-to-end data marketplace with model-based pricing | Data Shapley Values (DSV) for data valuation, pricing based on model privacy parameters | [378] |
| A Marketplace for Trading AI Models based on Blockchain and Incentives for IoT Data | Trading AI models and incentivizing IoT data contributions | Distributed Data Shapley Value (DSV) for data valuation, Distributed Ledger Technology (DLT) | [379] |
| Transparent Contribution Evaluation for Secure Federated Learning on Blockchain | Transparent contribution evaluation in federated learning | Blockchain-based framework evaluating contributions based on model updates | [380] |
| Golden Grain | Secure and decentralized model marketplace for MLaaS | Blockchain-empowered benchmarking with TEEs for transparent pricing, fair model-money swap | [381] |
| OmniLytics | Secure data market for decentralized machine learning | Smart contract-based marketplace, secure model splitting and aggregation, resilience to malicious actors | [382] |
| PredictChain | Decentralized marketplace for predictive machine learning models | Blockchain network for uploading data, requesting training, and querying models, nodes provide computation | [383] |
| Trustless Machine Learning Contracts | Trustless evaluation and exchange of ML models on blockchain | Smart contracts for automatic model validation and reward distribution | [384, 384] |
| ProML | Decentralized provenance management for ML software systems | Artefact-as-a-State-Machine architecture, blockchain and smart contracts for ML provenance | [354] |
| Distributed Ledger for Provenance Tracking of Artificial Intelligence Assets | Provenance tracking of AI assets in a value chain | Graph-based provenance model, smart contract implementation on a permissionless blockchain | [385] |
| SciChain | Trustworthy scientific data provenance for HPC | Proof-of-Scalable-Traceability (POST) protocol, blockchain for immutable data provenance | [290] |
| Providing Assurance and Scrutability on Shared Data and Machine Learning Models with Verifiable Credentials | Assurance and scrutability for shared data and ML models | Verifiable credentials, blockchain-recorded Bill of Materials (BOM) for model supply chain | [386] |


### 5.4 Privacy-Preserving Decentralized AI with Advanced Cryptography

The convergence of blockchain and artificial intelligence (AI) for 6G networks necessitates robust privacy safeguards, as decentralized data sharing and collaborative model training inherently risk exposing sensitive information. Advanced cryptographic techniques, when integrated with blockchain's immutable ledger and smart contract automation, create powerful frameworks for privacy-preserving decentralized AI. These frameworks primarily leverage Zero-Knowledge Proofs (ZKPs), homomorphic encryption, and differential privacy to protect data at rest, in transit, and during computation, thereby enabling trustworthy AI operations across distributed 6G environments like federated learning (FL) at the edge.

Zero-Knowledge Proofs have emerged as a cornerstone technology for verifiable computation without disclosure. In blockchain-based AI systems, ZKPs allow participants to prove the correctness of their computations—such as local model training in FL or data preprocessing—without revealing the underlying private data or model parameters. For instance, a Zero-Knowledge Proof-based Practical Federated Learning (ZKP-FL) scheme on blockchain enables the verification of local computation and secure aggregation processes, ensuring participants have correctly executed the learning protocol without accessing their plaintext data [72]. This capability is crucial for establishing trust in decentralized AI, where malicious or lazy participants might submit incorrect updates. Beyond FL, ZKPs are instrumental in proving broader properties about AI models and data. The concept of Zero-Knowledge Machine Learning (ZKML) allows model owners to cryptographically prove that a model's output was generated by a specific, unaltered model meeting certain performance criteria, all while keeping the model weights private [387]. This is vital for auditing generative AI in sensitive 6G applications like healthcare or legal services without exposing proprietary models. Similarly, ZKPs can be used for trustless audits, where a model provider commits to a dataset and model, and later proves compliance with copyright rules or data provenance requirements via a ZKP, without ever revealing the raw data or model [388]. The efficiency of these systems is being continuously improved; for example, aggregated ZKP mechanisms within Merkle Tree structures can drastically reduce proof size and verification overhead on blockchains like Ethereum, making frequent, lightweight verification feasible for 6G's low-latency use cases [325].

Homomorphic encryption (HE) complements ZKPs by enabling direct computation on encrypted data. In a decentralized AI context, HE allows clients in an FL system to encrypt their local model updates before sending them to an aggregator. The aggregator, which could be a smart contract or a designated node, can then perform the aggregation operation (e.g., summation or averaging) directly on the ciphertexts, producing an encrypted global model. Only the final result, or a derived version of it, is decrypted. This ensures that the aggregator and any eavesdroppers on the blockchain learn nothing about any individual participant's contribution. Frameworks like AerisAI utilize homomorphic encryption for secure parameter aggregation in a decentralized collaborative AI setting, removing the need for a trusted central server [389]. HE is also pivotal in secure multi-party computation (MPC) protocols for distributed ML, where parties jointly compute a function over their private inputs. A framework for distributed, secure machine learning combines homomorphic addition for a two-step training protocol with ZKPs for data validity, enabling privacy-preserving collaboration among untrusted individuals [390]. However, the computational intensity of fully homomorphic encryption remains a challenge for resource-constrained edge devices in 6G. Hybrid approaches, such as combining HE with differential privacy or performing only critical operations in the encrypted domain, are often employed to balance privacy and practicality.

Differential privacy (DP) provides a statistical guarantee of privacy by injecting calibrated noise into data or computations, making it difficult to infer whether any specific individual's data was part of the dataset. Within blockchain-based FL, DP is applied at the client level (local DP) or during aggregation. Clients can add noise to their model updates before submitting them, ensuring that even if the update is intercepted or the global model is reverse-engineered, their raw data cannot be reliably reconstructed. This is essential for protecting against membership inference and model inversion attacks. A Privacy Protected Blockchain-based Federated Learning Model (PPBFL) incorporates an adaptive differential privacy algorithm applied to both local and global models. It introduces a novel method of adding "reverse noise" to the global model to achieve a zero-bias estimate, countering the cumulative privacy loss from multiple local contributions and enhancing security against inference attacks [391]. The integration of DP with blockchain also addresses auditability; the parameters of the DP mechanism (like the privacy budget ε) can be recorded immutably on-chain, providing transparent and verifiable proof that privacy-preserving practices were followed. Furthermore, attribute-based differential privacy can be integrated for fine-grained control, as seen in AerisAI, where different privacy levels are applied based on service-level agreements or data sensitivity [389].

The synergistic application of these cryptographic primitives within a blockchain-managed framework creates a powerful paradigm for 6G. Smart contracts orchestrate the workflow—enforcing participation rules, collecting encrypted or noise-infused updates, triggering ZKP verification, and distributing incentives—all on an immutable ledger. For example, a zkDFL scheme utilizes blockchain smart contracts to manage the aggregation algorithm, while a server uses ZKPs to prove to clients that the aggregation was performed correctly and that all inputs were used, thereby ensuring verifiability alongside privacy [53]. This combination tackles the dual challenges of integrity and confidentiality. In supply chain AI for 6G-enabled IoT, a framework like PrivChain uses Zero-Knowledge Range Proofs (ZKRPs) to allow entities to prove a product's origin lies within a certain geographical region or meets a quality threshold without disclosing the exact, sensitive location or proprietary process data [289]. For identity and access management in decentralized AI services, protocols like zkFaith or ZKBID leverage ZKPs to allow users to prove they possess required credentials (e.g., a valid certification to contribute medical data to an FL task) without revealing their full identity, enabling Sybil-resistant and privacy-preserving authentication [392] [282].

Despite significant progress, challenges remain for deploying these cryptographic-heavy solutions in 6G networks. The computational and communication overhead of generating ZKPs, especially for complex deep learning models, can be substantial, though ongoing research into more efficient proof systems (like zk-SNARKs and zk-STARKs) and hardware acceleration is mitigating this. The integration of multiple techniques (ZKP, HE, DP) also increases system complexity. Furthermore, while these techniques protect data privacy, they must be carefully designed to avoid functionality-inherent leakage—where the output of the computation itself reveals information about the inputs, a concern highlighted by research into automatically quantifying such leakage using model counting [393]. For 6G, which promises ultra-reliable low-latency communication (URLLC) and massive machine-type communication (mMTC), future work must focus on lightweight cryptographic protocols, cross-layer optimization, and standardized frameworks that allow developers to implement privacy-preserving decentralized AI without deep expertise in cryptography, as envisioned by projects like Fact Fortress [80]. Ultimately, the fusion of blockchain with advanced cryptography is not merely an enhancement but a foundational requirement for realizing secure, private, and trustworthy decentralized intelligence across the pervasive and hyper-connected fabric of 6G wireless ecosystems.

**Table: Comparison of approaches in 5.4 Privacy-Preserving Decentralized AI with Advanced Cryptography**

| Technique / Framework | Primary Cryptographic Method(s) | Key Purpose / Contribution | Application Context / Use Case | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Zero-Knowledge Proof-based Practical Federated Learning (ZKP-FL) | Zero-Knowledge Proofs (ZKPs) | Verifies local computation and secure aggregation processes without accessing plaintext data. | Federated Learning (FL) on blockchain for collaborative learning. | [72] |
| Zero-Knowledge Machine Learning (ZKML) / snarkGPT | Zero-Knowledge Proofs (ZKPs) | Allows model owners to cryptographically prove a model's output was generated by a specific, unaltered model meeting performance criteria, keeping model weights private. | Auditing generative AI in sensitive applications (e.g., healthcare, legal services). | [387] |
| Trustless Audits (ZkAudit) | Zero-Knowledge Proofs (ZKPs) | Enables trustless audits where a model provider commits to a dataset and model, and later proves compliance (e.g., with copyright rules) via a ZKP without revealing raw data or model. | Auditing model training data for copyright, censorship, etc. | [388] |
| Aggregated ZKP Mechanisms | Aggregated Zero-Knowledge Proofs | Reduces proof size and verification overhead within Merkle Tree structures on blockchains like Ethereum. | General blockchain data verification for low-latency 6G use cases. | [325] |
| AerisAI | Homomorphic Encryption (HE), Attribute-based Differential Privacy | Provides secure parameter aggregation in decentralized collaborative AI, removing the need for a trusted central server, with fine-grained privacy control. | Decentralized collaborative AI / Federated Learning. | [389] |
| Distributed and Secure ML Framework | Homomorphic Encryption (HE), Zero-Knowledge Proofs (ZKPs) | Combines homomorphic addition for a two-step training protocol with ZKPs for data validity, enabling privacy-preserving collaboration among untrusted parties. | Distributed, secure machine learning (e.g., LDA, Naive Bayes). | [390] |
| Privacy Protected Blockchain-based Federated Learning Model (PPBFL) | Adaptive Differential Privacy (DP) | Incorporates an adaptive DP algorithm applied to local and global models, adding "reverse noise" to achieve a zero-bias estimate and counter cumulative privacy loss. | Blockchain-based Federated Learning. | [391] |
| zkDFL | Zero-Knowledge Proofs (ZKPs) | Uses ZKPs to allow a server to prove to clients that aggregation was performed correctly and that all inputs were used, managed via blockchain smart contracts. | Decentralized Federated Learning (DFL) with blockchain. | [53] |
| PrivChain | Zero-Knowledge Range Proofs (ZKRPs) | Allows entities to prove a product's origin lies within a certain geographical region or meets a quality threshold without disclosing exact, sensitive data. | Supply chain provenance and privacy (e.g., 6G-enabled IoT). | [289] |
| zkFaith / ZKBID | Zero-Knowledge Proofs (ZKPs) | Allows users to prove they possess required credentials (e.g., for contributing medical data) without revealing their full identity, enabling Sybil-resistant authentication. | Decentralized Identity and Access Management for AI services. | [392], [282] |
| McFIL | Model Counting (for quantifying leakage) | Algorithmically quantifies functionality-inherent leakage in secure protocols (e.g., MPC, FHE, ZKP) to assess privacy compromise. | Analyzing leakage in privacy-preserving computations. | [393] |
| Fact Fortress (Deploying ZKP Frameworks) | Zero-Knowledge Proofs (ZKPs), Data Provenance Proofs | An end-to-end framework for designing/deploying ZKPs of general statements, providing high-level abstractions for developers. | Standardized, developer-friendly ZKP deployment for 6G. | [80] |


### 5.5 AI for Optimizing Blockchain Performance and Security

The intrinsic challenges of blockchain systems—namely, scalability bottlenecks, energy-intensive consensus, and evolving security threats—present significant hurdles for their integration into high-performance, low-latency 6G networks. Artificial Intelligence, with its capabilities in pattern recognition, adaptive optimization, and predictive analytics, offers a powerful toolkit to enhance blockchain performance and fortify its security posture directly. This involves re-engineering core blockchain components, from consensus and sharding to transaction validation and threat monitoring, using AI-driven methodologies.

A primary application is the design of **AI-enhanced consensus mechanisms** that move beyond static cryptographic puzzles. Traditional Proof-of-Work (PoW) is notoriously wasteful, while Proof-of-Stake (PoS) can lead to centralization. AI introduces dynamic, utility-driven alternatives. For instance, consensus can be framed as a reinforcement learning (RL) problem where agents learn optimal block verification strategies, effectively using the blockchain's growth as a Markov decision process to preserve transaction order while utilizing computational resources for meaningful parallel neural network training [57]. More directly, the concept of **Proof-of-Useful-Work (PoUW)** seeks to repurpose mining energy towards socially valuable computations, such as optimizing machine learning models. Protocols have been proposed where miners compete to improve ML models on provided datasets, with a committee overseeing the competition, thereby linking blockchain security directly to productive AI training [56]. Similarly, **Proof-of-Training (PoT)** explicitly harnesses crypto-mining infrastructure for distributed AI training, synchronizing global states via Byzantine fault tolerance consensus to create a robust decentralized training network [394]. Other approaches integrate AI to make consensus more adaptive and fair. The **AICons** algorithm utilizes local ML models from all participating nodes to generate a global model for selecting consensus winners, significantly reducing energy waste. It further employs a Shapley value-based utility function to evaluate and reward node contributions based on model accuracy, energy use, and bandwidth, promoting fairness and scalability [58]. For leader-based protocols, machine learning can optimize the election process. In smart city applications, ML algorithms are deployed for efficient and honest leader election, ensuring transaction prioritization for critical events, coupled with peer-prediction mechanisms for block verification [395]. Multi-agent reinforcement learning (MRL) has also been applied to PoS, creating systems like **MRL-PoS** where agents dynamically adapt to user behavior, applying rewards and penalties to eliminate malicious nodes and learn new adversarial tactics in real-time [396].

To address scalability, AI plays a crucial role in optimizing **sharding and resource management**. Sharding partitions the blockchain network into smaller, parallel-processing groups (shards) but introduces risks like single-shard takeovers. AI can intelligently manage node assignment and shard formation to balance load and enhance security. Deep Reinforcement Learning (DRL) is particularly suited for this dynamic, multi-dimensional optimization. The **TbDd** framework uses DRL to dynamically adjust node allocation across shards, aiming to maximize throughput while maintaining security. It incorporates a comprehensive trust evaluation mechanism to identify node types (honest/dishonest) and performs targeted resharding to mitigate collusion risks, effectively balancing shard risk and reducing cross-shard transactions [397]. Beyond node assignment, AI can optimize overall network performance metrics. Generative AI, specifically generative diffusion models, has been shown to optimize blockchain network parameters, converging faster and achieving higher rewards than traditional AI approaches, leading to significant improvements in throughput and latency [398]. This intelligent orchestration is vital for blockchain to handle the Visa-level transaction throughput required for 6G-enabled massive IoT and smart city applications.

Perhaps the most critical application of AI is in **proactive security and anomaly detection**. The immutable and transparent nature of blockchain does not inherently prevent malicious transactions, smart contract vulnerabilities, or network-level attacks like majority (51%) attacks. Machine learning models, trained on historical transaction data and network behavior, can identify subtle, anomalous patterns indicative of fraud or intrusion. Supervised learning and algorithmic game theory can be combined to monitor stakeholder activity in consortium blockchains, detecting anomalies such as collusion that could lead to majority attacks [399]. For general threat detection, deep learning models like Self-Organized Stacked Networks (SOSN) can be used within a two-way intrusion detection system. Such systems first authenticate nodes and evaluate their trust using hierarchical weighted fuzzy algorithms, then verify transactions using the deep learning model to flag malicious activities [400]. Graph Neural Networks (GNNs) offer another powerful approach by analyzing the blockchain interaction graph. Frameworks like **Ethident** use hierarchical graph attention encoders to characterize account-level features and subgraph-level behavior patterns, effectively de-anonymizing accounts and identifying malicious actors such as phishing scammers or hackers by their behavioral fingerprints [401]. Furthermore, collaborative learning frameworks can be designed to detect attacks in both transactions and smart contracts by transforming transaction features into visual representations for analysis, enabling real-time detection of complex, low-level machine code injections at distributed nodes [402]. For smart contract security specifically, AI can assist in both auditing and testing. While tools for detecting smart contract vulnerabilities are often considered immature, AI can power automated test-case generation. Tools like **AGSOLT** employ search algorithms, including genetic algorithms, to automatically generate high-coverage test suites for Solidity smart contracts, uncovering errors in real-world contracts [403]. In the context of federated learning on blockchain, AI is also needed to defend the AI models themselves from poisoning attacks, creating a virtuous cycle where blockchain secures AI, and AI secures the blockchain infrastructure [52].

In conclusion, the application of AI to optimize blockchain performance and security transforms it from a relatively rigid, protocol-driven infrastructure into an intelligent, adaptive, and self-securing network layer. By introducing learning-based consensus, intelligent resource management, and proactive, ML-driven security monitoring, AI directly addresses the trilemma of decentralization, security, and scalability. This internal enhancement is a prerequisite for blockchain to function as a robust, efficient, and trustworthy foundational service for the diverse and demanding applications envisioned for 6G wireless ecosystems, from decentralized AI marketplaces and smart healthcare to autonomous vehicle coordination and real-time IoT data markets.

**Table: Comparison of approaches in 5.5 AI for Optimizing Blockchain Performance and Security**

| AI Application Area | Specific Method/Model Name | Key Idea/Mechanism | Reference (Exact Paper Title from Input 2) |
| :--- | :--- | :--- | :--- |
| AI-Enhanced Consensus | Reinforcement Learning (RL) for Consensus | Frames consensus as an RL problem; blockchain growth as a Markov decision process to preserve transaction order while using nodes to train neural networks in parallel. | [57] |
| AI-Enhanced Consensus | Proof-of-Useful-Work (PoUW) | Repurposes mining energy for socially valuable computations (e.g., optimizing ML models). Miners compete to improve models on provided datasets, overseen by a committee. | [56] |
| AI-Enhanced Consensus | Proof-of-Training (PoT) | Harnesses crypto-mining infrastructure for distributed AI training, synchronizing global states via Byzantine fault tolerance consensus. | [394] |
| AI-Enhanced Consensus | AICons Algorithm | Uses local ML models from all nodes to generate a global model for selecting consensus winners. Employs a Shapley value-based utility function to reward nodes based on model accuracy, energy use, and bandwidth. | [58] |
| AI-Enhanced Consensus | ML for Leader Election & Peer-Prediction | In smart city applications, ML algorithms are deployed for efficient and honest leader election for transaction prioritization, coupled with peer-prediction mechanisms for block verification. | [395] |
| AI-Enhanced Consensus | Multi-agent RL for PoS (MRL-PoS) | Agents dynamically adapt to user behavior in a PoS system, applying rewards and penalties to eliminate malicious nodes and learn new adversarial tactics in real-time. | [396] |
| Sharding & Resource Management | TbDd Framework | Uses Deep Reinforcement Learning (DRL) to dynamically adjust node allocation across shards. Incorporates a trust evaluation mechanism and performs targeted resharding to mitigate collusion risks. | [397] |
| Sharding & Resource Management | Generative Diffusion Models | Uses generative AI (diffusion models) to optimize blockchain network parameters, converging faster and achieving higher rewards than traditional AI approaches to improve throughput and latency. | [398] |
| Proactive Security & Anomaly Detection | Supervised Learning & Algorithmic Game Theory | Monitors stakeholder activity in consortium blockchains to detect anomalies like collusion that could lead to majority attacks. | [399] |
| Proactive Security & Anomaly Detection | Two-way IDS with SOSN & Hierarchical Weighted Fuzzy Algorithm | A two-way intrusion detection system: first authenticates nodes and evaluates trust using a hierarchical weighted fuzzy algorithm, then verifies transactions using a Self-Organized Stacked Network (SOSN) deep learning model. | [400] |
| Proactive Security & Anomaly Detection | Ethident (GNN Framework) | Uses hierarchical graph attention encoders (HGATE) to characterize account-level features and subgraph-level behavior patterns on the Ethereum interaction graph for de-anonymization and identifying malicious actors. | [401] |
| Proactive Security & Anomaly Detection | Collaborative Learning Framework | Detects attacks in transactions and smart contracts by transforming transaction features into visual representations for analysis, enabling real-time detection of complex attacks at distributed nodes. | [402] |
| Proactive Security & Anomaly Detection | AGSOLT (Automated Test-Case Generation) | Employs search algorithms (e.g., genetic algorithms) to automatically generate high-coverage test suites for Solidity smart contracts. | [403] |
| Proactive Security & Anomaly Detection | AI for Federated Learning Defense | Uses AI to defend federated learning models on blockchain from poisoning attacks, creating a cycle where blockchain secures AI and AI secures the blockchain. | [52] |


### 5.6 AI-Enabled Smart Contracts and Autonomous Systems

The evolution of smart contracts from static, rule-based scripts to dynamic, intelligent agents represents a pivotal convergence of blockchain and artificial intelligence, unlocking a new generation of autonomous systems for 6G networks. Traditional smart contracts execute predefined logic deterministically, lacking the adaptability to respond to complex, real-world dynamics. By integrating AI models—particularly machine learning (ML) and deep learning (DL)—into the smart contract lifecycle, these decentralized applications (DApps) can perceive, learn, and make context-aware decisions. This fusion is critical for 6G’s vision of hyper-automation, where massive numbers of Internet of Things (IoT) devices, autonomous robots, and network slices require real-time, intelligent coordination without centralized control. The integration manifests through several architectural paradigms, primarily revolving around oracle-based AI inference and hybrid on-chain/off-chain execution models.

A fundamental challenge in creating AI-enabled smart contracts is the inherent limitation of blockchains as closed, deterministic systems. AI models, especially large-scale neural networks, require significant computational resources and often process stochastic, real-world data. The predominant solution is the use of oracle mechanisms, which act as trusted bridges between the blockchain and external data sources or computation services. For AI inference, oracles can be designed to fetch predictions from off-chain ML models hosted on cloud or edge servers. As studied in [404], oracle networks like ChainLink are extensively used to feed external data into contracts, establishing a pattern readily extendable to delivering AI model outputs. This architecture allows the smart contract to trigger based on an AI’s judgment—for instance, a supply chain contract releasing payment only after an oracle-confirmed AI analysis of a delivered goods’ quality from an IoT sensor stream. However, this introduces a trust dependency on the oracle provider. To mitigate this, decentralized oracle networks and consensus mechanisms for AI outputs are proposed. For example, [362] presents a consensus algorithm that derives a robust, statistically guaranteed set of data from multiple oracles, a method applicable to aggregating inferences from multiple AI models to resist adversarial or faulty nodes.

Beyond simple oracle queries, more sophisticated architectures delegate complex AI computation entirely off-chain while using the blockchain for verification, consensus, and triggering actions. The "hybrid-solver" pattern, as seen in [405], handles complex optimization computations off-blockchain while a smart contract validates the solution. This pattern is directly applicable to AI; a smart contract can specify an ML inference task, which is computed off-chain by a designated party or a decentralized network, and only the result (or a cryptographic proof of correct execution) is submitted on-chain for validation and contract state update. Projects like [179] push this further by creating a verification paradigm specifically for deep neural networks. Agatha enables native off-chain DNN execution while using a graph-based pinpoint protocol for on-chain arbitration, ensuring the correctness of the computation without requiring every node to re-execute the massive model, thus addressing scalability. Similarly, [406] proposes platform-level redesigns where non-deterministic, compute-intensive smart contract transactions (like DNN training) are executed only by nodes that need the results, with validation possible through verifying properties of the results rather than exact values.

The inverse direction, where AI enhances the smart contract ecosystem itself, is equally vital. AI techniques are being leveraged to address critical pain points in smart contract development and security. The automatic generation and auditing of smart contract code is a prominent application. [407] demonstrates the use of fine-tuned Large Language Models (LLMs) like MazzumaGPT to generate Solidity code, scaffolding development and lowering the barrier to entry. For security, AI-driven vulnerability detection has become a robust field. Traditional rule-based analyzers struggle with novel vulnerabilities and complex code interactions. Deep learning models, particularly those leveraging graph neural networks (GNNs), analyze smart contract code structure (e.g., control-flow and data-flow graphs) to detect vulnerabilities. [408] and [409] show how hybrid deep learning models can achieve high accuracy in detecting reentrancy, timestamp dependence, and other flaws by learning from code representations. Furthermore, [410] presents a DNN framework extensible to new vulnerability types via transfer learning, ensuring the detection system can evolve with the threat landscape. AI also aids in understanding contract behavior post-deployment; [411] and [320] use AI to mine behavioral specifications and automata from blockchain transaction histories, providing crucial insights for auditing and analysis.

In the context of 6G, AI-enabled smart contracts become the backbone for autonomous systems operating at the network edge. For autonomous IoT and robotic systems, smart contracts can encode collaboration protocols and business logic, while AI provides the perceptual and decision-making intelligence. [412] integrates IOTA’s DLT with a robot operating system (ROS 2), enabling a group of robots to reach consensus on shared maps or tasks in a Byzantine-tolerant manner, even with network partitions. Here, AI models for perception (e.g., SLAM) run on the robots, while the blockchain records agreed-upon states and enforces collaboration rules. Similarly, [413] proposes an architecture where smart contracts control robots by processing data from external AI oracles for tasks like image analysis, creating an immutable ledger of events and commands. This is essential for applications like autonomous manufacturing or warehouse logistics in Industry 4.0.

Intelligent resource trading and allocation in dynamic 6G environments is another transformative use case. Network slicing, mobile edge computing (MEC) resources, and even spectrum can be treated as tradable commodities. AI-enabled smart contracts can autonomously negotiate and execute resource agreements based on real-time network conditions and predicted demand. [414] exemplifies this in a mobility context, where AI-enabled multi-agent systems in vehicles and toll infrastructure negotiate dynamic pricing, with smart contracts securing the transactions. In a broader 6G network, a slice requester (e.g., an AR/VR service provider) could use a smart contract embedded with a reinforcement learning (RL) agent. This agent, informed by oracles providing real-time network performance data, could dynamically bid for and adjust its resource slice composition from multiple infrastructure providers to maintain QoS, with all transactions and SLAs immutably recorded on a blockchain. This creates a decentralized, efficient market for 6G network resources.

Finally, the concept extends to Decentralized Autonomous Organizations (DAOs) and complex socio-technical systems. [415] analyzes the governance of DAOs, which are essentially coordinated by smart contracts. Integrating AI into these governance mechanisms—such as using AI models to analyze proposal impacts, optimize treasury management, or even automate certain governance responses—could lead to more efficient and effective "intelligent DAOs." [416] formalizes Human Intelligence Primitives (HIPs) for on-chain collection and integration into ML workflows, pointing towards hybrid human-AI governance models. For smart cities, frameworks like [417] highlight the AI needed to fuse heterogeneous IoT data. When combined with blockchain-based transaction platforms like SolidWorx, these AI insights can trigger automated, trustless actions across city infrastructure—from adjusting traffic light cycles to trading renewable energy between prosumers—governed by intelligent contracts.

In summary, AI-enabled smart contracts move beyond static automation to create adaptive, cognitive, and collaborative autonomous systems. Through oracle architectures, verifiable off-chain computation, and AI-driven contract security, this synergy addresses the core requirements of 6G: ultra-reliable low-latency communication (URLLC) for control loops, massive machine-type communication (mMTC) for IoT coordination, and pervasive intelligence. The result is a foundational layer for a truly decentralized and intelligent digital economy, where devices, networks, and services can negotiate, collaborate, and transact with minimal human intervention, underpinned by the verifiable trust of blockchain and the adaptive intelligence of AI.

**Table: Comparison of approaches in 5.6 AI-Enabled Smart Contracts and Autonomous Systems**

| Method / Model Name | Primary Purpose / Function | Key Architectural Feature / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| Oracle-based AI Inference | To feed external AI model predictions (e.g., from cloud/edge servers) into deterministic smart contracts. | Uses oracle networks (e.g., ChainLink) as trusted bridges to fetch and deliver off-chain AI/ML model outputs to the blockchain. | [404] |
| Adaptive Conformal Consensus (ACon²) | To derive a robust, statistically guaranteed consensus from multiple oracles, mitigating trust dependency and adversarial nodes. | A consensus algorithm that aggregates data from multiple oracle contracts using online uncertainty quantification learning, providing correctness guarantees under distribution shift. | [362] |
| Hybrid-Solver Pattern (SolidWorx) | To handle complex computations (e.g., optimization, AI inference) off-chain while using the blockchain for verification and triggering. | Delegates complex computation off-blockchain; a smart contract validates the solution or a proof of correct execution. | [405] |
| Agatha (Graph-based Pinpoint Protocol) | To enable native off-chain execution of Deep Neural Network (DNN) computation with on-chain verifiability. | Uses a graph-based pinpoint protocol (GPP) for on-chain arbitration and Cross-evaluator Consistent Execution (XCE) to ensure cross-platform consistency. | [179] |
| "A New Hope" (ANH) Platform Design | To enable training/running of massive, non-deterministic DNNs as part of smart contracts. | Computationally intensive transactions are executed only by nodes needing the results; validation is done by verifying properties of results rather than exact values. | [406] |
| MazzumaGPT (Fine-tuned LLM) | To automatically generate Solidity smart contract code, scaffolding development. | Uses a fine-tuned Large Language Model (LLM) optimized for generating functional smart contract code. | [407] |
| HyMo (Multi-Modal Hybrid Model) | To detect vulnerabilities in smart contracts using deep learning. | A multi-modal hybrid deep learning model that uses FastText word embeddings and BiGRU to analyze various code representations for vulnerability detection. | [408] |
| Graph Neural Network (GNN) with Expert Knowledge | To detect smart contract vulnerabilities by learning from code structure graphs combined with expert patterns. | Casts contract control-/data-flow semantics into a graph, uses a temporal message propagation network for feature extraction, and combines features with expert-defined security patterns. | [409] |
| ESCORT (Deep Neural Network Framework) | To detect multiple types of smart contract vulnerabilities in an extensible manner using transfer learning. | A multi-output DNN with a common feature extractor and multiple branch structures for different vulnerability types, supporting lightweight transfer learning for new vulnerabilities. | [410] |
| Specification Mining with Automatic Abstraction Tuning | To understand smart contract behavior by mining finite automata specifications from blockchain transaction histories. | Extracts possible behaviors from contract executions, uses dependency analysis to separate interactions, and automatically tunes abstractions for automata construction. | [411] |
| IOTA + ROS 2 Integration for Robotic Systems | To enable partition-tolerant and Byzantine-tolerant decision-making for distributed robotic systems. | Integrates IOTA's DLT with the Robot Operating System (ROS 2), allowing robots to reach consensus on shared states (e.g., maps) via blockchain in intermittent network conditions. | [412] |
| Consortium Blockchain with AI Oracles for Robot Control | To control robots using smart contracts that process data from external AI oracles, creating an immutable ledger. | Proposes an architecture where smart contracts control robots by processing data (e.g., for image analysis) from external AI services (oracles). | [413] |
| AI-enabled Multi-Agent Systems for Dynamic Pricing | To enable real-time, intelligent negotiation and execution of resource agreements (e.g., dynamic toll pricing). | Uses AI-enabled multi-agent systems in devices (e.g., vehicles, toll infrastructure) to negotiate dynamic pricing, with smart contracts securing the transactions. | [414] |
| Human Intelligence Primitives (HIPs) Protocol | To formally integrate human intelligence into on-chain ML workflows and DAO governance. | Defines HIPs and implements an Ethereum protocol for their on-chain collection, modeling, and integration into machine learning processes. | [416] |
| Transformer Framework for Smart City Data Fusion | To fuse heterogeneous IoT data and perform multi-task learning for smart city applications. | A pure encoder Transformer backbone with customizable input embedding and output task heads to handle diverse data types (time-series, images) and tasks in smart cities. | [417] |


### 5.7 Architectural Patterns and Performance Trade-offs

The effective integration of Blockchain and Artificial Intelligence (AI) within 6G networks necessitates carefully designed system architectures that navigate the inherent trade-offs between performance, scalability, security, and resource efficiency. In resource-constrained edge environments, where computational power, energy, and bandwidth are at a premium, selecting an appropriate architectural pattern is paramount. Prevalent designs include layered (hierarchical) structures, sharded federated learning (FL) systems, and hybrid consensus models, each presenting distinct advantages and compromises tailored for specific 6G use cases.

Layered or hierarchical architectures, such as mainchain-subchain designs, are instrumental in managing scalability and workload distribution. A prominent example is the two-layer blockchain-driven FL system proposed in [62], termed ChainFL. This architecture splits the Internet of Things (IoT) network into multiple shards within a subchain layer, effectively reducing the scale of local information exchange and communication overhead. A Direct Acyclic Graph (DAG)-based mainchain operates as a superior layer, enabling parallel and asynchronous cross-shard validation. This separation of concerns allows the subchains to handle high-frequency, localized model updates and transactions with lower latency, while the mainchain provides overarching security, finality, and global consensus. The performance trade-off here involves balancing the complexity of cross-layer communication against the gains in scalability and robustness, which the system shows can lead to a 14% improvement in training efficiency and a threefold increase in robustness compared to conventional FL systems. Similarly, the concept of a Hierarchical Integrated Federated Ledger (HIFL) for dynamic edge resource federation, as discussed in [418], uses blockchain to create a secure, multi-domain orchestration framework. While enhancing security and trust across administrative domains, such layered approaches introduce additional latency for inter-layer synchronization and require sophisticated smart contracts for resource coordination, which must be optimized for the low-latency demands of 6G applications like the Metaverse [419].

Sharding, applied directly to federated learning processes, represents another critical architectural pattern for scaling Blockchain-AI systems. By partitioning the network of AI training nodes (e.g., IoT devices, edge servers) into smaller, manageable groups or shards, the system can process model updates and reach consensus in parallel. The work in [62] explicitly combines sharding with layering. The primary trade-off in sharded FL architectures is between scalability gains and potential security risks, such as intra-shard collusion or reduced resilience if a single shard is compromised. Furthermore, sharding introduces complexity in assigning nodes to shards fairly and efficiently, especially in heterogeneous edge networks with varying device capabilities and trust levels. The design must ensure that the shard formation and cross-shard communication protocols do not become a bottleneck, negating the performance benefits. For 6G edge environments, where devices may join and leave dynamically, adaptive sharding mechanisms that consider device connectivity, computational resource, and data distribution are essential to maintain low latency and high throughput for collaborative AI tasks.

Hybrid consensus models are architectural innovations that leverage AI to optimize the core blockchain mechanism itself, directly addressing the trade-offs between energy consumption, latency, and fairness. Traditional consensus protocols like Proof-of-Work (PoW) are notoriously energy-intensive and slow, making them unsuitable for edge devices. AI-driven consensus algorithms, such as AICons proposed in [58], represent a paradigm shift. AICons utilizes the local ML models trained by all participating nodes to generate a global model for selecting block validators, thereby reducing the energy waste associated with discarding the work of non-winning nodes. It further incorporates a multi-faceted utility function based on the Shapley value to reward nodes fairly based on model accuracy, energy consumption, and network bandwidth. The architectural trade-off here involves the computational overhead of continuously training and evaluating ML models for consensus versus the achieved gains in energy efficiency, fairness, and transaction throughput (claimed to handle 38.4 more transactions per second than state-of-the-art schemes). Another hybrid approach involves modular architectures that decouple consensus from execution, as noted in [420]. While this can increase throughput, it risks centralization at the execution layer. AI can be deployed to optimize task scheduling and workload distribution in such decoupled architectures, but this requires careful resource allocation to avoid introducing new latency points.

The ultimate performance of these architectures in 6G is measured against key metrics: latency, scalability, energy efficiency, and resource consumption. For latency-sensitive applications like autonomous vehicles or extended reality (XR), architectures that prioritize local processing and minimal consensus overhead are critical. The conditionally deep hybrid neural network proposed in [421] exemplifies an AI-centric architectural pattern that minimizes latency and energy by allowing inferences to exit early at the edge when confidence is high, conditionally activating deeper cloud layers only when necessary. Integrating such an AI inference pattern with a lightweight blockchain layer for model integrity and data provenance verification creates a trade-off: the security and auditability provided by blockchain must not reintroduce the latency the conditional network aims to reduce. Energy efficiency is a dominant concern for battery-powered edge IoT devices. Architectural choices like employing ultra-low-power accelerators [422] or near-subthreshold processors [423] for on-device AI, combined with energy-aware consensus like AICons or lightweight permissioned blockchains (e.g., Quorum, as assessed in [38]), are essential. The performance assessment in [424] and [425] quantitatively highlights the significant energy savings possible by running blockchain nodes on balanced, low-power ARM architectures compared to traditional servers, though often at the cost of raw throughput.

In conclusion, there is no one-size-fits-all architectural pattern for Blockchain-AI integration in 6G. The choice depends on the specific application's requirements. A layered mainchain-subchain design excels in large-scale, multi-domain deployments requiring robust security and scalability. Sharded FL architectures are optimal for massively parallel AI training across vast device networks. Hybrid AI-enhanced consensus models are key for sustainable, fair, and efficient decentralized systems. The overarching design principle for 6G edge environments is to achieve an optimal Pareto frontier where gains in scalability and security do not come at prohibitive costs in latency and energy consumption, often through cross-layer co-design and context-aware adaptation, as advocated in works like [426] and [427].

**Table: Comparison of approaches in 5.7 Architectural Patterns and Performance Trade-offs**

| Architectural Pattern | Key Mechanism / Example | Primary Trade-offs / Performance Metrics | Key Reference(s) |
| :--- | :--- | :--- | :--- |
| Layered/Hierarchical Architecture | Mainchain-subchain design (e.g., ChainFL). Splits IoT network into shards in a subchain layer; uses a DAG-based mainchain for cross-shard validation. | **Trade-off:** Complexity of cross-layer communication vs. gains in scalability and robustness. **Performance:** 14% improvement in training efficiency, 3x increase in robustness. | [62], [418], [419] |
| Sharded Federated Learning (FL) Architecture | Partitioning the network of AI training nodes into smaller, parallel groups (shards) for model updates and consensus. | **Trade-off:** Scalability gains vs. security risks (intra-shard collusion, reduced resilience). **Performance:** Requires adaptive sharding for dynamic 6G edge environments to maintain low latency/high throughput. | [62] |
| Hybrid AI-Enhanced Consensus Models | AI-driven consensus algorithms (e.g., AICons) using local ML models to select validators, incorporating multi-faceted utility functions (e.g., Shapley value). | **Trade-off:** Computational overhead of training/evaluating ML models for consensus vs. gains in energy efficiency, fairness, and throughput. **Performance:** Handles 38.4 more transactions per second than state-of-the-art schemes. | [58], [420] |
| AI-Centric Conditional Inference Architecture | Conditionally deep hybrid neural networks allowing early exits at the edge, activating deeper cloud layers only when necessary. | **Trade-off:** Security/auditability from a lightweight blockchain layer vs. potential reintroduction of latency. **Performance:** Minimizes latency and energy; processes 65% of inferences at edge, leading to 5.5x computational energy reduction on CIFAR-10. | [421] |
| Energy-Efficient Hardware-Consensus Co-Design | Combining ultra-low-power accelerators / near-subthreshold processors for on-device AI with energy-aware consensus (e.g., AICons) or lightweight permissioned blockchains (e.g., Quorum). | **Trade-off:** Energy savings vs. raw throughput. **Performance:** Significant energy savings using low-power ARM architectures vs. traditional servers. | [422], [423], [38], [424], [425] |


## 6 Architectural Frameworks and Enabling Technologies

This section analyzes proposed system-level architectures and key enabling technologies that facilitate the Blockchain-AI-6G integration. It discusses the integration with Mobile Edge Computing (MEC), Reconfigurable Intelligent Surfaces (RIS), network digital twins, and non-terrestrial networks (NTN). The concept of AI-native and self-evolving network architectures, supported by a decentralized trust layer, is also explored.

### 6.1 Integration with Mobile Edge Computing (MEC) and Edge Intelligence

The architectural convergence of Mobile Edge Computing (MEC), Artificial Intelligence (AI), and Blockchain is a cornerstone for realizing the vision of 6G networks as decentralized, intelligent, and trustworthy ecosystems. MEC fundamentally repositions cloud-like computing, storage, and networking resources to the network periphery, proximate to data sources such as IoT devices, autonomous vehicles, and user equipment. This proximity is critical for enabling low-latency, high-bandwidth applications and forms the foundational infrastructure for Edge Intelligence, where AI model training and inference are performed at or near the data generation point. However, the distributed and multi-stakeholder nature of MEC introduces significant challenges in resource management, service orchestration, trust establishment, and security. Blockchain technology emerges as a pivotal enabler to address these challenges, providing a decentralized, immutable, and transparent ledger for secure coordination among untrusted edge nodes, thereby facilitating the creation of robust and autonomous edge ecosystems.

A primary synergy lies in using blockchain to secure and orchestrate privacy-preserving AI training paradigms like Federated Learning (FL) within MEC. Traditional FL relies on a central aggregator, which becomes a single point of failure and a target for model corruption or data privacy attacks. Blockchain decentralizes this process, creating a trusted and auditable environment for collaborative learning. In a blockchain-empowered FL (BFL) system, edge devices or local edge servers train models on local data and submit model updates (e.g., gradients or weights) as transactions to a blockchain network. Smart contracts then automate the critical functions of the FL process: they verify the authenticity and quality of submitted updates, aggregate them to form a new global model, and record the entire process immutably. This architecture, as explored in frameworks like BFL-MEC [428], mitigates risks associated with a malicious central server and provides a verifiable record of model evolution. Furthermore, blockchain can manage sophisticated incentive mechanisms, as seen in [429], which use multi-dimensional auctions to encourage high-quality, resource-efficient edge nodes to participate in FL, improving overall model performance and system efficiency.

Beyond FL, blockchain enables dynamic and trustworthy edge resource federation and service management. In a multi-vendor MEC environment, edge servers owned by different service providers need to collaborate for task offloading, computation sharing, and load balancing. Establishing trust and ensuring fair resource trading in such a decentralized setting is non-trivial. Blockchain provides a neutral, tamper-proof platform for this purpose. Frameworks like [430] and [431] propose using permissioned blockchains and smart contracts to create decentralized marketplaces for edge resources. Service requirements and resource offers are encoded into smart contracts, which then execute pre-agreed algorithms to match tasks with the most suitable edge host based on latency, cost, and resource availability. All transactions—such as task offloading requests, resource allocation decisions, and payments—are recorded on-chain, ensuring transparency, auditability, and non-repudiation. This automates Service Level Agreements (SLAs) and enables "trustless" collaboration among otherwise competitive entities.

The integration also addresses critical security and privacy concerns inherent in edge intelligence. MEC nodes, often deployed in less secure environments, are vulnerable to attacks. Blockchain enhances security by providing immutable logging for all activities, from data provenance to model updates. For instance, [62] proposes a two-layer blockchain (ChainFL) that uses sharding within subchains to manage local model updates efficiently and a DAG-based mainchain for secure cross-shard validation, significantly improving robustness against abnormal models. Furthermore, blockchain can be combined with advanced cryptographic techniques for enhanced privacy. [205] integrates Local Differential Privacy (LDP) with blockchain-assisted FL, where LDP adds noise to local model updates before they are recorded on the blockchain, strengthening data confidentiality against inference attacks while maintaining the auditability of the aggregation process.

AI, particularly Deep Reinforcement Learning (DRL), reciprocally optimizes the performance of blockchain-MEC systems. The operation of blockchain consensus (e.g., mining) and the allocation of MEC resources (e.g., computing power, bandwidth) are complex, dynamic optimization problems. DRL agents can learn optimal policies for these tasks. For example, [150] proposes a cooperative task offloading and blockchain mining (TOBM) scheme where a multi-agent DRL algorithm dynamically decides how edge devices should split their resources between processing computation tasks and participating in blockchain consensus to maximize a system utility. Similarly, [432] uses multi-agent DRL to help heterogeneous aggregators in a BMA-FL architecture decide optimal training strategies, balancing speed and accuracy. These AI-driven optimizations ensure that the blockchain layer and the MEC resource layer operate synergistically and efficiently.

Finally, this triad enables novel architectural patterns for scalable and secure edge services. Concepts like Blockchain Function Virtualization (BFV) [165] propose virtualizing all blockchain functions (mining, encryption) so they can be executed on-demand on MEC or cloud servers, alleviating the resource burden on end devices. Hierarchical and sharded blockchain architectures, as seen in [433], are designed specifically for large-scale FEL, using a main chain for global coordination and subchains for local model update management to achieve scalability and performance isolation. These frameworks collectively illustrate a future where MEC provides the pervasive computing fabric, AI supplies the embedded intelligence, and blockchain ensures the secure, decentralized, and automated governance of the entire ecosystem, forming an indispensable architectural pillar for 6G.

**Table: Comparison of approaches in 6.1 Integration with Mobile Edge Computing (MEC) and Edge Intelligence**

| Method / Framework Name | Primary Purpose / Contribution | Key Technologies / Mechanisms | Reference |
| :--- | :--- | :--- | :--- |
| BFL-MEC | A fully asynchronous Blockchained Federated Learning framework for MEC, designed to handle mobility-induced impairments and provide post-quantum security. | Asynchronous FL, Blockchain, Post-Quantum Cryptography, Identity Verification | [428] |
| FMore | An incentive scheme using multi-dimensional auctions to encourage high-quality, resource-efficient edge node participation in Federated Learning. | Multi-dimensional Auction, Incentive Mechanism, Lightweight Design, Nash Equilibrium | [429] |
| EdgeChain | A blockchain-based architecture for making multi-vendor mobile edge application placement decisions, ensuring fairness and transparency. | Blockchain, Smart Contracts, Stochastic Programming, Heuristic Placement Algorithm | [430] |
| (Framework for Secure Task Sharing) | A blockchain framework to provide a trusted collaboration and task-sharing mechanism between edge servers in a MEC environment. | Permissioned Blockchain, Smart Contracts, Incentive Mechanism, Hyperledger Fabric | [431] |
| ChainFL | A two-layer blockchain-driven FL system using sharding and a DAG-based mainchain to improve scalability and robustness against abnormal models. | Two-layer Blockchain, Sharding, DAG-based Mainchain, Cross-shard Validation | [62] |
| (Joint Framework for Vehicular Networks) | Integrates Local Differential Privacy with blockchain-assisted FL to enhance data confidentiality and traffic prediction accuracy in vehicular networks. | Federated Learning, Blockchain, Local Differential Privacy (LDP), Traffic Prediction | [205] |
| TOBM Scheme | A cooperative task offloading and blockchain mining scheme optimized via multi-agent DRL to maximize system utility in blockchain-based MEC. | Deep Reinforcement Learning (DRL), Multi-agent DDPG, Proof-of-Reputation, Task Offloading, Blockchain Mining | [150] |
| BMA-FL | A Blockchain-empowered Heterogeneous Multi-Aggregator FL architecture with a lightweight Byzantine consensus mechanism and multi-agent DRL for training strategy optimization. | Multi-Aggregator FL, Lightweight Byzantine Consensus (PBCM), Multi-agent DRL, Heterogeneity Management | [432] |
| Blockchain Function Virtualization (BFV) | Virtualizes all blockchain functions (mining, encryption) to be executed on-demand on MEC or cloud servers, reducing the resource burden on end devices. | Function Virtualization, Resource Allocation, Energy-Reward Optimization | [165] |
| (Multi-blockchain FEL Framework) | A hierarchical blockchain framework with a main chain and subchains for scalable, secure, and communication-efficient decentralized Federated Edge Learning. | Hierarchical Blockchain, Proof-of-Verifying Consensus, Gradient Compression, Subchain Management | [433] |


### 6.2 Synergy with Reconfigurable Intelligent Surfaces (RIS) for Smart Radio Environments

The vision of smart, programmable radio environments is a cornerstone of 6G, promising unprecedented control over wireless propagation to enhance coverage, spectral efficiency, and security. Reconfigurable Intelligent Surfaces (RIS) are the fundamental physical enabler for this vision, comprising arrays of passive (or increasingly, active) elements that can dynamically manipulate electromagnetic waves. The realization of this vision, however, hinges on solving two intertwined challenges: the intelligent, real-time optimization of RIS configurations for diverse objectives, and the secure, trustworthy management of these distributed, shared assets in multi-operator ecosystems. This is where the synergistic convergence of Artificial Intelligence (AI) and Blockchain technology becomes indispensable, creating a closed-loop framework where AI optimizes the physical layer and Blockchain secures the control and data planes.

AI serves as the computational brain for RIS optimization, tackling problems that are analytically intractable due to high dimensionality, non-convexity, and partial channel state information (CSI). Machine learning, particularly Deep Reinforcement Learning (DRL), is adept at learning optimal phase-shift policies through trial-and-error interactions with the environment, as demonstrated in works like [229]. DRL agents can jointly design transmit beamforming and RIS phase shifts simultaneously, learning to maximize network utility such as sum-rate or secrecy capacity. For scalability with RIS elements numbering in the thousands, specialized neural network architectures like RISnet are proposed [434, 435]. These domain-knowledge-driven models, which respect the inherent symmetry of RIS structures and can operate with CSI for only a small subset of elements, significantly reduce channel estimation overhead and computational complexity. Furthermore, the trend is moving towards autonomous RIS operation, where the surface itself, equipped with a few sensing elements, uses a DRL agent to configure its reflection pattern without continuous control signaling from a base station, thereby eliminating network overhead [436]. Beyond optimization, AI is critical for security. Explainable AI (XAI) frameworks can be employed to detect and combat malicious RIS (MITM-RIS) attacks, where an adversarial surface poisons the channel to eavesdrop. As shown in [437], generative adversarial networks (GANs) can help legitimate users learn a common feature space unknown to the eavesdropper, with symbolic XAI providing interpretable rules for feature validation and future secure system design.

While AI optimizes the "how," Blockchain establishes the "who," "when," and "with what authority" in a trustless environment. In a multi-stakeholder 6G landscape, RIS infrastructure may be deployed by neutral hosts or individual operators and shared dynamically. Blockchain provides a secure, immutable, and decentralized ledger to manage this shared ecosystem. Smart contracts can codify complex access policies, leasing agreements, and service level agreements (SLAs) for RIS usage. When a base station or user equipment requests a specific RIS configuration to enhance its link, a smart contract can automatically verify credentials, execute a micropayment in cryptocurrency or tokenized credit, and log the transaction and the agreed-upon configuration on-chain. This creates a transparent and auditable record of resource usage, crucial for billing, dispute resolution, and regulatory compliance. The consortium blockchain model is particularly suitable, as it allows a permissioned network of known operators (e.g., mobile network operators, infrastructure providers) to participate in the consensus, balancing decentralization with the performance and governance needs of a commercial system [438]. This ledger also becomes the single source of truth for the RIS's state history. Each validated configuration update can be hashed and stored on the blockchain, creating an immutable audit trail. This prevents rogue actors, including the RIS hardware owner, from maliciously rolling back or denying prior configurations, thereby ensuring non-repudiation and enhancing overall system trustworthiness.

The synergy is most potent when AI and Blockchain operate in a tightly integrated loop. AI-driven decisions on RIS configuration (e.g., for maximizing secrecy rate as in [439]) are executed via transactions validated and recorded on the blockchain. The blockchain, in turn, can securely aggregate distributed channel measurements or performance feedback from user equipment across the network. This aggregated, trust-verified data can then be used to retrain and improve the AI models in a privacy-preserving manner, potentially using federated learning frameworks logged on the blockchain [52]. Furthermore, blockchain can manage incentives for data sharing and collaborative AI model training among competing operators, who may be reluctant to share proprietary channel data directly. By using tokenized incentives recorded on-chain, operators can be rewarded for contributing to a global RIS optimization model without exposing their raw data, as explored in concepts like [440].

This combined architecture directly addresses key security applications. For physical layer security, AI optimizes RIS phase shifts to create secure beams towards legitimate users and nulls towards eavesdroppers, or to generate artificial noise, significantly improving metrics like secrecy outage probability [441]. Blockchain secures the process by ensuring that the security-critical configuration deployed is the one that was optimally computed and agreed upon, preventing man-in-the-middle attacks on the control link. It also provides a secure platform for distributing and managing cryptographic keys used in conjunction with RIS-enhanced physical layer security schemes. As RIS technology evolves to include active and absorptive elements [442, 443], which introduce amplification and amplitude control, the complexity and security criticality of configuration increase, making the AI-Blockchain management layer even more vital.

In conclusion, the path to truly smart radio environments in 6G is paved by the deep integration of RIS, AI, and Blockchain. AI provides the necessary intelligence to dynamically harness the flexibility of RIS for performance and security gains, while Blockchain provides the trust, automation, and business logic required for their secure and efficient operation in open, decentralized networks. This triad transforms the wireless propagation environment from a passive, uncontrollable medium into a actively programmable, intelligently optimized, and securely governed network asset.

**Table: Comparison of approaches in 6.2 Synergy with Reconfigurable Intelligent Surfaces (RIS) for Smart Radio Environments**

| Method/Model | Key Idea/Contribution | Application Context | Reference |
| :--- | :--- | :--- | :--- |
| Deep Reinforcement Learning (DRL) for RIS Optimization | Uses trial-and-error interactions to learn optimal phase-shift and beamforming policies, enabling joint design without alternating optimization. | Optimizing RIS configurations for sum-rate or secrecy capacity in multiuser MISO systems. | [229] |
| RISnet (Scalable Neural Network) | A domain-knowledge-driven neural network architecture designed for scalability (e.g., 1296 elements) and operation with partial CSI (e.g., for 16 elements), reducing channel estimation overhead. | Sum-rate maximization in downlink multi-user MISO systems with large RIS arrays and partial CSI. | [434, 435] |
| Autonomous RIS Operation with DRL | Enables RIS to self-configure its reflection pattern using a DRL agent and a few sensing elements, eliminating continuous control signaling from the base station. | Autonomous operation of RIS to enhance network sum-rate without dedicated control links. | [436] |
| Explainable AI (XAI) with GANs for Security | Uses Generative Adversarial Networks (GANs) to help legitimate users learn a common feature space unknown to an eavesdropper, with symbolic XAI providing interpretable rules for validation. | Detecting and combating Man-in-the-Middle Malicious RIS (MITM-RIS) attacks to secure physical layer secret key generation. | [437] |
| Blockchain with Smart Contracts for Resource Management | Uses a decentralized, immutable ledger and smart contracts to automate access policies, leasing agreements, micropayments, and log transactions for RIS usage in multi-operator ecosystems. | Secure and transparent management of shared RIS infrastructure, enabling billing, dispute resolution, and regulatory compliance. | [438] |
| Federated Learning integrated with Blockchain | Employs blockchain to securely aggregate distributed data for retraining AI models in a privacy-preserving manner, managing incentives for collaborative training among operators. | Privacy-preserving, collaborative improvement of global RIS optimization models across competing entities. | [52] |
| AI-Blockchain Synergy for Secrecy Optimization | AI optimizes RIS configurations for physical layer security (e.g., creating secure beams), while blockchain secures the deployment and provides an audit trail for the configurations. | Maximizing secrecy spectral efficiency in RIS-assisted systems and ensuring the integrity of security-critical configurations. | [439] |
| Tokenized Incentive Mechanisms via Blockchain | Uses blockchain to manage tokenized incentives, rewarding operators for contributing to a global model without sharing raw proprietary data. | Incentivizing data sharing and collaborative AI model training in complex wireless blockchain networks for IoT devices. | [440] |
| Analysis of Secrecy Performance with RIS | Provides theoretical analysis and closed-form expressions for secrecy metrics (e.g., secrecy outage probability) in RIS-assisted systems with random eavesdroppers. | Evaluating and designing the physical layer security performance of RIS-assisted MISO systems over Rician channels. | [441] |
| Active/Absorptive RIS for Enhanced Security | Explores RIS with active (amplifying) or absorptive (amplitude-controlling) elements to overcome the "double fading" effect and improve secrecy performance. | Enhancing physical layer security and interference mitigation in wireless communications. | [442, 443] |


### 6.3 Network Digital Twins for Simulation, Optimization, and Security

The paradigm of Network Digital Twins (NDTs) represents a cornerstone architectural framework for 6G, creating high-fidelity, dynamic, and synchronized virtual replicas of the physical network and its constituent entities. This digital mirroring transcends simple monitoring, enabling a closed-loop ecosystem for simulation, proactive optimization, and robust security enforcement. The realization of this vision hinges on a synergistic integration where Artificial Intelligence (AI) serves as the analytical and decision-making engine of the DT, while Blockchain provides the foundational trust layer for the entire data pipeline, ensuring integrity, provenance, and decentralized security.

AI is the core intelligence that breathes life into the static model of a DT, transforming it into a predictive and prescriptive tool. A primary application is in network optimization and "what-if" analysis. By leveraging real-time and historical data streams from the physical network—including traffic patterns, channel states, and resource utilization—AI models, particularly those based on reinforcement learning (RL) and deep learning, can simulate countless future scenarios. Frameworks like the one proposed in [444] utilize generative models such as Conditional Tabular GANs (CTGAN) to synthesize diverse network conditions, allowing operators to pre-emptively assess the impact of configuration changes, traffic spikes, or potential failures on key performance indicators like throughput and latency. This capability is critical for zero-touch network and service management (ZSM). Furthermore, AI-driven DTs enable continuous optimization. For instance, multi-agent RL can be deployed within the DT to learn optimal policies for radio resource allocation, beamforming, or network slicing, which are then safely deployed to the physical network [445]. The concept of continual learning is vital here, as seen in [446], where DTs dynamically adapt their models to evolving physical twin behaviors, minimizing desynchronization and maintaining accuracy over time. Generative AI also plays a transformative role, as highlighted in [194], where models like transformers and diffusion models can enhance the realism of simulations, improve physical-digital synchronization, and generate synthetic data for robust AI training within the twin.

However, the efficacy of an AI-driven DT is fundamentally dependent on the quality, integrity, and trustworthiness of the data it ingests. This is where blockchain technology becomes indispensable. Blockchain acts as a secure and immutable ledger for the DT data pipeline, addressing critical challenges of data provenance and integrity. In complex Cyber-Physical Systems (CPS) and Industrial IoT (IIoT) environments, data is collected from myriad sensors and devices owned by different stakeholders. A blockchain-based framework, as envisioned in [447] and [448], can cryptographically seal sensor readings and system events, creating an auditable trail from the physical source to the digital twin. This ensures that the data driving simulations and AI models has not been tampered with, mitigating risks from malicious actors or faulty sensors. The integration also facilitates decentralized trust models essential for collaborative DTs. For example, in a multi-stakeholder scenario like a smart city or a federated learning system, blockchain can manage and verify the reputation of data sources and DT contributors, as discussed in [143]. Smart contracts can automate data-sharing agreements and access control to the DT itself, as proposed in [449], where access is granted to virtual twins rather than physical devices, enhancing security and privacy.

The convergence of blockchain and AI within the DT framework is particularly powerful for advancing security postures, including zero-trust architectures. A DT provides a safe sandbox for security testing and anomaly detection without risking the live network. AI models trained within the DT can learn normal network behavior and identify subtle, sophisticated cyber-attacks, such as insider threats or low-and-slow intrusions. The work in [400] demonstrates the use of deep learning for anomaly detection within blockchain systems, a concept directly applicable to securing the DT's own operations. Blockchain enhances this by providing a trustworthy record of security events, policies, and model updates. A decentralized, blockchain-based zero-trust framework for DT-enabled 6G, as suggested in [350], can authenticate not just physical devices but also their digital twin instances and the AI agents operating within them. Every access request and policy decision can be immutably logged on-chain, enabling transparent auditability and preventing a single point of compromise. This creates a resilient security fabric where the DT is both a tool for security (via simulation and detection) and a entity that is itself secured by blockchain.

Implementing this integrated architecture presents significant challenges. The computational and communication overhead of maintaining high-fidelity, real-time synchronization for massive 6G networks is immense, necessitating efficient edge computing paradigms [450]. The scalability of blockchain to handle the high-frequency, fine-grained data streams from millions of IoT devices remains a concern, though lightweight consensus mechanisms and DAG-based structures like those in [163] offer promising directions. Furthermore, ensuring the explainability of AI decisions made within the DT is crucial for operator trust and regulatory compliance, an area addressed by approaches like the neuro-symbolic framework in [451]. Despite these hurdles, the trajectory is clear: Network Digital Twins, powered by the dual engines of AI and anchored by blockchain trust, will be pivotal in transitioning 6G from a reactive infrastructure to a proactive, self-optimizing, and intrinsically secure ecosystem capable of supporting the most demanding and critical future applications.

**Table: Comparison of approaches in 6.3 Network Digital Twins for Simulation, Optimization, and Security**

| Method/Model | Key Idea/Contribution | Reference |
| :--- | :--- | :--- |
| Conditional Tabular GANs (CTGAN) for "What-if" Analysis | Uses generative models (CTGAN) to synthesize diverse network conditions for pre-emptive assessment of configuration changes, traffic spikes, or failures on KPIs like throughput and latency. | [444] |
| Multi-agent Reinforcement Learning (RL) for Network Optimization | Deploys multi-agent RL within the DT to learn optimal policies for radio resource allocation, beamforming, or network slicing, which are then safely deployed to the physical network. | [445] |
| Edge Continual Learning for Dynamic Synchronization | Proposes a continual learning framework where DTs dynamically adapt their models to evolving physical twin behaviors, minimizing desynchronization and maintaining accuracy over time. | [446] |
| Generative AI (Transformers, Diffusion Models) for Enhanced Realism | Utilizes generative AI models like transformers and diffusion models to enhance the realism of simulations, improve physical-digital synchronization, and generate synthetic data for robust AI training. | [194] |
| Blockchain-based Data Provenance & Integrity Framework | Employs blockchain as a secure, immutable ledger to cryptographically seal sensor readings and system events, creating an auditable trail from the physical source to the DT to ensure data integrity. | [447], [448] |
| Blockchain for Trust & Reputation Management (TRM) | Uses blockchain as a decentralized platform for collaboratively managing and processing interaction evidence to quantify and maintain trust/reputation scores of nodes in multi-stakeholder scenarios. | [143] |
| Smart Contracts for DT Access Control | Uses smart contracts to automate data-sharing agreements and access control, granting access to virtual twins rather than physical devices to enhance security and privacy. | [449] |
| Deep Learning for Anomaly Detection in Blockchain Systems | Demonstrates the use of deep learning models (e.g., self-organized stacked network) for anomaly detection within blockchain systems, applicable to securing DT operations. | [400] |
| Decentralized, Blockchain-based Zero-Trust Framework | Proposes a decentralized zero-trust framework for DT-enabled 6G that uses blockchain to authenticate physical devices, their digital twins, and AI agents, with all access requests immutably logged. | [350] |
| Two-Layer DAG-based Protocol for IoT Data Reliability | Proposes a lightweight, two-layer directed acyclic graph (2LDAG) protocol and Proof-of-Path (PoP) for on-demand data verification, offering significantly lower storage/communication costs than traditional blockchain. | [163] |
| Neuro-symbolic XAI Twin for Explainable ZSM | Proposes a neuro-symbolic XAI twin framework combining neural networks for environment capture with a Bayesian network for symbolic reasoning, enabling explainable, trustworthy zero-touch network management. | [451] |
| Multi-Tier Computing for DT Scalability | Proposes multi-tier computing (edge/fog/cloud) architectures to address the high computational and communication overhead of maintaining real-time, high-fidelity DTs for massive 6G networks. | [450] |


### 6.4 Enabling Ubiquitous Coverage: Integration with Non-Terrestrial Networks (NTN)

The vision of 6G extends beyond terrestrial confines, aiming for truly ubiquitous, three-dimensional connectivity. This necessitates the seamless integration of Non-Terrestrial Networks (NTNs), encompassing satellites (GEO, MEO, LEO), High-Altitude Platforms (HAPs), and swarms of Unmanned Aerial Vehicles (UAVs), into a unified Space-Air-Ground Integrated Network (SAGIN) [452]. However, this integration introduces profound architectural challenges, including extreme heterogeneity, high mobility, dynamic topologies, intermittent connectivity, and stringent resource constraints on aerial platforms. The synergistic application of Artificial Intelligence (AI) and Blockchain emerges as a pivotal enabler to address these complexities, facilitating intelligent resource orchestration and secure, decentralized operations across the NTN ecosystem.

AI serves as the core intelligence for managing the dynamic and resource-constrained NTN environment. A primary application is the AI-driven optimization of UAV and satellite resource management and trajectory planning. Given the unpredictable nature of MEC environments and user mobility, deep reinforcement learning (DRL) algorithms, such as Double Deep Q-Networks (DDQN) and Multi-Agent Deep Deterministic Policy Gradient (MADDPG), are extensively employed. These algorithms enable UAVs to autonomously and adaptively optimize their flight trajectories, user association, and computation offloading strategies to minimize total system energy consumption or maximize service quality [453] [454]. For instance, in UAV-assisted MEC systems, DRL can jointly optimize bit allocation, transmit power, and UAV trajectory to minimize energy consumption while meeting latency constraints [455]. Furthermore, the integration of Reconfigurable Intelligent Surfaces (RIS) with UAVs, forming aerial STAR-RIS systems, introduces additional degrees of freedom for coverage and signal enhancement. AI algorithms, including Proximal Policy Optimization (PPO), are crucial for jointly optimizing the RIS phase shifts, UAV trajectory, and task offloading decisions to enhance energy efficiency [456]. In broader SAGINs, AI is essential for complex, multi-layer resource allocation, such as optimizing user equipment association, power control, and the 3D deployment of UAVs and HAPs to maximize system energy efficiency [457]. Machine learning models, including ensemble deep neural networks, are also proposed for intelligent user scheduling in integrated space-HAPS-ground networks, overcoming the limitations of traditional model-based optimization in highly heterogeneous environments [458].

While AI manages operational efficiency, Blockchain provides the critical trust and security foundation for decentralized NTN operations. In sparse, delay-tolerant environments where central authorities are impractical, blockchain enables secure, transparent, and tamper-proof access control, identity management, and data exchange among heterogeneous NTN entities (e.g., satellites, UAVs from different providers, ground stations). For UAV networks, blockchain frameworks can establish immutable logs for drone registration, flight paths, and data transactions, preventing spoofing and ensuring accountability [459]. This is particularly vital for applications like UAV Traffic Management (UTM), where a decentralized blockchain protocol, potentially combined with mobile crowdsensing, can securely govern airspace access and enforce regulations without a single point of failure [460]. In data collection scenarios, blockchain can secure the data provenance from IoT sensors to UAVs and beyond. Lightweight consensus mechanisms, such as Proof-of-Stake (PoS) or novel Proof-of-Competence (PoC), are tailored for resource-constrained UAVs to form a secure blockchain network that validates and records collected data, with incentive models designed to encourage honest participation [461] [462]. For post-disaster communication networks, blockchain-assisted decentralized flocking algorithms enable secure and autonomous coordination among UAVs from multiple agencies, ensuring resilient operations even under adversarial conditions [463].

The convergence of AI and Blockchain finds its ultimate expression in the concept of "MEC in the Sky" or "Air Computing," which envisions on-demand edge intelligence provisioned by NTN platforms [464]. This paradigm shift involves deploying MEC capabilities on UAVs, HAPs, and even LEO satellites, transforming them into agile, floating edge servers. AI is fundamental to this vision, managing the dynamic placement of computing workloads (computation offloading), caching of content, and allocation of communication and computation resources across the tiered NTN architecture [465] [466]. Blockchain complements this by securing the entire service chain. It can manage service-level agreements (SLAs) via smart contracts, facilitate secure and auditable resource trading between service consumers (e.g., ground vehicles, IoT devices) and providers (e.g., a UAV-MEC server), and ensure the integrity of offloaded tasks and computed results [309] [467]. For example, in a SAGIN, a hybrid cloud/MEC resource allocation problem can be solved in a distributed manner, with blockchain ensuring the transparency and enforcement of the agreed-upon optimization decisions [468]. Furthermore, blockchain can secure Federated Learning (FL) processes conducted across distributed NTN edge nodes, enabling collaborative AI model training on sensitive, geographically dispersed data (e.g., from maritime IoT sensors or rural vehicles) without central data aggregation, thus preserving privacy while leveraging collective intelligence [428] [469].

In conclusion, the integration of Blockchain and AI is indispensable for realizing the full potential of NTNs in 6G. AI provides the cognitive engine for autonomous, efficient, and adaptive management of the complex NTN fabric, while blockchain furnishes a resilient trust layer for decentralized coordination, security, and transparent service delivery. Together, they enable the robust and secure "MEC in the Sky" paradigm, paving the way for 6G to deliver pervasive, intelligent, and reliable connectivity and computing services across the globe, from dense urban centers to remote oceans and skies.

**Table: Comparison of approaches in 6.4 Enabling Ubiquitous Coverage: Integration with Non-Terrestrial Networks (NTN)**

| Method/Model | Key Idea/Objective | Application Context | AI/Blockchain Role | Key Techniques/Algorithms | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AI-driven UAV/Satellite Resource & Trajectory Optimization | Minimize system energy consumption or maximize service quality by optimizing UAV flight trajectories, user association, and computation offloading in dynamic MEC environments. | UAV-assisted Mobile Edge Computing (MEC) systems for IoT. | AI as core intelligence for autonomous, adaptive management. | Deep Reinforcement Learning (DRL), Double Deep Q-Networks (DDQN), Multi-Agent Deep Deterministic Policy Gradient (MADDPG). | [453], [454], [455] |
| AI for RIS-UAV (Aerial STAR-RIS) Empowered MEC | Enhance energy efficiency by jointly optimizing RIS phase shifts, UAV trajectory, and task offloading decisions. | MEC systems with UAVs and Reconfigurable Intelligent Surfaces (RIS). | AI for managing complex joint optimization in dynamic environments. | Proximal Policy Optimization (PPO), Deep Reinforcement Learning (DRL). | [456] |
| AI for Multi-Layer Resource Allocation in SAGIN | Maximize system energy efficiency by optimizing user equipment association, power control, and 3D deployment of UAVs and HAPs. | Space-Air-Ground Integrated Networks (SAGIN), e.g., maritime coverage. | AI for complex, multi-layer resource orchestration in heterogeneous networks. | Mixed-integer nonlinear programming, Benders decomposition, Dinkelbach algorithm, ADMM. | [457] |
| Machine Learning for User Scheduling | Optimize user scheduling policies to overcome limitations of model-based optimization in highly heterogeneous networks. | Integrated Satellite-HAPS-Ground Networks. | AI for intelligent resource management and real-time processing. | Ensemble Deep Neural Networks. | [458] |
| Blockchain for Secure UAV Operations & Data Provenance | Establish secure, transparent, and tamper-proof access control, identity management, and data exchange for heterogeneous NTN entities. | UAV networks for delivery, data collection, and general operations. | Blockchain as a trust layer for decentralized security and accountability. | Proof-of-Stake (PoS), Proof-of-Competence (PoC), smart contracts. | [459], [461], [462] |
| Blockchain for Decentralized UAV Traffic Management (UTM) | Securely govern airspace access and enforce regulations without a single point of failure. | UAV Traffic Management (UTM). | Blockchain for decentralized, secure coordination and rule enforcement. | Blockchain protocol combined with mobile crowdsensing. | [460] |
| Blockchain for Secure Post-Disaster UAV Coordination | Enable secure and autonomous coordination among UAVs from multiple agencies under adversarial conditions. | Post-disaster communication networks. | Blockchain for resilient, secure multi-agency operations. | Decentralized flocking algorithms, hybrid consensus protocols (e.g., DPOS-PBFT). | [463] |
| Converged AI & Blockchain for "MEC in the Sky" | Secure the entire service chain for on-demand edge intelligence provisioned by NTN platforms, including SLA management and resource trading. | "Air Computing" or "MEC in the Sky" paradigm with UAVs, HAPs, LEO satellites as edge servers. | AI manages dynamic workload placement and resource allocation; Blockchain secures transactions and service integrity. | Smart contracts, DRL for resource trading optimization, Federated Learning (FL). | [464], [465], [466], [309], [468], [428], [469] |


### 6.5 AI-Native and Self-Evolving Network Architectures

The envisioned 6G network transcends its predecessors by moving beyond a communication-centric infrastructure to become a cognitive, self-sustaining ecosystem. This transformation is predicated on architectural paradigms where Artificial Intelligence (AI) and Blockchain are not merely add-on features but are natively and inseparably embedded into the network fabric. These AI-native and self-evolving architectures aim to deliver "intelligence inclusion," providing ubiquitous access to AI services with guaranteed trust, transparency, and autonomy [2]. A cornerstone of this vision is the reimagining of the network core to include dedicated functional planes. Beyond the traditional control and user planes, proposals introduce an independent data plane for unified data collection and governance, and, crucially, an intelligent plane. This intelligent plane is responsible for the end-to-end orchestration, lifecycle management, and operation of AI workflows, treating AI as a fundamental, manageable resource across the entire network [2]. This architectural shift enables the network to offer "everything as a service" (XaaS), where intelligence itself becomes a commoditized service—Pervasive AI-as-a-Service (PAIaaS) [34].

Achieving this vision necessitates networks capable of zero-touch operations, autonomously performing self-configuration, self-optimization, self-healing, and self-protection with minimal human intervention. This is the domain of self-evolving networks. A key enabler is the integration of Machine Learning Operations (MLOps) and Explainable AI (XAI) directly into the network slicing fabric. For instance, the concept of "SliceOps" proposes a dedicated, embedded network slice that manages the entire AI lifecycle for other slices, from continuous monitoring and re-training to the deployment of machine learning models as a service [19]. By leveraging XAI, these systems can move beyond opaque "black-box" decisions. Explanation-guided learning techniques, such as using Jensen-Shannon divergence to align model behavior with human-interpretable explanations, ensure that autonomous decisions in critical areas like resource allocation are transparent, trustworthy, and fair [131]. This transparency is vital for building trust in automated systems managing mission-critical services, transforming XAI from a diagnostic tool into a core component of responsible network automation [209].

However, the autonomy and intelligence of these native-AI systems introduce profound challenges in governance, security, and trust. This is where blockchain technology emerges as an indispensable architectural component, providing a decentralized trust layer. Blockchain's immutable ledger and smart contract capabilities are pivotal for creating verifiable audit trails for AI decisions, ensuring data provenance for training corpora, and enabling secure, traceable AI-generated content [470]. It facilitates the development of trustworthy AI marketplaces where data owners, model developers, and compute resource providers can interact without ceding ownership or privacy. Smart contracts can govern data usage agreements, automate royalty payments, and provide verifiable proof of a model's training lineage, thereby incentivizing collaboration while protecting intellectual property [55]. For decentralized AI paradigms like Federated Learning (FL), blockchain provides a secure coordination layer. It can orchestrate the FL process, aggregate model updates via smart contracts, and maintain an immutable record of participant contributions, which is crucial for fair incentive mechanisms and detecting malicious actors [471].

Furthermore, blockchain is instrumental in formalizing the governance of autonomous AI systems, particularly as foundation models and large language models become more pervasive. It addresses key governance challenges—decision rights, incentives, and accountability—by providing a platform for decentralized autonomous organizations (DAOs) or similar structures [472]. Smart contracts can encode governance policies, manage stakeholder voting on model behavior or updates, and ensure automated, tamper-proof execution of agreed-upon rules. This is especially critical for enforcing ethical AI guidelines and safety constraints across a decentralized network of AI agents. In essence, blockchain shifts the paradigm from centralized, opaque control to a decentralized, transparent, and auditable governance framework, making the "self" in self-evolving networks accountable and trustworthy [473].

The convergence of these technologies finds practical expression in advanced use cases. Digital Twin (DT)-enabled 6G networks, which create virtual replicas of physical systems for simulation and optimization, require a decentralized zero-trust security framework. Blockchain can authenticate DTs and the data they exchange, while AI provides the analytical engine for the twin, creating a secure and intelligent feedback loop between the physical and cyber worlds [350]. In smart environments and industrial IoT, hybrid blockchain-enabled microservices fabrics decompose complex systems into secure, modular, and loosely-coupled services, with blockchain ensuring immutability and auditability across domain boundaries [474]. Ultimately, the synthesis of AI-native architectures and blockchain-based trust layers paves the way for 6G to become a resilient, intelligent, and democratized platform. It promises networks that not only evolve autonomously to meet dynamic demands but do so within a framework of verifiable security, transparent operation, and decentralized governance, fulfilling the stringent requirements of future immersive and mission-critical applications [37].

**Table: Comparison of approaches in 6.5 AI-Native and Self-Evolving Network Architectures**

| Aspect | Key Concept/Paradigm | Proposed Method/Architecture | Role in 6G Vision | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Core Network Architecture | AI-Native & Self-Evolving Networks | Introduction of an independent intelligent plane for end-to-end AI workflow orchestration and management, alongside a data plane. | Transforms 6G from communication-centric to a cognitive ecosystem providing "intelligence inclusion" and XaaS. | [2] |
| Service Delivery Model | Pervasive AI-as-a-Service (PAIaaS) | Zero-touch platform for deploying AI services across 6G networks, abstracting complexity for users. | Commoditizes intelligence, enabling ubiquitous access to AI services within an XaaS framework. | [34] |
| Network Automation & Slicing | SliceOps (Explainable MLOps) | Dedicated network slice that manages the full AI lifecycle (monitoring, re-training, deployment) for other slices using MLOps and XAI. | Enables transparent, trustworthy, and automated zero-touch network management and optimization. | [19] |
| Trustworthy AI & Fairness | Explanation-Guided Federated Learning (EGFL) | Uses XAI outputs (e.g., Jensen-Shannon divergence) during federated training to align model decisions with explanations and fairness constraints. | Ensures transparent, fair, and explainable autonomous decisions in critical tasks like RAN slicing. | [131] |
| Foundational Trust Principle | Explainable AI (XAI) as Responsible AI (RAI) | Positions XAI not just for transparency but as the essential foundation for all RAI pillars (fairness, robustness, privacy, security, accountability). | Creates trustworthy and socially responsible AI systems, which is critical for mission-critical 6G services. | [209] |
| Decentralized Trust & Audit | Blockchain for AI Governance & Provenance | Uses blockchain's immutable ledger and smart contracts for verifiable AI audit trails, data provenance, and secure AI marketplaces. | Provides a decentralized trust layer for AI decisions, data, and models, enabling collaboration without ceding ownership. | [470], [55] |
| Decentralized AI Training Coordination | Blockchain for Federated Learning (FL) | Uses blockchain (e.g., consortium blockchain) as a secure coordination layer to orchestrate FL, aggregate updates, and record contributions. | Secures decentralized AI paradigms, ensures privacy, enables fair incentives, and detects malicious actors in FL. | [471] |
| Autonomous System Governance | Decentralized Governance (e.g., DAOs) via Blockchain | Leverages blockchain and smart contracts to formalize decentralized governance structures (e.g., DAOs) for foundation model-based systems. | Addresses governance challenges (decision rights, incentives, accountability) for responsible and trustworthy autonomous AI. | [472] |
| Foundational Design Principle | Blockchain as a Decentralized Trust Engine | Proposes blockchain as a synthetic solution to provide decentralized trust for privacy, security, and auditability in CPSS. | Shifts governance from centralized control to a decentralized, transparent, and accountable framework for self-evolving networks. | [473] |
| Advanced Use Case: Security | Decentralized Zero-Trust for Digital Twins | Integrates blockchain for DT authentication and data integrity with AI for analytics in a decentralized zero-trust security framework. | Creates a secure, intelligent feedback loop between physical and cyber worlds in DT-enabled 6G networks. | [350] |
| Advanced Use Case: Architecture | Hybrid Blockchain-Enabled Secure Microservices Fabric | Decomposes systems into containerized microservices secured by a hybrid blockchain fabric for immutability and auditability across domains. | Enables decentralized, secure, and efficient data fusion and operations for complex systems like avionics in 6G contexts. | [474] |
| Vision Synthesis | Converged AI-Native & Blockchain-Based Trust | Synthesizes AI-native architectures for autonomy with blockchain-based layers for decentralized trust and security. | Paves the way for 6G as a resilient, intelligent, democratized platform meeting stringent future application requirements. | [37] |


### 6.6 Virtualization and Programmable Infrastructure: SDN, NFV, and O-RAN

The realization of a programmable, agile, and efficient 6G network is fundamentally predicated on the principles of network virtualization and softwarization. Core enabling technologies such as Software-Defined Networking (SDN), Network Function Virtualization (NFV), and the Open Radio Access Network (O-RAN) architecture collectively disaggregate hardware from software, centralize network intelligence, and introduce open, standardized interfaces. This paradigm shift is essential for supporting the heterogeneous, dynamic, and stringent service requirements of 6G, including ultra-reliable low-latency communication (URLLC), massive machine-type communication (mMTC), and enhanced mobile broadband (eMBB). However, the inherent complexity, dynamism, and multi-vendor, multi-domain nature of these virtualized environments introduce significant challenges in orchestration, security, and trust management. Here, the synergistic integration of Artificial Intelligence (AI) and Blockchain technology emerges as a transformative force, enhancing the autonomy, security, and reliability of SDN, NFV, and O-RAN ecosystems.

AI, particularly through Machine Learning (ML) and Deep Reinforcement Learning (DRL), serves as the cognitive engine for the programmable infrastructure. In SDN, the logically centralized controller can leverage AI models to make real-time, optimized decisions on traffic engineering, flow routing, and network reconfiguration based on global visibility. For instance, AI can predict traffic patterns and proactively install flow rules to prevent congestion or reroute traffic during failures, moving beyond reactive, rule-based control. Within the NFV paradigm, the lifecycle management of Virtualized Network Functions (VNFs)—including instantiation, scaling, migration, and termination—becomes a complex optimization problem. AI-driven orchestration can dynamically allocate compute, storage, and networking resources across cloud, edge, and fog nodes to meet Service Level Agreements (SLAs) while minimizing operational costs and energy consumption. This is exemplified by research on predictive closed-loop service automation, where AI models forecast resource demands to prevent SLA violations in O-RAN-based network slicing [475]. Furthermore, the need for advanced intelligence in NFV Management and Orchestration (MANO) is critical to handle scalability, privacy, and concept drift, with techniques like federated learning being proposed to address these issues collaboratively [476].

The O-RAN architecture, a seminal evolution of the RAN leveraging SDN and NFV principles, explicitly embeds intelligence through its RAN Intelligent Controllers (RICs). Near-Real-Time RICs (near-RT RICs) and Non-Real-Time RICs (non-RT RICs) host AI/ML applications (xApps and rApps) that control RAN functions. AI is pivotal for tasks such as radio resource management, beamforming optimization, mobility management, and energy-saving strategies. For example, multi-agent DRL approaches can be deployed as xApps for distributed yet coordinated RAN resource allocation across multiple cells or slices [216]. However, the deployment and operation of these AI models themselves require intelligent management. Frameworks like ScalO-RAN address the challenge of dynamically scaling and placing AI-based xApps/rApps within a containerized O-Cloud to meet stringent latency requirements and optimize energy consumption [477]. The complexity introduced by AI also necessitates eXplainable AI (XAI) to build operator trust, debug misconfigurations, and ensure that the automated decisions align with network policies, a crucial area of study for O-RAN [478].

While AI provides the "brains" for automation, Blockchain provides the "trust backbone" for the open and disaggregated virtualization layer. The decentralized, immutable, and transparent ledger of Blockchain technology addresses critical security and trust deficits in SDN, NFV, and O-RAN. In SDN, the centralized controller represents a single point of failure and a lucrative target for attacks. Blockchain can decentralize critical control plane functions, such as flow rule verification and insertion. Proposals include using blockchain-as-a-service frameworks to create immutable audit trails for flow rules, ensuring that only policy-compliant rules are installed in switches and preventing malicious modifications [479]. This enhances security in SDN-enabled IoT networks, where a permissioned blockchain can provide tamper-proof logging and access control [480].

For NFV and network slicing, Blockchain introduces trust and automation into multi-domain orchestration. The lifecycle of a network slice—from creation and modification to termination—involves multiple administrative domains (e.g., different operators, cloud providers). Blockchain smart contracts can automate the slice provisioning process, enforce SLAs, and manage resource sharing agreements in a transparent and conflict-free manner. This enables secure and dynamic edge resource federation across domains, as proposed in architectures integrating network slicing and blockchain [418]. Furthermore, Blockchain can decentralize the traditionally centralized NFV Orchestrator (NFVO), mitigating single points of failure and security risks. Resource allocation for Service Function Chains (SFCs) can be managed via a decentralized ledger and smart contracts, where miners validate and record transactions for VNF deployment, creating a secure and efficient marketplace for virtual resources [481].

In the O-RAN context, Blockchain's role is multifaceted. First, it can secure the supply chain of multi-vendor, disaggregated hardware and software components. By recording hardware provenance, firmware hashes, and software bill of materials on an immutable ledger, operators can verify the authenticity and integrity of each O-RAN network function before deployment, mitigating supply chain attacks [482]. Second, Blockchain enables novel business models like RAN-as-a-Service (RANaaS), where infrastructure, spectrum, or AI models can be traded securely among mobile network operators, verticals, and third-party service providers. Smart contracts can automate reverse auctions or marketplace transactions for RAN resources, fostering a dynamic, open RAN ecosystem [483] [484]. This aligns with the vision of blockchain function virtualization (BFV), where the computationally intensive tasks of blockchain consensus and mining are virtualized and offloaded to edge/cloud servers, making blockchain participation feasible for resource-constrained network entities [165].

The convergence of AI and Blockchain within this virtualized infrastructure creates powerful synergies. Blockchain can secure the AI lifecycle in O-RAN and NFV. For instance, it can create immutable logs for AI model training data, parameters, and performance metrics, ensuring model provenance and auditability. This is crucial for debugging AI misconfigurations or conflicts between xApps, a recognized challenge in O-RAN [242]. Federated Learning (FL), a privacy-preserving AI technique ideal for distributed network data, can be integrated with Blockchain to orchestrate the learning process among distributed nodes (e.g., base stations, user equipment) without a central aggregator. Blockchain manages node registration, incentivizes participation with tokens, and securely aggregates model updates, as seen in architectures like APPFLChain [471]. Conversely, AI can optimize Blockchain operations within the network; for example, AI can predict network conditions to optimize consensus protocol parameters or smart contract execution, reducing latency and resource overhead for blockchain-enabled network services.

In conclusion, SDN, NFV, and O-RAN form the programmable bedrock of 6G networks, but their full potential is unlocked only with embedded intelligence and inherent trust. AI provides the necessary cognitive capabilities for autonomous, efficient, and adaptive control and orchestration across the virtualized infrastructure. Simultaneously, Blockchain introduces a decentralized trust layer, securing component provenance, automating multi-party agreements, and ensuring the integrity of control logic and data. Their combined application addresses the core challenges of security, complexity, and multi-stakeholder coordination, transforming the virtualized network from a merely programmable substrate into a resilient, self-organizing, and trustworthy platform for 6G's diverse and demanding services.

**Table: Comparison of approaches in 6.6 Virtualization and Programmable Infrastructure: SDN, NFV, and O-RAN**

| Technology / Paradigm | Primary Role in 6G Virtualization | Key AI/ML Applications | Key Blockchain Applications | Challenges Addressed | Reference (Source Paper) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Software-Defined Networking (SDN) | Disaggregates control & data planes, enables centralized, programmable network control. | AI models for real-time traffic engineering, flow routing, congestion prediction, and proactive network reconfiguration. | Decentralizing control plane; immutable audit trails for flow rule verification; securing SDN-enabled IoT via permissioned blockchain for access control and tamper-proof logging. | Single point of failure in controller; malicious flow rule insertion; security in IoT-cloud networks. | [479], [480] |
| Network Function Virtualization (NFV) | Decouples network functions from hardware, enabling flexible VNF lifecycle management. | AI-driven orchestration for dynamic VNF placement, scaling, and migration; predictive resource allocation to meet SLAs; Federated Learning for scalable, privacy-preserving MANO. | Decentralizing the NFV Orchestrator (NFVO) via smart contracts; automating and securing multi-domain resource allocation and SFC provisioning; enabling a secure marketplace for virtual resources. | Centralized orchestration bottlenecks; security & trust in multi-domain operations; efficient & cost-effective resource allocation. | [475], [476], [481] |
| Open RAN (O-RAN) | Disaggregated, virtualized RAN with open interfaces, managed by RAN Intelligent Controllers (RICs). | AI/ML applications (xApps/rApps) for RRM, beamforming, mobility, energy savings; Multi-agent DRL for distributed RAN slicing; XAI for operator trust and debugging. | Securing multi-vendor supply chain via provenance tracking; enabling RAN-as-a-Service (RANaaS) business models via smart contracts; Blockchain Function Virtualization (BFV) to offload consensus tasks. | Supply chain attacks; trust in multi-vendor open ecosystem; managing latency/energy of AI apps; AI misconfigurations and conflicts. | [216], [477], [478], [482], [483], [484], [165], [242] |
| Converged AI & Blockchain | Synergistic integration to provide cognitive automation and decentralized trust. | AI optimizes blockchain operations (e.g., consensus parameters); Federated Learning for distributed, private model training. | Blockchain secures the AI lifecycle (model provenance, data integrity); manages and incentivizes Federated Learning processes. | Trust in AI decisions; privacy in distributed AI; security and auditability of automated systems. | [471], [57] |
| Network Slicing (enabled by SDN/NFV/O-RAN) | Creates isolated, customized virtual networks over shared infrastructure. | Closed-loop automation for proactive SLA assurance; intelligent admission control and resource allocation across slices. | Smart contracts automate slice lifecycle management across domains; enables secure, dynamic edge resource federation. | Complex multi-domain orchestration; dynamic SLA enforcement; secure resource sharing between tenants/domains. | [418] |


## 7 Application Domains and Synergistic Use Cases

This section presents concrete applications and frameworks leveraging the combined power of Blockchain and AI across major 6G verticals. Detailed use cases include intelligent IoT/IIoT and smart cities, secure autonomous vehicle networks (V2X), privacy-preserving smart healthcare, trustworthy metaverse and immersive services, resilient post-disaster networks, and decentralized edge intelligence ecosystems.

### 7.1 Intelligent Industrial IoT (IIoT) and Smart Manufacturing

The convergence of Blockchain and Artificial Intelligence (AI) is fundamentally reshaping the landscape of Industrial Internet of Things (IIoT) and smart manufacturing, creating a foundation for secure, autonomous, and hyper-efficient industrial ecosystems. This synergy leverages AI's analytical and decision-making prowess to optimize physical operations, while blockchain provides the immutable, decentralized trust layer necessary for secure coordination among disparate, often untrusted, entities. The result is a paradigm shift from centralized, rigid automation towards decentralized, resilient, and self-optimizing smart factories.

At the core of this transformation is AI-driven predictive maintenance and process optimization. Machine learning models analyze vast streams of sensor data from manufacturing equipment to predict failures before they occur, significantly reducing downtime and maintenance costs. For instance, AI can be integrated directly within circuit design to create "digital shadows" that predict component degradation, as explored in [485]. Furthermore, multi-agent reinforcement learning (MARL) frameworks enable dynamic resource allocation and real-time optimization of production lines. Robots and automated guided vehicles (AGVs) can autonomously negotiate tasks and adapt to changing demands, as seen in systems where AI enables customized manufacturing with higher flexibility and efficiency [486]. These AI systems require high-quality, trustworthy data to function reliably, which is where blockchain becomes indispensable.

Blockchain establishes a foundational layer of trust for the IIoT by providing secure device authentication, immutable data provenance, and automated contract execution. In a smart factory with thousands of interconnected devices, blockchain can manage decentralized identity, ensuring that only authorized machines and users can access the network or specific services [487]. This is critical for preventing unauthorized access and tampering. Moreover, blockchain's immutable ledger is perfectly suited for creating trustworthy Digital Twins (DTs). A DT is a virtual replica of a physical asset or process that relies on accurate, real-time data. By recording sensor data and lifecycle events on a blockchain, the integrity and provenance of the data feeding the DT are guaranteed. This creates a reliable audit trail for quality control, compliance, and diagnostics, forming a "chain of trust" for data-driven insights [488], [448].

The automation of complex, multi-party business processes is another revolutionary application enabled by smart contracts. These self-executing contracts encode the terms of agreements between manufacturers, suppliers, and service providers. For example, a smart contract can automatically trigger payments upon verification of goods delivery or completion of a maintenance service, eliminating delays and disputes. This is particularly valuable for building hybrid business models in Industry 4.0, where workflows defined in legal contracts can be digitized and automated, as discussed in [489]. Platforms like FabRec demonstrate how a decentralized network of manufacturing nodes can share capability information and form paperless contracts via smart contracts, fostering collaboration in a trustless environment [490].

The integration reaches its full potential in frameworks that tightly couple AI and blockchain. Federated Learning (FL), a privacy-preserving AI technique, allows multiple factories or industrial entities to collaboratively train a global machine learning model without sharing their raw, sensitive data. Blockchain can orchestrate this process by securely aggregating model updates, incentivizing participation, and maintaining an immutable record of contributions. This enables collaborative predictive maintenance models across a supply chain without compromising data privacy [471]. Furthermore, AI can enhance blockchain performance within IIoT settings. AI algorithms can optimize consensus mechanisms for lower latency or manage efficient data storage strategies on the ledger, addressing scalability concerns crucial for real-time industrial applications [491].

However, deploying these integrated systems in a 6G-enabled IIoT context presents unique challenges and requirements. 6G's ultra-reliable low-latency communication (URLLC) and massive connectivity are essential for supporting real-time control loops and the dense sensor networks of smart factories. AI models for predictive maintenance or robotic control require the high bandwidth and low latency promised by 6G to process data and make decisions at the edge. Concurrently, blockchain networks must be optimized to operate efficiently within these constraints. This may involve using lightweight consensus protocols suitable for edge devices, hybrid blockchain architectures that partition data for scalability, and zero-knowledge proofs to validate transactions without revealing sensitive industrial data. The combination aims to deliver a system where AI agents can make split-second decisions based on data whose integrity is cryptographically assured by a distributed ledger.

In conclusion, the fusion of Blockchain and AI is not merely an enhancement but a necessary evolution for the next generation of intelligent IIoT and smart manufacturing. AI injects cognitive capabilities for optimization and autonomy, while blockchain provides the trust, security, and automation framework for decentralized industrial ecosystems. This powerful combination, underpinned by the high-performance connectivity of 6G networks, paves the way for fully transparent, resilient, and efficient smart factories where machines collaborate securely, processes self-optimize, and business agreements execute autonomously, ultimately driving the vision of Industry 4.0 and beyond into a tangible reality.

**Table: Comparison of approaches in 7.1 Intelligent Industrial IoT (IIoT) and Smart Manufacturing**

| Method/Model | Key Features | Application Domain | Reference |
| :--- | :--- | :--- | :--- |
| AI-driven Predictive Maintenance | Machine learning models analyze sensor data to predict equipment failures; integrated circuit design for "digital shadows" to predict component degradation. | Smart Manufacturing / IIoT | [485] |
| Multi-Agent Reinforcement Learning (MARL) | Enables dynamic resource allocation and real-time optimization; robots/AGVs autonomously negotiate tasks for customized manufacturing. | Smart Manufacturing / IIoT | [486] |
| Blockchain-based Access Control | Provides secure device authentication and decentralized identity management via smart contracts to prevent unauthorized access. | Smart Manufacturing / IIoT | [487] |
| Blockchain for Digital Twin (DT) Trust | Uses immutable ledger to guarantee data integrity and provenance for Digital Twins, creating a reliable audit trail. | Industrial Internet of Things (IIoT) | [488], [448] |
| Smart Contracts for Business Process Automation | Self-executing contracts automate multi-party agreements (e.g., payments upon delivery), digitizing workflows for hybrid business models. | Industry 4.0 / Supply Chain | [489] |
| Decentralized Manufacturing Network (FabRec) | Peer-to-peer network of manufacturing nodes sharing capability info and forming paperless contracts via smart contracts. | Manufacturing / Collaborative Production | [490] |
| Federated Learning with Blockchain (APPFLChain) | Privacy-preserving collaborative AI training; blockchain orchestrates model update aggregation and incentivizes participation. | Distributed AI / Supply Chain | [471] |
| AI-Optimized Blockchain for IIoT | AI algorithms optimize blockchain consensus mechanisms and data storage for lower latency and scalability in industrial settings. | Smart Industry / Cyber-Physical Systems | [491] |


### 7.2 Secure and Autonomous Vehicular Networks (V2X)

The realization of secure, efficient, and truly autonomous vehicular networks is a cornerstone of the 6G vision for intelligent transportation systems (ITS). Vehicle-to-Everything (V2X) communication, encompassing Vehicle-to-Vehicle (V2V), Vehicle-to-Infrastructure (V2I), Vehicle-to-Network (V2N), and Vehicle-to-Pedestrian (V2P) links, generates a massive, dynamic, and sensitive data ecosystem. This environment demands unprecedented levels of security, trust, low-latency decision-making, and robust resource management. The synergistic fusion of blockchain and artificial intelligence (AI) emerges as a transformative paradigm to address these multifaceted challenges, moving beyond isolated solutions to create holistic, resilient, and intelligent V2X frameworks.

Blockchain technology provides the foundational trust layer for decentralized V2X operations. Its immutable ledger and consensus mechanisms are instrumental in securing critical vehicular processes against tampering and single points of failure. For instance, secure firmware and software updates for autonomous vehicles (AVs), which are vital for patching vulnerabilities, can be managed via a consortium blockchain formed by manufacturers. As detailed in [90], such a scheme uses smart contracts to ensure the authenticity and integrity of updates, while incentivizing other AVs to act as distributors, leveraging their mobility for efficient delivery. Similarly, blockchain establishes trust in data provenance and sharing. Frameworks like the Intelligent Vehicle-Trust Point (IV-TP) mechanism [492] and the broader Intelligent Vehicle data sharing framework [493] utilize blockchain to create a reward-based system for trustworthy behavior, recording vehicle actions and reputations immutably. This extends to managing sensitive records like Vehicle Health Records (VHR) in a system such as V-CARE [494], enabling multi-stakeholder access (owners, insurers, mechanics) in a secure, transparent, and permissioned manner. For autonomous systems beyond road vehicles, blockchain also secures communication in networks of Automated Guided Vehicles (AGVs) [495] and integrates with robot operating systems (ROS) for trusted industrial applications [496].

While blockchain provides trust in data and transactions, AI supplies the cognitive intelligence needed for real-time perception, optimization, and security analytics in highly dynamic vehicular environments. Machine learning (ML), and particularly deep learning, is crucial for collaborative perception, which fuses sensor data from multiple vehicles and roadside units (RSUs) to create a comprehensive, beyond-line-of-sight understanding of the environment. Datasets and benchmarks like V2X-Sim [497] and V2X-Real [498] are vital for developing these AI models. Advanced frameworks employ vision transformers (ViTs) for robust multi-agent feature fusion, as seen in V2X-ViT [499], or address domain gaps between simulation and reality and between heterogeneous agents using domain-invariant learning techniques like DI-V2X [500]. For decision-making and control, Deep Reinforcement Learning (DRL) is extensively applied. It optimizes complex, sequential decisions such as resource allocation in spectrum-sharing scenarios between V2V and V2I links [501], or manages vertical handovers between different radio access technologies (RATs) to maintain communication redundancy and reliability [502]. AI also directly enhances security; statistical detectors can be integrated to identify adversarial examples designed to poison or evade ML-based Intrusion Detection Systems (IDS) [503].

The most significant advancements occur where blockchain and AI are interwoven to create mutually reinforcing systems. A prime example is the application of blockchain to secure and orchestrate federated learning (FL) processes within V2X networks. FL allows vehicles to collaboratively train ML models (e.g., for anomaly detection or traffic prediction) without sharing raw, private data. Blockchain manages this process by providing a transparent and tamper-proof record of model updates, participant contributions, and incentive distributions. The Blockchain-based Federated Forest (BFF) approach for IDS [503] exemplifies this, where the blockchain protects data confidentiality and model integrity during collaborative training. Furthermore, AI optimizes blockchain operations themselves, creating efficient and scalable V2X systems. Multi-Agent Reinforcement Learning can be used to design incentive mechanisms and deployment strategies for UAV-assisted blockchain networks that secure IoT data collection [461]. DRL can also optimize peer selection in permissioned blockchains like Hyperledger Fabric within V2X networks to maintain security despite vehicle mobility [504].

This fusion also addresses critical privacy and nuanced trust issues. Zero-knowledge proofs (ZKPs), often facilitated by blockchain frameworks, can enable privacy-preserving authentication and data exchange. Concepts like Proof-of-Travel (POT) [505] use cryptographic proofs of a vehicle's movement, attested by infrastructure, to establish reputation without revealing detailed trajectory data. For fine-grained security, fuzzy logic systems can be integrated with blockchain to analyze vehicle behavior and detect false data injection attacks in a more interpretable manner [506]. Looking ahead, the integration of generative AI introduces new frontiers, such as creating synthetic data for training, simulating rare traffic scenarios, or optimizing semantic communication for more efficient V2X information exchange [507]. The confluence of these technologies also paves the way for novel paradigms like the vehicular metaverse, where blockchain secures the migration and trading of digital twin resources (e.g., Vehicle Twins) between RSUs and vehicles [508].

However, the path forward is laden with challenges. The computational and latency overhead of consensus mechanisms must be minimized to meet the ultra-reliable low-latency communication (URLLC) demands of safety-critical V2X applications. Solutions like lightweight consensus protocols [509] and efficient data structures such as Directed Acyclic Graphs (DAGs) [510] are being explored. The scalability of blockchain-AI systems to support dense urban vehicular networks remains a significant hurdle. Furthermore, the advent of quantum computing poses a long-term threat to the cryptographic primitives underlying both blockchain and AI security, as demonstrated by research into quantum impersonation attacks on blockchain-based VANETs [511], necessitating a shift towards post-quantum cryptography. Finally, achieving true interoperability between heterogeneous V2X technologies, legacy systems, and non-connected road users requires innovative architectural solutions, such as Augmenting V2X Roadside Units (A-RSUs) [512]. In conclusion, the fusion of blockchain and AI is not merely an enhancement but a necessary evolution for V2X networks in the 6G era. It creates a virtuous cycle where blockchain provides the trusted, auditable data foundation upon which AI models can reliably operate, and AI, in turn, enables the intelligent, adaptive, and efficient management of the blockchain-secured vehicular ecosystem, ultimately steering us towards safer, more efficient, and fully autonomous transportation.

**Table: Comparison of approaches in 7.2 Secure and Autonomous Vehicular Networks (V2X)**

| Technology Category | Specific Method / Framework / Concept | Primary Application / Purpose in V2X | Key Mechanism / Approach | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Blockchain | Consortium Blockchain for Firmware Updates | Secure and efficient firmware/software updates for Autonomous Vehicles (AVs) | Uses smart contracts on a manufacturer consortium blockchain to ensure authenticity/integrity; incentivizes AVs to act as mobile distributors using a credit reputation system. | [90] |
| Blockchain | Intelligent Vehicle-Trust Point (IV-TP) | Establishing trust and rewarding trustworthy behavior in IV communication | A reward-based system using blockchain to immutably record vehicle actions and reputations, exchanging IV-TP points during successful communication. | [492] |
| Blockchain | Intelligent Vehicle Data Sharing Framework | Secure and reliable data sharing among intelligent vehicles | Uses blockchain as a backbone to create a trusted data-sharing environment based on proof of driving. | [493] |
| Blockchain | V-CARE Framework | Secure multi-stakeholder management of Vehicle Health Records (VHR) | A blockchain-based decentralized system for managing VHR, enabling secure, transparent, and permissioned access for owners, insurers, mechanics, etc. | [494] |
| Blockchain | Data Transmission for AGVs | Secure collaboration and data sharing for Automated Guided Vehicles (AGVs) | Integrates blockchain with Named Data Networking (NDN) principles for efficient and secure data querying and sharing among a fleet of AGVs. | [495] |
| Blockchain | Hyperledger Fabric & ROS 2 Integration | Trusted data aggregation and control for Autonomous Mobile Robots | Integrates Hyperledger Fabric blockchain with the Robot Operating System (ROS 2) for secure identity management, data control, and processing in industrial robotic applications. | [496] |
| AI / Machine Learning | V2X-Sim Dataset & Benchmark | Developing AI models for multi-agent collaborative perception | A comprehensive simulated multi-agent perception dataset supporting tasks like detection, tracking, and segmentation for V2X-aided autonomous driving. | [497] |
| AI / Machine Learning | V2X-Real Dataset | Real-world cooperative perception for V2X | A large-scale real-world dataset with LiDAR and camera data from vehicles and infrastructure to facilitate V2X cooperative perception research. | [498] |
| AI / Machine Learning | V2X-ViT (Vision Transformer) | Robust multi-agent cooperative perception | A vision Transformer-based model using heterogeneous multi-agent self-attention and multi-scale window self-attention to effectively fuse information across vehicles and infrastructure. | [499] |
| AI / Machine Learning | DI-V2X | Domain-invariant collaborative 3D object detection for V2X | A distillation framework with domain-mixing instance augmentation and progressive distillation to learn domain-invariant representations, mitigating sensor heterogeneity gaps between vehicles and infrastructure. | [500] |
| AI / Machine Learning | Deep Reinforcement Learning for STAR-RIS | Joint spectrum allocation and RIS configuration for V2X | Uses a combined Double Deep Q-Network (DDQN) with attention mechanism to optimize spectrum allocation, STAR-RIS parameters, and beamforming to maximize V2I data rate while meeting V2V latency/reliability requirements. | [501] |
| AI / Machine Learning | Deep Reinforcement Learning for Hybrid V2X | Optimal vertical handover between multiple Radio Access Technologies (RATs) | Applies DRL algorithms to manage vertical handovers (e.g., between DSRC and V-VLC) to maintain communication redundancy and reliability in dynamic vehicular environments. | [502] |
| AI / Machine Learning | Statistical Adversarial Detector in BFF-IDS | Enhancing security of blockchain-based federated intrusion detection systems | Integrates a statistical detector to identify adversarial examples (evasion, poisoning attacks) in a Blockchain-based Federated Forest IDS, augmenting the model with detected samples for sustained security. | [503] |
| Blockchain & AI Fusion | Blockchain-based Federated Forest (BFF) for IDS | Secure, collaborative intrusion detection training | Uses blockchain to secure the federated learning process for training ML-based IDS models, protecting data confidentiality and model integrity while enabling collaborative learning from multiple IoV entities. | [503] |
| Blockchain & AI Fusion | Multi-Agent RL for UAV Blockchain Incentives | Optimizing incentive and deployment for UAV-assisted secure IoT data collection | Uses Multi-Agent Deep Deterministic Policy Gradient (MADDPG) to design stake investment and profit-sharing strategies, optimizing UAV deployment and blockchain incentives for secure data collection. | [461] |
| Blockchain & AI Fusion | RL for Peer Selection in Hyperledger Fabric | Optimizing peer selection in permissioned V2X blockchains under mobility | Models peer selection in Hyperledger Fabric as a contextual Multi-Armed Bandit problem solved with Reinforcement Learning to maintain Byzantine fault tolerance despite vehicle mobility. | [504] |
| Privacy & Advanced Trust | Proof-of-Travel (POT) | Privacy-preserving, trust-based data validation for V2I | Uses cryptographic proofs of a vehicle's movement (attested by infrastructure signatures) to build reputation and validate data trustworthiness without revealing detailed trajectory data. | [505] |
| Privacy & Advanced Trust | Blockchain & Fuzzy Logic for False Data Discovery | Detecting false data injection attacks in autonomous vehicular systems | Integrates fuzzy logic with blockchain at Road-side Units to analyze vehicle behavior and filter false/anomalous data before authorization on the blockchain network. | [506] |
| Emerging Paradigms | Generative AI-enabled Vehicular Networks | Enhancing V2X with data generation, simulation, and semantic communication | Proposes a multi-modality semantic-aware framework leveraging generative AI for applications like synthetic data generation, traffic scenario simulation, and optimized semantic communication. | [507] |
| Emerging Paradigms | Blockchain-assisted Twin Migration for Vehicular Metaverses | Secure migration and trading of Vehicle Twin (VT) resources | Uses a coalition game based on RSU reputation and a Stackelberg model to form RSU coalitions and incentivize VMUs, secured by blockchain, for reliable large-scale VT migration. | [508] |
| Challenges & Enablers | Lightweight Consensus & DAGs | Addressing blockchain latency and scalability for V2X | Explores lightweight consensus protocols (e.g., reputation-based) and efficient data structures like Directed Acyclic Graphs (DAGs) for scalable and low-latency knowledge sharing. | [509], [510] |
| Challenges & Enablers | Quantum Impersonation Attack Analysis | Highlighting long-term cryptographic threats to blockchain-based VANETs | Demonstrates a quantum impersonation attack using Shor's algorithm to break RSA-encrypted digital signatures in a blockchain-based VANET, emphasizing the need for post-quantum cryptography. | [511] |
| Challenges & Enablers | Augmenting V2X Roadside Units (A-RSUs) | Enhancing cooperative awareness for heterogeneous road users | Proposes A-RSUs as a concept to establish pervasive cooperative awareness by accommodating both V2X-enabled and non-V2X-enabled road users through compatible communication channels. | [512] |



## References
[1] The Journey Towards 6G  A Digital and Societal Revolution in the Making

[2] Toward Native Artificial Intelligence in 6G Networks  System Design,   Architectures, and Paradigms

[3] Five Facets of 6G  Research Challenges and Opportunities

[4] The Roadmap to 6G -- AI Empowered Wireless Networks

[5] 6G  Connectivity in the Era of Distributed Intelligence

[6] Towards 6G Hyper-Connectivity  Vision, Challenges, and Key Enabling   Technologies

[7] Toward 6G TK$μ$ Extreme Connectivity  Architecture, Key Technologies   and Experiments

[8] Development of A Fully Data-Driven Artificial Intelligence and Deep   Learning for URLLC Application in 6G Wireless Systems  A Survey

[9] A Functional Architecture for 6G Special Purpose Industrial IoT Networks

[10] 6G Communication  Envisioning the Key Issues and Challenges

[11] Energy Self-Sustainability in Full-Spectrum 6G

[12] Toward Immersive Communications in 6G

[13] 6G Mobile-Edge Empowered Metaverse  Requirements, Technologies,   Challenges and Research Directions

[14] When Internet of Things meets Metaverse  Convergence of Physical and   Cyber Worlds

[15] Metaverse for Wireless Systems  Vision, Enablers, Architecture, and   Future Directions

[16] 6G V2X Technologies and Orchestrated Sensing for Autonomous Driving

[17] 6G Positioning and Sensing Through the Lens of Sustainability,   Inclusiveness, and Trustworthiness

[18] Blockchain-enabled Resource Management and Sharing for 6G Communications

[19] SliceOps  Explainable MLOps for Streamlined Automation-Native 6G   Networks

[20] 6G opens up a New Era for Aeronautical Communication and Services

[21] Integrating Satellites and Mobile Edge Computing for 6G Wide-Area Edge   Intelligence  Minimal Structures and Systematic Thinking

[22] 6AInets  Harnessing artificial intelligence for the 6G network security    Impacts and Challenges

[23] Security and privacy for 6G  A survey on prospective technologies and   challenges

[24] Adversarial Attacks and Defenses in 6G Network-Assisted IoT Systems

[25] Edge Learning for 6G-enabled Internet of Things  A Comprehensive Survey   of Vulnerabilities, Datasets, and Defenses

[26] What Physical Layer Security Can Do for 6G Security

[27] Context-Aware Security for 6G Wireless The Role of Physical Layer   Security

[28] Physical Layer Security for 6G Systems why it is needed and how to make   it happen

[29] La Résistance  Harnessing Heterogeneous Resources for Adaptive   Resiliency in 6G Networks

[30] Distributed Sensing, Computing, Communication, and Control Fabric  A   Unified Service-Level Architecture for 6G

[31] Task-Oriented Communications for 6G  Vision, Principles, and   Technologies

[32] Towards Deterministic Communications in 6G Networks  State of the Art,   Open Challenges and the Way Forward

[33] How Crucial Is It for 6G Networks to Be Autonomous 

[34] Zero-touch realization of Pervasive Artificial Intelligence-as-a-service   in 6G networks

[35] Evolution Toward 6G Wireless Networks  A Resource Management Perspective

[36] Toward Experience-Driven Traffic Management and Orchestration in   Digital-Twin-Enabled 6G Networks

[37] Blockchain and 6G  The Future of Secure and Ubiquitous Communication

[38] The Confluence of Blockchain and 6G Network  Scenarios Analysis and   Performance Assessment

[39] Internet of Intelligence  The Collective Advantage for Advancing   Communications and Intelligence

[40] 6G Wireless Communication Systems  Applications, Requirements,   Technologies, Challenges, and Research Directions

[41] Self-Evolving Integrated Vertical Heterogeneous Networks

[42] Edge Artificial Intelligence for 6G  Vision, Enabling Technologies, and   Applications

[43] AI-enabled Future Wireless Networks  Challenges, Opportunities and Open   Issues

[44] AI Empowered Net-RCA for 6G

[45] 6G Network AI Architecture for Everyone-Centric Customized Services

[46] Explainable Artificial Intelligence (XAI) for 6G  Improving Trust   between Human and Machine

[47] Scalable and Secure Architecture for Distributed IoT Systems

[48] Advancing Federated Learning in 6G  A Trusted Architecture with   Graph-based Analysis

[49] Holistic Network Virtualization and Pervasive Network Intelligence for   6G

[50] Rapid Prototyping of a Text Mining Application for Cryptocurrency Market   Intelligence

[51] Federated Learning using Smart Contracts on Blockchains, based on Reward   Driven Approach

[52] Trustworthy Federated Learning via Blockchain

[53] zkDFL  An efficient and privacy-preserving decentralized federated   learning with zero-knowledge proof

[54] Decentralized Energy Marketplace via NFTs and AI-based Agents

[55] Ownership preserving AI Market Places using Blockchain

[56] Proof-of-Useful-Work as Dual-Purpose Mechanism for Blockchain and AI    Blockchain Consensus that Enables Privacy Preserving Data Mining

[57] Blockchain Framework for Artificial Intelligence Computation

[58] AICons  An AI-Enabled Consensus Algorithm Driven by Energy Preservation   and Fairness

[59] Transaction Confirmation Time Prediction in Ethereum Blockchain Using   Machine Learning

[60] Blockchain Intelligence  When Blockchain Meets Artificial Intelligence

[61] Leveraging Machine Learning for Multichain DeFi Fraud Detection

[62] Secure and Efficient Federated Learning Through Layering and Sharding   Blockchain

[63] Rationality-proof consensus  extended abstract

[64] TIPS  Transaction Inclusion Protocol with Signaling in DAG-based   Blockchain

[65] Sharding-Based Proof-of-Stake Blockchain Protocols  Security Analysis

[66] Towards Scaling Blockchain Systems via Sharding

[67] Front-running Attack in Sharded Blockchains and Fair Cross-shard   Consensus

[68] Kronos  A Robust Sharding Blockchain Consensus with Optimal   Communication Overhead

[69] Consensus Mechanism Design based on Structured Directed Acyclic Graphs

[70] Trust-Worthy Semantic Communications for the Metaverse Relying on   Federated Learning

[71] GHAST  Breaking Confirmation Delay Barrier in Nakamoto Consensus via   Adaptive Weighted Blocks

[72] Zero-Knowledge Proof-based Practical Federated Learning on Blockchain

[73] Privacy-Preserving in Blockchain-based Federated Learning Systems

[74] A context-aware multiple Blockchain architecture for managing low memory   devices

[75] 6G Network Business Support System

[76] A Novel Channel-Constrained Model for 6G Vehicular Networks with Traffic   Spikes

[77] Blockchain-based Federated Learning with Secure Aggregation in Trusted   Execution Environment for Internet-of-Things

[78] FLoW3 -- Web3 Empowered Federated Learning

[79] Decentralized Healthcare Systems with Federated Learning and Blockchain

[80] Deploying ZKP Frameworks with Real-World Data  Challenges and Proposed   Solutions

[81] zk-IoT  Securing the Internet of Things with Zero-Knowledge Proofs on   Blockchain Platforms

[82] Delayed Blockchain Protocols

[83] Incentive Attacks on DAG-Based Blockchains with Random Transaction   Selection

[84] Secure, Robust, and Energy-Efficient Authenticated Data Sharing in   UAV-Assisted 6G Networks

[85] Parallel and Asynchronous Smart Contract Execution

[86] Blockchain for Internet of Things  A Survey

[87] Mobile Edge Computing and AI Enabled Web3 Metaverse over 6G Wireless   Communications  A Deep Reinforcement Learning Approach

[88] Blockchain-empowered Federated Learning for Healthcare Metaverses    User-centric Incentive Mechanism with Optimal Data Freshness

[89] FedBlockHealth  A Synergistic Approach to Privacy and Security in   IoT-Enabled Healthcare through Federated Learning and Blockchain

[90] Blockchain-based Firmware Update Scheme Tailored for Autonomous Vehicles

[91] FedDefender  Backdoor Attack Defense in Federated Learning

[92] THz-Empowered UAVs in 6G  Opportunities, Challenges, and Trade-Offs

[93] Streamlined Transmission  A Semantic-Aware XR Deployment Framework   Enhanced by Generative AI

[94] From Data to Action  Exploring AI and IoT-driven Solutions for Smarter   Cities

[95] Energy-Efficient Design for IRS-Assisted MEC Networks with NOMA

[96] A Multi-Agent Deep Reinforcement Learning Approach for RAN Resource   Allocation in O-RAN

[97] Leveraging Federated Learning and Edge Computing for Recommendation   Systems within Cloud Computing Networks

[98] Learning Quantum Processes with Quantum Statistical Queries

[99] Cross-Consensus Measurement of Individual-level Decentralization in   Blockchains

[100] A Secure Federated Learning Framework for 5G Networks

[101] Generative AI for Immersive Communication  The Next Frontier in   Internet-of-Senses Through 6G

[102] Large AI Model-Based Semantic Communications

[103] Large Generative Model Assisted 3D Semantic Communication

[104] Task-Oriented Integrated Sensing, Computation and Communication for   Wireless Edge AI

[105] Adaptive Resource Allocation for Semantic Communication Networks

[106] Towards Bridging the FL Performance-Explainability Trade-Off  A   Trustworthy 6G RAN Slicing Use-Case

[107] Stable and Interpretable Deep Learning for Tabular Data  Introducing   InterpreTabNet with the Novel InterpreStability Metric

[108] FLEX  FLEXible Federated Learning Framework

[109] Metaverse  A Vision, Architectural Elements, and Future Directions for   Scalable and Realtime Virtual Worlds

[110] Towards quantum enhanced adversarial robustness in machine learning

[111] Poisoning Attacks in Federated Edge Learning for Digital Twin 6G-enabled   IoTs  An Anticipatory Study

[112] Federated Learning for Computationally-Constrained Heterogeneous   Devices  A Survey

[113] Federated Learning for Privacy Preservation in Smart Healthcare Systems    A Comprehensive Survey

[114] Parallel Proof-of-Work with DAG-Style Voting and Targeted Reward   Discounting

[115] A Unified Framework for Integrating Semantic Communication and   AI-Generated Content in Metaverse

[116] GainNet  Coordinates the Odd Couple of Generative AI and 6G Networks

[117] OGMP  Oracle Guided Multimodal Policies for Agile and Versatile Robot   Control

[118] Applications of Reinforcement Learning in Deregulated Power Market  A   Comprehensive Review

[119] Energy-Efficient Blockchain-enabled User-Centric Mobile Edge Computing

[120] The Fusion of Deep Reinforcement Learning and Edge Computing for   Real-time Monitoring and Control Optimization in IoT Environments

[121] Trustworthy Privacy-preserving Hierarchical Ensemble and Federated   Learning in Healthcare 4.0 with Blockchain

[122] Trustless Privacy-Preserving Data Aggregation on Ethereum with Hypercube   Network Topology

[123] Enhancing Scalability and Reliability in Semi-Decentralized Federated   Learning With Blockchain  Trust Penalization and Asynchronous Functionality

[124] Non-Disclosing Credential On-chaining for Blockchain-based Decentralized   Applications

[125] Digital Healthcare in The Metaverse  Insights into Privacy and Security

[126] Securing the Skies  An IRS-Assisted AoI-Aware Secure Multi-UAV System   with Efficient Task Offloading

[127] Security and Privacy Enhancing in Blockchain-based IoT Environments via   Anonym Auditing

[128] Detection and Prevention Against Poisoning Attacks in Federated Learning

[129] Amplification of Addictive New Media Features in the Metaverse

[130] RIS-Based On-the-Air Semantic Communications -- a Diffractional Deep   Neural Network Approach

[131] Explanation-Guided Fair Federated Learning for Transparent 6G RAN   Slicing

[132] Resource Allocation for Secure Ultra-Reliable Low-Latency-Communication   in IoT Applications

[133] Immersive Media and Massive Twinning  Advancing Towards the Metaverse

[134] A Survey of Machine Learning Algorithms for 6G Wireless Networks

[135] The Energy Footprint of Blockchain Consensus Mechanisms Beyond   Proof-of-Work

[136] BEAT  Blockchain-Enabled Accountable and Transparent Network Sharing in   6G

[137] Fed-DDM  A Federated Ledgers based Framework for Hierarchical   Decentralized Data Marketplaces

[138] Connecting AI Learning and Blockchain Mining in 6G Systems

[139] Unsealing the secrets of blockchain consensus  A systematic comparison   of the formal security of proof-of-work and proof-of-stake

[140] Performance Analysis and Comparison of Non-ideal Wireless PBFT and RAFT   Consensus Networks in 6G Communications

[141] Performance Analysis of Non-ideal Wireless PBFT Networks with mmWave and   Terahertz Signals

[142] Proof-of-Reputation  An Alternative Consensus Mechanism for Blockchain   Systems

[143] Towards Blockchain-based Trust and Reputation Management for Trustworthy   6G Networks

[144] PoAh  A Novel Consensus Algorithm for Fast Scalable Private Blockchain   for Large-scale IoT Frameworks

[145] Direct Acyclic Graph based Ledger for Internet of Things  Performance   and Security Analysis

[146] StakeDag  Stake-based Consensus For Scalable Trustless Systems

[147] Symbiotic Blockchain Consensus  Cognitive Backscatter   Communications-enabled Wireless Blockchain Consensus

[148] Performance evaluation of Private and Public Blockchains for multi-cloud   service federation

[149] On performance of PBFT for IoT-applications with constrained devices

[150] Intelligent Blockchain-based Edge Computing via Deep Reinforcement   Learning  Solutions and Challenges

[151] State sharding model on the blockchain

[152] A Flexible n 2 Adversary Node Resistant and Halting Recoverable   Blockchain Sharding Protocol

[153] A $p 2$ Adversary Power Resistant Blockchain Sharding Approach

[154] Efficient Cross-Shard Transaction Execution in Sharded Blockchains

[155] Denial-of-Service Vulnerability of Hash-based Transaction Sharding    Attack and Countermeasure

[156] Divide and Scale  Formalization and Roadmap to Robust Sharding

[157] Building Blocks of Sharding Blockchain Systems  Concepts, Approaches,   and Open Problems

[158] Layer 2 Blockchain Scaling  a Survey

[159] Rapido  A Layer2 Payment System for Decentralized Currencies

[160] StreamNet  A DAG System with Streaming Graph Computing

[161] DAG-Oriented Protocols PHANTOM and GHOSTDAG under Incentive Attack via   Transaction Selection Strategy

[162] Distributed Ledger Technology for IoT  Parasite Chain Attacks

[163] A Novel Two-Layer DAG-based Reactive Protocol for IoT Data Reliability   in Metaverse

[164] Towards Mobile Distributed Ledgers

[165] Blockchain Function Virtualization  A New Approach for Mobile Networks   Beyond 5G

[166] Smart Contract Templates  foundations, design landscape and research   directions

[167] Can We Effectively Use Smart Contracts to Stipulate Time Constraints 

[168] Bandcoin  Using Smart Contracts to Automate Mobile Network Bandwidth   Roaming Agreements

[169] Smart Contract SLAs for Dense Small-Cell-as-a-Service

[170] How to Design Autonomous Service Level Agreements for 6G

[171] Lazy Contracts  Alleviating High Gas Costs by Secure and Trustless   Off-chain Execution of Smart Contracts

[172] Scalable and Privacy-preserving Design of On Off-chain Smart Contracts

[173] OV  Validity-based Optimistic Smart Contracts

[174] Smart Contract Upgradeability on the Ethereum Blockchain Platform  An   Exploratory Study

[175] Annotary  A Concolic Execution System for Developing Secure Smart   Contracts

[176] Smart Contract Vulnerability Detection Technique  A Survey

[177] Smart Contract Repair

[178] Building Executable Secure Design Models for Smart Contracts with Formal   Methods

[179] Agatha  Smart Contract for DNN Computation

[180] Explanation-Guided Deep Reinforcement Learning for Trustworthy 6G RAN   Slicing

[181] Deep Learning for Radio Resource Allocation in Multi-Cell Networks

[182] Federated Learning for 5G Base Station Traffic Forecasting

[183] Implicit Channel Learning for Machine Learning Applications in 6G   Wireless Networks

[184] Transformer-Empowered 6G Intelligent Networks  From Massive MIMO   Processing to Semantic Communication

[185] Multi-agent Reinforcement Learning for Dynamic Resource Management in 6G   in-X Subnetworks

[186] Single and Multi-Agent Deep Reinforcement Learning for AI-Enabled   Wireless Networks  A Tutorial

[187] Dual Attention-Based Federated Learning for Wireless Traffic Prediction

[188] ML-Assisted UE Positioning  Performance Analysis and 5G Architecture   Enhancements

[189] 5G-NIDD  A Comprehensive Network Intrusion Detection Dataset Generated   over 5G Wireless Network

[190] Towards Ubiquitous AI in 6G with Federated Learning

[191] Split Federated Learning for 6G Enabled-Networks  Requirements,   Challenges and Future Directions

[192] Federated Deep Reinforcement Learning for the Distributed Control of   NextG Wireless Networks

[193] At the Dawn of Generative AI Era  A Tutorial-cum-Survey on New Frontiers   in 6G Wireless Intelligence

[194] Wireless Network Digital Twin for 6G  Generative AI as A Key Enabler

[195] Large Generative AI Models for Telecom  The Next Big Thing 

[196] 6G Networks  Beyond Shannon Towards Semantic and Goal-Oriented   Communications

[197] Semantic Communications for Image Recovery and Classification via Deep   Joint Source and Channel Coding

[198] A Wireless AI-Generated Content (AIGC) Provisioning Framework Empowered   by Semantic Communication

[199] Integrated Sensing-Communication-Computation for Edge Artificial   Intelligence

[200] Twelve Scientific Challenges for 6G  Rethinking the Foundations of   Communications Theory

[201] Pragmatic Goal-Oriented Communications under Semantic-Effectiveness   Channel Errors

[202] Neuro-Symbolic Artificial Intelligence (AI) for Intent based Semantic   Communication

[203] Knowledge Base Enabled Semantic Communication  A Generative Perspective

[204] A Survey on Semantic Communications for Intelligent Wireless Networks

[205] A Joint Framework to Privacy-Preserving Edge Intelligence in Vehicular   Networks

[206] Privacy Meets Explainability  A Comprehensive Impact Benchmark

[207] TRUST XAI  Model-Agnostic Explanations for AI With a Case Study on IIoT   Security

[208] TEFL  Turbo Explainable Federated Learning for 6G Trustworthy Zero-Touch   Network Slicing

[209] Explainable AI is Responsible AI  How Explainability Creates Trustworthy   and Socially Responsible Artificial Intelligence

[210] Understanding the (Extra-)Ordinary  Validating Deep Model Decisions with   Prototypical Concept-based Explanations

[211] AUTOLYCUS  Exploiting Explainable AI (XAI) for Model Extraction Attacks   against White-Box Models

[212] Confidential Federated Computations

[213] AIaaS for ORAN-based 6G Networks  Multi-time Scale Slice Resource   Management with DRL

[214] Reinforcement Learning Based Resource Allocation for Network Slices in   O-RAN Midhaul

[215] Network Slicing with MEC and Deep Reinforcement Learning for the   Internet of Vehicles

[216] On the Specialization of FDRL Agents for Scalable and Distributed 6G RAN   Slicing Orchestration

[217] Graph Attention Network-based Multi-agent Reinforcement Learning for   Slicing Resource Management in Dense Cellular Network

[218] Inter-Cell Network Slicing With Transfer Learning Empowered Multi-Agent   Deep Reinforcement Learning

[219] A Collaborative Statistical Actor-Critic Learning Approach for 6G   Network Slicing Control

[220] Actor-Critic-Based Learning for Zero-touch Joint Resource and Energy   Control in Network Slicing

[221] Zero-touch Continuous Network Slicing Control via Scalable Actor-Critic   Learning

[222] Safe and Accelerated Deep Reinforcement Learning-based O-RAN Slicing  A   Hybrid Transfer Learning Approach

[223] How Does Forecasting Affect the Convergence of DRL Techniques in O-RAN   Slicing 

[224] Advancing RAN Slicing with Offline Reinforcement Learning

[225] MR-iNet Gym  Framework for Edge Deployment of Deep Reinforcement   Learning on Embedded Software Defined Radio

[226] EdgeSlice  Slicing Wireless Edge Computing Network with Decentralized   Deep Reinforcement Learning

[227] Edge Intelligence for Energy-efficient Computation Offloading and   Resource Allocation in 5G Beyond

[228] Efficient Embedding VNFs in 5G Network Slicing  A Deep Reinforcement   Learning Approach

[229] Reconfigurable Intelligent Surface Assisted Multiuser MISO Systems   Exploiting Deep Reinforcement Learning

[230] Max-Min SINR Analysis of STAR-RIS Assisted Massive MIMO Systems with   Hardware Impairments

[231] Beamforming Design and Performance Evaluation for Reconfigurable   Intelligent Surface Assisted Wireless Communication Systems With Non-Ideal   Hardware

[232] CaRL  Cascade Reinforcement Learning with State Space Splitting for   O-RAN based Traffic Steering

[233] Programmable and Customized Intelligence for Traffic Steering in 5G   Networks Using Open RAN Architectures

[234] A Comparative Analysis of Deep Reinforcement Learning-based xApps in   O-RAN

[235] Team Learning-Based Resource Allocation for Open Radio Access Network   (O-RAN)

[236] ChARM  NextG Spectrum Sharing Through Data-Driven Real-Time O-RAN   Dynamic Control

[237] Sim2real for Reinforcement Learning Driven Next Generation Networks

[238] AI Testing Framework for Next-G O-RAN Networks  Requirements, Design,   and Research Opportunities

[239] Colosseum  The Open RAN Digital Twin

[240] OpenRAN Gym  An Open Toolbox for Data Collection and Experimentation   with AI in O-RAN

[241] Conflict Management in the Near-RT-RIC of Open RAN  A Game Theoretic   Approach

[242] Misconfiguration in O-RAN  Analysis of the impact of AI ML

[243] Intent-driven Intelligent Control and Orchestration in O-RAN Via   Hierarchical Reinforcement Learning

[244] Experimental Study of Adversarial Attacks on ML-based xApps in O-RAN

[245] System-level Analysis of Adversarial Attacks and Defenses on   Intelligence in O-RAN based Cellular Networks

[246] dApps  Distributed Applications for Real-time Inference and Control in   O-RAN

[247] Learning at the Speed of Wireless  Online Real-Time Learning for   AI-Enabled MIMO in NextG

[248] NeuroRIS  Neuromorphic-Inspired Metasurfaces

[249] Enhancing Semantic Communication with Deep Generative Models -- An   ICASSP Special Session Overview

[250] Semantic Communications With AI Tasks

[251] Less Data, More Knowledge  Building Next Generation Semantic   Communication Networks

[252] Generative AI for Semantic Communication  Architecture, Challenges, and   Outlook

[253] AI-enabled mm-Waveform Configuration for Autonomous Vehicles with   Integrated Communication and Sensing

[254] Integrated Sensing and Communication Driven Digital Twin for Intelligent   Machine Network

[255] Interplay between RIS and AI in Wireless Communications  Fundamentals,   Architectures, Applications, and Open Research Problems

[256] Pervasive AI for IoT applications  A Survey on Resource-efficient   Distributed Artificial Intelligence

[257] The Internet of Senses  Building on Semantic Communications and Edge   Intelligence

[258] The Interplay of AI and Digital Twin  Bridging the Gap between   Data-Driven and Model-Driven Approaches

[259] Digital Twin-Enhanced Deep Reinforcement Learning for Resource   Management in Networks Slicing

[260] Digital Twin-Driven Computing Resource Management for Vehicular Networks

[261] Digital Twin Assisted Intelligent Network Management for Vehicular   Applications

[262] Slicing-Based AI Service Provisioning on Network Edge

[263] Edge-MultiAI  Multi-Tenancy of Latency-Sensitive Deep Learning   Applications on Edge

[264] AI Multi-Tenancy on Edge  Concurrent Deep Learning Model Executions and   Dynamic Model Placements on Edge Devices

[265] Energy-Efficient Resource Management for Federated Edge Learning with   CPU-GPU Heterogeneous Computing

[266] Deep-Edge  An Efficient Framework for Deep Learning Model Update on   Heterogeneous Edge

[267] DEFER  Distributed Edge Inference for Deep Neural Networks

[268] EaaS  A Service-Oriented Edge Computing Framework Towards Distributed   Intelligence

[269] Towards AIOps in Edge Computing Environments

[270] DeepFT  Fault-Tolerant Edge Computing using a Self-Supervised Deep   Surrogate Model

[271] A Survey on Decentralized Identifiers and Verifiable Credentials

[272] Decentralized Identifiers and Self-sovereign Identity in 6G

[273] Beyond Certificates  6G-ready Access Control for the Service-Based   Architecture with Decentralized Identifiers and Verifiable Credentials

[274] Design Patterns for Blockchain-based Self-Sovereign Identity

[275] A low-overhead approach for self-sovereign identity in IoT

[276] Blockchain-based Decentralized Identity Management for Healthcare   Systems

[277] BlendCAC  A BLockchain-ENabled Decentralized Capability-based Access   Control for IoTs

[278] Efficient Attribute-Based Smart Contract Access Control Enhanced by   Reputation Assessment

[279] IoT based Smart Access Controlled Secure Smart City Architecture Using   Blockchain

[280] Physical Access Control Management System Based on Permissioned   Blockchain

[281] None Shall Pass  A blockchain-based federated identity management system

[282] Linking Souls to Humans with ZKBID  Accountable Anonymous Blockchain   Accounts for Web 3.0 Decentralized Identity

[283] ESIA  An Efficient and Stable Identity Authentication for Internet of   Vehicles

[284] BlockMarkchain  A Secure Decentralized Data Market with a Constant Load   on the Blockchain

[285] Energy-aware Demand Selection and Allocation for Real-time IoT Data   Trading

[286] Secure and Transparent Audit Logs with BlockAudit

[287] Towards Blockchain-Driven, Secure and Transparent Audit Logs

[288] Harpocrates  Privacy-Preserving and Immutable Audit Log for Sensitive   Data Operations

[289] PrivChain  Provenance and Privacy Preservation in Blockchain enabled   Supply Chains

[290] SciChain  Trustworthy Scientific Data Provenance

[291] AUDITEM  Toward an Automated and Efficient Data Integrity Verification   Model Using Blockchain

[292] Decentralized Inverse Transparency With Blockchain

[293] On-Chain IoT Data Modification in Blockchains

[294] Blockchain Mutability  Challenges and Proposed Solutions

[295] LSB  A Lightweight Scalable BlockChain for IoT Security and Privacy

[296] Microchain  a Light Hierarchical Consensus Protocol for IoT System

[297] Differential Privacy in Blockchain Technology  A Futuristic Approach

[298] Secure IoT access at scale using blockchains and smart contracts

[299] A Scalable Architecture for Monitoring IoT Devices Using Ethereum and   Fog Computing

[300] Towards a secure behavior modeling for IoT networks using Blockchain

[301] Incentivized Delivery Network of IoT Software Updates Based on Trustless   Proof-of-Distribution

[302] Reliable IoT Firmware Updates  A Large-scale Mesh Network Performance   Investigation

[303] Towards a Scalable and Trustworthy Blockchain  IoT Use Case

[304] A Hierarchical and Location-aware Consensus Protocol for IoT-Blockchain   Applications

[305] A Blockchain-based Approach for Assessing Compliance with SLA-guaranteed   IoT Services

[306] SoK  Oracles from the Ground Truth to Market Manipulation

[307] Data Integrity Verification in Network Slicing using Oracles and Smart   Contracts

[308] Smart Contract-based Secure Spectrum Sharing in Multi-Operators Wireless   Communication Networks

[309] Let' s Trade in The Future! A Futures-Enabled Fast Resource Trading   Mechanism in Edge Computing-Assisted UAV Networks

[310] Resource Trading in Edge Computing-enabled IoV  An Efficient   Futures-based Approach

[311] Unifying Futures and Spot Market  Overbooking-Enabled Resource Trading   in Mobile Edge Networks

[312] An Incentive-Compatible Mechanism for Decentralized Storage Network

[313] BEAT  Blockchain-Enabled Accountable and Transparent Infrastructure   Sharing in 6G and Beyond

[314] 5G and Beyond  Smart Devices as part of the Network Fabric

[315] Decentralized Caching for Content Delivery Based on Blockchain  A Game   Theoretic Perspective

[316] Socially Trusted Collaborative Edge Computing in Ultra Dense Networks

[317] A Decentralized IoT Data Marketplace

[318] Life cycle management of automotive data functions in MEC   infrastructures

[319] PDFS  Practical Data Feed Service for Smart Contracts

[320] Specification Mining for Smart Contracts with Trace Slicing and   Predicate Abstraction

[321] A Systematic Literature Review on Smart Contracts Security

[322] GDPR Compliant Blockchains-A Systematic Literature Review

[323] Citadel  Self-Sovereign Identities on Dusk Network

[324] Moving Smart Contracts -- A Privacy Preserving Method for Off-Chain Data   Trust

[325] Enhanced Security and Efficiency in Blockchain with Aggregated   Zero-Knowledge Proof Mechanisms

[326] An Overview of AI and Blockchain Integration for Privacy-Preserving

[327] Towards Data Redaction in Bitcoin

[328] Enabling Deletion in Append-Only Blockchains (Short Summary   Work in   Progress)

[329] A Blockchain-based Data Governance Framework with Privacy Protection and   Provenance for e-Prescription

[330] OConsent -- Open Consent Protocol for Privacy and Consent Management   with Blockchain

[331] A Blockchain-Based Consent Mechanism for Access to Fitness Data in the   Healthcare Context

[332] A Scalable Multi-Layered Blockchain Architecture for Enhanced EHR   Sharing and Drug Supply Chain Management

[333] Harmonizing sensitive data exchange and double-spending prevention   through blockchain and digital wallets  The case of e-prescription management

[334] Hybrid DLT as a data layer for real-time, data-intensive applications

[335] HE-DKSAP  Privacy-Preserving Stealth Address Protocol via Additively   Homomorphic Encryption

[336] Coloured Ring Confidential Transactions

[337] Differential Privacy-based Permissioned Blockchain for Private Data   Sharing in Industrial IoT

[338] Second layer data governance for permissioned blockchains  the privacy   management challenge

[339] SeDe  Balancing Blockchain Privacy and Regulatory Compliance by   Selective De-Anonymization

[340] Trust-based Blockchain Authorization for IoT

[341] Trust Management in Decentralized IoT Access Control System

[342] TrustChain  Trust Management in Blockchain and IoT supported Supply   Chains

[343] DeTRM  Decentralised Trust and Reputation Management for   Blockchain-based Supply Chains

[344] Generative Adversarial Learning for Intelligent Trust Management in 6G   Wireless Networks

[345] COBRA  Context-aware Bernoulli Neural Networks for Reputation Assessment

[346] Trust2Vec  Large-Scale IoT Trust Management System based on Signed   Network Embeddings

[347] Trust-as-a-Service  A reputation-enabled trust framework for 5G networks

[348] Towards Decentralized Identity Management in Multi-stakeholder 6G   Networks

[349] Blockchain-based Zero Trust on the Edge

[350] Decentralized Zero-Trust Framework for Digital Twin-based 6G

[351] RepChain  A Reputation-based Secure, Fast and High Incentive Blockchain   System via Sharding

[352] An Intrinsic Integrity-Driven Rating Model for a Sustainable Reputation   System

[353] Defining Blockchain Governance Principles  A Comprehensive Framework

[354] ProML  A Decentralised Platform for Provenance Management of Machine   Learning Software Systems

[355] Is Your AI Truly Yours  Leveraging Blockchain for Copyrights,   Provenance, and Lineage

[356] SmartQC  An Extensible DLT-Based Framework for Trusted Data Workflows in   Smart Manufacturing

[357] Proof-of-Contribution-Based Design for Collaborative Machine Learning on   Blockchain

[358] BlockFLow  An Accountable and Privacy-Preserving Solution for Federated   Learning

[359] A Blockchain-based Platform for Reliable Inference and Training of   Large-Scale Models

[360] Daml  A Smart Contract Language for Securely Automating Real-World   Multi-Party Business Workflows

[361] Understanding Blockchain Governance  Analyzing Decentralized Voting to   Amend DeFi Smart Contracts

[362] ACon$^2$  Adaptive Conformal Consensus for Provable Blockchain Oracles

[363] SmartScan  An approach to detect Denial of Service Vulnerability in   Ethereum Smart Contracts

[364] Fixing Smart Contract Vulnerabilities  A Comparative Analysis of   Literature and Developer's Practices

[365] Blockchain-Enabled Federated Learning  A Reference Architecture Design,   Implementation, and Verification

[366] VeryFL  A Verify Federated Learning Framework Embedded with Blockchain

[367] FLock  Defending Malicious Behaviors in Federated Learning with   Blockchain

[368] Robust Blockchained Federated Learning with Model Validation and   Proof-of-Stake Inspired Consensus

[369] FAIR-BFL  Flexible and Incentive Redesign for Blockchain-based Federated   Learning

[370] On the Decentralization of Blockchain-enabled Asynchronous Federated   Learning

[371] The Implications of Decentralization in Blockchained Federated Learning    Evaluating the Impact of Model Staleness and Inconsistencies

[372] ScaleSFL  A Sharding Solution for Blockchain-Based Federated Learning

[373] A Fast Blockchain-based Federated Learning Framework with Compressed   Communications

[374] Towards On-Device Federated Learning  A Direct Acyclic Graph-based   Blockchain Approach

[375] zkFL  Zero-Knowledge Proof-based Gradient Aggregation for Federated   Learning

[376] Tokenized Model  A Blockchain-Empowered Decentralized Model Ownership   Verification Platform

[377] IPProtect  protecting the intellectual property of visual datasets   during data valuation

[378] Dealer  End-to-End Data Marketplace with Model-based Pricing

[379] A Marketplace for Trading AI Models based on Blockchain and Incentives   for IoT Data

[380] Transparent Contribution Evaluation for Secure Federated Learning on   Blockchain

[381] Golden Grain  Building a Secure and Decentralized Model Marketplace for   MLaaS

[382] OmniLytics  A Blockchain-based Secure Data Market for Decentralized   Machine Learning

[383] PredictChain  Empowering Collaboration and Data Accessibility for AI in   a Decentralized Blockchain-based Marketplace

[384] Trustless Machine Learning Contracts; Evaluating and Exchanging Machine   Learning Models on the Ethereum Blockchain

[385] Distributed Ledger for Provenance Tracking of Artificial Intelligence   Assets

[386] Providing Assurance and Scrutability on Shared Data and Machine Learning   Models with Verifiable Credentials

[387] Trust the Process  Zero-Knowledge Machine Learning to Enhance Trust in   Generative AI Interactions

[388] Trustless Audits without Revealing Data or Models

[389] Auditable Homomorphic-based Decentralized Collaborative AI with   Attribute-based Differential Privacy

[390] Distributed and Secure ML with Self-tallying Multi-party Aggregation

[391] PPBFL  A Privacy Protected Blockchain-based Federated Learning Model

[392] zkFaith  Soonami's Zero-Knowledge Identity Protocol

[393] McFIL  Model Counting Functionality-Inherent Leakage

[394] Proof of Training (PoT)  Harnessing Crypto Mining Power for Distributed   AI Training

[395] Machine Learning Enhanced Blockchain Consensus with Transaction   Prioritization for Smart Cities

[396] MRL-PoS  A Multi-agent Reinforcement Learning based Proof of Stake   Consensus Algorithm for Blockchain

[397] TBDD  A New Trust-based, DRL-driven Framework for Blockchain Sharding in   IoT

[398] Generative AI-enabled Blockchain Networks  Fundamentals, Applications,   and Case Study

[399] Securing Majority-Attack In Blockchain Using Machine Learning And   Algorithmic Game Theory  A Proof of Work

[400] Detection Of Insider Attacks In Block Chain Network Using The Trusted   Two Way Intrusion Detection System

[401] Behavior-aware Account De-anonymization on Ethereum Interaction Graph

[402] Securing Blockchain Systems  A Novel Collaborative Learning Framework to   Detect Attacks in Transactions and Smart Contracts

[403] Automated Test-Case Generation for Solidity Smart Contracts  the AGSolT   Approach and its Evaluation

[404] Demystifying Pythia  A Survey of ChainLink Oracles Usage on Ethereum

[405] SolidWorx  A Resilient and Trustworthy Transactive Platform for Smart   and Connected Communities

[406] Training Massive Deep Neural Networks in a Smart Contract  A New Hope

[407] Optimizing Large Language Models to Expedite the Development of Smart   Contracts

[408] HyMo  Vulnerability Detection in Smart Contracts using a Novel   Multi-Modal Hybrid Model

[409] Combining Graph Neural Networks with Expert Knowledge for Smart Contract   Vulnerability Detection

[410] ESCORT  Ethereum Smart COntRacTs Vulnerability Detection using Deep   Neural Network and Transfer Learning

[411] Specification Mining for Smart Contracts with Automatic Abstraction   Tuning

[412] Partition-Tolerant and Byzantine-Tolerant Decision-Making for   Distributed Robotic Systems with IOTA and ROS 2

[413] Controlling Robots using Artificial Intelligence and a Consortium   Blockchain

[414] Real time Smart Contracts for IoT using Blockchain and Collaborative   Intelligence based Dynamic Pricing for the next generation Smart Toll   Application

[415] Unpacking How Decentralized Autonomous Organizations (DAOs) Work in   Practice

[416] A Blockchain Protocol for Human-in-the-Loop AI

[417] A Transformer Framework for Data Fusion and Multi-Task Learning in Smart   Cities

[418] A Secure Dynamic Edge Resource Federation Architecture for Cross-Domain   IoT Systems

[419] 6G-enabled Edge AI for Metaverse  Challenges, Methods, and Future   Research Directions

[420] CHIRON  Accelerating Node Synchronization without Security Trade-offs in   Distributed Ledgers

[421] Conditionally Deep Hybrid Neural Networks Across Edge and Cloud

[422] Circuit and System Technologies for Energy-Efficient Edge Robotics

[423] Big-Little Adaptive Neural Networks on Low-Power Near-Subthreshold   Processors

[424] Blockchain Goes Green  An Analysis of Blockchain on Low-Power Nodes

[425] Blockchain Goes Green  Part II  Characterizing the Performance and Cost   of Blockchains on the Cloud and at the Edge

[426] CONVOLVE  Smart and seamless design of smart edge processors

[427] Toward 6G  From New Hardware Design to Wireless Semantic and   Goal-Oriented Communication Paradigms

[428] Post Quantum Secure Blockchain-based Federated Learning for Mobile Edge   Computing

[429] FMore  An Incentive Scheme of Multi-dimensional Auction for Federated   Learning in MEC

[430] EdgeChain  Blockchain-based Multi-vendor Mobile Edge Application   Placement

[431] A Blockchain Framework for Secure Task Sharing in Multi-access Edge   Computing

[432] A Blockchain-empowered Multi-Aggregator Federated Learning Architecture   in Edge Computing with Deep Reinforcement Learning Optimization

[433] Scalable and Communication-efficient Decentralized Federated Edge   Learning with Multi-blockchain Framework

[434] RISnet  A Scalable Approach for Reconfigurable Intelligent Surface   Optimization with Partial CSI

[435] RISnet  A Domain-Knowledge Driven Neural Network Architecture for RIS   Optimization with Mutual Coupling and Partial CSI

[436] A Deep Reinforcement Learning Approach for Autonomous Reconfigurable   Intelligent Surfaces

[437] Explainable Adversarial Learning Framework on Physical Layer Secret Keys   Combating Malicious Reconfigurable Intelligent Surface

[438] Secure Decentralized IoT Service Platform using Consortium Blockchain

[439] Spatial Secrecy Spectral Efficiency Optimization Enabled by   Reconfigurable Intelligent Surfaces

[440] Connectivity-Aware Contract for Incentivizing IoT Devices in Complex   Wireless Blockchain

[441] On Secrecy Performance of RIS-Assisted MISO Systems over Rician Channels   with Spatially Random Eavesdroppers

[442] Applications of Absorptive Reconfigurable Intelligent Surfaces in   Interference Mitigation and Physical Layer Security

[443] Active Reconfigurable Intelligent Surface Aided Secure Transmission

[444] What-if Analysis Framework for Digital Twins in 6G Wireless Network   Management

[445] Digital Twin-Empowered Communications  A New Frontier of Wireless   Networks

[446] Edge Continual Learning for Dynamic Digital Twins over Wireless Networks

[447] Towards Situational Aware Cyber-Physical Systems  A Security-Enhancing   Use Case of Blockchain-based Digital Twins

[448] Trustworthy Digital Twins in the Industrial Internet of Things with   Blockchain

[449] Digital Twins and Blockchain for IoT Management

[450] Multi-Tier Computing-Enabled Digital Twin in 6G Networks

[451] Neuro-symbolic Explainable Artificial Intelligence Twin for Zero-touch   IoE in Wireless Network

[452] Structured Satellite-UAV-Terrestrial Networks for 6G Internet of Things

[453] Digital Twin Assisted Task Offloading for Aerial Edge Computing and   Networks

[454] Decentralized Computation Offloading With Cooperative UAVs  Multi-Agent   Deep Reinforcement Learning Perspective

[455] Joint Computation and Communication Design for UAV-Assisted Mobile Edge   Computing in IoT

[456] Aerial STAR-RIS Empowered MEC  A DRL Approach for Energy Minimization

[457] Seamless and Energy Efficient Maritime Coverage in Coordinated 6G   Space-Air-Sea Non-Terrestrial Networks

[458] Machine Learning-Based User Scheduling in Integrated   Satellite-HAPS-Ground Networks

[459] Blockchain-Empowered Immutable and Reliable Delivery Service (BIRDS)   Using UAV Networks

[460] Unmanned Aerial Vehicles Traffic Management Solution Using Crowd-sensing   and Blockchain

[461] Incentivizing Proof-of-Stake Blockchain for Secured Data Collection in   UAV-Assisted IoT  A Multi-Agent Reinforcement Learning Approach

[462] PROACT  Parallel Multi-Miner Proof of Accumulated Trust Protocol for   Internet of Drones

[463] Blockchain-Enhanced UAV Networks for Post-Disaster Communication  A   Decentralized Flocking Approach

[464] Air Computing  A Survey on a New Generation Computation Paradigm in 6G   Wireless Networks

[465] UAVs as a Service  Boosting Edge Intelligence for Air-Ground Integrated   Networks

[466] 6G in the Sky  On-Demand Intelligence at the Edge of 3D Networks

[467] Enhancing Autonomy with Blockchain and Multi-Access Edge Computing in   Distributed Robotic Systems

[468] Joint Communication and Computation in Hybrid Cloud Mobile Edge   Computing Networks

[469] Marine IoT Systems with Space-Air-Sea Integrated Networks  Hybrid LEO   and UAV Edge Computing

[470] BC4LLM  Trusted Artificial Intelligence When Blockchain Meets Large   Language Models

[471] APPFLChain  A Privacy Protection Distributed Artificial-Intelligence   Architecture Based on Federated Learning and Consortium Blockchain

[472] Decentralised Governance-Driven Architecture for Designing Foundation   Model based Systems  Exploring the Role of Blockchain in Responsible AI

[473] The Design Principle of Blockchain  An Initiative for the SoK of SoKs

[474] Hybrid Blockchain-Enabled Secure Microservices Fabric for Decentralized   Multi-Domain Avionics Systems

[475] Predictive Closed-Loop Service Automation in O-RAN based Network Slicing

[476] The Need for Advanced Intelligence in NFV Management and Orchestration

[477] ScalO-RAN  Energy-aware Network Intelligence Scaling in Open RAN

[478] A Survey on Explainable AI for 6G O-RAN  Architecture, Use Cases,   Challenges and Research Directions

[479] Blockchain-Aided Flow Insertion and Verification in Software Defined   Networks

[480] Permissioned Blockchain-Based Security for SDN in IoT Cloud Networks

[481] Energy and Cost Efficient Resource Allocation for Blockchain-Enabled NFV

[482] Securing OPEN-RAN Equipment Using Blockchain-Based Supply Chain   Verification

[483] Blockchain-enabled Network Sharing for O-RAN in 5G and Beyond

[484] On the Performance of Blockchain-enabled RAN-as-a-service in Beyond 5G   Networks

[485] Circuit Design for Predictive Maintenance

[486] Artificial Intelligence-Driven Customized Manufacturing Factory  Key   Technologies, Applications, and Challenges

[487] Blockchain-based Access Control for Secure Smart Industry Management   Systems

[488] Towards Trusted and Intelligent Cyber-Physical Systems  A   Security-by-Design Approach

[489] Agreements between Enterprises digitized by Smart Contracts in the   Domain of Industry 4.0

[490] A Case Study for Blockchain in Manufacturing   FabRec   A Prototype for   Peer-to-Peer Network of Manufacturing Nodes

[491] Blockchain and Fog Computing for Cyberphysical Systems  The Case of   Smart Industry

[492] Intelligent Vehicle-Trust Point  Reward based Intelligent Vehicle   Communication using Blockchain

[493] Blockchain Based Intelligent Vehicle Data sharing Framework

[494] V-CARE  A Blockchain Based Framework for Secure Vehicle Health Record   System

[495] Data Transmissions in Blockchain enabled AGVs

[496] Hyperledger Fabric Blockchain and ROS 2 Integration for Autonomous   Mobile Robots

[497] V2X-Sim  Multi-Agent Collaborative Perception Dataset and Benchmark for   Autonomous Driving

[498] V2X-Real  a Largs-Scale Dataset for Vehicle-to-Everything Cooperative   Perception

[499] V2X-ViT  Vehicle-to-Everything Cooperative Perception with Vision   Transformer

[500] DI-V2X  Learning Domain-Invariant Representation for   Vehicle-Infrastructure Collaborative 3D Object Detection

[501] Deep Reinforcement Learning based Joint Spectrum Allocation and   Configuration Design for STAR-RIS-Assisted V2X Communications

[502] Deep Reinforcement Learning Algorithms for Hybrid V2X Communication  A   Benchmarking Study

[503] Statistical Detection of Adversarial examples in Blockchain-based   Federated Forest In-vehicle Network Intrusion Detection Systems

[504] Byzantine-Fault-Tolerant Consensus via Reinforcement Learning for   Permissioned Blockchain Implemented in a V2X Network

[505] Proof of Travel for Trust-Based Data Validation in V2I Communication

[506] Blockchain-Based and Fuzzy Logic-Enabled False Data Discovery for the   Intelligent Autonomous Vehicular System

[507] Generative AI-enabled Vehicular Networks  Fundamentals, Framework, and   Case Study

[508] Blockchain-assisted Twin Migration for Vehicular Metaverses  A Game   Theory Approach

[509] A Secure and Intelligent Data Sharing Scheme for UAV-Assisted Disaster   Rescue

[510] Secure and Efficient Blockchain based Knowledge Sharing for Intelligent   Connected Vehicles

[511] Quantum Cyber-Attack on Blockchain-based VANET

[512] Proposition of Augmenting V2X Roadside Unit to Enhance Cooperative   Awareness of Heterogeneously Connected Road Users


