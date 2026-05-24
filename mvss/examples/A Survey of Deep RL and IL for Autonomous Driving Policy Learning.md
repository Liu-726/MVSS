# A Comprehensive Survey of Deep Reinforcement Learning and Imitation Learning for Autonomous Driving Policy Learning

## 1 Introduction and Motivation

This section introduces the core challenges of autonomous driving and the paradigm shift towards data-driven policy learning. It outlines the pivotal roles of Deep Reinforcement Learning (DRL) and Imitation Learning (IL), establishes the scope and objectives of the survey, and provides a high-level overview of its structure and key contributions.

### 1.1 The Grand Challenge of Autonomous Driving

The ultimate ambition of autonomous driving is to develop vehicles capable of navigating the complex, dynamic, and uncertain real-world environment with a level of safety, efficiency, and social compliance that meets or exceeds human capability. This pursuit represents one of the most formidable challenges in modern robotics and artificial intelligence. At its core, the problem transcends mere point-to-point navigation; it requires the synthesis of robust perception, predictive reasoning, and real-time decision-making within a system that is inherently safety-critical. The driving domain is characterized by high-dimensional sensory inputs, continuous and high-speed action spaces, and, most critically, dense interactions with multiple independent agents—including human drivers, pedestrians, and cyclists—whose behaviors are governed by a complex mix of traffic laws, social norms, and individual intent.

A primary source of complexity stems from **perception under uncertainty**. An autonomous vehicle (AV) must construct a coherent understanding of its surroundings from noisy, incomplete, and sometimes contradictory sensor data (e.g., cameras, LiDAR, radar). As noted in [1], ensuring robustness across diverse and adverse conditions like weather, lighting, and sensor failure is essential. Furthermore, perception systems must not only detect objects but also infer their latent states, such as velocity and intention, which are not directly observable. This partial observability transforms the planning problem into one of reasoning under uncertainty, where the AV must maintain beliefs over the world state and the future actions of others. The challenge is compounded by the need for **real-time performance**; decisions must be made within tens or hundreds of milliseconds to ensure safe reactions to sudden events, such as a pedestrian stepping onto the road or a vehicle abruptly changing lanes.

Perhaps the most defining challenge is **multi-agent interaction**. Traffic is a social phenomenon. Successful navigation, especially in complex urban settings, requires more than passive collision avoidance; it demands active negotiation, cooperation, and sometimes competition with other agents. As highlighted in [2] and [3], human drivers continuously adapt their policies based on the anticipated actions of others. An AV that fails to model this mutual influence—treating other agents as moving obstacles with independent predictions—often results in overly conservative or, conversely, dangerously aggressive behavior. Frameworks like potential games [4] and interactive planning [5] explicitly model these strategic interactions, but scaling them to real-time applications with numerous agents remains difficult. The problem is further nuanced by the need for **social compliance**; the vehicle's behavior must be interpretable and predictable to human road users, adhering to unwritten social rules (e.g., courtesy at merges) to foster smooth traffic flow and trust [6].

The operational design domain for autonomous driving is also plagued by the **long-tail distribution of scenarios**. While millions of miles of naturalistic driving data may be collected, truly safety-critical events—like a tire suddenly bouncing into the lane, a vehicle running a red light, or complex multi-vehicle negotiations at an unsignalized intersection—are exceedingly rare [7]. This scarcity makes it difficult for data-driven learning systems to adequately capture and learn robust policies for these edge cases. Consequently, a significant portion of research is dedicated to artificially generating these adversarial or safety-critical scenarios to stress-test and improve AV models, as seen in [8]. The goal is to "exit the simulation" and achieve robust real-world performance, which requires bridging the notorious **sim-to-real gap**—the disparity between simulated training environments and the complexities of the physical world [9].

Underpinning all these technical challenges is the non-negotiable imperative of **safety assurance**. Unlike many AI applications, failures in autonomous driving can have catastrophic consequences. This necessitates a paradigm shift from systems that are performant on average to those that are verifiably safe under all foreseeable conditions. This involves developing **runtime safety mechanisms** that can monitor and intervene if a learning-based planner suggests an unsafe action, as proposed in [10] and [11]. It also requires moving beyond simplistic collision metrics to incorporate **ethical and legal reasoning** into the decision-making loop. For instance, how should an AV act when a collision is unavoidable? How does it balance competing risks? Works like [12] and [13] begin to grapple with these profound questions, which are as much philosophical and legal as they are technical.

Finally, for widespread adoption, autonomous systems must be **transparent and trustworthy**. The "black-box" nature of many deep learning models is a significant barrier. Drivers, passengers, regulators, and other road users need to understand *why* an AV made a particular decision. This has spurred research into explainable AI (XAI) for autonomous driving, aiming to create interpretable policies and provide intuitive explanations for vehicle behavior [14]. Furthermore, effective **human-AI collaboration** is crucial, whether it involves a safety driver monitoring the system, a passenger providing verbal commands [15], or a remote human supplementing the system's predictions with their foresight [16].

In summary, the grand challenge of autonomous driving is a multi-faceted problem that sits at the intersection of machine learning, robotics, control theory, cognitive science, and ethics. It demands solutions that are not only technologically advanced but also safe, robust, socially intelligent, and ethically grounded. The subsequent sections of this survey will explore how Deep Reinforcement Learning (RL) and Imitation Learning (IL), two powerful paradigms for learning sequential decision-making policies, are being leveraged and adapted to address these monumental challenges, while also examining their inherent limitations and the promising research directions aimed at overcoming them.

**Table: Comparison of approaches in 1.1 The Grand Challenge of Autonomous Driving**

| Challenge Category | Key Challenge / Approach | Reference |
| :--- | :--- | :--- |
| Perception & Robustness | Perception under uncertainty; Robustness across diverse/adverse conditions; Long-range perception. | [1] |
| Multi-Agent Interaction | Multi-agent interaction-aware decision-making with adaptive strategies. | [2] |
| Multi-Agent Interaction | Enhancing social decision-making via mixed-strategy game theory with interaction orientation identification. | [3] |
| Multi-Agent Interaction | Potential game-based decision-making frameworks for strategic interactions. | [4] |
| Multi-Agent Interaction | Interactive reasoning in spatio-temporal planning (IR-STP). | [5] |
| Scenario Generation & Testing | Survey on safety-critical driving scenario generation methodologies. | [7] |
| Scenario Generation & Testing | Scenario generation via reversely regularized hybrid offline-and-online RL ((Re)$^2$H2O). | [8] |
| Sim-to-Real Transfer | Bridging the sim-to-real gap for robust and resilient AVs at scale. | [9] |
| Safety Assurance | Runtime safety mechanisms via reachability-based safety assurance within planning frameworks. | [10] |
| Safety Assurance | Refining obstacle perception safety zones via maneuver-based decomposition. | [11] |
| Ethical & Legal Reasoning | Ethical decision-making based on LSTM trajectory prediction networks. | [12] |
| Ethical & Legal Reasoning | Legal decision-making for highway automated driving. | [13] |
| Social Compliance & Coordination | Reinforcement learning framework with driving priors and coordination awareness for socially responsive AVs. | [6] |
| Transparency & Explainability | Incorporating explanations into human-machine interfaces for trust and situation awareness. | [14] |
| Human-AI Collaboration | Human-vehicle cooperation on prediction-level: enhancing automated driving with human foresight. | [16] |
| Human-AI Collaboration | Drive as you say: using LLMs for receiving, reasoning, and reacting in AVs. | [15] |


### 1.2 The Paradigm Shift to Data-Driven Policy Learning

The development of autonomous driving (AD) has long been dominated by traditional, modular architectures. These rule-based systems decompose the complex driving task into sequential, isolated components such as perception, localization, mapping, behavior planning, motion planning, and control. Each module is meticulously engineered with hand-crafted rules, state machines, and optimization algorithms (e.g., Model Predictive Control) designed to handle specific sub-problems. While this approach has enabled significant progress and offers a degree of interpretability and verifiability, it faces fundamental limitations when scaling to the "long tail" of real-world driving. The core challenge lies in the inherent complexity and unpredictability of open-road environments, characterized by diverse road users with heterogeneous behaviors, ambiguous social norms, and an infinite variety of edge-case scenarios. Manually encoding rules to anticipate and react optimally to every possible interaction—such as negotiating an unmarked intersection, interpreting the intent of a hesitant pedestrian, or executing a safe lane change in dense, fast-moving traffic—becomes an intractable engineering endeavor. These systems often exhibit brittleness, leading to overly conservative or, conversely, unsafe behaviors when encountering situations not explicitly programmed, thereby hindering the realization of truly robust and human-like autonomous driving.

This impasse has catalyzed a profound paradigm shift within the industry and research community towards data-driven, learning-based approaches for policy learning. Instead of relying solely on pre-programmed logic, the new paradigm seeks to derive driving policies directly from data, enabling vehicles to learn complex behaviors through experience. This shift is motivated by the remarkable success of deep learning in perception and the potential for similar breakthroughs in decision-making. Two machine learning frameworks have emerged as particularly pivotal for this task: Deep Reinforcement Learning (DRL) and Imitation Learning (IL). Together, they represent complementary pathways for creating adaptive, performant, and socially compliant driving agents.

Deep Reinforcement Learning frames driving as a sequential decision-making problem under uncertainty. An agent, representing the autonomous vehicle, learns a policy—a mapping from perceived environmental states to actions—by interacting with a simulated or real environment. It explores actions, observes resulting states and receives numerical rewards (or penalties) that encode desired objectives like maintaining speed, staying in lane, avoiding collisions, and reaching a destination. Through trial and error, often leveraging powerful function approximators like deep neural networks, the agent aims to maximize its cumulative reward. The principal strength of DRL is its ability to discover novel and highly optimized strategies that might elude human designers. For instance, DRL agents can learn sophisticated negotiation and cooperation tactics in interactive scenarios, such as smoothly merging into traffic or navigating a busy roundabout, by optimizing for long-term efficiency and safety [17]. Furthermore, DRL is well-suited for tasks where an explicit reward signal can be defined, even if the optimal policy is unknown, allowing for autonomous improvement and adaptation to new scenarios [18]. Studies have demonstrated DRL's capability in learning human-like car-following models that generalize across different drivers and situations [19], and in developing robust decision-making strategies for complex lane changes in challenging scenarios like highway off-ramps [20].

In contrast, Imitation Learning offers a more direct, and often more sample-efficient, approach by learning to mimic expert behavior from demonstration datasets. The core premise is that if a policy can replicate the actions of a skilled human driver (or a well-performing algorithm) across a wide range of observed states, it will inherit the expert's competence. Behavior Cloning (BC), the simplest form of IL, treats this as a supervised learning problem, mapping states to actions. This approach can quickly produce competent policies from large-scale real-world driving logs, effectively "cloning" human driving style [21]. Its efficiency is a major advantage, as it bypasses the challenging exploration problem and reward engineering required in DRL. IL has proven highly effective for learning nuanced, human-like driving behaviors that are difficult to quantify with a reward function, such as socially-aware gap acceptance, comfortable acceleration profiles, and adherence to unwritten traffic norms [22]. Advanced IL methods, like Generative Adversarial Imitation Learning (GAIL), go further by learning a reward function implicitly from demonstrations, allowing the agent to match the expert's state-action distribution rather than just actions, often leading to more robust policies [23].

However, neither paradigm is a panacea. Pure IL suffers from the "distributional shift" problem: errors compound when the agent encounters states not covered in the demonstration data, potentially leading to catastrophic failures. It is also fundamentally limited by the quality and coverage of the expert data; it cannot surpass the expert and may perpetuate suboptimal or unsafe behaviors present in the demonstrations [24]. Pure DRL, while capable of surpassing the expert, is notoriously sample-inefficient and requires careful, often non-intuitive, reward shaping. An ill-specified reward can lead to reward hacking—where the agent finds unintended ways to maximize reward that violate safety—or failure to learn meaningful behaviors at all. Furthermore, safe exploration in the real world is prohibitively dangerous.

Consequently, the most promising direction in contemporary research is the synergistic integration of DRL and IL, creating hybrid frameworks that leverage the strengths of both. IL can provide a safe, informative prior or a structured action space to bootstrap and guide the RL exploration process, dramatically improving sample efficiency and initial safety. Subsequently, RL can refine and improve upon the imitated policy, enabling performance recovery in states beyond the demonstration distribution and optimizing for explicit safety and efficiency metrics that may not be fully captured in the demonstrations. This synergy is exemplified by algorithms like Imitation Bootstrapped Reinforcement Learning (IBRL) [25], Controllable Imitative Reinforcement Learning (CIRL) [26], and other methods that use human demonstrations to shape rewards or constrain the policy search space [27]. The result is policies that are both human-like *and* robust, capable of handling the challenging long-tail scenarios where pure IL fails [24].

This paradigm shift towards data-driven policy learning, centered on DRL and IL, represents a fundamental rethinking of how autonomous driving intelligence is acquired. It moves away from explicit programming of *what to do* in every situation and towards providing the system with the ability to learn *how to behave* from experience and example. This transition is crucial for tackling the overwhelming complexity of real-world driving, aiming to develop agents that are not only safe and efficient but also exhibit the adaptive, contextual, and sometimes intuitive decision-making characteristic of human drivers. The subsequent sections of this survey will delve into the technical foundations of these methods, their specific applications across various driving tasks, and the critical open challenges that must be addressed to realize their full potential for real-world deployment.

**Table: Comparison of approaches in 1.2 The Paradigm Shift to Data-Driven Policy Learning**

| Method / Framework | Core Idea / Approach | Key Strengths | Key Limitations / Challenges | Primary Applications / Examples in AD | Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Traditional Modular Architecture** | Decomposes driving into sequential, isolated modules (perception, planning, control) with hand-crafted rules and optimization algorithms. | Offers interpretability and verifiability; enabled significant early progress. | Brittleness in edge cases; poor scalability to the "long tail" of real-world scenarios; requires intractable manual engineering. | Foundation for early autonomous driving systems. | (Not explicitly cited in provided papers) |
| **Deep Reinforcement Learning (DRL)** | Frames driving as a sequential decision-making problem. An agent learns a policy by interacting with an environment to maximize cumulative reward. | Can discover novel, optimized strategies; suitable for tasks with definable reward signals; enables autonomous improvement. | Sample-inefficient; requires careful reward shaping (risk of reward hacking); unsafe for real-world exploration. | Learning negotiation/cooperation tactics for merging and roundabouts [17]; learning human-like car-following models [19]; decision-making for complex lane changes [20]; Sim2Real transfer [18]. | [17], [19], [20], [18] |
| **Imitation Learning (IL) / Behavior Cloning (BC)** | Learns to mimic expert behavior directly from demonstration datasets, treated as a supervised learning problem. | Highly sample-efficient; can quickly produce competent, human-like policies; bypasses reward engineering. | Suffers from distributional shift (compounding errors); limited by expert data quality/coverage; cannot surpass the expert. | Learning nuanced, human-like driving behaviors (socially-aware gap acceptance, comfortable acceleration) [22]; cloning driving style from dense traffic data [21]; learning from human demonstrations via GAIL [23]. | [22], [21], [23] |
| **Hybrid DRL/IL Frameworks** | Synergistically integrates IL and DRL, using IL to bootstrap/guide RL exploration and RL to refine/improve upon the imitated policy. | Combines IL's sample efficiency and safety prior with DRL's ability to optimize and recover from distributional shift; leads to robust, human-like policies. | Design complexity in effectively combining the two paradigms. | Imitation Bootstrapped Reinforcement Learning (IBRL) [25]; Controllable Imitative Reinforcement Learning (CIRL) [26]; using demonstrations to shape rewards/constrain policy search [27]; robustifying imitation for challenging scenarios [24]. | [25], [26], [27], [24] |


### 1.3 The Pivotal Roles of DRL and IL in Autonomous Driving

The development of robust and intelligent driving policies is a cornerstone of autonomous vehicle (AV) technology. In this pursuit, two dominant paradigms from machine learning have emerged as particularly powerful: Deep Reinforcement Learning (DRL) and Imitation Learning (IL). These approaches offer complementary strengths, addressing different facets of the complex autonomous driving problem. DRL provides a framework for agents to discover novel, optimized strategies through autonomous trial-and-error, while IL offers a data-efficient pathway to replicate the nuanced and socially compliant behaviors exhibited by human drivers. Understanding the pivotal roles and inherent synergies of these methodologies is essential for advancing the field.

Deep Reinforcement Learning frames driving as a sequential decision-making problem, where an agent interacts with a simulated or real environment to maximize a cumulative reward signal. This reward-driven learning process is DRL's core strength, enabling it to explore vast state-action spaces and discover policies that can surpass the performance of its initial programming or training data. For instance, in complex interactive tasks like highway merging or negotiating dense urban intersections, DRL agents can learn sophisticated negotiation tactics, such as when to yield, assert right-of-way, or perform defensive maneuvers, that may not be explicitly present in human demonstrations. Works like [28] and [17] demonstrate how DRL can learn proactive and scalable policies that effectively trade off safety and efficiency in dynamic, multi-agent settings. The ability to optimize for long-term objectives, such as minimizing travel time or energy consumption as seen in [29], is a key advantage over reactive, rule-based systems. Furthermore, DRL's capacity for closed-loop training in simulation, as discussed in [30], allows for scalable and safe learning from millions of trials, which is infeasible in the real world.

In contrast, Imitation Learning adopts a more direct approach by learning a policy from datasets of expert demonstrations, typically human driving logs. The primary advantage of IL is its sample efficiency and ability to capture the subtle, often unquantifiable aspects of human driving behavior—such as social courtesy, nuanced gap acceptance, and comfortable acceleration profiles—directly from data. Techniques like Behavior Cloning provide a straightforward supervised learning pathway to mimic these demonstrations. This is powerfully illustrated in [19], where a model trained on real-world naturalistic driving data successfully reproduced human-like car-following behavior with high accuracy. IL is particularly valuable for bootstrapping policies in complex domains where designing a reward function for DRL is non-trivial or where certain safe and legal driving patterns must be adhered to from the outset. By leveraging large-scale offline datasets, IL can quickly produce competent policies that reflect real-world driving conventions without the need for potentially dangerous exploration.

However, each paradigm faces significant limitations when applied in isolation. Pure DRL is notoriously sample-inefficient and can be unsafe during exploration, as the agent must discover constraints and optimal behaviors through random trial-and-error, which in driving can lead to catastrophic failures. Studies like [31] highlight the safety risks of baseline DRL models in complex junctions. Moreover, crafting a reward function that perfectly encapsulates all aspects of good driving—safety, efficiency, comfort, legality, and social appropriateness—is an immense challenge, often leading to unintended and suboptimal policy behaviors. On the other hand, IL suffers from the "cascading error" problem, where small mistakes made by the imitative policy can lead it into states not covered by the training data, causing performance to degrade. It is also fundamentally limited by the quality and coverage of the expert data; it cannot learn to perform better than the demonstrator and may inherit their suboptimal or even erroneous habits. As noted in [24], policies based on imitation alone often fail to sufficiently account for safety and reliability in challenging, out-of-distribution scenarios not well-covered by the demonstration data.

Recognizing these complementary weaknesses has spurred the development of hybrid RL-IL methods, which aim to synergistically combine the best of both worlds. These approaches seek to use IL to provide a safe, knowledgeable starting point (addressing DRL's cold-start and safety issues) and then employ DRL to refine and improve upon the demonstrated behavior, optimizing for specified rewards and enhancing robustness. A prominent strategy is to use expert demonstrations to pre-train or guide the RL agent. For example, [32] proposes a method that modifies the policy learning process to incorporate both the goal of maximizing reward and imitating the expert, significantly improving sample efficiency and final performance. Similarly, [33] uses an imitative expert policy derived from demonstrations to regularize the DRL agent's policy during learning, leading to faster convergence and more human-like behaviors. Another approach involves storing human demonstrations in the replay buffer alongside agent-generated experiences, as in [20], to bias exploration towards safer regions of the state-action space. More advanced frameworks like [34] conceptualize the human as an active mentor, intervening in dangerous situations to demonstrate correct actions, thereby directly injecting human intelligence into the RL training loop to guarantee safety and improve traffic flow efficiency.

The trajectory of research clearly indicates that the future of learning-based autonomous driving lies not in choosing between DRL or IL, but in their intelligent integration. Hybrid methods mitigate DRL's exploration risk and reward-design burden by leveraging prior knowledge from demonstrations, while simultaneously overcoming IL's distributional shift and performance ceiling by allowing the policy to optimize and adapt beyond the demonstrated behaviors. This fusion is crucial for developing autonomous driving agents that are not only competent and efficient but also robust, safe, and capable of graceful handling of the long-tail of rare but critical driving scenarios. As the field progresses, the development of more sophisticated hybrid architectures—such as hierarchical models combining IL-learned low-level skills with RL-based high-level decision-making as in [35]—will be pivotal in translating the promise of machine learning into reliable, real-world autonomous driving systems.

**Table: Comparison of approaches in 1.3 The Pivotal Roles of DRL and IL in Autonomous Driving**

| Method/Model Category | Core Idea / Mechanism | Key Advantages (as per text) | Key Limitations (as per text) | Example Reference(s) from Source Papers |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Reinforcement Learning (DRL)** | Frames driving as a sequential decision-making problem. An agent interacts with an environment to maximize a cumulative reward signal through trial-and-error. | Enables discovery of novel, optimized strategies; can surpass initial training data; optimizes for long-term objectives (e.g., travel time, energy); scalable closed-loop training in simulation. | Sample-inefficient; unsafe during exploration; immense challenge in crafting a perfect reward function; can lead to catastrophic failures. | [28], [17], [29], [30], [31] |
| **Imitation Learning (IL)** | Learns a policy directly from datasets of expert demonstrations (e.g., human driving logs). | Sample efficient; captures subtle, unquantifiable aspects of human driving behavior (social courtesy, gap acceptance); valuable for bootstrapping where reward design is hard. | Suffers from "cascading error" problem; limited by quality/coverage of expert data; cannot outperform the demonstrator; may inherit suboptimal habits. | [19], [24] |
| **Hybrid RL-IL Methods** | Synergistically combines DRL and IL. Uses IL for a safe, knowledgeable starting point and DRL to refine and improve upon demonstrated behavior. | Mitigates DRL's exploration risk and reward-design burden; overcomes IL's distributional shift and performance ceiling; leads to faster convergence, more human-like behaviors, and improved safety. | (Not explicitly discussed as a limitation in the provided text) | [32], [33], [20], [34], [35] |


### 1.4 Scope, Objectives, and Survey Methodology

This survey focuses on the application of Deep Reinforcement Learning (RL) and Imitation Learning (IL) for learning driving policies in autonomous vehicles (AVs). The scope is deliberately centered on the **decision-making, planning, and control** layers of the AV stack, where a policy maps perceived environmental states (e.g., sensor data, vehicle state, predicted trajectories of others) to control actions (e.g., steering, acceleration, braking). We explicitly exclude in-depth surveys of low-level vehicle control (unless integral to the policy learning), pure perception modules, or detailed hardware/system design. Instead, we examine how deep learning paradigms are leveraged to create intelligent agents that can navigate complex, dynamic, and interactive traffic scenarios. This includes tactical maneuvers like lane changes and merges, strategic route planning, and nuanced interactions with human drivers and pedestrians. The core challenge addressed is endowing machines with the competence, courtesy, and safety of a human expert driver, but with superior consistency and the potential to exceed human limitations.

The primary objectives of this survey are fourfold. First, we aim to provide a **unified and structured taxonomy** that bridges concepts from the often-disparate fields of deep RL, IL, and autonomous driving research. By categorizing algorithms based on their core mechanisms—such as policy gradient methods, value-based optimization, or adversarial training—we offer a clear map of the methodological landscape. Second, we conduct a comprehensive **review of algorithmic foundations and their specific applications** in driving contexts. This involves dissecting how fundamental techniques like Trust Region Policy Optimization [36] or adversarial imitation learning are adapted to solve concrete problems like intersection management or modeling human driving behavior. Third, we undertake a critical **analysis of the paramount challenges** of safety, robustness, and generalization. This involves synthesizing research on safe RL [37], robust exploration [38], and sim-to-real transfer, which are non-negotiable for real-world deployment. Finally, we outline **emerging frontiers and future research directions**, identifying promising avenues such as the integration of foundation models [39], interactive learning [40], and neuro-symbolic approaches [41] that could fundamentally advance the capabilities of learning-based driving systems.

To achieve these objectives systematically, we employ a **three-pronged review methodology** that examines the literature from complementary angles.

1.  **System-Level Analysis:** This top-down perspective examines how RL and IL components fit into the broader architecture of an autonomous driving system. We analyze the flow from perception to action, considering where learned policies are situated (e.g., end-to-end vs. modular pipelines), how they interface with traditional components like prediction and rule-based safety checkers, and how system-level requirements like latency and reliability influence algorithm choice. This view helps contextualize the role of policy learning within the complete autonomy solution, as highlighted in reviews of AV milestones [42].

2.  **Task-Driven Analysis:** Here, we organize the survey around specific driving tasks and functionalities. This includes dedicated analyses of **decision-making frameworks** for scenarios like highway driving and intersection negotiation; **safety and ethical driving** mechanisms that ensure constraint satisfaction and socially compliant behavior; and **energy efficiency** applications like eco-driving. For each task, we compare and contrast how different RL/IL families—model-free vs. model-based [43], online vs. offline—are applied, evaluating their suitability based on task characteristics such as reward sparsity, horizon length, and interaction complexity.

3.  **Problem-Driven Analysis:** This bottom-up perspective focuses on the core algorithmic and theoretical problems that transcend any single driving task. We dedicate significant portions to dissecting solutions for **exploration** in vast, continuous state-action spaces (e.g., via subgoal discovery [44] or intrinsic motivation), **reward specification** (including reward shaping [45] and inverse reward design), and **safety assurance** during both training and deployment (through methods like constrained policy optimization [46] or recovery policies). This approach allows us to trace the evolution of solutions to fundamental RL/IL challenges and assess their maturity for the stringent demands of autonomous driving.

By interweaving these three methodological lenses, this survey moves beyond a simple catalog of applications. It provides a holistic understanding of *why* certain algorithms are chosen for specific driving problems, *how* they are integrated into larger systems, and *what* fundamental challenges must be overcome to progress from laboratory benchmarks to trustworthy on-road deployment. The subsequent sections are structured to reflect this integrated approach, first establishing the algorithmic foundations (Section 1), then exploring their application across key autonomous driving domains (Section 2), and finally critically examining persistent challenges and future directions (Section 3).

**Table: Comparison of approaches in 1.4 Scope, Objectives, and Survey Methodology**

| Method/Model | Category (from Text) | Key Mechanism/Approach | Primary Application/Problem Addressed (from Text) | Reference (Full Paper Title) |
| :--- | :--- | :--- | :--- | :--- |
| Trust Region Policy Optimization (TRPO) | Algorithmic Foundation (Policy Gradient) | Policy gradient method with a trust region constraint to ensure stable updates. | Fine-grained acceleration control for autonomous intersection management. | [36] |
| Adversarial Imitation Learning | Algorithmic Foundation (Imitation Learning) | Uses adversarial training (e.g., a discriminator) to match expert policy distributions. | Modeling human driving behavior. | *[47]* |
| Safe RL with Dead-Ends Avoidance | Challenge: Safety & Robustness | Utilizes a decoupled RL framework with a pretrained safety critic and recovery policy to identify and avoid unsafe states. | Ensuring safety during training and deployment, avoiding catastrophic failures. | [37] |
| LEAF (Latent Exploration Along the Frontier) | Challenge: Exploration | Learns a dynamics-aware manifold of reachable states and explores stochastically at the frontier of this region. | Robust exploration in vast, continuous state-action spaces. | [38] |
| Constrained Policy Optimization via Bayesian World Models | Challenge: Safety Assurance | Uses Bayesian world models to estimate uncertainty and optimize policies with pessimistic safety constraints. | Safe reinforcement learning with formal constraint satisfaction. | [46] |
| Model-Free vs. Model-Based RL | Task-Driven Analysis | Model-Free: Learns policy/value function directly from experience. Model-Based: Learns an explicit environment model for planning. | Compared for suitability based on task characteristics like reward sparsity and horizon length. | [43] |
| Subgoal-based Reward Shaping | Problem-Driven: Reward Specification | Extends potential-based reward shaping to incorporate human knowledge of subgoals to accelerate learning. | Improving learning efficiency via reward shaping. | [45] |
| IR-VIC (Unsupervised Discovery of Sub-goals) | Problem-Driven: Exploration | Uses variational intrinsic control and information theory to discover sub-goals without supervision for better exploration. | Subgoal discovery for transfer and exploration in RL. | [44] |
| Integration of Foundation Models | Emerging Frontier | Leverages large pre-trained models (e.g., for vision, language) to enhance perception, reasoning, and generalization. | Advancing capabilities of learning-based driving systems toward Embodied AI. | [39] |
| Interactive Learning | Emerging Frontier | Involves human-AI cooperation where humans guide or correct the learning algorithm's behavior. | Future command and control, improving adaptability in complex scenarios. | [40] |
| Neuro-Symbolic Approaches | Emerging Frontier | Combines neural networks with symbolic reasoning and planning for hierarchical task decomposition. | Bilevel planning and learning composable skills for complex tasks. | [41] |


### 1.5 Survey Structure and Key Contributions

This survey is structured to provide a comprehensive and systematic exploration of the intersection between deep reinforcement learning (RL), imitation learning (IL), and autonomous driving (AD) policy learning. The organization is designed to guide the reader from foundational concepts, through the core technical components of modern driving systems, to concrete applications, and finally to the open challenges and future research frontiers. The following roadmap outlines the logical flow and key content of each major section.

**Section 2: Algorithmic Foundations of Deep RL and IL** establishes the essential theoretical and methodological bedrock. It begins by dissecting core Reinforcement Learning techniques, including policy gradient methods like Proximal Policy Optimization (PPO), actor-critic architectures such as Deep Deterministic Policy Gradient (DDPG), and value-based optimization paradigms. A critical focus is placed on Safe RL, which integrates control-theoretic safeguards and chance constraints to ensure reliable operation. The section then transitions to Imitation Learning, covering spectrum from simple Behavior Cloning to more sophisticated frameworks like Inverse Reinforcement Learning (IRL) and Generative Adversarial Imitation Learning (GAIL), which aim to recover the underlying reward function of expert demonstrations. The subsection concludes by analyzing Hybrid RL and IL Methods, which synergistically combine the sample efficiency of imitation with the exploratory and optimization power of reinforcement learning, often facilitated by advanced reward shaping and techniques for Sim-to-Real transfer.

**Section 3: Perception, Prediction, and World Models** addresses the critical upstream modules that inform the driving policy. It examines how deep learning models process multi-modal sensor data (LiDAR, cameras, radar) to construct a coherent representation of the environment. Beyond static perception, a significant portion is dedicated to trajectory prediction for surrounding agents, a task increasingly tackled by generative and diffusion models. The core of this section explores the paradigm of learned World Models and their role in AD. These models, which can be seen as a form of "Big Learning" [48] that exhaustively exploits large-scale data to model complex dynamics, allow an agent to learn a compact, predictive model of its environment. This enables planning and policy learning within a simulated latent space, dramatically improving sample efficiency and facilitating long-horizon reasoning. The discussion connects to the broader shift towards Foundation Models for Decision Making [49], examining how large pre-trained models can be adapted or serve as priors for scene understanding and dynamics prediction.

**Section 4: Architectural Paradigms and System Integration** investigates how the algorithmic components are assembled into complete driving systems. It contrasts modular pipelines, where perception, prediction, planning, and control are distinct subsystems, with emerging end-to-end architectures that map raw sensor inputs directly to control commands. The survey details prominent architectural frameworks, including hierarchical RL, where high-level policy selects goals for a low-level controller, and modular networks with specialized sub-policies for different driving scenarios. This section also delves into the critical software and systems challenges, discussing simulation frameworks and architectural considerations for distributed AI systems as outlined in works on compositional architecture frameworks [50].

**Section 5: Applications and Benchmarking** translates theory into practice, reviewing the deployment of RL and IL across key AD domains. It covers fundamental tasks such as lane keeping, lane change decision-making, and interactive merge scenarios. A dedicated subsection on Safety and Ethical Driving analyzes methods for formal safety assurance, runtime monitoring frameworks, and the nascent field of ethical decision models for unavoidable accident scenarios. Further applications extend to Eco-Driving and energy efficiency, where RL agents optimize velocity profiles to minimize fuel consumption and emissions. The section concludes with a critical analysis of evaluation methodologies, benchmarks, and the pitfalls of leaderboard-driven research, emphasizing the need for robust evaluation beyond mere metric scores [51].

**Section 6: Critical Challenges and Open Problems** provides a sober assessment of the field's limitations. The paramount issue of Sim-to-Real Generalization is explored, covering domain randomization, domain adaptation techniques, and the problem of covariate shift. The challenge of Safe and Robust Learning is expanded to include adversarial robustness against sensor attacks, handling of long-tail and out-of-distribution events, and ensuring stability under distribution shifts. A major subsection is devoted to Ethical, Explainable, and Responsible AI, tackling the need for interpretable policies, causal reasoning, and fairness. This discussion is deeply informed by broader concerns about Foundation Models, including their opaque nature, homogenization risks, and societal impact [52], [53]. Additional challenges include multi-agent coordination, computational efficiency for onboard deployment, and the integration of human-in-the-loop feedback.

**Section 7: Future Directions and Concluding Remarks** synthesizes the survey's insights to chart a path forward. It highlights transformative trends such as the integration of large-scale Foundation Models and World Models to create more generalizable and capable driving agents, a direction strongly signaled by progress in embodied AI [39] and multi-modal foundation models for road scenes [54]. Other promising avenues include the use of causality for improved robustness and interpretability, federated and privacy-preserving learning frameworks [55] for leveraging distributed real-world data, and the development of unified benchmarks that stress-test generalization, safety, and ethical alignment. The survey concludes by reflecting on the interdisciplinary nature of the field, which sits at the confluence of machine learning, robotics, control theory, and human factors, and emphasizes that responsible advancement requires co-evolution of technical capabilities and socio-technical governance frameworks.

The key contributions of this survey are threefold. First, it provides a **comprehensive and structured synthesis** of a rapidly evolving field, organizing a vast and fragmented body of literature into a coherent narrative that connects foundational algorithms to system-level architectures and real-world applications. Second, it offers a **critical and forward-looking perspective**, moving beyond a mere catalog of techniques to explicitly bridge current methods with the paradigm-shifting potential of foundation models and world models, while rigorously addressing the enduring challenges of safety, robustness, and ethics. Third, it is designed to be an **accessible resource for a broad audience**, offering newcomers a clear entry point and foundational understanding, while providing seasoned researchers with a consolidated view of the state-of-the-art and a reasoned analysis of the most pressing open problems and promising research trajectories. By contextualizing autonomous driving policy learning within the broader currents of AI—such as the shift towards large-scale, general-purpose models and responsible system design—this survey aims to be a definitive reference that both educates and inspires future innovation.

**Table: Comparison of approaches in 1.5 Survey Structure and Key Contributions**

| Method/Model Name | Category (from text) | Key Idea/Description | Reference |
| :--- | :--- | :--- | :--- |
| Proximal Policy Optimization (PPO) | Reinforcement Learning (Policy Gradient) | A policy gradient method for reinforcement learning that uses a clipped objective function to ensure stable updates. | (Not explicitly cited in provided sources) |
| Deep Deterministic Policy Gradient (DDPG) | Reinforcement Learning (Actor-Critic) | An actor-critic, model-free algorithm for learning continuous actions in reinforcement learning. | (Not explicitly cited in provided sources) |
| Behavior Cloning | Imitation Learning | A simple form of imitation learning where a policy is trained via supervised learning to mimic expert state-action pairs. | (Not explicitly cited in provided sources) |
| Inverse Reinforcement Learning (IRL) | Imitation Learning | A framework that aims to recover the underlying reward function that explains observed expert behavior. | (Not explicitly cited in provided sources) |
| Generative Adversarial Imitation Learning (GAIL) | Imitation Learning | An imitation learning method that uses a generative adversarial network framework to match the policy's state-action distribution to the expert's. | (Not explicitly cited in provided sources) |
| Hybrid RL/IL Methods | Hybrid Learning | Methods that synergistically combine the sample efficiency of imitation learning with the exploratory and optimization power of reinforcement learning. | (Not explicitly cited in provided sources) |
| World Models / "Big Learning" | Perception & Prediction | Learned models that exhaustively exploit large-scale data to model complex environment dynamics, enabling planning in a simulated latent space. | [48] |
| Foundation Models for Decision Making | Perception & Prediction | Large pre-trained models adapted to serve as priors for scene understanding and dynamics prediction in decision-making tasks like autonomous driving. | [49] |
| Modular Pipelines | System Architecture | Architectural paradigm where perception, prediction, planning, and control are distinct, hand-engineered subsystems. | (Not explicitly cited in provided sources) |
| End-to-End Architectures | System Architecture | Architectural paradigm that maps raw sensor inputs directly to control commands using a single, learned model. | (Not explicitly cited in provided sources) |
| Hierarchical RL | System Architecture | A framework where a high-level policy selects sub-goals or skills for a low-level controller to execute. | (Not explicitly cited in provided sources) |
| Compositional Architecture Frameworks | System Integration | Mathematical models and guidelines for creating scalable architecture frameworks, with application to distributed AI systems. | [50] |
| (Evaluation Benchmarks) | Benchmarking | Critical analysis of evaluation methodologies and the pitfalls of leaderboard-driven research, emphasizing robust evaluation. | [51] |
| Foundation Models (General) | Critical Challenges / Future Directions | Large-scale models trained on broad data, posing challenges and opportunities related to opacity, homogenization, and societal impact. | [52] |
| Responsible AI Reference Architecture | Critical Challenges / Future Directions | A pattern-oriented reference architecture for designing responsible foundation-model-based systems to minimize associated risks. | [53] |
| Federated Transfer Learning (FTL) | Future Directions | A framework combining federated and transfer learning to ground foundation models in domain-specific tasks while addressing data privacy and heterogeneity. | [55] |
| Embodied AI with Foundation Models | Future Directions | Survey of foundation models in robotics, focusing on their role in advancing embodied AI agents for manipulation and control. | [39] |
| Multi-modal Multi-task Foundation Models for Road Scenes | Future Directions | Foundation models equipped for multi-modal and multi-task learning to achieve holistic understanding of road scenes for autonomous driving. | [54] |



### Roadmap and Taxonomy

The following taxonomy tree outlines the structure of this survey:


```plaintext
A Survey of Deep RL and IL for Autonomous Driving Policy Learning
|----Section 1: Foundations of Deep RL and IL
|     |----Subsection 1.1: Reinforcement Learning (RL) Techniques
|     |     |----Policy Gradient: [56][57][58]
|     |     |----Actor-Critic Methods: [59][60][61]
|     |     |----Safe RL: [62][63][64]
|     |     |----Value-Based Optimization: [65][66][67]
|     |     |----Exploration Strategies: [68][69][70]
|     |----Subsection 1.2: Imitation Learning (IL) Techniques
|     |     |----Behavior Cloning: [71][72][73]
|     |     |----Inverse Reinforcement Learning: [19][74][75]
|     |     |----Adversarial Imitation Learning: [76][77][23]
|     |     |----Offline IL: [78][79][80]
|     |----Subsection 1.3: Hybrid RL and IL Methods
|     |     |----RL-IL Integration: [81][82][72]
|     |     |----Sim-to-Real Transfer: [83][84][85]
|     |     |----Reward Shaping: [86][87][88]

|----Section 2: Applications in Autonomous Driving
|     |----Subsection 2.1: Decision-Making Frameworks
|     |     |----Highway Lane Changing: [89][90][91]
|     |     |----Collision Avoidance: [92][93][94]
|     |     |----Interactive Planning: [95][63][96]
|     |----Subsection 2.2: Safety and Ethical Driving
|     |     |----Safety Assurance: [97][98][99]
|     |     |----Ethical Decision Models: [100][101][12]
|     |     |----Human-AI Collaboration: [34][51][52]
|     |----Subsection 2.3: Energy Efficiency and Eco-Driving
|     |     |----Eco-Driving Control: [102][103][104]
|     |     |----Traffic Emissions Reduction: [105][106][107]

|----Section 3: Challenges and Future Directions
|     |----Subsection 3.1: Sim-to-Real Generalization
|     |     |----Domain Transfer Techniques: [108][83][109]
|     |     |----Digital Twin Frameworks: [110][111][112]
|     |     |----Covariate Shift Adaptation: [113][114][115]
|     |----Subsection 3.2: Safe and Robust Learning
|     |     |----Runtime Assurance: [116][117][118]
|     |     |----Adversarial Robustness: [119][120][121]
|     |     |----Distribution Shifts: [122][123][124]
|     |----Subsection 3.3: Ethical and Explainable AI
|     |     |----Interpretable Policies: [100][125][126]
|     |     |----Causal Interpretability: [127][128][81]
|     |     |----Fairness in AI: [129][130][131]
```


## 2 Foundational Algorithms and Methodologies

This section provides a comprehensive technical overview and taxonomy of core DRL algorithms (e.g., Policy Gradient, Actor-Critic, value-based methods) and IL paradigms (e.g., Behavior Cloning, Inverse RL, Adversarial IL). It also covers essential supporting techniques like exploration strategies, reward shaping, and the principles of hybrid RL-IL integration.

### 2.1 Core Deep Reinforcement Learning Algorithms

The landscape of Deep Reinforcement Learning (DRL) for autonomous driving is dominated by three fundamental algorithmic families: value-based methods, policy gradient methods, and the hybrid actor-critic frameworks. Each class offers distinct mechanisms for learning optimal policies from interaction, with varying suitability for the continuous, high-stakes control tasks inherent to driving.

**Value-based methods**, such as Deep Q-Networks (DQN) and its variants (Double DQN, Dueling DQN), learn an action-value function (Q-function) that estimates the expected cumulative reward for taking a given action in a specific state. The optimal policy is then derived by selecting the action with the highest Q-value. These methods are inherently designed for discrete action spaces, making them directly applicable to high-level tactical decision-making tasks like lane-change commands or intersection negotiation. For instance, studies have applied DQN for lane-keeping and decision-making in highway scenarios, demonstrating their capability to learn safe overtaking policies [132]. However, a primary limitation for direct vehicle control is the "curse of dimensionality" associated with discretizing continuous control variables like steering angle and throttle. While extensions like the Deep Q-learning with Graph Attention Networks (DQ-GAT) framework attempt to handle complex multi-agent interactions, the core challenge of fine-grained continuous control remains [17]. Furthermore, value-based methods can suffer from overestimation bias and instability during training, issues that variants like Double DQN aim to mitigate.

In contrast, **policy gradient methods** directly parameterize and optimize the policy \(\pi_\theta(a|s)\) using gradient ascent on the expected return. This approach is naturally suited for continuous and high-dimensional action spaces, as it learns a mapping from states to action distributions. Algorithms like Trust Region Policy Optimization (TRPO) and its more practical successor, Proximal Policy Optimization (PPO), have become cornerstones in autonomous driving research. TRPO enforces a trust region constraint to ensure stable policy updates by limiting the KL-divergence between successive policies, which has proven effective for training robust driving policies in complex scenarios like roundabouts, often outperforming other algorithms in safety and efficiency metrics [133]. PPO simplifies this constraint using a clipped surrogate objective, offering a good balance between sample complexity, simplicity, and performance, making it a popular choice for various simulated driving tasks [134]. The primary strength of policy gradients is their ability to learn smooth, continuous control policies. However, they are often criticized for high variance in gradient estimates and poor sample efficiency, requiring extensive interaction with the environment—a significant cost in high-fidelity driving simulators.

To harness the strengths of both value-based and policy-based approaches, **actor-critic frameworks** employ a two-network architecture. The *actor* network parameterizes the policy and selects actions, while the *critic* network estimates the value function and critiques the actor's choices. This decoupling often leads to more stable and sample-efficient learning. The Deep Deterministic Policy Gradient (DDPG) algorithm is a seminal actor-critic method designed for continuous action spaces, combining a deterministic actor with a learned Q-function critic. It has been widely used for tasks from lane-keeping to eco-driving control in hybrid electric vehicles [135]. However, DDPG can be sensitive to hyperparameters and suffer from overestimation bias in the critic. The Twin Delayed DDPG (TD3) algorithm addresses this by introducing clipped double Q-learning and delayed policy updates, resulting in more stable and reliable learning. For autonomous driving, where safety and predictability are paramount, reducing such bias is crucial. Soft Actor-Critic (SAC) incorporates entropy regularization into the reward, encouraging exploration by maximizing both expected return and policy entropy. This often leads to more robust policies that can better generalize to unseen situations, a critical requirement for real-world deployment [136]. Variants like Encoding Distributional SAC (E-DSAC) further enhance this by handling variable numbers of surrounding vehicles without manual feature sorting, improving policy performance and generality [137].

The theoretical underpinning of these algorithms lies in solving the Markov Decision Process (MDP) or its partially observable variant (POMDP) that formalizes the driving task. Value-based methods leverage Bellman optimality equations, policy gradients rely on the policy gradient theorem, and actor-critic methods combine both. For autonomous driving, the choice of algorithm is heavily influenced by the action space granularity (discrete tactical decisions vs. continuous low-level control), the need for sample efficiency given expensive simulation, and the paramount importance of training stability to converge on safe policies. While PPO and SAC are frequently highlighted for their robustness in continuous control, DQN variants remain relevant for hierarchical frameworks where high-level decisions are discrete. The ongoing evolution of these core algorithms, including efforts to reduce action oscillations [138] and improve policy gradient estimation [139], continues to push the boundaries of what is learnable in the complex, interactive domain of autonomous driving.

**Table: Comparison of approaches in 2.1 Core Deep Reinforcement Learning Algorithms**

| Method Family | Core Algorithm(s) | Key Characteristics / Strengths | Key Limitations / Weaknesses | Typical Use Cases in Autonomous Driving (from text) | Reference(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Value-based | Deep Q-Networks (DQN), Double DQN, Dueling DQN | Learns an action-value (Q) function; optimal policy derived by selecting action with highest Q-value; suitable for discrete action spaces. | Designed for discrete action spaces, struggles with "curse of dimensionality" for continuous control (e.g., steering, throttle); can suffer from overestimation bias and training instability. | High-level tactical decision-making (lane-change, intersection negotiation), highway overtaking. | [132], [17] |
| Policy Gradient | Trust Region Policy Optimization (TRPO), Proximal Policy Optimization (PPO) | Directly parameterizes and optimizes the policy; naturally suited for continuous, high-dimensional action spaces; learns smooth control policies. | High variance in gradient estimates; poor sample efficiency, requiring extensive environment interaction. | Complex continuous control tasks (roundabout navigation, general simulated driving maneuvers). | [133], [134] |
| Actor-Critic | Deep Deterministic Policy Gradient (DDPG), Twin Delayed DDPG (TD3), Soft Actor-Critic (SAC) | Two-network architecture (actor + critic) for more stable, sample-efficient learning; combines policy optimization with value estimation. | Can be sensitive to hyperparameters (DDPG); may suffer from overestimation bias (addressed by TD3). | Continuous control tasks from lane-keeping to eco-driving; tasks requiring robust generalization and exploration. | [135], [136], [137] |


### 2.2 Imitation Learning Paradigms and Techniques

Imitation Learning (IL) provides a powerful alternative to reinforcement learning by enabling agents to learn policies directly from expert demonstrations, circumventing the often difficult and unsafe process of reward engineering. The spectrum of IL paradigms ranges from simple supervised learning approaches to complex frameworks that infer underlying reward structures, each with distinct methodologies, strengths, and challenges pertinent to autonomous driving.

The most straightforward approach is **Behavior Cloning (BC)**, which treats IL as a supervised learning problem, mapping observed states to expert actions. Its simplicity and efficiency make it attractive for initial policy bootstrapping. However, BC suffers fundamentally from **covariate shift**: errors compound as the agent deviates from the expert's state distribution during execution, leading to catastrophic failures in long-horizon tasks. This is particularly problematic in driving, where a small error in steering can place the vehicle in a novel, unsafe state. Furthermore, BC's performance is heavily dependent on **data quality** and quantity; it requires a large volume of near-optimal demonstrations covering a wide variety of scenarios, which can be expensive to collect. Recent analyses suggest that even advanced adversarial methods can effectively reduce to BC in certain offline settings, highlighting its enduring role as a strong, if flawed, baseline [140].

To address the limitations of BC, **Inverse Reinforcement Learning (IRL)** seeks to infer the expert's underlying reward function, assuming demonstrations are optimal with respect to this unknown reward. The learned reward can then be used with standard RL to recover a robust policy. Classical IRL methods, like Maximum Entropy IRL, frame the problem as matching the expected feature counts of the expert's trajectories. Recent advancements focus on improving IRL's practicality and robustness. For instance, methods have been developed to learn from **suboptimal and heterogeneous demonstrations** by modeling demonstrator expertise or incorporating confidence scores, which is crucial for real-world driving data collected from human drivers of varying skill [141] [142]. Other works address the **sample efficiency** challenge, especially with limited demonstrations, through meta-learning for reward extrapolation or by leveraging offline data without requiring further environment interactions [143] [144]. A significant theoretical and practical challenge in IRL is **reward ambiguity**—many different reward functions can explain the same expert behavior. Techniques that consider both the ranking and the degree of difference between trajectories, or that learn context-hierarchical reward structures, have been proposed to resolve this ambiguity and improve interpretability [145] [146]. Furthermore, ensuring the **robustness** of the learned reward against model misspecification or dynamics mismatch between training and deployment environments is critical for safe transfer to real vehicles [147].

**Adversarial Imitation Learning (AIL)**, most notably Generative Adversarial Imitation Learning (GAIL), emerged as a highly influential paradigm that bypasses explicit reward function inference. It frames IL as a distribution matching problem, where a discriminator is trained to distinguish between state-action pairs from the expert and the agent, and the agent's policy is trained to "fool" the discriminator. This adversarial process implicitly drives the agent's state-action occupancy measure to match the expert's. GAIL and its variants are often more sample-efficient in terms of expert data and better mitigate covariate shift than BC, as they consider temporal consistency. However, they introduce their own challenges, including **training instability** due to the minimax optimization, sensitivity to hyperparameters, and high **interaction complexity** with the environment during training. A large body of recent research aims to stabilize and improve AIL. This includes replacing the Jensen-Shannon divergence with more stable metrics like the Wasserstein distance [148], integrating AIL with offline RL techniques for better data utilization [149], and developing non-adversarial alternatives that offer stronger convergence guarantees [150]. Other innovations incorporate energy-based models or diffusion models to better capture the expert distribution [151] [152]. Theoretical work has also begun to establish global convergence guarantees for AIL under certain conditions, providing a firmer foundation for its application [153].

Beyond these core paradigms, several specialized techniques address key IL challenges. **Offline IL** is crucial for autonomous driving, where online interaction in the real world is dangerous. Methods in this setting must learn solely from a static dataset of demonstrations, often mixed with suboptimal data. Successful approaches combine dynamics models with discriminators to increase effective data coverage or employ conservative reward learning to mitigate extrapolation errors [149] [154]. **State-only IL** is another practical direction, where demonstrations contain only state sequences (e.g., from video), not actions. This relaxes data collection constraints but is complicated by dynamics mismatch between the expert and learner environments [155]. Finally, **hybrid methods** that strategically combine IL and RL are gaining traction. These methods might use BC to initialize a policy and then refine it with RL, use IL to guide exploration, or shape rewards using demonstration information, aiming to achieve both the sample efficiency of IL and the asymptotic performance of RL [25] [156] [157].

In summary, the landscape of IL is rich and evolving, offering a suite of tools for learning driving policies from demonstration data. The choice of paradigm involves trade-offs between simplicity, data efficiency, robustness, and computational cost. For autonomous driving, overcoming distribution shift, learning robustly from imperfect human data, and ensuring safe offline training remain central challenges guiding the development of next-generation IL algorithms.

**Table: Comparison of approaches in 2.2 Imitation Learning Paradigms and Techniques**

| Paradigm / Method | Key Idea / Description | Primary Advantages | Primary Challenges / Limitations | Key References (from Source Papers) |
| :--- | :--- | :--- | :--- | :--- |
| **Behavior Cloning (BC)** | Treats IL as supervised learning, mapping states to expert actions. | Simple, efficient for initial policy bootstrapping. | Suffers from covariate shift; performance heavily dependent on data quality/quantity. | [140] |
| **Inverse Reinforcement Learning (IRL)** | Infers the expert's underlying reward function from demonstrations, then uses RL to recover a policy. | Can learn robust policies; can handle suboptimal demonstrations; can extrapolate beyond demonstrator. | Reward ambiguity; sample inefficiency; requires solving RL subproblem; robustness to dynamics mismatch. | [141], [142], [143], [144], [145], [146], [147] |
| **Adversarial Imitation Learning (AIL) / GAIL** | Frames IL as distribution matching via a discriminator that distinguishes expert vs. agent state-action pairs. | More sample-efficient in expert data than BC; mitigates covariate shift. | Training instability (minimax optimization); high interaction complexity; sensitive to hyperparameters. | [148], [149], [150], [151], [152], [153] |
| **Offline IL** | Learns solely from a static dataset without online environment interaction. | Safe for real-world applications like autonomous driving. | Must handle limited expert data and suboptimal data; risk of extrapolation errors. | [149], [154] |
| **State-only IL** | Learns from demonstrations containing only state sequences (no actions). | Relaxes data collection constraints (e.g., from video). | Complicated by dynamics mismatch between expert and learner environments. | [155] |
| **Hybrid IL/RL Methods** | Strategically combines IL (e.g., BC) and RL to leverage strengths of both. | Aims for sample efficiency of IL and asymptotic performance of RL. | Design complexity; balancing the contributions of IL and RL components. | [25], [156], [157] |


### 2.3 Safe and Robust Reinforcement Learning

The paramount importance of safety in autonomous driving necessitates that reinforcement learning (RL) policies are not only optimal but also robust and reliable under a wide spectrum of uncertainties. This has spurred significant research into Safe and Robust Reinforcement Learning, a subfield dedicated to formalizing and enforcing safety constraints while maintaining resilience against environmental perturbations and distribution shifts. The core methodologies can be categorized into three interconnected strands: constrained optimization formulations, runtime assurance techniques, and adversarial robustness frameworks.

A foundational approach is **Constrained RL**, which frames the problem as maximizing expected cumulative reward subject to constraints on expected cumulative cost, often modeled as a Constrained Markov Decision Process (CMDP). Lagrangian methods are widely employed to solve this optimization, where a multiplier penalizes constraint violations. However, traditional Lagrangian updates can lead to oscillatory and unstable training dynamics. Recent advancements address these issues by incorporating control-theoretic principles. For instance, **Responsive Safety in Reinforcement Learning by PID Lagrangian Methods** introduces proportional and derivative terms into the Lagrange multiplier update, analogous to a PID controller, which dampens oscillations and accelerates safe convergence [158]. Similarly, **Separated Proportional-Integral Lagrangian for Chance Constrained Reinforcement Learning** proposes a proportional-integral Lagrangian method with integral separation to prevent overshoot and reduce conservatism, ensuring a steadier learning process for probabilistic safety constraints [159]. Other algorithms seek to improve stability and optimality guarantees from different perspectives. **Constrained Variational Policy Optimization for Safe Reinforcement Learning** reframes safe RL as a probabilistic inference problem, decomposing it into a convex optimization phase (E-step) and a supervised learning phase (M-step), leading to more stable training [160]. For handling multiple, potentially conflicting constraints, **Trust Region-Based Safe Distributional Reinforcement Learning for Multiple Constraints** introduces a gradient integration method to manage infeasibility and uses a TD(λ) target distribution to estimate risk-averse constraints with low bias [161]. Furthermore, **Policy Bifurcation in Safe Reinforcement Learning** identifies scenarios where the feasible policy must be discontinuous to avoid constraint violations, proposing a multimodal policy optimization (MUPO) algorithm that uses a Gaussian mixture distribution to capture such necessary bifurcated behaviors, which is critical for complex navigation tasks [162].

While constrained RL optimizes for safety on average, **Runtime Assurance (RTA)** methods provide stricter, often instantaneous, safety guarantees by monitoring and correcting a potentially unsafe primary policy. A prominent RTA technique is **shielding**, which intercepts unsafe actions before execution. **Approximate Model-Based Shielding for Safe Reinforcement Learning** and its extension in **Leveraging Approximate Model-based Shielding for Probabilistic Safety Guarantees in Continuous Environments** demonstrate how learned world models can be used to verify policy rollouts in a latent space, providing strong probabilistic safety guarantees even in continuous settings without prior safety-relevant abstractions [81, 163]. Another powerful RTA framework leverages **Control Barrier Functions (CBFs)**. CBFs are Lyapunov-like functions used to define safe sets in the state space; a controller is then certified safe if it ensures the CBF derivative remains non-negative, thus keeping the state within the safe set. This concept is effectively integrated with RL in frameworks like the **Barrier-Lyapunov Actor-Critic (BLAC)** and its neural ODE-based variant **NLBAC**, which combine CBFs for safety and Control Lyapunov Functions (CLFs) for stability within an actor-critic architecture, using an augmented Lagrangian method for constraint satisfaction [164, 165]. **Safe Reinforcement Learning via Confidence-Based Filters** presents a control-theoretic safety filter that minimally adjusts a nominal RL policy towards a probabilistically safe backup policy, providing formal safety guarantees based on confidence intervals from a probabilistic dynamics model [166]. The idea of a **safety filter** is also applied in **Safety Filtering for Reinforcement Learning-based Adaptive Cruise Control**, where CBFs derived for high relative degree systems are used to project RL actions into a collision-safe set, allowing safe exploration [167].

Ensuring robustness against **adversarial perturbations and distribution shifts** is equally critical, as real-world sensors are noisy and environments are non-stationary. **Adversarial RL** methods train policies to be robust against worst-case disturbances. **ISAACS: Iterative Soft Adversarial Actor-Critic for Safety** co-trains a safety-seeking policy with an adversarial disturbance agent that simulates worst-case model errors, and the resulting policy is used to construct a real-time safety shield with robust guarantees [168]. **Certifying Safety in Reinforcement Learning under Adversarial Perturbation Attacks** situates RL in partially observable MDPs and proposes a framework for certifying the safety of policies under adversarial input perturbations, disentangling nominal efficiency from adversarial safety [169]. **Robust Policy Learning over Multiple Uncertainty Sets** moves beyond robustness to a single uncertainty set, formulating a multi-set robustness problem that combines system identification with robust RL to handle varied environmental perturbations efficiently [170]. To evaluate and benchmark progress in this diverse field, toolkits like **SafeRL-Kit** and **GUARD: A Safe Reinforcement Learning Benchmark** have been developed. SafeRL-Kit provides unified implementations of state-of-the-art safe RL algorithms under an off-policy setting, facilitating fair comparison and incorporation of domain knowledge [171], while GUARD offers a generalized benchmark with a wide variety of agents, tasks, and safety constraint specifications [117].

In summary, the development of safe and robust RL for autonomous driving is a multi-faceted endeavor. It combines the policy optimization rigor of constrained Lagrangian and variational methods with the instantaneous certification power of shielding and control-theoretic filters, all while hardening policies against adversarial realities through robust and adversarial training. The synergy of these approaches, supported by dedicated benchmarking suites, is essential for progressing from high-performing simulated agents to trustworthy real-world autonomous driving systems.

**Table: Comparison of approaches in 2.3 Safe and Robust Reinforcement Learning**

| Category | Method Name (as in text) | Key Idea / Mechanism | Reference (Exact Paper Title from Source List) |
| :--- | :--- | :--- | :--- |
| Constrained RL | PID Lagrangian Methods | Introduces proportional and derivative terms into the Lagrange multiplier update, analogous to a PID controller, to dampen oscillations and accelerate safe convergence. | [158] |
| Constrained RL | Separated Proportional-Integral Lagrangian | Proposes a proportional-integral Lagrangian method with integral separation to prevent overshoot and reduce conservatism for probabilistic safety constraints. | [159] |
| Constrained RL | Constrained Variational Policy Optimization (CVPO) | Reframes safe RL as probabilistic inference, decomposing it into a convex optimization phase (E-step) and a supervised learning phase (M-step) for stable training. | [160] |
| Constrained RL | Trust Region-Based Safe Distributional RL | Introduces a gradient integration method to manage infeasibility and uses a TD(λ) target distribution to estimate risk-averse constraints with low bias. | [161] |
| Constrained RL | Policy Bifurcation / Multimodal Policy Optimization (MUPO) | Uses a Gaussian mixture distribution to capture necessary discontinuous (bifurcated) policy behaviors for safety in non-simply connected state spaces. | [162] |
| Runtime Assurance (RTA) / Shielding | Approximate Model-Based Shielding (AMBS) | Uses learned world models to verify policy rollouts in a latent space, providing probabilistic safety guarantees without prior safety-relevant abstractions. | [81, 163] |
| Runtime Assurance (RTA) / Control Barrier Functions | Barrier-Lyapunov Actor-Critic (BLAC) | Combines Control Barrier Functions (CBFs) for safety and Control Lyapunov Functions (CLFs) for stability within an actor-critic architecture using an augmented Lagrangian. | [164, 165] |
| Runtime Assurance (RTA) / Safety Filter | Confidence-Based Safety Filters | A control-theoretic filter that minimally adjusts a nominal RL policy towards a probabilistically safe backup policy based on confidence intervals from a probabilistic dynamics model. | [166] |
| Runtime Assurance (RTA) / Safety Filter | Safety Filtering for ACC | Uses CBFs derived for high relative degree systems to project RL actions into a collision-safe set, allowing safe exploration for adaptive cruise control. | [167] |
| Adversarial Robustness | ISAACS: Iterative Soft Adversarial Actor-Critic for Safety | Co-trains a safety-seeking policy with an adversarial disturbance agent simulating worst-case model errors; the policy is used to construct a real-time safety shield. | [168] |
| Adversarial Robustness | Certifying Safety under Adversarial Perturbations | Situates RL in POMDPs and proposes a framework for certifying policy safety under adversarial input perturbations, disentangling nominal efficiency from safety. | [169] |
| Adversarial Robustness | Robust Policy Learning over Multiple Uncertainty Sets | Formulates a multi-set robustness problem combining system identification with robust RL to handle varied environmental perturbations efficiently. | [170] |
| Benchmarking | SafeRL-Kit | Provides unified implementations of state-of-the-art safe RL algorithms under an off-policy setting for fair comparison in autonomous driving. | [171] |
| Benchmarking | GUARD | A generalized benchmark with a wide variety of agents, tasks, and safety constraint specifications for comparing safe RL algorithms. | [117] |


### 2.4 Exploration Strategies and Sample Efficiency

A fundamental challenge in applying reinforcement learning (RL) to autonomous driving is the immense sample inefficiency and the difficulty of exploration in complex, safety-critical environments. The state and action spaces are vast, and informative rewards (e.g., for avoiding a collision that never happened) are exceptionally sparse. Consequently, developing sophisticated exploration strategies and data-efficient learning paradigms is not merely beneficial but essential for viable policy learning. This subsection dissects key methodologies aimed at improving exploration and sample efficiency, moving beyond simple ε-greedy or entropy-based heuristics.

**Intrinsic Motivation and Curiosity-Driven Exploration** form a cornerstone of modern exploration strategies. The core idea is to supplement the sparse extrinsic task reward with a dense intrinsic reward that encourages the agent to visit novel or informative states. Classical approaches reward state novelty, but as noted in [172], there is a critical gap between observation novelty and exploratory behavior, as environmental stochasticity can also cause new observations. DEIR addresses this by deriving an intrinsic reward based on the novelty *contributed by the agent's actions*, implemented via a discriminative forward model, leading to more accurate exploration assessment. However, a persistent issue with intrinsic motivation is its potential to distract the agent in environments where extrinsic rewards are sufficient. [173] tackles this by framing the balance between intrinsic and extrinsic rewards as a constrained optimization problem. Their Extrinsic-Intrinsic Policy Optimization (EIPO) method automatically suppresses intrinsic rewards when exploration is unnecessary and amplifies them when required, ensuring consistent performance across diverse tasks without manual tuning. For goal-conditioned settings, such as navigating to arbitrary destinations, exploration can be even more challenging. [174] demonstrates how curiosity-driven exploration can first generate a robust world model and diverse trajectories. They then show that extracting a goal-conditioned policy from this unsupervised data requires careful offline value function learning, proposing a combination of model-based planning and graph-based value aggregation to mitigate estimation artifacts and enable effective zero-shot goal reaching.

**Off-Policy Learning and Hybrid Data Utilization** are critical for sample efficiency, as they allow learning from historical data not generated by the current policy. Standard off-policy algorithms like DDPG or SAC leverage experience replay, but their effectiveness can be limited by the quality and coverage of the stored data. [175] investigates how to effectively combine offline datasets with online interaction, demonstrating that minimal modifications to existing off-policy algorithms can yield significant (2.5x) improvements by properly handling the mixed data distribution. This aligns with the hybrid RL paradigm, where [176] explicitly integrates off-policy training into an on-policy Natural Policy Gradient (NPG) framework. This approach offers theoretical guarantees, achieving the robustness of on-policy methods while leveraging the sample efficiency of off-policy learning from prior data. When dealing with multiple suboptimal data sources, such as different driving styles, [177] introduces MAPS, which actively selects which oracle to imitate in each state, and MAPS-SE, which adds an active state exploration criterion. This allows for sample-efficient policy improvement by dynamically leveraging the strengths of various demonstrators. The challenge of exploration is particularly acute in the purely offline setting, where no further environment interaction is allowed. [178] decouples data collection from policy learning, evaluating exploration strategies like curiosity-based intrinsic motivation by measuring the quality of the datasets they produce for solving downstream tasks, providing crucial intuition about the data prerequisites for effective offline RL.

**Evolutionary and Gradient-Based Hybrids** combine population-based evolutionary algorithms (EAs) with gradient-based RL to harness complementary strengths: EAs offer global exploration, robustness to sparse rewards, and stability, while gradient methods provide sample efficiency and precise local optimization. [179] introduces Evolutionary RL (ERL), where a population of agents explored via EA provides diversified training data for an RL agent, which is periodically injected back into the population to guide evolution with gradient information. This synergy addresses core RL difficulties like credit assignment and brittle convergence. Building on this, [180] proposes a two-scale representation: a shared nonlinear state representation learned collectively and individual linear policy representations. This design enables efficient behavior-level crossover and mutation in a semantically meaningful policy space, further improving sample efficiency and final performance. Similarly, [181] combines the Cross-Entropy Method (CEM) with TD3, using CEM to maintain a population of policy parameters that explore broadly, while TD3 refines the best performers with gradient updates, achieving a superior trade-off between performance and sample efficiency. These hybrids are particularly promising for autonomous driving, where policies must be robust and learn complex skills without getting trapped in local optima.

**Structured and Meta-Learning Exploration Strategies** move beyond adding simple noise, seeking to learn or structure exploration in more principled ways. [182] argues that bonus-based exploration (BBE) can be detrimental in continuous control due to bias and slow coverage. Their DEEP framework decouples the exploration policy from the exploitation (task) policy, allowing the former to be optimized purely for directed exploration without compromising the latter's stability. For meta-learning scenarios where an agent must quickly adapt to new tasks, [183] explicitly learns a separate exploration policy for a distribution of tasks. This provides more flexible and efficient exploration during meta-testing compared to methods that force a single policy to handle both exploration and exploitation. The principle of separating exploration and exploitation phases is also central to [184], which uses a meta-RL framework to train one policy solely to explore (e.g., learning to exhaustively search or open doors) and another to exploit the gathered information, avoiding the conflict inherent in simultaneous exploration and exploitation. In continuous action spaces, [185] introduces a novel strategy within a double-Q framework, constructing an exploration policy from sampled actions weighted by a conservative Q-value, while learning a surrogate policy to mimic this exploratory behavior, leading to more robust and efficient learning.

In summary, advancing autonomous driving policy learning necessitates a multi-faceted approach to exploration and sample efficiency. Intrinsic motivation must be intelligently regulated to avoid distraction. Off-policy and hybrid algorithms must robustly synthesize offline data with online learning. Evolutionary hybrids offer a path to global robustness and exploration. Finally, structured and meta-learned exploration strategies promise to move beyond heuristic noise towards systematic, intelligent investigation of the environment. The integration of these techniques is pivotal for developing RL policies that can learn complex, safe driving behaviors within a practical computational and data budget.

**Table: Comparison of approaches in 2.4 Exploration Strategies and Sample Efficiency**

| Method Category | Core Idea / Mechanism | Key Contribution / Differentiator | Reference |
| :--- | :--- | :--- | :--- |
| Intrinsic Motivation & Curiosity | Supplement sparse extrinsic reward with dense intrinsic reward for visiting novel/informative states. | DEIR derives reward from novelty *contributed by agent's actions* via a discriminative forward model, addressing the gap between observation novelty and exploratory behavior. | [172] |
| Intrinsic Motivation & Curiosity | Balance intrinsic and extrinsic rewards via constrained optimization. | EIPO automatically suppresses intrinsic rewards when unnecessary and amplifies them when required, ensuring consistent performance without manual tuning. | [173] |
| Intrinsic Motivation & Curiosity | Use curiosity-driven exploration to build a world model, then extract a goal-conditioned policy from the unsupervised data. | Combines model-based planning over learned value landscapes with graph-based value aggregation to correct estimation artifacts for effective zero-shot goal reaching. | [174] |
| Off-Policy & Hybrid Data | Combine offline datasets with online interaction using minimal modifications to off-policy algorithms. | Demonstrates significant (2.5x) sample efficiency improvements by properly handling the mixed data distribution. | [175] |
| Off-Policy & Hybrid Data | Integrate off-policy training into an on-policy Natural Policy Gradient (NPG) framework. | Provides theoretical guarantees, achieving on-policy robustness while leveraging off-policy sample efficiency from prior data. | [176] |
| Off-Policy & Hybrid Data | Imitate and improve from multiple suboptimal black-box oracles. | MAPS actively selects which oracle to imitate per state; MAPS-SE adds an active state exploration criterion for sample-efficient policy improvement. | [177] |
| Off-Policy & Hybrid Data | Decouple data collection from policy learning to evaluate exploration strategies for offline RL. | Proposes evaluating data collection quality by measuring downstream task performance, providing intuition about data prerequisites for offline RL. | [178] |
| Evolutionary & Gradient Hybrids | Combine EA population (for global exploration) with a gradient-based RL agent (for sample efficiency). | ERL uses an EA population to provide diversified training data for an RL agent, which is injected back to guide evolution, addressing credit assignment and brittle convergence. | [179] |
| Evolutionary & Gradient Hybrids | Use a two-scale representation: shared state representation and individual linear policy representations. | Enables efficient behavior-level crossover/mutation in a meaningful policy space, improving sample efficiency and final performance. | [180] |
| Evolutionary & Gradient Hybrids | Combine Cross-Entropy Method (CEM) with TD3. | Uses CEM to maintain a population for broad exploration and TD3 for gradient-based refinement of the best performers, achieving a superior performance-sample efficiency trade-off. | [181] |
| Structured & Meta-Learning Exploration | Decouple the exploration policy from the exploitation (task) policy. | DEEP allows the exploration policy to be optimized purely for directed exploration without compromising the exploitation policy's stability, improving performance in sparse environments. | [182] |
| Structured & Meta-Learning Exploration | Learn a separate exploration policy for a distribution of tasks in meta-RL. | MAME provides more flexible and efficient exploration during meta-testing compared to methods using a single policy for both exploration and exploitation. | [183] |
| Structured & Meta-Learning Exploration | Meta-RL framework with one policy trained solely to explore and another to exploit the gathered information. | First-Explore avoids the conflict of simultaneous exploration and exploitation, enabling learning of intelligent exploration strategies like exhaustive search. | [184] |
| Structured & Meta-Learning Exploration | Novel exploration strategy within a double-Q framework for continuous action spaces. | Constructs an exploration policy from sampled actions weighted by a conservative Q-value and learns a surrogate policy to mimic it, leading to robust and efficient learning. | [185] |


### 2.5 Reward Design and Shaping

The efficacy of Deep Reinforcement Learning (DRL) for autonomous driving is fundamentally governed by the reward function, which translates the complex, multi-faceted objectives of safe and efficient navigation into a scalar signal the agent can optimize. Naive reward design, such as sparse terminal rewards for reaching a destination, leads to prohibitive sample inefficiency and poor convergence. Consequently, sophisticated reward engineering and shaping are indispensable for practical policy learning. This involves crafting dense, informative reward signals that guide exploration, balance competing objectives, and ensure the learned policy aligns with nuanced human preferences and safety imperatives.

A foundational principle for effective reward design is to maximize the "action gap"—the difference in value between optimal and suboptimal actions—and minimize the "subjective discount" horizon over which rewards need to be optimized, thereby making optimal decisions easier to learn [186]. Simple heuristics like penalizing each step and gradually increasing reward for subgoal achievement along a target trajectory can significantly accelerate learning. For autonomous driving, this translates to dense reward structures that provide continuous feedback. A common paradigm decomposes the monolithic task into weighted sub-rewards for longitudinal control (e.g., maintaining a safe headway, tracking a desired speed), lateral control (e.g., lane keeping, smooth steering), and safety (e.g., collision penalties, dangerous proximity warnings) [187]. However, manually tuning the weights for these components is a brittle and labor-intensive process known as "reward hacking."

Reward shaping formally addresses this by adding auxiliary rewards \( F(s, a, s') \) to the environmental reward \( R(s, a, s') \) to provide more frequent guidance without altering the optimal policy. The gold standard is Potential-Based Reward Shaping (PBRS), where \( F(s, a, s') = \gamma \Phi(s') - \Phi(s) \), guaranteeing policy invariance [188]. In driving, a potential function \( \Phi(s) \) can be defined based on progress along the route, alignment with the lane center, or inverse distance to obstacles. For instance, [86] draws inspiration from control barrier functions to create safety-oriented potential functions that aggressively penalize proximity to constraint violations, leading to faster convergence and lower control effort in robotic locomotion, a principle directly applicable to collision avoidance in driving. Similarly, [189] proposes a physics-inspired shaping method where targets and obstacles generate nonlinear, anisotropic potential fields, offering more nuanced guidance than simple distance metrics in dynamic environments.

A significant advancement is the move from manual shaping to learning the reward function itself. Inverse Reinforcement Learning (IRL) and its adversarial counterpart, Generative Adversarial Imitation Learning (GAIL), learn a reward function from expert demonstrations that explains the expert's behavior, thereby implicitly capturing complex driving styles and safety considerations. More recently, preference-based RL (PbRL) learns a reward model from human preferences over trajectory segments, which is particularly valuable for specifying nuanced objectives like "comfort" or "assertiveness" that are difficult to quantify [190]. The PRIOR framework improves PbRL efficiency by incorporating structural priors about the reward function during learning [191]. Furthermore, large foundation models are being leveraged for automatic reward generation. [192] uses Vision-Language Models (VLMs) to provide preference labels on image observations based on text task descriptions, enabling reward learning for manipulation without manual engineering, a technique with clear potential for interpreting driving scenes. [193] explores using Large Language Models (LLMs) to encode social and moral norms into reward signals, which is critical for driving in complex social environments.

Autonomous driving inherently involves multiple, often competing objectives: efficiency (travel time), safety (collision avoidance), comfort (low jerk), and energy economy. Multi-Objective Reinforcement Learning (MORL) and utility-based frameworks provide principled ways to balance these [194]. Instead of a scalar sum, the reward can be a vector, and the agent learns a Pareto-optimal policy. The utility-based paradigm incorporates a function that maps this vector to a scalar utility based on user preferences, unifying MORL with risk-aware and safe RL. For instance, [195] optimizes objectives defined on the Cumulative Distribution Function (CDF) of returns, allowing designers to specify "pessimistic" risk profiles that focus on improving worst-case performance, directly enhancing safety. [196] further generalizes this by considering MDPs where the objective is to optimize a general utility function of the cumulative reward, providing a theoretical framework for diverse risk preferences crucial for handling the uncertainties of real-world traffic.

Hierarchical and structured reward methods offer another powerful avenue. [197] expose the finite-state-machine structure of non-Markovian reward functions, enabling automated reward shaping, task decomposition, and counterfactual reasoning that dramatically improve sample efficiency. This is apt for driving, where tasks have clear stages (e.g., lane change: check blind spot, signal, execute). Similarly, [198] and [199] learn reusable dense rewards or subtask compositions from high-level task structures, reducing the need for per-task reward engineering. For safety-critical constraints, methods like [200] use a bi-level optimization to learn how to best combine (or ignore) heuristic auxiliary rewards with environment rewards, enhancing robustness against misspecified shaping rewards—a common pitfall in practice.

Finally, the integrity of the reward function is paramount. The field must contend with reward tampering, where an advanced agent might exploit flaws in the reward specification to achieve high reward through unintended, potentially dangerous behaviors [201]. Furthermore, the reward function is a core site for embedding ethical values and ensuring accountability. The concept of "Reward Reports" has been proposed as living documents that demarcate design choices, making the values and assumptions baked into the AI system transparent for policymakers and stakeholders [202]. In summary, reward design and shaping have evolved from a manual tuning art to a rich discipline combining principled shaping, learned reward models from diverse feedback, multi-objective optimization, and structured decomposition. This progression is essential for developing autonomous driving policies that are not only performant but also safe, aligned, and trustworthy.

**Table: Comparison of approaches in 2.5 Reward Design and Shaping**

| Method Category | Specific Method/Concept | Key Idea/Contribution | Reference |
| :--- | :--- | :--- | :--- |
| Reward Shaping | Potential-Based Reward Shaping (PBRS) | Adds auxiliary rewards F(s, a, s') = γΦ(s') - Φ(s) to provide guidance without altering the optimal policy. | [188] |
| Reward Shaping | Barrier Functions Inspired Reward Shaping | Creates safety-oriented potential functions inspired by control barrier functions to aggressively penalize proximity to constraint violations. | [86] |
| Reward Shaping | Magnetic Field-Based Reward Shaping | Proposes a physics-inspired method where targets/obstacles generate nonlinear, anisotropic potential fields for nuanced guidance. | [189] |
| Learned Reward Models | Inverse Reinforcement Learning (IRL) / Generative Adversarial Imitation Learning (GAIL) | Learns a reward function from expert demonstrations to implicitly capture complex behaviors and safety considerations. | (Not explicitly listed in provided sources, but foundational to the text's discussion) |
| Learned Reward Models | Preference-based RL (PbRL) | Learns a reward model from human preferences over trajectory segments to specify nuanced objectives like "comfort". | [190] |
| Learned Reward Models | PRIOR Framework | Improves PbRL efficiency by incorporating structural priors about the reward function during learning. | [191] |
| Foundation Model Reward Generation | RL-VLM-F | Uses Vision-Language Models (VLMs) to provide preference labels on image observations based on text descriptions for automatic reward generation. | [192] |
| Foundation Model Reward Generation | LLMs for Social/Moral Norms | Explores using Large Language Models (LLMs) to encode social and moral norms into reward signals. | [193] |
| Multi-Objective & Risk-Aware RL | Multi-Objective RL (MORL) / Utility-based Frameworks | Balances competing objectives via vector rewards or a utility function mapping rewards to a scalar based on user preferences. | [194] |
| Multi-Objective & Risk-Aware RL | Risk-Sensitive Policy Optimization | Optimizes objectives defined on the CDF of returns, allowing for "pessimistic" risk profiles that focus on worst-case performance. | [195] |
| Multi-Objective & Risk-Aware RL | Risk-sensitive MDPs under General Utility | Considers MDPs where the objective is to optimize a general utility function of the cumulative reward for diverse risk preferences. | [196] |
| Hierarchical & Structured Methods | Reward Machines | Exposes the finite-state-machine structure of non-Markovian reward functions for automated shaping, decomposition, and reasoning. | [197] |
| Hierarchical & Structured Methods | DrS (Learning Reusable Dense Rewards) | Learns reusable dense rewards for multi-stage tasks from sparse rewards and demonstrations. | [198] |
| Hierarchical & Structured Methods | Automatic Subtask Composition | Automatically learns to compose subtasks given a set of labels to structure the reward function for sample efficiency. | [199] |
| Robust Reward Integration | Behavior Alignment via Reward Function Optimization | Uses bi-level optimization to learn how to best combine heuristic auxiliary rewards with environment rewards for robustness. | [200] |
| Reward Safety & Ethics | Reward Tampering Analysis | Studies and provides design principles to prevent agents from having an instrumental goal to tamper with their reward process. | [201] |
| Reward Safety & Ethics | Reward Reports | Proposes living documents that demarcate design choices to make the values and assumptions in AI systems transparent. | [202] |


### 2.6 Hybrid and Integrated RL-IL Methods

The paradigm of learning from demonstrations and then refining through interaction is a cornerstone of modern autonomous driving research, addressing the critical need for sample efficiency, safety, and stable policy improvement. Hybrid and integrated Reinforcement Learning (RL) and Imitation Learning (IL) methods provide a structured pathway to achieve this, moving beyond the limitations of purely offline or purely online approaches. These frameworks can be broadly categorized into sequential pre-training and fine-tuning, interleaved online learning, and unified theoretical formulations that leverage offline data as a constraint or guide.

A foundational sequential approach is **Jump-Start Reinforcement Learning (JSRL)** [203]. This meta-algorithm employs two policies: a guide-policy (often derived from offline data or demonstrations) and an exploration-policy. The guide-policy creates a curriculum of starting states, effectively "jump-starting" the exploration-policy from progressively more challenging initial configurations. This method bypasses the need for extensive random exploration from scratch, significantly reducing the sample complexity required for the RL agent to learn competent behavior, which is paramount in costly real-world driving domains. The concept of using prior data to initialize or guide online RL is extended in works like [204], which explicitly treats offline RL as a "launchpad" for efficient online policy improvement, pre-training on historical data before switching to online interaction. Similarly, [205] investigates optimal strategies for allocating a limited online interaction budget between executing a suboptimal teacher policy and exploring with a student policy, finding that a hybrid use of data from both yields the best performance—a finding directly applicable to autonomous driving where logged human driver data is abundant but suboptimal.

The transition from offline pre-training to online fine-tuning, however, is fraught with challenges such as performance degradation and distribution shift. This **offline-to-online (O2O) RL** setting has spawned numerous algorithms designed for smooth and efficient adaptation. [206] introduces a prioritized sampling scheme that dynamically adjusts the mixture of offline and online data in the replay buffer to facilitate stable transfer. [207] proposes a trust-region-style update with an iteratively evolving regularization term, gradually relaxing the constraint from the offline policy to enable stable initial fine-tuning and optimal final performance. Simpler yet effective frameworks like [208] and [209] (SUNG) aim to unify objectives. Uni-O4 uses an on-policy objective for both phases, aligning the learning process, while SUNG employs a density estimator to quantify uncertainty, using it to guide optimistic exploration for high-uncertainty states and conservative exploitation for low-uncertainty states, thereby bridging the two stages seamlessly.

A significant challenge in O2O RL is overcoming the inherent conservatism of offline RL algorithms, which can stifle necessary exploration. Methods like [210] (PTGOOD) explicitly frame O2O as an exploration problem. Instead of constraining the policy to the offline data distribution, PTGOOD uses non-myopic planning to target exploration in high-reward regions of the state-action space that are unlikely to be visited by the behavior policy, thereby actively seeking to improve beyond the dataset's limitations. Conversely, [211] (OOO) proposes a decoupled strategy: an optimistic exploration policy collects online data, while a separate pessimistic exploitation policy is periodically retrained from scratch on the entire aggregated dataset (offline + online). This decoupling mitigates the bias introduced by exploratory bonuses or intrinsic rewards in the final evaluation policy, often leading to superior performance.

Beyond sequential pipelines, other methods **interleave or unify IL and RL in a single objective**. The **Dual RL** framework [212] provides a theoretical unification, casting offline RL and imitation learning as instances of an unconstrained dual optimization problem. This perspective helps diagnose shortcomings in prior methods and leads to new algorithms like ReCOIL for imitation learning from arbitrary off-policy data. [213] (BPPO) makes the observation that on-policy algorithms like PPO possess an inherent conservatism suitable for offline RL, requiring no extra constraints or regularization. [214] is an online algorithm that intelligently interleaves off-policy updates with on-policy updates, using the effective sample size to control the trade-off, thereby gaining the sample efficiency of off-policy learning with the stability of on-policy methods.

The integration often relies on **leveraging offline data as an adaptive constraint or guide**. [215] (GORL) moves away from a "one-size-fits-all" policy constraint. It uses a small set of expert demonstrations to train a guiding network that adaptively weights the importance of policy improvement versus policy constraint on a per-sample basis, allowing for more aggressive improvement on promising data points. [216] (FamO2O) extends this idea by training a family of policies with different constraint intensities and a meta-learner to select the appropriate policy for each state, achieving state-adaptive balance. For model-based methods, [217] (ORPO) explicitly generates optimistic rollouts in out-of-distribution regions using a separate rollout policy, then relabels them with penalized rewards for use in a pessimistic policy optimization step, thereby safely harnessing the generalization power of the learned model.

In the context of autonomous driving, these hybrid paradigms are essential. They enable starting from vast datasets of human driving (offline IL/RL) to acquire foundational road rules and safety reflexes. Subsequent online fine-tuning in simulation or controlled real-world settings allows the policy to learn superior, more robust strategies for complex scenarios like interactive merges or extreme edge cases. Frameworks that support safe exploration and adaptive constraints are particularly valuable for navigating the sim-to-real gap and ensuring reliable deployment. By synergistically combining the stability and data-efficiency of IL with the optimality-seeking nature of RL, hybrid methods represent a mature and promising direction for developing high-performance, robust, and safe autonomous driving policies.

**Table: Comparison of approaches in 2.6 Hybrid and Integrated RL-IL Methods**

| Method Name (as in text) | Category (as in text) | Key Idea / Mechanism (from text) | Reference (Exact Full Paper Title from Input 2) |
| :--- | :--- | :--- | :--- |
| Jump-Start Reinforcement Learning (JSRL) | Sequential pre-training and fine-tuning | Employs a guide-policy (from offline data/demos) and an exploration-policy. The guide-policy creates a curriculum of starting states to "jump-start" exploration, bypassing extensive random exploration. | [203] |
| Launchpad | Sequential pre-training and fine-tuning | Treats offline RL as a "launchpad" for efficient online policy improvement, pre-training on historical data before switching to online interaction. | [204] |
| How to Spend Your Robot Time | Sequential pre-training and fine-tuning | Investigates optimal allocation of a limited online interaction budget between a suboptimal teacher policy and a student policy, finding hybrid use of data yields best performance. | [205] |
| MOORe | Offline-to-Online (O2O) RL | Introduces a prioritized sampling scheme that dynamically adjusts the mixture of offline and online data in the replay buffer to facilitate stable transfer. | [206] |
| PROTO | Offline-to-Online (O2O) RL | Proposes a trust-region-style update with an iteratively evolving regularization term, gradually relaxing the constraint from the offline policy. | [207] |
| Uni-O4 | Offline-to-Online (O2O) RL | Uses a multi-step on-policy objective for both offline and online phases, aligning the learning process. | [208] |
| SUNG | Offline-to-Online (O2O) RL | Employs a density estimator to quantify uncertainty, using it to guide optimistic exploration for high-uncertainty states and conservative exploitation for low-uncertainty states. | [209] |
| PTGOOD | Offline-to-Online (O2O) RL | Frames O2O as an exploration problem, using non-myopic planning to target exploration in high-reward regions unlikely to be visited by the behavior policy. | [210] |
| OOO | Offline-to-Online (O2O) RL | Proposes a decoupled strategy: an optimistic exploration policy collects online data, while a separate pessimistic exploitation policy is periodically retrained from scratch on the aggregated dataset. | [211] |
| Dual RL | Interleave/unify IL and RL | Provides a theoretical unification, casting offline RL and imitation learning as instances of an unconstrained dual optimization problem. | [212] |
| BPPO | Interleave/unify IL and RL | Observes that on-policy algorithms like PPO possess inherent conservatism suitable for offline RL, requiring no extra constraints. | [213] |
| P3O | Interleave/unify IL and RL | An online algorithm that intelligently interleaves off-policy updates with on-policy updates, using effective sample size to control the trade-off. | [214] |
| GORL | Leveraging offline data as adaptive constraint/guide | Uses a small set of expert demonstrations to train a guiding network that adaptively weights the importance of policy improvement vs. constraint per sample. | [215] |
| FamO2O | Leveraging offline data as adaptive constraint/guide | Trains a family of policies with different constraint intensities and a meta-learner to select the appropriate policy for each state. | [216] |
| ORPO | Leveraging offline data as adaptive constraint/guide | Generates optimistic rollouts in out-of-distribution regions using a separate rollout policy, then relabels them with penalized rewards for use in pessimistic policy optimization. | [217] |


### 2.7 Offline Reinforcement and Imitation Learning

Learning policies exclusively from static, pre-collected datasets, without any online interaction with the environment, represents a paradigm shift crucial for real-world autonomous driving. This offline learning setting directly addresses the prohibitive costs, safety risks, and logistical challenges of training policies through trial-and-error in physical vehicles. The core challenge, however, is the **distributional shift** between the state-action visitation distribution of the dataset's behavior policy and the learned target policy. When a policy queries values for actions not represented in the data, standard off-policy RL algorithms suffer from extrapolation errors and unconstrained value overestimation, leading to catastrophic failure. Offline Reinforcement Learning (RL) and Offline Imitation Learning (IL) have thus emerged as distinct yet complementary frameworks to extract performant and safe driving policies from historical logs, telemetry, or demonstration datasets.

A dominant strategy in offline RL is to learn **conservative value functions** that penalize or underestimate the value of out-of-distribution (OOD) actions. **Conservative Q-Learning (CQL)** is a seminal algorithm in this vein, which augments the standard Bellman error objective with a regularizer that minimizes Q-values for actions under the learned policy while maximizing them for actions present in the dataset, thereby learning a lower-bound Q-function [218]. This principle of pessimism under uncertainty is foundational. Extensions like **Mildly Conservative Q-Learning (MCQ)** aim to refine this approach by actively training on OOD actions with assigned pseudo Q-values to prevent over-pessimism that hinders generalization [219]. Other methods induce conservatism through uncertainty quantification, such as **Pessimistic Bootstrapping for Uncertainty-Driven Offline Reinforcement Learning (PBRL)**, which uses the disagreement of an ensemble of Q-functions to estimate uncertainty and penalize the value function accordingly [220]. A related approach is to learn **confidence-conditioned value functions**, which enable adaptive conservatism during evaluation by conditioning the Q-function on a desired confidence level [221].

An alternative to modifying the value function is to directly constrain the policy to remain close to the data distribution, a technique known as **behavior regularization**. This can be implemented as an explicit constraint or a penalty in the policy objective. Algorithms like **TD3+BC** and **Behavior Regularized Actor Critic (BRAC)** add a simple behavior cloning loss to the policy update, tethering the policy to actions observed in the dataset [222][223]. However, a uniform constraint can be overly restrictive. **Advantage-Aware Policy Optimization (A2PO)** addresses this by disentangling action distributions based on their advantage values, allowing the policy to deviate more freely from low-advantage actions while adhering closely to high-advantage ones [224]. Similarly, **Soft Behavior-regularized Actor Critic (SBAC)** derives a state-dependent regularization weight, allowing more policy deviation at high-confidence states [225]. The **Guided Offline RL (GORL)** framework uses a small set of expert demonstrations to adaptively determine the constraint intensity per sample, moving beyond a one-size-fits-all balance [215].

A significant advancement is the **in-sample learning** paradigm, which entirely avoids querying the value of unseen actions. **Implicit Q-Learning (IQL)** is a prominent example that approximates the optimal value function using expectile regression on the dataset's actions, subsequently extracting the policy via advantage-weighted regression [226]. This principle is extended in methods like **Offline RL with No OOD Actions  In-Sample Learning via Implicit Value Regularization**, which frames in-sample learning as implicit value regularization [227]. **Critic Regularized Regression (CRR)** also operates within this spirit, using the critic to weight behavior cloning losses without evaluating OOD actions [228].

The characteristics of the offline dataset itself are paramount. Algorithms must handle **mixed-quality datasets** containing trajectories of varying optimality. When data is highly suboptimal, strict behavior cloning fails, and offline RL methods must carefully balance improvement against distribution shift. Studies show that in sparse-reward or long-horizon tasks with suboptimal data, offline RL can significantly outperform pure Behavior Cloning (BC) [229]. Techniques like **Harnessing Mixed Offline Reinforcement Learning Datasets via Trajectory Weighting** reweight the dataset sampling to emphasize higher-return trajectories, enabling algorithms to better exploit high-performing data [230]. For **imbalanced datasets** with non-uniform coverage, methods like **CQL (ReDS)** reweight the data distribution to enforce an approximate support constraint, allowing the policy more freedom in states with high behavioral variability [231]. **Beyond Uniform Sampling  Offline RL with Imbalanced Datasets** proposes sampling strategies that constrain the policy only to "good data" rather than all actions [232].

**Offline Imitation Learning** faces analogous distribution shift challenges when demonstrations are suboptimal. **Relaxed Distribution Matching (RelaxDICE)** addresses this by employing an asymmetrically-relaxed f-divergence, imposing little penalty when the learned policy's density is within a bound of the behavior policy's, thus avoiding overly conservative constraints [92]. **Curriculum Offline Imitation Learning (COIL)** uses an experience-picking strategy to imitate progressively better neighboring policies within the dataset, improving the policy through curriculum stages [233].

A highly practical setting is **offline-to-online reinforcement learning**, where a policy pre-trained on offline data is fine-tuned with limited online interaction. The key challenge is to avoid performance collapse due to the sudden distribution shift while enabling efficient online learning. **Calibrated Q-learning (Cal-QL)** learns a calibrated, conservative Q-function initialization that underestimates the offline policy's value but provides a reasonable scale, enabling stable and rapid online fine-tuning [234]. **Adaptive Policy Learning** framework applies a pessimistic update strategy for offline data and an optimistic one for online data [235]. Furthermore, **Train Once, Get a Family  State-Adaptive Balances for Offline-to-Online Reinforcement Learning (FamO2O)** trains a family of policies with different constraint intensities and uses a balance model to select the appropriate policy per state during fine-tuning [216].

Other important directions include **model-based offline RL**, where a learned dynamics model can be used for planning or data augmentation while penalizing rewards by model uncertainty to mitigate distribution shift, as in **Model-based Offline Policy Optimization (MOPO)** [236]. **Representation learning** from offline data via unsupervised objectives can also provide powerful pretraining for downstream policy learning [237]. For autonomous driving specifically, where action spaces are continuous, **action quantization** via state-conditioned discretization (e.g., using VQ-VAE) can make offline RL constraints more precise and improve performance [238].

In summary, offline RL and IL provide the essential methodologies for bootstrapping autonomous driving policies from the vast amounts of historical driving data. The field has evolved from simple behavior cloning and conservative value learning to sophisticated techniques handling dataset imbalance, enabling safe offline-to-online transfer, and performing in-sample optimization. The choice of algorithm depends critically on dataset properties—its coverage, optimality, and heterogeneity—highlighting the need for robust methods that can extract maximal performance from static datasets while rigorously managing the ever-present risk of distributional shift.

**Table: Comparison of approaches in 2.7 Offline Reinforcement and Imitation Learning**

| Method Name | Category | Key Idea / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| Conservative Q-Learning (CQL) | Conservative Value Learning | Augments Bellman error with a regularizer to minimize Q-values for actions under the learned policy and maximize them for actions in the dataset, learning a lower-bound Q-function. | [218] |
| Mildly Conservative Q-Learning (MCQ) | Conservative Value Learning | Actively trains on OOD actions with assigned pseudo Q-values to prevent over-pessimism and improve generalization. | [219] |
| Pessimistic Bootstrapping for Uncertainty-Driven Offline Reinforcement Learning (PBRL) | Conservative Value Learning | Uses disagreement of an ensemble of Q-functions to estimate uncertainty and penalize the value function accordingly. | [220] |
| Confidence-Conditioned Value Functions | Conservative Value Learning | Conditions the Q-function on a desired confidence level to enable adaptive conservatism during evaluation. | [221] |
| TD3+BC | Behavior Regularization | Adds a simple behavior cloning loss to the policy update to tether the policy to actions observed in the dataset. | [222] |
| Behavior Regularized Actor Critic (BRAC) | Behavior Regularization | Regularizes the policy to stay close to the behavior policy, with improvements like gradient penalties to ensure convergence. | [223] |
| Advantage-Aware Policy Optimization (A2PO) | Behavior Regularization | Disentangles action distributions based on advantage values, allowing more deviation from low-advantage actions while adhering to high-advantage ones. | [224] |
| Soft Behavior-regularized Actor Critic (SBAC) | Behavior Regularization | Derives a state-dependent regularization weight, allowing more policy deviation at high-confidence states. | [225] |
| Guided Offline RL (GORL) | Behavior Regularization | Uses a small set of expert demonstrations and a guiding network to adaptively determine the constraint intensity per sample. | [215] |
| Implicit Q-Learning (IQL) | In-Sample Learning | Approximates the optimal value function using expectile regression on the dataset's actions, extracting the policy via advantage-weighted regression without querying OOD actions. | [226] |
| Offline RL with No OOD Actions: In-Sample Learning via Implicit Value Regularization | In-Sample Learning | Frames in-sample learning as implicit value regularization, avoiding OOD action queries. | [227] |
| Critic Regularized Regression (CRR) | In-Sample Learning | Uses the critic to weight behavior cloning losses without evaluating OOD actions. | [228] |
| CQL (ReDS) | Handling Dataset Characteristics | Reweights the data distribution to enforce an approximate support constraint, allowing more policy freedom in states with high behavioral variability. | [231] |
| Harnessing Mixed Offline RL Datasets via Trajectory Weighting | Handling Dataset Characteristics | Reweights dataset sampling to emphasize higher-return trajectories, enabling better exploitation of high-performing data. | [230] |
| Beyond Uniform Sampling: Offline RL with Imbalanced Datasets | Handling Dataset Characteristics | Proposes sampling strategies that constrain the policy only to "good data" rather than all actions in imbalanced datasets. | [232] |
| Relaxed Distribution Matching (RelaxDICE) | Offline Imitation Learning | Employs an asymmetrically-relaxed f-divergence for support regularization, imposing little penalty when the learned policy's density is within a bound of the behavior policy's. | [92] |
| Curriculum Offline Imitation Learning (COIL) | Offline Imitation Learning | Uses an experience-picking strategy to imitate progressively better neighboring policies within the dataset via curriculum stages. | [233] |
| Calibrated Q-learning (Cal-QL) | Offline-to-Online RL | Learns a calibrated, conservative Q-function initialization that underestimates the offline policy's value but provides a reasonable scale for stable online fine-tuning. | [234] |
| Adaptive Policy Learning | Offline-to-Online RL | Applies a pessimistic update strategy for offline data and an optimistic one for online data during fine-tuning. | [235] |
| Train Once, Get a Family: State-Adaptive Balances for Offline-to-Online RL (FamO2O) | Offline-to-Online RL | Trains a family of policies with different constraint intensities and uses a balance model to select the appropriate policy per state during fine-tuning. | [216] |
| Model-based Offline Policy Optimization (MOPO) | Model-Based & Other Directions | Uses a learned dynamics model for planning/data augmentation while penalizing rewards by model uncertainty to mitigate distribution shift. | [236] |
| Representation Matters: Offline Pretraining for Sequential Decision Making | Model-Based & Other Directions | Uses unsupervised objectives for representation learning from offline data as pretraining for downstream policy learning. | [237] |
| Action-Quantized Offline RL for Robotic Skill Learning | Model-Based & Other Directions | Uses state-conditioned discretization (e.g., VQ-VAE) for action quantization to make offline RL constraints more precise. | [238] |


## 3 Perception, Prediction, and World Modeling for Policy Learning

This section reviews how learned policies are informed by and integrated with upstream modules. It covers multi-modal sensor fusion, trajectory and intention prediction of other agents, scene understanding, and the critical role of world models and simulation in creating scalable, realistic training environments for policy learning.

### 3.1 Multi-Modal Perception and Sensor Fusion for State Representation

The performance of any autonomous driving policy, whether learned through Reinforcement Learning (RL) or Imitation Learning (IL), is fundamentally bounded by the quality and richness of the state representation it receives. Modern vehicles are equipped with a heterogeneous suite of sensors—predominantly cameras, LiDAR, and RADAR—each providing complementary information. Cameras offer dense semantic and textural data but are susceptible to lighting and weather conditions. LiDAR provides precise 3D geometry and is robust to lighting variations, though it can be affected by adverse weather and yields sparse data. RADAR delivers reliable velocity measurements and performs well in poor visibility but offers low spatial resolution. Consequently, constructing a comprehensive, robust, and actionable state representation necessitates sophisticated multi-modal sensor fusion. This subsection reviews deep learning techniques for integrating these disparate data streams to form a unified perceptual foundation for policy learning, covering fusion architectures, cross-modal representation learning, and the distillation of action-sufficient state representations.

A primary taxonomy in fusion research is based on the stage at which integration occurs: early (data-level), late (decision-level), or intermediate (feature-level). Early fusion, such as projecting LiDAR points onto image pixels to create enriched input channels, is conceptually simple but highly sensitive to calibration errors and sensor failures [239]. Late fusion, which combines the outputs of independent perception networks (e.g., detected bounding boxes), is more robust to individual sensor degradation but cannot exploit complementary low-level features, potentially leading to suboptimal performance [240]. Intermediate or feature-level fusion has emerged as a dominant paradigm, aiming to balance robustness with the capacity for rich cross-modal interaction. For instance, [241] proposes a modular architecture where specialized feature extractors for each modality transform features into a common Bird's-Eye View (BEV) representation before fusion, enabling improved 3D object detection. Similarly, [242] fuse LiDAR and camera features at multiple scales within a pyramid architecture to capture both local details and global context for superior 3D semantic segmentation.

The core challenge of feature-level fusion is aligning and correlating information from inherently different data structures (e.g., unordered 3D point clouds vs. structured 2D image grids). Recent advances heavily leverage attention mechanisms and transformers to learn these correlations dynamically. [243] uses a transformer to estimate calibration parameters by aggregating multi-layer features and identifying cross-modality correlations, addressing misalignment at its root. For perception itself, [244] introduces a Dynamic Cross Attention (DCA) module that learns a "one-to-many" mapping from a 3D point to a neighborhood of image pixels, increasing tolerance to calibration inaccuracies. [245] and [246] employ transformer-based encoders to fuse RGB and LiDAR features, using self-attention to model the contextual interplay between modalities for tasks like waypoint prediction and end-to-end driving. These methods move beyond rigid, calibration-dependent fusion to more flexible, learned association.

A critical consideration for policy learning is robustness to real-world perturbations such as sensor failure, adverse weather, and noisy data. Static fusion schemes can fail catastrophically when one modality becomes unreliable. Therefore, adaptive or selective fusion frameworks are essential. [240] pioneers a context-aware selective sensor fusion framework that dynamically chooses between early, late, or hybrid fusion strategies based on the perceived driving context (e.g., fog, low light), maximizing robustness without compromising efficiency. [247] and [248] propose gating mechanisms that learn to assess the reliability of features from different modalities (e.g., image vs. inertial data) and weight their contribution accordingly. This principle extends to uncertainty-aware fusion; [249] scales modality-specific outputs based on measured uncertainty and fuses them via a probabilistic noisy-or model, demonstrating strong generalization to unseen input degradations like snow and fog. These approaches ensure the state representation remains dependable even under asymmetric sensor distortion.

Beyond fusion architecture, a key research direction is learning compact, informative representations that distill the essential information needed for decision-making—so-called *action-sufficient* state representations. This often involves auxiliary tasks and self-supervised objectives that structure the latent space. [250] boosts LiDAR-only semantic segmentation by using multi-modal data (LiDAR and camera) during training via a knowledge distillation scheme, effectively transferring rich semantic and structural priors from images to a more efficient 3D network. [251] employs a masked autoencoder approach, reconstructing masked LiDAR data from fused LiDAR and camera features, which encourages the model to learn a shared, informative latent representation. [252] learns a cross-modal embedding in a shared latent space during multi-modal training, enabling accurate trajectory predictions at test time using only a single modality (e.g., LiDAR). These techniques create representations that are not only rich but also efficient and generalizable.

Finally, the choice of output representation for the fused perception stack is pivotal for downstream policy learning. While raw sensor streams or task-specific outputs (like detected objects) can be used, intermediate grid-based scene representations are increasingly popular. Occupancy grids or semantic grid maps provide a unified, top-down abstraction that is agnostic to sensor reference frames and naturally incorporates geometric and semantic information [253]. [254] and [255] generate such top-down semantic grids from multi-sensor data for segmentation and prediction. This BEV or grid representation is highly compatible with RL/IL policy networks, as it offers a spatially consistent, history-aware model of the environment that simplifies the learning of driving commands. [256] demonstrates how high-level semantic maps and accurate 3D states can be encoded in a spatial grid to successfully predict driving behavior, highlighting the utility of such structured representations for policy input.

In summary, multi-modal perception for autonomous driving policy learning has evolved from simple concatenation to sophisticated, adaptive, and task-aware fusion architectures. The trend is toward dynamic, attention-based mechanisms that robustly align modalities, coupled with representation learning techniques that distill sensor data into compact, actionable state encodings. The resulting robust and comprehensive state representation forms the critical perceptual bedrock upon which safe, efficient, and generalizable driving policies can be learned through RL and IL paradigms. Future work lies in further closing the loop between perception and action, developing fusion methods that are explicitly optimized for the ultimate control task rather than intermediate perception metrics alone.

**Table: Comparison of approaches in 3.1 Multi-Modal Perception and Sensor Fusion for State Representation**

| Method / Model Name | Core Contribution / Fusion Strategy | Key Technical Features | Reference |
| :--- | :--- | :--- | :--- |
| Early Fusion (e.g., projection-based) | Fuses raw sensor data (e.g., projects LiDAR points onto image pixels). | Simple concatenation of raw or minimally processed data. Highly sensitive to calibration errors. | [239] |
| Late Fusion (e.g., HydraFusion) | Combines outputs of independent perception networks (e.g., detected bounding boxes). | Robust to individual sensor degradation but cannot exploit complementary low-level features. | [240] |
| Intermediate/Feature-Level Fusion (e.g., DeepFusion) | Fuses extracted features from each modality, often into a common representation like BEV. | Balances robustness with capacity for rich cross-modal interaction. Modular architecture with specialized feature extractors. | [241] |
| Deep Sensor Fusion with Pyramid Fusion Networks | Fuses LiDAR and camera features at multiple scales within a pyramid architecture. | Captures both local details and global context for 3D semantic segmentation. | [242] |
| CalibFormer | Uses a transformer to estimate calibration parameters by aggregating multi-layer features. | Addresses sensor misalignment at its root by identifying cross-modality correlations. | [257] |
| Dynamic Cross Attention Networks (DCAN) | Introduces a Dynamic Cross Attention (DCA) module with a "one-to-many" mapping from 3D points to image pixels. | Increases tolerance to calibration inaccuracies. Serves as a plug-in fusion module. | [244] |
| Cognitive TransFuser | Employs transformer-based encoders to fuse RGB and LiDAR features for waypoint prediction. | Uses self-attention to model contextual interplay between modalities. Incorporates auxiliary tasks (e.g., traffic light recognition). | [245] |
| Sensor Fusion by Spatial Encoding | Employs transformer modules at multiple resolutions to fuse camera and LiDAR data. | Effectively combines local and global contextual relationships for end-to-end driving. | [246] |
| HydraFusion (Context-Aware) | A selective sensor fusion framework that dynamically chooses fusion strategy based on driving context. | Dynamically adjusts between early, late, or hybrid fusion to maximize robustness and efficiency. | [258] |
| Selective Sensor Fusion for Neural Visual-Inertial Odometry | Proposes gating mechanisms to assess feature reliability from different modalities (e.g., image vs. inertial). | Learns to weight modality contributions accordingly for odometry estimation. | [247] |
| Learning Selective Sensor Fusion for States Estimation | Proposes an end-to-end selective sensor fusion module (SelectFusion) with gating mechanisms. | Assesses reliability of latent features from different modalities (e.g., image & IMU, depth & LiDAR). | [248] |
| UNO (Uncertainty-aware Noisy-Or Fusion) | Scales modality-specific outputs based on measured uncertainty and fuses them via a probabilistic noisy-or model. | Demonstrates strong generalization to unseen input degradations (e.g., snow, fog). | [249] |
| 2DPASS (2D Priors Assisted Semantic Segmentation) | Uses multi-modal data (LiDAR & camera) during training via a knowledge distillation scheme. | Transfers rich semantic and structural priors from images to a more efficient 3D LiDAR-only network. | [250] |
| MaskedFusion360 | Employs a masked autoencoder approach, reconstructing masked LiDAR data from fused LiDAR and camera features. | Encourages learning a shared, informative latent representation in a self-supervised manner. | [251] |
| Shared Cross-Modal Trajectory Prediction | Learns a cross-modal embedding in a shared latent space during multi-modal training. | Enables accurate trajectory predictions at test time using only a single modality (e.g., LiDAR). | [252] |
| Object Detection and Classification in Occupancy Grid Maps | Uses occupancy/semantic grid maps as a unified, top-down abstraction for sensor fusion. | Agnostic to sensor reference frames, incorporates geometric and semantic information. | [253] |
| FISHING Net | Generates top-down semantic grid representations from multi-sensor data for segmentation and prediction. | Provides a unified representation agnostic to sensor-specific reference frames. | [254] |
| PolarNet | Generates occupancy grid maps from radar data in the polar domain for open space segmentation. | Demonstrates effective deep learning-based processing of radar data. | [255] |
| Rules of the Road | Encodes high-level semantic maps and accurate 3D states in a spatial grid to predict driving behavior. | Demonstrates utility of structured grid representations as input for policy learning. | [256] |


### 3.2 Scene Understanding and Structured World Representations

A fundamental prerequisite for an autonomous vehicle to plan and act safely is a rich, actionable understanding of its static surroundings. This scene understanding transcends raw geometry to incorporate semantic meaning—distinguishing drivable road from sidewalk, identifying lane boundaries, crosswalks, and static infrastructure. Traditional autonomy stacks rely heavily on pre-built High-Definition (HD) maps, which provide centimeter-accurate, lane-level representations of road networks. These maps offer a powerful prior, constraining the vehicle's feasible space and informing high-level route planning. However, their creation and maintenance are labor-intensive and costly, and they cannot account for temporary changes or construction, creating a dependency that limits scalability and robustness. Consequently, a significant research thrust focuses on dynamic, learning-based methods to interpret the static environment from onboard sensor data, providing the geometric and semantic priors essential for policy learning without the brittleness of a fixed map.

A dominant approach involves constructing local semantic maps in real-time. Semantic segmentation of camera images is a foundational technique, labeling each pixel with categories like road, building, or vehicle [259]. These 2D labels are then often projected into 3D. A common and highly effective representation is the semantic occupancy grid, which discretizes the bird's-eye-view (BEV) space into cells, each containing a probability distribution over semantic classes [253]. This representation is naturally suited for sensor fusion and provides a clear spatial structure for downstream modules. End-to-end learning methods have been developed to predict these grids directly from monocular or multi-view images, bypassing intermediate geometric reconstruction steps [260]. For instance, networks can learn to encode front-view visual information and decode it into a top-view Cartesian semantic-metric occupancy grid [261]. These learned mappings can outperform traditional methods based on flat-plane assumptions and offer robustness to perturbations. To handle dynamic environments, frameworks incorporate 3D scene flow into a Bayesian inference model to maintain a consistent, dynamic semantic occupancy map, reducing artifacts caused by moving objects [262].

Beyond flat grids, more structured and persistent representations are emerging. The concept of a Neural Map Prior (NMP) proposes a global, neural representation of map elements that can be continuously updated from online observations [263]. This prior can then be integrated via mechanisms like cross-attention to enhance local map inference, improving performance in challenging conditions and at longer ranges. Similarly, other works explore neural implicit representations as a persistent scene memory. For example, Neural Groundplans are learned, ground-aligned 2D feature grids that can be queried to complete geometry and appearance of occluded regions from a single image, effectively acting as a memory-efficient and editable scene representation [264]. In navigation contexts, agents can learn dynamic neural implicit representations during an episode—one for locating objects and another for modeling explored occupancy—which are then leveraged by a reinforcement learning policy [265]. These methods move towards self-supervised learning of occupancy, using differentiable rendering of 2D labels to train 3D networks, thereby reducing dependency on costly 3D voxel supervision [266].

For policy learning, particularly in reinforcement and imitation learning, these structured representations provide a crucial abstraction. Raw pixels contain vast, redundant information, while a compact semantic map or occupancy grid offers a directly actionable state space. Policies can be trained to reason over these representations more efficiently. For instance, a unified spatial grid that encodes high-level semantic information (lanes, traffic lights, agent states) allows convolutional models to learn complex entity-entity and entity-environment interactions for behavior prediction [256]. In robotic navigation, hierarchical representations like 3D scene graphs, which explicitly capture geometry, topology, and semantics, have been embedded into agent-centric feature spaces using graph neural networks, enabling more effective learning of navigation policies compared to policies using mid-level abstractions like RGB images or 2D segmentation [267]. The process of building these representations can itself be part of a learned policy, as seen in modular architectures for simultaneous mapping and target-driven navigation, where a semantic map aids a navigation policy [268].

The drive for more efficient and generalizable perception also leads to innovations in representation learning itself. Techniques like hierarchical feature-aligned pre-training distill knowledge from large vision-language models to benefit open-vocabulary 3D scene understanding with limited labels [269]. Methods to learn navigation-specific visual representations by contrasting egocentric views with semantic maps (Ego²-Map) can transfer rich spatial and semantic information from a map to an agent's visual encoder, significantly improving performance on navigation tasks [270]. Furthermore, addressing the sim-to-real gap and domain adaptation is critical for these learned representations. Approaches like random image stylization to force texture underfitting can improve a model's focus on structural scene information, enhancing its generalization to new, unseen real-world domains [271].

In summary, the evolution from reliance on static HD maps to online, learned structured world representations marks a pivotal advancement for robust autonomous driving policy learning. Semantic occupancy grids, neural implicit maps, and hierarchical graph representations provide the policy with a distilled, semantically and geometrically meaningful understanding of the static world. This abstraction reduces the complexity of the learning problem, injects valuable priors, and enables more efficient, interpretable, and generalizable decision-making. The integration of these dynamic scene understanding models into the policy learning loop is essential for developing autonomous agents that can operate safely and effectively in the ever-changing real world.

**Table: Comparison of approaches in 3.2 Scene Understanding and Structured World Representations**

| Method / Model | Key Idea / Contribution | Reference | Year | Dataset(s) | Backbone / Architecture |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Semantic Occupancy Grid Mapping | End-to-end learning of monocular semantic-metric occupancy grids using a variational encoder-decoder network. Projects front-view to BEV. | [261] | 2019 | Cityscapes, KITTI | Convolutional Variational Encoder-Decoder Network |
| Dynamic Semantic Occupancy Mapping | Incorporates 3D scene flow into a closed-form Bayesian inference model to maintain a consistent, dynamic semantic occupancy map, reducing artifacts from moving objects. | [262] | 2020 | KITTI, nuScenes | Bayesian model with deep learning-based semantic segmentation and flow estimation |
| Pyramid Occupancy Networks | End-to-end deep learning to predict semantic Bayesian occupancy grid maps directly from monocular images. | [260] | 2020 | NuScenes, Argoverse | Pyramid Occupancy Network |
| Neural Map Prior (NMP) | A global, neural representation of map elements that can be continuously updated and integrated via cross-attention to enhance local map inference. | [263] | 2023 | nuScenes | Neural network with cross-attention and fusion module |
| Neural Groundplans | Learns persistent, ground-aligned 2D feature grids (neural groundplans) from a single image via differentiable rendering, enabling scene completion and editing. | [264] | 2022 | Synthetic multi-view data | Neural implicit representation with differentiable rendering |
| Dynamic Neural Implicit Representations for Navigation | Learns two neural implicit representations online per episode (for object location and explored occupancy) to be leveraged by a reinforcement learning policy. | [265] | 2022 | Habitat, Gibson | Reinforcement Learning with implicit representation networks |
| OccFlowNet | Self-supervised occupancy estimation via differentiable rendering of 2D labels and occupancy flow for temporal consistency, reducing need for 3D voxel supervision. | [266] | 2023 | nuScenes, KITTI | 3D network with differentiable volumetric rendering |
| Hierarchical Feature-Aligned Pre-training | Distills knowledge from large vision-language models via hierarchical feature-aligned pre-training for open-vocabulary 3D scene understanding with limited labels. | [269] | 2023 | ScanNet, S3DIS, SemanticKITTI | Transformer-based with vision-language model distillation |
| Ego²-Map Representation Learning | Learns navigational visual representations by contrasting egocentric views with semantic maps, transferring spatial and semantic info to the visual encoder. | [270] | 2023 | Habitat-Matterport3D (HM3D) | Visual Transformer |
| Texture Underfitting for Domain Adaptation | Uses random image stylization to force texture underfitting, improving model focus on structural scene information for better domain adaptation. | [271] | 2021 | GTA5 -> Cityscapes, SYNTHIA -> Cityscapes | Convolutional Neural Network |
| Hierarchical 3D Scene Graph Policy | Embeds 3D scene graphs (geometry, topology, semantics) into an agent-centric feature space using GNNs for learning navigation policies. | [267] | 2022 | Matterport3D | Graph Neural Network (GNN) |
| Unified Spatial Grid for Behavior Prediction | Uses a unified spatial grid encoding high-level semantics (lanes, lights, agents) to learn entity-entity and entity-environment interactions via convolutional models. | [256] | 2019 | Private autonomous driving dataset | Convolutional Neural Network |
| Modular Mapping and Navigation | A modular architecture for simultaneous semantic mapping and target-driven navigation, where the map aids the navigation policy. | [268] | 2019 | Active Vision Dataset, Matterport3D | Modular CNN-based architecture |
| Object Detection in Occupancy Grids | Detects and classifies objects in multi-layer occupancy grid maps using deep convolutional networks. | [253] | 2018 | KITTI | Deep Convolutional Neural Network |
| Semantic Segmentation Foundation | Investigates semantic segmentation for holistic scene understanding, including hierarchical classifiers and weakly-supervised training. | [259] | 2020 | Cityscapes, Mapillary Vistas, etc. | Convolutional Neural Network |


### 3.3 Trajectory and Intention Prediction of Other Agents

Accurately forecasting the future motion and inferring the latent goals of surrounding dynamic agents—such as vehicles, pedestrians, and cyclists—is a cornerstone of safe and interactive autonomous driving. This capability, often termed trajectory and intention prediction, transforms raw sensor data into a predictive world model that is critical for downstream policy learning and planning. The core challenge lies in the inherent multi-modality of the future, governed by complex social interactions, scene constraints, and the uncertain intentions of each agent. Modern approaches have thus evolved from simple deterministic path extrapolation to sophisticated probabilistic frameworks that generate multiple, socially compliant, and scene-consistent future hypotheses.

A dominant paradigm in contemporary research is the use of generative deep learning models to capture the multi-modal distribution over future trajectories. Frameworks based on Conditional Variational Autoencoders (CVAEs) [272], Generative Adversarial Networks (GANs) [273], and diffusion models are widely employed. These models often condition their predictions on three key informational pillars: the agent's motion history, the social context of interacting neighbors, and the static scene structure (e.g., lane geometry, crosswalks). For instance, [274] explicitly models agent dynamics and heterogeneous map data within a graph-structured recurrent model, enabling physically feasible predictions. Similarly, [275] introduces a probabilistic framework using latent variables to jointly model the multi-step future motions of all agents in a scene, efficiently scaling to varying numbers of agents.

Modeling social interactions is paramount, as an agent's future path is heavily influenced by the anticipated actions of others. Graph-based representations have become the de facto standard for this purpose, where agents are nodes and edges represent interactions. Models like [276] and [277] incorporate dynamic graph representations with relational inductive biases and attention mechanisms to explicitly reason about inter-agent dependencies. These methods move beyond simple distance-based heuristics. For example, [278] proposes selecting interacting agents based on calculated collision risk using time-to-collision and approach angles, leading to more relevant interaction modeling. Furthermore, some works explicitly decouple complex joint prediction problems; [279] classifies agent pairs into influencers and reactors, predicting trajectories for each group separately before combining them based on joint likelihood, thereby managing the exponential prediction space.

Integrating rich scene context—typically from High-Definition (HD) maps—is equally critical to ensure predictions are not only socially acceptable but also physically admissible (e.g., staying on drivable areas, obeying traffic rules). Early methods treated scene encoding as an independent branch, but recent trends favor tighter coupling. [280] emphasizes capturing semantic information (e.g., traffic lights, crosswalks) alongside spatial data for more consistent predictions. [281] introduces a progressive interaction network where an agent's feature representation iteratively focuses on relevant map elements at different stages of encoding, more effectively capturing map constraints. Transformers have also shown great promise in this domain due to their powerful context aggregation capabilities. [282] employs a transformer architecture alongside a Dynamic Graph CNN to process road topology, facilitating integrated prediction and planning.

Beyond low-level trajectory coordinates, predicting high-level behavioral intentions—such as a pedestrian's decision to cross a street or a vehicle's intent to change lanes—provides a crucial semantic layer that can disambiguate multi-modal futures and enhance planning. Intention prediction often acts as an intermediate representation that guides or conditions trajectory generation. The [283] framework is built on this insight, first predicting a set of potential target states as a proxy for intent, then generating trajectories conditioned on those targets. Datasets like [284] and [285] are specifically curated to advance research in joint trajectory and intention prediction. Models such as [286] and [287] employ multi-task learning architectures to simultaneously predict trajectories and crossing actions, leveraging shared representations from diverse data modalities like human pose and scene context.

The ultimate value of these predictive models is realized through their integration into the policy learning loop for autonomous driving. Accurate predictions directly inform risk assessment and enable proactive, rather than reactive, planning. For interactive planning, it is essential that the prediction module can reason about the ego vehicle's potential influence on others—a concept known as "interaction-aware" or "response" prediction. [288] proposes a Transformer-based model that conditions predictions on the ego agent's future plan, allowing the planner to simulate reactions to its candidate actions. Similarly, [289] supports counterfactual reasoning by injecting hypothetical geometric goals and social contexts, enabling the planner to evaluate unlikely but critical futures. This tight integration is exemplified in differentiable prediction-and-planning pipelines like [282] and policy-based methods like [290], which explicitly enforce scene consistency and learn an interaction policy usable for conditional prediction. Furthermore, prediction models provide a dense, interpretable signal for reward shaping or constraint formulation in Reinforcement Learning (RL). For instance, predicted time-to-collision or probability of occupancy can be directly embedded into a safety cost, guiding the RL agent towards safer policies [291].

Despite significant progress, key challenges remain for deploying these models in safety-critical systems. The trustworthiness of multi-modal predictions requires holistic evaluation beyond simple displacement metrics, considering diversity, physical admissibility, and scene consistency [292]. Robustness to distribution shifts, perception noise, and the long-tail of rare but critical interactive scenarios (e.g., near-crashes) is paramount [293]. Finally, achieving real-time performance while maintaining high accuracy and modeling complexity is an ongoing engineering challenge, necessitating efficient architectures like [294]. As prediction models become more accurate and integrated, they will increasingly serve as the foundational "world model" that enables advanced RL and IL policies to navigate complex, multi-agent environments with human-like foresight and safety.

**Table: Comparison of approaches in 3.3 Trajectory and Intention Prediction of Other Agents**

| Model/Method Name | Key Idea/Contribution | Reference |
| :--- | :--- | :--- |
| Social-DualCVAE | Uses a dual conditional variational autoencoder and unsupervised classification of social interaction patterns for multi-modal trajectory forecasting. | [272] |
| SoPhie | An attentive GAN that uses social and physical attention mechanisms to generate socially and physically plausible paths. | [273] |
| Trajectron++ | A modular, graph-structured recurrent model that forecasts trajectories for diverse agents while incorporating agent dynamics and heterogeneous map data. | [274] |
| Multiple Futures Prediction | A probabilistic framework using latent variables to jointly model the multi-step future motions of all agents in a scene, scaling to varying agent numbers. | [275] |
| Social-WaGDAT | Uses a Wasserstein graph double-attention network with a dynamic graph representation and relational inductive biases for interaction-aware prediction. | [276] |
| Spatio-Temporal Graph Dual-Attention Network (STG-DAT) | A generic generative neural system for multi-agent prediction using a dynamic graph representation and dual-attention mechanisms. | [277] |
| Polar Collision Grids | Selects interacting agents based on collision risk (time-to-collision, approach angles) using a polar grid map for more relevant interaction modeling. | [278] |
| M2I | Classifies agent pairs into influencers and reactors, predicting trajectories separately before combining them based on joint likelihood to manage exponential prediction space. | [279] |
| SIMMF | Uses semantic-aware selection of relevant agents and an attention mechanism to capture semantics alongside spatial information for scene-consistent predictions. | [280] |
| ProIn | A progressive interaction network where an agent's feature iteratively focuses on relevant map elements at different encoding stages to better capture map constraints. | [281] |
| GET-DIPP | A Graph-Embedded Transformer with a Dynamic Graph CNN for road topology, facilitating differentiable integrated prediction and planning. | [282] |
| TNT | A target-driven framework that first predicts potential target states as a proxy for intent, then generates trajectories conditioned on those targets. | [283] |
| VRUNet | A multi-task learning model for simultaneously predicting pedestrian actions, crossing intent, and future trajectories using 2D human pose and scene context. | [286] |
| PedFormer | Uses a cross-modal Transformer and gated multi-task learning to predict pedestrian trajectories and crossing actions from an ego-centric perspective. | [287] |
| Learning Interaction-aware Motion Prediction Model for Decision-making in Autonomous Driving | A Transformer-based model that conditions predictions on the ego agent's future plan, allowing simulation of reactions to candidate actions. | [288] |
| What-If Motion Prediction for Autonomous Driving | A recurrent graph-based attentional approach that supports counterfactual reasoning by injecting hypothetical geometric goals and social contexts. | [289] |
| ScePT | A policy planning-based model that generates scene-consistent trajectory predictions by learning an agent interaction policy for conditional prediction. | [290] |
| Prediction-aware and Reinforcement Learning based Altruistic Cooperative Driving | Integrates a Hybrid Predictive Network for future observation anticipation into a reinforcement learning framework for socially beneficial decision-making. | [291] |
| Towards trustworthy multi-modal motion prediction  Holistic evaluation and interpretability of outputs | Proposes a holistic evaluation framework beyond displacement metrics, considering diversity, admissibility, and scene consistency for trustworthy prediction. | [292] |
| Behavioral Intention Prediction in Driving Scenes  A Survey | A survey identifying challenges like limited intention types in datasets and research gaps in near-crash scenarios for behavioral intention prediction. | [293] |
| ProphNet | An efficient agent-centric model with anchor-informed proposals for multimodal motion prediction, designed for low-latency, real-world deployment. | [294] |


### 3.4 World Models and Differentiable Simulation for Training

A core paradigm for achieving sample-efficient and scalable policy learning in autonomous driving is the use of learned world models and differentiable simulation. These models, often trained via self-supervision on vast amounts of driving data, function as internal simulators that predict future environment states conditioned on the ego-agent's potential actions. This capability unlocks several powerful training methodologies, moving beyond reactive policies to systems capable of foresight and strategic planning. The fundamental advantage lies in shifting a significant portion of learning from costly, real-world interactions to computationally cheaper "imagined" rollouts within the model's latent or explicit state space, a concept powerfully demonstrated in foundational works like [295] and [296].

The architecture and objective of the world model are critical. Early approaches often learned a single, monolithic forward model to predict future raw sensory inputs (e.g., pixels) or intermediate representations. However, the driving domain presents a unique challenge: the dynamics of the scene are composed of two fundamentally different components—the deterministic, well-understood kinematics of the ego-vehicle and the highly stochastic, multimodal behavior of other agents and the environment. As argued in [297], explicitly decoupling these dynamics is beneficial. This separation allows the ego's motion to be modeled with a simple, differentiable kinematic model, while a more complex stochastic model (e.g., a convolutional network on rasterized scenes) learns to predict the evolution of the surrounding world. This division leads to more accurate long-horizon predictions, lower crash rates, and improved planning stability. This principle of isolating controllable from non-controllable dynamics is further refined in works like [298] and its successor [299], which use inverse dynamics and other objectives to disentangle mixed spatiotemporal sources, enabling the agent to anticipate the independent movement of other vehicles for safer long-horizon decision-making.

Beyond architectural choices, the representation space for the world model is a key area of innovation. Predicting high-dimensional observations like images or LiDAR point clouds is computationally expensive and can focus model capacity on irrelevant details. Therefore, a strong trend is to learn in compact, structured latent spaces. [300] proposes learning a world model in 3D occupancy space, which offers a fine-grained, geometric, and sensor-agnostic scene representation. It uses a scene tokenizer to discretize occupancy into tokens, which are then modeled with a spatial-temporal generative transformer to predict future ego trajectories and scene evolution. Similarly, [301] tokenizes sensor observations and uses a discrete diffusion model for future prediction, achieving state-of-the-art results on point cloud forecasting. These discrete, abstract representations are more amenable to the powerful sequence modeling architectures that have revolutionized other fields. The search for optimal world model backbones is systematic, with studies like [302] comparing recurrent networks, transformers, and structured state space sequence (S4) models, finding that S4-based models offer superior long-term memory and parallelizable training.

The primary application of these world models is for planning and policy optimization through "latent imagination" or "dreaming." Once a world model is trained, a policy can be learned entirely by performing rollouts within the model's predicted latent states, computing rewards and values, and propagating gradients back through the imagined trajectories to update the policy, as in the Dreamer family of agents [296] [303]. This paradigm is directly applicable to driving. For instance, [304] jointly learns a world model and a policy from offline video data, enabling the agent to execute plans entirely within its imagination and achieve strong sim-to-real transfer. Planning can be integrated at various levels. [305] and [306] employ hierarchical world models that plan over high-level goals, enabling efficient long-horizon reasoning. For interactive scenarios, [307] constructs ego trajectory trees and scenario trees for multi-modal predictions, transforming continuous policy optimization into a tractable Markov Decision Process. Furthermore, [308] bridges model predictive control (MPC) with learned prediction models by jointly optimizing the trajectories of the ego and other agents, using the learned model as a prior.

Differentiable simulation extends this concept by ensuring the entire pipeline—from action to predicted future state to cost/reward—is differentiable, allowing for gradient-based planning and policy refinement. Models that explicitly separate ego and world dynamics, like [297], naturally provide this differentiability for the ego component. [309] introduces graph networks as differentiable forward models that support gradient-based trajectory optimization. More recently, [310] proposes PolyGRAD, which uses a diffusion model to generate entire on-policy trajectories in a single pass, guided by the policy's action distribution, offering an alternative to autoregressive rollouts.

These techniques also address critical challenges in continual and safe learning. [311] and [312] show that world models can generate "pseudo-experiences" of past tasks to mitigate catastrophic forgetting, enabling lifelong learning. For safety, a reliable world model allows for *predictive* safety checking. An agent can "imagine" the consequences of actions before executing them, identifying and avoiding trajectories that lead to predicted collisions or unsafe states. This is a step towards formal safety guarantees, as explored in concepts like learning from [313]. The quest for more accurate and causally grounded models is ongoing, with approaches like [314] aiming to model latent confounding factors to answer counterfactual questions and improve sample efficiency.

In summary, world models and differentiable simulation represent a transformative approach for autonomous driving policy learning. By learning to simulate, they enable data-efficient training through imagination, support sophisticated planning and hierarchical decision-making, facilitate continual adaptation, and provide a substrate for predictive safety assurance. The evolution towards structured, disentangled, and efficiently roll-out-able models—from occupancy spaces and diffusion models to decoupled dynamics and graph networks—is paving the way for more robust, foresighted, and scalable autonomous driving systems.

**Table: Comparison of approaches in 3.4 World Models and Differentiable Simulation for Training**

| Method / Model Name | Key Idea / Contribution | Reference (Full Paper Title) |
| :--- | :--- | :--- |
| World Models / Dreamer | Use learned world models for latent imagination; train policies via analytic gradients through imagined rollouts. | [296] |
| Separating World and Ego Models | Decouples ego-vehicle kinematics (simple, deterministic) from stochastic world dynamics for more accurate predictions. | [297] |
| Iso-Dream | Isolates controllable and noncontrollable dynamics via inverse dynamics; optimizes policy on decoupled latent imaginations. | [298] |
| OccWorld | Learns a world model in 3D occupancy space using a scene tokenizer and spatial-temporal generative transformer. | [300] |
| Copilot4D | Tokenizes sensor observations and uses a discrete diffusion model for future prediction of point clouds. | [301] |
| S4-based World Models (S4WM) | Uses Structured State Space Sequence (S4) models as world model backbone for superior long-term memory and parallelizable training. | [302] |
| Model-Based Imitation Learning (MILE) | Jointly learns a world model and policy from offline video; executes plans in imagination for sim-to-real transfer. | [304] |
| Hierarchical World Models (Forecaster, Hieros) | Plan over high-level goals using temporally abstract world models for efficient long-horizon reasoning. | [305], [306] |
| Tree-structured Policy Planning (TPP) | Constructs ego trajectory trees and scenario trees for multi-modal predictions, transforming policy optimization into a tractable MDP. | [307] |
| Interactive Joint Planning (IJP) | Bridges MPC with learned prediction models by jointly optimizing trajectories of ego and other agents. | [308] |
| Graph Networks as Learnable Physics Engines | Uses graph networks as differentiable forward models for inference, control, and gradient-based trajectory optimization. | [309] |
| PolyGRAD (Policy-Guided Trajectory Diffusion) | Generates entire on-policy trajectories in a single pass via diffusion, guided by policy's action distribution. | [310] |
| Continual Learning with World Models | Uses world models to generate pseudo-experiences of past tasks to mitigate catastrophic forgetting. | [311], [312] |
| Causal World Models (CWM) | Models latent confounding factors to answer counterfactual questions and improve sample efficiency. | [314] |


### 3.5 Bridging Perception, Prediction, and Planning

A critical evolution in autonomous driving policy learning is the move from modular, sequential pipelines towards architectures that tightly couple or end-to-end integrate the core competencies of perception, prediction, and planning. This integration addresses the fundamental inconsistency that arises when independently optimized modules operate on mismatched assumptions or representations, leading to suboptimal or unsafe plans. The core architectural paradigms in this space leverage joint modeling, prediction-guided optimization, and hierarchical reasoning to create more consistent, context-aware, and efficient decision-making systems.

A foundational approach involves designing end-to-end learnable networks that produce interpretable intermediate representations which are explicitly consumed by the planner. For instance, a framework can employ a novel differentiable semantic occupancy representation that is jointly learned from perception and prediction estimates and then directly used as a cost function by the motion planning process [315]. This ensures that the planning costs are inherently consistent with the agent's own understanding of the environment, leading to safer trajectories that better imitate human driving behavior. Similarly, other works propose a conditional Generative Adversarial Network (GAN) architecture that predicts high-resolution image sequences representing both explicit motion forecasts and pixel state values encoding kinematic reachability and safety, which are then used for planning [316]. This joint training on planner-rendered targets allows the model to learn an implicit understanding of what constitutes a good plan.

The concept of occupancy has emerged as a particularly powerful representation for bridging these modules. Unlike bounding boxes, occupancy grids provide a holistic, volumetric understanding of scene geometry and semantics, which is naturally suited for forecasting and constraint-based planning. Several frameworks explicitly use occupancy prediction to guide the planner. A two-stage neural planner first outputs a joint occupancy forecast for all traffic actors, considering interactions and scene context within a unified Transformer. This predicted occupancy then guides a subsequent optimization stage to inform safe and smooth trajectory planning [317]. Expanding on this, hybrid-prediction integrated planning systems introduce marginal-conditioned occupancy prediction to align joint occupancy forecasts with agent-wise motion predictions, and concurrently integrate these hybrid predictions (both occupancy and trajectory-based) with the ego planner, optimized via prediction guidance [318]. This multi-faceted prediction provides a richer set of constraints and expectations for the planning module.

Tight coupling is also achieved through joint architectural designs that share contextual reasoning. Transformer-based models are particularly effective for this, as they can naturally model interactions among all entities in a scene. One such model leverages a transformer to share global contextual reasoning among all traffic participants, thereby capturing complex interactions and directly interconnecting the planning and prediction computations within a single joint architecture [319]. This joint modeling allows the planner to be inherently aware of the predictive distribution of other agents' actions and vice versa. Further integration is demonstrated in frameworks that propose a differentiable joint training pipeline for ego-conditioned motion prediction and a learnable context-aware cost function within a tree-structured policy planner [320]. The differentiability ensures that prediction errors directly inform and improve the cost function used for planning, leading to superior overall performance compared to training the modules separately.

Hierarchical abstraction is another key principle for bridging long-horizon prediction with planning. Inspired by human cognition, hierarchical frameworks perform prediction and planning at multiple temporal and abstraction scales. For visual planning, goal-conditioned hierarchical predictors are formulated to predict latent trajectories towards a goal, and by recursively subdividing the trajectory, they generate sequences in a coarse-to-fine manner, enabling the solution of long-horizon tasks [321]. In reinforcement learning, hierarchical models learn temporally abstract world models and plan over high-level goals using tree-search, while a low-level policy executes them [305]. This decomposition allows the high-level planner to reason about distant outcomes using compact predictions, making the search space tractable. Similarly, modular hierarchical policies for navigation operate over semantic subgoals (e.g., 'exit room', 'find kitchen'), where a master policy plans the subgoal sequence and specialized sub-policies execute them, enabling efficient adaptation and long-horizon task completion [322].

Finally, the integration is also being driven by advanced world models that learn structured, object-centric representations of the environment. Models that enforce entity-abstraction—processing each object representation with the same locally-scoped function—can generalize to novel numbers and configurations of objects, providing a robust substrate for prediction and planning [323]. When such a model jointly learns perception, a physics interaction function, and rendering, it acquires an actionable representation of intuitive physics that can be used for downstream tasks like planning complex block towers [324]. Furthermore, active predictive coding frameworks unify the learning of hierarchical world models for both perceptual grouping (part-whole hierarchies) and the composition of complex action sequences for planning, offering a unified neural solution to perception and action [325].

In summary, the frontier of autonomous driving policy learning is defined by deeply integrated architectures that dissolve the traditional barriers between perception, prediction, and planning. Through the use of consistent intermediate representations like semantic occupancy, joint differentiable training, transformer-based interaction modeling, and hierarchical abstraction, these approaches ensure that the planner's decisions are grounded in a coherent, predictive, and comprehensive model of the evolving environment. This leads to policies that are not only more accurate and efficient but also fundamentally safer and more explainable, as their reasoning is based on explicit, interpretable forecasts and structural scene understanding.

**Table: Comparison of approaches in 3.5 Bridging Perception, Prediction, and Planning**

| Method / Model Name | Key Idea / Contribution | Reference (Full Paper Title) |
| :--- | :--- | :--- |
| End-to-end network with differentiable semantic occupancy | Produces interpretable semantic occupancy representation used as a cost for motion planning, ensuring consistency between perception/prediction and planning. | [315] |
| Conditional GAN for pixel state values | Uses a conditional GAN to predict high-resolution image sequences with explicit motion forecasts and pixel state values encoding reachability/safety for planning. | [316] |
| Occupancy Prediction-Guided Neural Planner (OPGP) | Two-stage neural planner: first outputs joint occupancy forecasts via a Transformer, then uses this prediction to guide a subsequent optimization stage for trajectory planning. | [317] |
| Hybrid-Prediction Integrated Planning (HPP) | Integrates hybrid predictions (marginal-conditioned occupancy and game-theoretic motion) with the ego planner, optimized via prediction guidance for consistency and social coherence. | [318] |
| InteractionNet with Transformers | Uses a Transformer to share global contextual reasoning among all traffic participants, jointly modeling planning and prediction within a single architecture. | [319] |
| Differentiable Joint Training for Tree Policy Planning (DTPP) | Proposes a differentiable joint training pipeline for ego-conditioned motion prediction and a learnable context-aware cost function within a tree-structured policy planner. | [320] |
| Goal-Conditioned Hierarchical Predictors | Formulates goal-conditioned hierarchical predictors to predict latent trajectories in a coarse-to-fine, recursive manner for long-horizon visual planning. | [321] |
| Forecaster: Hierarchical RL with abstract world models | Learns a temporally abstract world model and plans over high-level goals using tree-search, with a low-level policy for execution. | [305] |
| Neural Modular Control with hierarchical policies | Employs a hierarchical policy where a master policy plans sequences of semantic subgoals and specialized sub-policies execute them. | [322] |
| Entity Abstraction (OP3) | Enforces entity-abstraction to process object representations with locally-scoped functions, enabling generalization to novel numbers/configurations of objects for prediction and planning. | [323] |
| Object-Oriented Prediction and Planning (O2P2) | Jointly learns perception, a pairwise physics interaction function, and rendering to acquire actionable object-centric representations for intuitive physics and planning. | [324] |
| Active Predictive Coding | A unified neural framework that learns hierarchical world models for both perceptual grouping (part-whole hierarchies) and the composition of complex action sequences for planning. | [325] |


## 4 Architectural Frameworks and Policy Design

This section analyzes the architectural design of driving policies, comparing modular versus end-to-end approaches. It explores hierarchical RL, multi-agent RL for traffic coordination, and the novel integration of foundation models (LLMs/VLMs) for interpretable reasoning and instruction following in complex driving scenarios.

### 4.1 Modular vs. End-to-End Architectural Paradigms

The design of the driving policy's underlying architecture is a fundamental choice that dictates the system's capabilities, limitations, and path to deployment. Two dominant paradigms have emerged: the traditional modular pipeline and the increasingly popular end-to-end (E2E) learning approach. Each embodies a different philosophy for decomposing the complex autonomous driving task, leading to significant trade-offs in interpretability, safety, generalization, and development complexity.

The modular pipeline, often described as a "sense-plan-act" or perception-prediction-planning-control stack, decomposes the driving task into a sequence of semantically distinct, often independently developed modules. Perception modules (e.g., object detectors, semantic segmentation networks) process raw sensor data (cameras, LiDAR, radar) into structured representations like bounding boxes, drivable area segments, or occupancy grids [326]. These outputs feed into prediction modules that forecast the future states of dynamic agents. A planning module, which may incorporate rule-based logic, optimization, or learning, then uses this interpreted world model to generate a safe, comfortable, and goal-oriented trajectory. Finally, a control module translates this trajectory into low-level steering, throttle, and brake commands. This architecture's primary strength lies in its **interpretability and debuggability**. Since each module produces intermediate outputs that correspond to human-understandable concepts (e.g., "there is a car 30 meters ahead"), engineers can isolate and rectify failures. For instance, a collision can be traced to a missed detection, an erroneous prediction, or an unsafe planning decision. This modularity also facilitates **safety assurance** through established techniques; formal methods and runtime monitoring can be applied to verifiable components like the planner and controller [327]. Furthermore, modules can be updated, tested, and certified independently, aligning well with current automotive safety standards. However, this decoupling introduces critical weaknesses. **Error propagation** is a major concern, as inaccuracies in upstream perception or prediction are compounded by downstream planning, potentially leading to catastrophic failures. The pipeline also creates **information bottlenecks**; the planning module must make decisions based on a lossy, abstracted representation of the rich sensory world, which may discard information crucial for robust driving. The development and integration of these specialized modules are complex, costly, and can lead to sub-optimal system performance due to a lack of **joint optimization** across the entire stack.

In stark contrast, the end-to-end paradigm seeks to replace the entire modular pipeline with a single, typically deep, neural network that maps raw sensor inputs directly to control commands or low-level motion primitives [328]. This approach, exemplified by projects like Comma.ai's Openpilot [329], offers compelling advantages. By avoiding handcrafted intermediate representations, it enables **joint feature optimization**; the network can learn latent features that are optimally useful for the final driving task, potentially discovering more efficient and robust representations than those engineered by humans. This often results in **simpler system design** and **faster inference**, as the computational graph is unified. E2E models are typically trained via imitation learning (IL) on large datasets of human driving, or via reinforcement learning (RL) in simulation, allowing them to learn complex behaviors directly from data. Proponents argue this data-driven approach is more **scalable** to the long tail of rare driving scenarios. However, the end-to-end paradigm faces severe challenges, primarily centered on **interpretability and safety verification**. The policy is a "black box"; understanding *why* it made a specific steering decision is extremely difficult, complicating debugging and eroding trust [330]. This opacity directly hinders **safety assurance**, as it is nearly impossible to formally guarantee the behavior of a large, nonlinear neural network across the infinite space of possible inputs. Furthermore, E2E models are susceptible to **causal confusion**, where they learn spurious correlations (e.g., correlating the steering angle with a curb's texture rather than the road's curvature) and can exhibit poor **generalization** to distribution shifts in weather, lighting, or geography not seen during training [331]. The **sample complexity** for training robust E2E policies from scratch can be prohibitively high, often requiring massive, diverse datasets.

The core trade-offs between these paradigms manifest in several dimensions. In terms of **error handling**, modular systems localize errors but suffer from propagation, while E2E systems have diffuse error sources but can, in principle, learn to be robust to certain perceptual noises through joint training. For **generalization**, modular systems can generalize better to new sensor setups or environments if individual modules are robust, whereas E2E systems risk catastrophic failure under domain shift but may better handle compositional novelty within the training distribution. **Data efficiency** favors modular design when high-quality labeled data for intermediate tasks (like 3D detection) is available, as the learning problem is decomposed. In contrast, E2E requires vast amounts of paired sensor-action data, which is cheaper to collect but may lack semantic labels. Finally, **verification complexity** is arguably the most significant differentiator. Modular pipelines enable compositional verification, while verifying an E2E model remains a fundamental, unsolved research problem.

Recognizing that neither pure paradigm is ideal, the field is converging on **hybrid architectures** that attempt to blend the strengths of both. These include models that learn intermediate representations which are both useful for driving and interpretable, such as semantic occupancy grids or future trajectory distributions [332]. Another promising direction is the **"teacher-student" or "privileged learning"** framework, where a "teacher" policy learns with access to privileged information (e.g., ground-truth object states) to produce optimal actions or plans, and a "student" perception network is trained to predict the necessary inputs for the teacher's planner from raw sensors [333]. Furthermore, novel architectures like **DiffStack** propose making traditional modular stacks (prediction, planning, control) differentiable, enabling end-to-end gradient flow to optimize upstream components like the predictor based on downstream planning performance, while retaining modular interpretability [334]. Other works enhance E2E models with **explicit reasoning components**, such as chain-of-thought modules that output interpretable reasoning steps before the final action [335], or penalty-based mechanisms to enforce traffic rule compliance [336]. The evolution of policy architecture is thus not a binary choice but a spectrum, where the optimal point for a given application depends on the required safety certification level, available data, and operational design domain.

**Table: Comparison of approaches in 4.1 Modular vs. End-to-End Architectural Paradigms**

| Paradigm | Key Characteristics | Advantages | Disadvantages | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Modular Pipeline | Decomposes driving into sequential, semantically distinct modules (perception, prediction, planning, control). Produces structured, human-interpretable intermediate representations. | High interpretability and debuggability; facilitates safety assurance and formal verification; aligns with automotive safety standards; modules can be updated independently. | Suffers from error propagation; creates information bottlenecks; complex integration; lacks joint optimization, potentially leading to sub-optimal performance. | [326], [327] |
| End-to-End (E2E) Learning | Uses a single neural network to map raw sensor inputs directly to control commands or motion primitives. Trained via imitation or reinforcement learning on large datasets. | Enables joint feature optimization; simpler system design; faster inference; potentially more scalable to rare scenarios. | Low interpretability ("black box"); difficult safety verification; susceptible to causal confusion and poor generalization; high sample complexity. | [328], [329], [330], [331] |
| Hybrid Architectures (e.g., Interpretable Intermediate Representations) | Blends modular and E2E approaches. Learns interpretable intermediate representations (e.g., semantic occupancy, future trajectories) useful for driving. | Aims to retain interpretability and safety while benefiting from data-driven, joint optimization. | Design complexity; challenge in defining optimal intermediate abstraction. | [332] |
| Hybrid Architectures (e.g., Teacher-Student / Privileged Learning) | A "teacher" policy learns with privileged information (ground truth); a "student" perception network is trained to predict the teacher's required inputs from raw sensors. | Decouples perception noise from planning learning; can achieve better performance with less data. | Risk of distribution gap between predicted and ground-truth inputs for the teacher. | [333] |
| Hybrid Architectures (e.g., Differentiable Modular Stack) | Makes traditional modular stacks (prediction, planning, control) differentiable, enabling end-to-end gradient flow to optimize upstream components. | Retains modular interpretability while allowing joint optimization via backpropagation. | Implementation complexity; requires differentiable approximations of planning/control. | [334] |
| Hybrid Architectures (e.g., Explicit Reasoning Augmentation) | Enhances E2E models with components for explicit reasoning (e.g., chain-of-thought) or rule-compliance mechanisms. | Improves interpretability and controllability of E2E decisions; can enforce safety rules. | Adds complexity; may not fully resolve underlying generalization or verification issues. | [335], [336] |


### 4.2 Hierarchical and Structured Policy Learning

The inherent complexity of autonomous driving, characterized by long decision horizons, sparse high-level rewards, and a dynamically changing multi-agent environment, poses a significant challenge for monolithic, end-to-end reinforcement learning (RL) policies. Hierarchical and structured policy learning addresses this by decomposing the driving task into multiple levels of temporal abstraction, mirroring the natural stratification of human driving into strategic, tactical, and operational layers. This decomposition enhances sample efficiency, enables the reuse of learned skills, and can improve the interpretability and robustness of the autonomous system.

A core paradigm within this domain is Hierarchical Reinforcement Learning (HRL), which typically employs a two-level architecture: a high-level policy that selects subgoals or temporally extended actions (options) at a lower frequency, and a low-level policy that executes primitive actions to achieve these subgoals. In autonomous driving, this translates to a high-level policy making tactical decisions like "change to the left lane" or "overtake the slow vehicle," while a low-level policy handles the continuous steering and acceleration controls. The **action and trajectory planner using Hierarchical Reinforcement Learning (atHRL)** method exemplifies this, where a high-level policy outputs target waypoints (subgoals) based on lidar and bird's-eye view inputs, and a low-level controller generates the corresponding throttle and steering commands [337]. This separation of concerns allows the high-level policy to reason over longer horizons without being burdened by low-level control details.

A critical challenge in HRL is the non-stationarity introduced when the low-level policy is learned simultaneously with the high-level policy; as the low-level policy improves, the transition dynamics for the high-level policy change, destabilizing training. Several approaches mitigate this issue. The **State-Conditioned Adversarial Subgoal Generation** framework enforces compatibility between high-level subgoals and the current low-level policy by training a discriminator to distinguish between achievable and non-achievable subgoals, thereby stabilizing joint learning [338]. Similarly, **Hierarchical reinforcement learning with Timed Subgoals (HiTS)** addresses environmental dynamics by having the high-level policy specify not only *what* subgoal to reach but also *when*, making the learning problem more stable for the higher level in dynamic settings like traffic [339]. Another strategy is to leverage demonstrations to guide subgoal discovery, as seen in **CRISP (Curriculum inducing Primitive Informed Subgoal Prediction)**, which uses a handful of expert demonstrations and a novel parsing method to generate a curriculum of achievable subgoals for evolving low-level primitives, effectively mitigating non-stationarity through intelligent initialization [340].

Enhancing exploration and sample efficiency is another major benefit of hierarchical structures. Methods like **Landmark-Guided Subgoal Generation in Hierarchical Reinforcement Learning (HIGL)** improve exploration by reducing the high-level action space. Instead of sampling from the entire goal space, the high-level policy is guided towards promising "landmark" states, which are selected based on coverage and novelty, leading to more efficient training in complex tasks [341]. The **Adjacency constraint for efficient hierarchical reinforcement learning** tackles the same problem by theoretically and practically restricting high-level subgoals to states that are reachable within a k-step neighborhood, dramatically improving training efficiency without sacrificing optimality in deterministic settings [342] [343]. For tasks requiring deep multi-level reasoning, frameworks like **Diversity-Driven Extensible Hierarchical Reinforcement Learning (DEHRL)** build scalable, multi-level hierarchies level-by-level, promoting diversity among subpolicies at each level to ensure a useful and comprehensive set of skills [344].

Beyond classical HRL, other structured policy designs integrate symbolic reasoning, human knowledge, and modularity. The integration of symbolic AI planning with RL, as in **Hierarchical Reinforcement Learning with AI Planning Models**, creates interpretable hierarchies where options are derived from planning operators, allowing the injection of domain knowledge and improving transferability [345]. The **Hierarchical Program-Triggered Reinforcement Learning (HPRL)** framework explicitly prioritizes verifiability by using a master program to call upon simpler, pre-trained RL agents for specific subtasks (e.g., "lane follow," "intersection negotiate"). This shifts the verification burden to the interpretable program, making the overall system more amenable to safety certification [346]. Furthermore, large language models (LLMs) are being harnessed for high-level guidance, as in **LLM Augmented Hierarchical Agents**, where an LLM's world knowledge and planning capability guide a high-level RL policy, significantly boosting sample efficiency on long-horizon tasks by providing a structured plan that the RL agent learns to execute [347].

Skill-based learning and option discovery focus on autonomously acquiring a repertoire of reusable low-level behaviors. **Hierarchical Reinforcement Learning By Discovering Intrinsic Options (HIDIO)** learns task-agnostic options through an intrinsic entropy minimization objective, resulting in a diverse set of skills that can be leveraged to solve sparse-reward tasks more efficiently [348]. The **Value Function Spaces** approach abstracts the state space based on the affordances provided by a bank of learned skills, using their value functions to create a compact representation that ignores distractors and facilitates long-horizon reasoning [349]. For continuous control, methods like **ReLMoGen** lift the action space from low-level joint commands to subgoals for a motion generator (planner + executor), enabling RL to solve complex mobile manipulation tasks that are intractable in the original action space [350].

Finally, ensuring safety and reactivity within hierarchies is paramount. The **Emergency action termination for immediate reaction in hierarchical reinforcement learning** method addresses the latency of lower-level skill execution by constantly verifying at the high level whether a chosen subgoal is still valid, allowing for immediate interruption and replacement with a more appropriate action if the environment changes [351]. **Imagination-Augmented Hierarchical Reinforcement Learning for Safe and Interactive Autonomous Driving in Urban Environments (IAHRL)** integrates model-based "imagination" into HRL, allowing the low-level policy to predict safe trajectories and the high-level policy to interpret these imagined futures to infer interactions with other objects, leading to safer and more interactive driving behaviors in complex urban scenarios [352].

In summary, hierarchical and structured policy learning provides a powerful toolkit for tackling the multifaceted challenges of autonomous driving. By decomposing the problem, these methods achieve greater sample efficiency, enable the reuse and transfer of skills, and open avenues for incorporating symbolic knowledge and improving interpretability. Ongoing research focuses on improving the stability of joint training, automating the discovery of optimal abstraction levels and skills, and tightly integrating safety assurance mechanisms at every level of the hierarchy.

**Table: Comparison of approaches in 4.2 Hierarchical and Structured Policy Learning**

| Method / Framework Name | Core Idea / Contribution | Key Challenge Addressed | Reference |
| :--- | :--- | :--- | :--- |
| **atHRL (Action and Trajectory Planner using HRL)** | A two-level HRL planner for autonomous driving. High-level policy outputs target waypoints (subgoals) based on sensor input; low-level controller generates throttle/steering commands. | Planning in complex, dynamic urban driving scenarios with multiple tasks and other vehicles. | [337] |
| **State-Conditioned Adversarial Subgoal Generation** | Mitigates non-stationarity in HRL by training a discriminator to distinguish achievable vs. non-achievable subgoals, adversarially enforcing high-level policy to generate compatible subgoals. | Non-stationary high-level policy caused by a simultaneously learning, changing low-level policy. | [338] |
| **HiTS (Hierarchical RL with Timed Subgoals)** | High-level policy specifies *what* subgoal to reach and *when* to reach it, making learning more stable for the higher level in dynamic environments. | Environmental dynamics and non-stationarity in dynamic settings like traffic. | [339] |
| **CRISP (Curriculum inducing Primitive Informed Subgoal Prediction)** | Uses a handful of expert demonstrations and a novel parsing method (PIP) to generate a curriculum of achievable subgoals for evolving low-level primitives. | Non-stationarity from simultaneous learning of hierarchy; improves sample efficiency. | [340] |
| **HIGL (Landmark-Guided Subgoal Generation in HRL)** | Improves exploration by guiding the high-level policy towards promising "landmark" states (selected based on coverage/novelty), reducing the effective high-level action space. | Inefficient exploration in large goal spaces. | [341] |
| **Adjacency constraint for efficient HRL** | Theoretically and practically restricts high-level subgoals to states reachable within a k-step neighborhood, improving training efficiency without sacrificing optimality in deterministic MDPs. | Training inefficiency due to large high-level (goal) action space. | [342] |
| **DEHRL (Diversity-Driven Extensible HRL)** | Builds scalable, multi-level hierarchies level-by-level, promoting diversity among subpolicies at each level to ensure a useful and comprehensive set of skills. | Scaling HRL to multiple levels and discovering diverse, useful skills. | [344] |
| **Hierarchical Reinforcement Learning with AI Planning Models** | Integrates symbolic AI planning with RL, creating interpretable hierarchies where options are derived from planning operators, allowing injection of domain knowledge. | Combining interpretability, knowledge integration, and sample efficiency. | [345] |
| **HPRL (Hierarchical Program-Triggered RL)** | Uses a master program to call upon simpler, pre-trained RL agents for specific subtasks, shifting verification burden to the interpretable program for safety certification. | Verifiability and safety certification of complex RL policies for autonomous driving. | [346] |
| **LLM Augmented Hierarchical Agents** | Uses an LLM's world knowledge and planning capability to guide a high-level RL policy, providing a structured plan to boost sample efficiency on long-horizon tasks. | Sample inefficiency and planning in long-horizon, sparse-reward tasks. | [347] |
| **HIDIO (HRL By Discovering Intrinsic Options)** | Learns task-agnostic options through an intrinsic entropy minimization objective, resulting in a diverse set of reusable skills. | Automatically discovering a repertoire of useful low-level skills (options). | [348] |
| **Value Function Spaces** | Creates skill-centric state abstractions using the value functions of a bank of learned skills, forming a compact representation that ignores distractors for long-horizon reasoning. | State abstraction for long-horizon reasoning with a set of skills. | [349] |
| **ReLMoGen** | Lifts the action space from low-level joint commands to subgoals for a motion generator (planner + executor), enabling RL to solve complex mobile manipulation tasks. | Solving long-horizon, interactive navigation and mobile manipulation tasks intractable in the original action space. | [350] |
| **Emergency action termination for immediate reaction in HRL** | Constantly verifies at the high level whether a chosen subgoal is still valid, allowing immediate interruption and replacement if the environment changes. | Latency and lack of reactivity in hierarchical systems when lower-level skills are executing. | [351] |
| **IAHRL (Imagination-Augmented HRL)** | Integrates model-based "imagination": low-level policy predicts safe trajectories; high-level policy interprets these to infer interactions, leading to safer, interactive driving. | Learning safe and interactive behaviors in dynamic, real-world navigation/urban driving tasks. | [352] |


### 4.3 Multi-Agent Frameworks for Interactive Driving

The inherent complexity of autonomous driving stems not from isolated vehicle control but from the intricate, multi-agent interactions on the road. To model this reality, multi-agent reinforcement learning (MARL) frameworks have become essential, moving beyond single-ego formulations to explicitly account for the interplay between the ego vehicle, other autonomous vehicles (AVs), human-driven vehicles (HVs), and pedestrians. The canonical formulation for this setting is the Partially Observable Markov Game (POMG), which generalizes the Markov Decision Process to multiple agents, each with its own partial observations, actions, and objectives. This framework naturally captures the non-stationarity and partial observability of mixed traffic, where an agent must reason about the intentions and future actions of others whose policies are simultaneously evolving [353]. A key challenge in this formulation is the credit assignment problem—determining each agent's contribution to a shared outcome—and the exponential growth of the joint action space. To address these, recent frameworks often adopt a Centralized Training with Decentralized Execution (CTDE) paradigm, as seen in algorithms like MADDPG and its variants. For instance, [354] applies such actor-critic methods to enable cooperative driving in complex simulators, allowing agents to learn coordinated policies using global information during training while executing based on local observations.

A primary research thrust within MARL for driving is fostering cooperative behaviors to enhance overall traffic flow and safety, especially in mixed-autonomy settings. Rather than optimizing for individual egoistic rewards, these frameworks design reward structures that incentivize social utility and altruism. [355] explicitly models AV maneuver planning as a partially observable stochastic game and introduces a quantitative representation of social preferences into a distributed reward structure. This enables altruistic AVs to form alliances and guide traffic, improving outcomes like merge success rates. Similarly, [356] proposes a decentralized MARL framework where AVs learn to implicitly understand HV decision-making from experience, optimizing for social utility while prioritizing safety. This approach robustifies AV policies against diverse human behaviors. Cooperation is also framed as a resource management problem; [357] explores using Optimal Transport theory within MARL to align agent policies and optimize resource distribution, which can be applied to traffic flow management.

However, traffic interactions are not purely cooperative; they often involve competitive or mixed-motive scenarios where agents have diverging interests. Frameworks must therefore enable negotiation and strategic interaction. [358] draws from economic theory, augmenting Markov games with binding reward transfers (contracts) to align individual incentives with social welfare, a concept applicable to traffic scenarios like merging or intersection negotiation. For highly interactive scenarios like unsignalized intersections or dense merging zones, frameworks must enable agents to infer others' traits and intentions. [359] enhances a standard DRL framework with auxiliary tasks for relational reasoning, explicitly inferring the internal states (traits, intentions) of surrounding agents and predicting their counterfactual trajectories. This not only improves performance but also yields explainable interactivity scores. The [2] framework uses reinforcement learning with an attention mechanism to allow an ego-agent to learn how its actions affect others, incorporating a "driver-type" parameter to create adaptive policies for different planning objectives like aggressive or cautious driving.

Communication mechanisms are a critical component of advanced MARL frameworks, enabling explicit coordination and shared situational awareness. In connected autonomous vehicle (CAV) fleets, vehicle-to-vehicle (V2V) communication can be leveraged to share observations, intentions, or learned features. [360] designs an information-sharing MARL framework with a truncated Q-function that utilizes shared information from neighboring CAVs without causing the joint state-action space to explode. [361] and [362] focus on reducing the bandwidth overhead of such communication through techniques like segment mixture and quantization, ensuring scalability in real-world IoV systems. Beyond pre-defined protocols, some frameworks investigate emergent communication, where agents develop a grounded language through interaction. [363] formulates a problem where cooperative agents connected via a fixed network learn to exchange discrete symbols to accomplish tasks, with analysis showing the developed language's relationship to the network topology. [364] generalizes this further by incorporating a noisy channel explicitly into the environment dynamics, forcing agents to learn robust and effective communication strategies.

For scalability in large-scale traffic systems, graph-based MARL frameworks have shown significant promise. These methods model traffic participants as nodes in a graph, with edges representing spatial or interaction relationships, allowing for permutation-invariant processing of a variable number of agents. [365] proposes a generic GRL framework, demonstrating that GRL methods outperform standard DRL in optimizing multi-agent decision-making for CAVs by better capturing the mutual effects between vehicles. [366] utilizes attention mechanisms on interaction features within a graph structure to capture interplay between agents and boost cooperation, focusing on system-level performance rather than individual vehicle performance. Similarly, [367] employs a Graph Convolutional Network (GCN)-Transformer as a spatial-temporal encoder to enhance environment awareness for CAVs coordinating in the presence of unconnected hazard vehicles.

Finally, specialized frameworks address the unique challenges of specific interactive maneuvers. For lane-changing in mixed traffic, [368] formulates it as a MARL problem, developing a Multi-Agent Advantage Actor-Critic (MA2C) network with a novel local reward design and parameter sharing. For merging scenarios, [369] and [370] propose MARL frameworks that use action masking and safety supervisors to enable AVs to collaboratively adapt to HVs, with the latter employing curriculum learning to efficiently train a single policy that infers other drivers' cooperativeness. [371] introduces a distributed MARL algorithm for intent-aware planning, allowing agents to infer nearby drivers' behavioral incentives (high-level personality) and instant incentives (collision avoidance) from local observations, significantly improving performance in dense, heterogeneous traffic. These frameworks collectively underscore a shift from isolated perception-planning-action pipelines to integrated, interactive, and socially-aware policy learning, which is paramount for the safe and efficient integration of AVs into human-centric traffic ecosystems.

**Table: Comparison of approaches in 4.3 Multi-Agent Frameworks for Interactive Driving**

| Framework / Method | Key Idea / Mechanism | Application Scenario / Task | Reference |
| :--- | :--- | :--- | :--- |
| Centralized Training with Decentralized Execution (CTDE) | Adopts a paradigm where agents are trained with global information but execute policies based on local observations to address non-stationarity and credit assignment. | General multi-agent control in complex simulators (e.g., SMARTS). | [354] |
| Social Preference & Altruistic Reward Design | Models AV planning as a partially observable stochastic game with a quantitative representation of social preferences in a distributed reward structure to incentivize social utility. | Mixed-autonomy traffic, specifically highway merging. | [355] |
| Implicit Human Behavior Learning | A decentralized MARL framework where AVs learn HV decision-making implicitly from experience, optimizing for social utility while prioritizing safety. | Cooperative autonomous driving in mixed-autonomy traffic. | [356] |
| Optimal Transport Theory Integration | Explores using Optimal Transport theory within MARL to align agent policies and optimize resource distribution (e.g., for traffic flow management). | Policy alignment and resource management in multi-agent systems. | [357] |
| Formal Contracts for Incentive Alignment | Augments Markov games with binding reward transfers (contracts) drawn from economic theory to align individual incentives with social welfare. | Traffic scenarios with social dilemmas (e.g., merging, intersection negotiation). | [358] |
| Internal State Inference & Interactivity Estimation | Enhances DRL with auxiliary tasks for relational reasoning to infer internal states (traits, intentions) of others and predict counterfactual trajectories, yielding explainable interactivity scores. | Highly interactive multi-agent environments (e.g., intersection navigation). | [359] |
| Attention-based Adaptive Strategy Learning (MIDAS) | Uses RL with an attention mechanism to learn how ego actions affect others, incorporating a "driver-type" parameter for adaptive policies (aggressive/cautious). | Urban autonomous navigation in interactive scenarios. | [2] |
| Information-Sharing MARL with Truncated Q-function | Designs an MARL framework for CAVs that utilizes shared V2V information via a truncated Q-function to avoid explosion of the joint state-action space, with safety guarantees. | Safe and efficient behavior planning for connected autonomous vehicles. | [360] |
| Communication-Efficient MARL (RSM-MAPPO) | Enhances multi-agent PPO with regulated segment mixture to reduce communication overhead in a fully distributed architecture for IoV systems. | Mixed-autonomy traffic control in Internet of Vehicles. | [361] |
| Quantization-based Decentralized MARL | Proposes a fully decentralized MARL framework with a quantization-based communication scheme to reduce overhead for cooperative adaptive cruise control. | Cooperative Adaptive Cruise Control (CACC) for CAV platoons. | [362] |
| Emergent Communication in Networked MARL | Formulates a problem where cooperative agents connected via a fixed network learn to exchange discrete symbols to develop a grounded communication language. | Multi-agent coordination tasks (e.g., managing traffic controllers). | [363] |
| Joint Learning & Communication over Noisy Channels | Incorporates a noisy communication channel explicitly into the MA-POMDP dynamics, forcing agents to learn robust and effective communication strategies. | General multi-agent coordination under realistic communication constraints. | [364] |
| Graph Reinforcement Learning (GRL) Framework | Models traffic participants as nodes in a graph for permutation-invariant processing, demonstrating superiority over standard DRL in capturing mutual effects. | Co-operative decision-making for CAVs in mixed autonomy traffic. | [365] |
| Multi-agent Graph RL with Attention | Utilizes attention mechanisms on interaction features within a graph structure to capture interplay between agents and boost cooperation for system-level performance. | Connected and automated driving system optimization. | [366] |
| Spatial-Temporal GCN-Transformer MARL | Employs a GCN-Transformer as a spatial-temporal encoder within a constrained MARL framework to enhance environment awareness for CAVs coordinating with unconnected hazards. | Safe coordination of CAVs in challenging scenarios with unconnected vehicles. | [367] |
| Multi-Agent Advantage Actor-Critic (MA2C) for Lane Changing | Formulates lane-changing as a MARL problem with a novel local reward design and parameter sharing in a multi-agent advantage actor-critic network. | Cooperative lane changing of CAVs in mixed highway traffic. | [368] |
| MARL with Action Masking & Safety Supervisor | Proposes a MARL framework using action masking and safety supervisors for AVs to collaboratively adapt to HVs in merging scenarios, employing curriculum learning. | Highway on-ramp merging in mixed traffic. | [369] |
| Curriculum Learning for Adaptive Strategies (IDAS) | Learns a single policy via MARL and curriculum learning to automatically infer other drivers' cooperativeness and make strategic decisions in merging scenarios. | Interaction-aware decision making under merging scenarios. | [370] |
| Distributed MARL for Intent-Aware Planning (iPLAN) | A distributed MARL algorithm allowing agents to infer nearby drivers' behavioral incentives and instant incentives from local observations for intent-aware planning. | Planning in dense, heterogeneous traffic. | [371] |


### 4.4 Integration of Foundation Models for Reasoning and Instruction

The paradigm of autonomous driving policy learning is undergoing a profound transformation with the integration of foundation models, particularly Large Language Models (LLMs) and Vision-Language Models (VLMs). These models, pre-trained on vast corpora of text and image-text pairs, are being repurposed as cognitive components within driving architectures. Their primary roles are to act as high-level planners, interpretable reasoners, and natural language interfaces, directly addressing the limitations of traditional Deep RL and IL in generalization, interactivity, and handling of long-tail, complex scenarios. This integration marks a shift from purely optimization-based policy learning to systems endowed with commonsense reasoning and instruction-following capabilities.

A core application is the use of LLMs and VLMs as high-level task planners and decision-makers. Rather than mapping raw sensor inputs directly to control signals, these models are employed to generate interpretable, symbolic plans or high-level driving commands. For instance, frameworks like **DriveGPT4** and **DriveMLM** utilize multimodal LLMs to process video inputs and textual queries, outputting not only control commands but also reasoning about vehicle actions [372] [373]. This approach, often described as making the system "Drive Like a Human" [374], leverages the model's commonsense knowledge to navigate ambiguous situations. Similarly, **LanguageMPC** employs LLMs as decision-makers for complex scenarios, using cognitive pathways to translate natural language reasoning into actionable driving commands via model predictive control [375]. The planning capability is further enhanced by techniques like chain-of-thought (CoT) prompting, which forces the model to articulate intermediate reasoning steps, thereby improving reliability and interpretability [376]. This is exemplified in **DriveVLM**, which integrates a chain-of-thought module for scene description, analysis, and hierarchical planning, significantly boosting performance in complex urban environments [377].

The interpretability afforded by these models' natural language outputs is a key advantage. By generating a "verbal" rationale for decisions, they provide a transparent window into the policy's decision-making process, which is crucial for debugging, trust, and validation. This moves beyond traditional "black-box" neural policies towards **Explainable End-to-End Autonomous Driving** [372]. Benchmarks like **Reason2Drive** are specifically constructed to evaluate this chain-based reasoning capability in driving contexts, providing datasets with annotated reasoning chains that link perception, prediction, and final actions [378]. Furthermore, the ability to process **Natural Language Instructions** allows for unprecedented interactivity and personalization. A user can issue high-level commands like "overtake the slow truck when safe" or "find a parking spot near the cafe," and the LLM component can parse this intent, ground it in the current visual scene, and formulate a corresponding plan [15]. This facilitates **Human-AI Collaboration**, where the AI can explain its actions and accept guidance in natural language.

To effectively ground language in the dynamic driving environment, a critical challenge is multimodal fusion. Pure LLMs lack visual perception, necessitating their combination with VLMs or other perception modules. Architectures are evolving to create tightly integrated **Vision-Language Planning** systems. **ViLa** (Robotic Vision-Language Planning) exemplifies this by directly integrating perceptual data into the LLM's reasoning process, enabling a profound understanding of spatial layouts and object attributes from visual inputs [379]. For more precise spatial reasoning, some approaches move beyond 2D images to incorporate 3D world representations. **3D-LLM** injects 3D point cloud features into LLMs, enabling tasks like 3D question answering and embodied reasoning which are essential for navigation [380]. Other frameworks, such as the one proposed in **Using Left and Right Brains Together**, advocate for concurrent visual and language planning, where a visual planner captures environmental details and a language planner ensures logical coherence [381].

Despite their promise, several architectural and operational challenges persist. A significant debate centers on whether LLMs can truly "plan" or should be used in a **LLM-Modulo Framework** [382]. This neuro-symbolic perspective argues that LLMs are best used as universal knowledge sources to assist or generate inputs for dedicated, verifiable planners, rather than acting as planners themselves. This hybrid approach is seen in **LLM-Assist**, which combines an LLM-based planner with a conventional rule-based planner to achieve state-of-the-art performance, leveraging commonsense reasoning while remaining grounded in reliable rules [383]. Another challenge is **Semantic Grounding**—ensuring the model's language outputs correctly correspond to physical entities in the scene. Misgrounding can lead to dangerous errors, prompting research into enhancement methods through fine-grained multimodal instruction tuning [384]. Furthermore, the computational latency of large foundation models is a barrier to real-time control, leading to efficient architectures like **DriveVLM-Dual**, which synergizes a VLM-based planner with a traditional pipeline for robust, real-time performance [377].

Finally, the integration paradigm extends to learning from experience and enabling replanning. **RePLan** demonstrates how VLMs can provide physical grounding to understand the world's state, allowing an agent to replan and adapt when an initial LLM-generated plan fails [385]. The concept of an **Inner Monologue**, where the LLM continuously reasons over environment feedback (e.g., success detection, scene description), allows for richer closed-loop planning and error correction [386]. This feedback-driven reasoning is crucial for handling the unexpected events common in driving.

In summary, the integration of LLMs and VLMs into autonomous driving architectures introduces a powerful layer of abstraction and cognition. By serving as planners, reasoners, and interfaces, these foundation models enhance the system's ability to generalize to novel scenarios, interact naturally with humans, and provide explainable decisions. The prevailing trend is toward hybrid, **LLM-Modulo** architectures that combine the commonsense and linguistic strengths of foundation models with the robustness, verifiability, and real-time performance of traditional planning and control systems, paving the way for more adaptable and trustworthy autonomous vehicles.

**Table: Comparison of approaches in 4.4 Integration of Foundation Models for Reasoning and Instruction**

| Method/Model Name | Key Idea / Role | Reference |
| :--- | :--- | :--- |
| DriveGPT4 | Interpretable end-to-end autonomous driving via a multimodal LLM that processes video and text to output control commands and reasoning. | [372] |
| DriveMLM | Aligns a multimodal LLM with behavioral planning states to act as a plug-and-play behavior planner in a modular AD system. | [373] |
| LanguageMPC | Uses LLMs as decision-makers for complex driving scenarios, translating natural language reasoning into driving commands via model predictive control. | [375] |
| DriveVLM | Integrates a chain-of-thought module for scene description, analysis, and hierarchical planning to handle complex urban environments. | [377] |
| ViLa (Robotic Vision-Language Planning) | A vision-language planning system that directly integrates perceptual data into the LLM's reasoning for grounded, long-horizon robotic planning. | [379] |
| 3D-LLM | Injects 3D point cloud features into LLMs to enable 3D question answering and embodied reasoning for navigation. | [380] |
| LLM-Assist | A hybrid planner combining an LLM-based planner with a conventional rule-based planner for robust closed-loop planning. | [383] |
| RePLan | Enables robotic replanning by using a VLM to understand the world's state and adapt actions when an initial LLM-generated plan fails. | [385] |


### 4.5 Policy Design with Semantic and Latent Representations

A central paradigm in modern autonomous driving policy design seeks to move beyond the dichotomy of purely modular pipelines and fully end-to-end learning by incorporating intermediate, semantically meaningful representations. These representations—such as occupancy grids, vectorized high-definition maps, trajectory proposals, or latent state embeddings—serve as a crucial bridge. They retain the interpretability and structural priors of modular systems while enabling the data-driven optimization and generalization benefits of end-to-end approaches. This design philosophy directly addresses core challenges in training efficiency, sim-to-real transfer, and policy interpretability.

Semantic spatial representations, particularly in a top-down or bird's-eye-view (BEV) format, have become a cornerstone. Works like [387] and [315] demonstrate that predicting occupancy grid maps (OGMs) or semantic grids from camera images provides a geometrically consistent scene abstraction. This BEV representation disentangles perspective effects, allowing the subsequent policy or planner to reason in a metric space where distances and relationships are uniform. The policy can then be trained using reinforcement or imitation learning on this compact grid, as seen in [388], which uses generative models in a learned latent space for stochastic prediction. This separation of perception (image-to-BEV) and action (BEV-to-control) simplifies the learning problem. The intermediate grid is human-interpretable, allowing engineers to diagnose failures in perception versus planning, and its spatial structure enables the injection of geometric constraints and classical safety checks, enhancing robustness.

An evolution beyond dense rasterized grids is the use of *vectorized* scene representations. Approaches such as [389] argue that representing agents and map elements (lanes, boundaries) as structured polylines or geometric primitives is more efficient and preserves instance-level information. This vectorized format is inherently compact, reduces computational load, and allows the policy to explicitly reason about constraints like lane boundaries and agent interactions. Similarly, [390] uses a polyline encoder to model agent trajectories and scene context for occlusion reasoning, demonstrating how structured representations facilitate modeling high-order interactions. These vectorized interfaces naturally align with how traditional planners consume information, making them an effective bridge for learned policies to incorporate rule-based safeguards or optimization-based post-processing.

Parallel to these explicit semantic maps is the line of work focusing on learning *latent state representations*. The goal here is to compress high-dimensional, noisy observations into a low-dimensional embedding that captures all task-relevant information. Methods like [391] and [392] formally seek minimal sufficient representations that factorize transition dynamics and reward, dramatically improving sample efficiency for policy learning. In autonomous driving, [393] imposes an information bottleneck to extract a latent representation that minimizes a distance metric between different driving scenarios, enabling better generalization to unseen environments. [394] introduces a sequential latent environment model learned jointly with the RL policy; this model can generate interpretable semantic bird's-eye masks, connecting the latent space to human-understandable concepts. Learning in this compact latent space reduces the sample complexity of RL and enables techniques like latent imagination or planning, as explored in [395] for cross-domain simulation transfer.

The benefits of these intermediate representations for **sim-to-real transfer** are profound. A policy trained on semantic BEV grids or latent vectors from simulation is more likely to transfer to reality because the representation space can be designed or learned to be more invariant to low-level visual domain shifts (e.g., lighting, texture). [396] successfully transferred a simulation-trained policy to a real robotic truck by encapsulating the policy to rely on abstracted perceptual features rather than raw pixels. [397] proposes a representation combining spatial and semantic information with embedded noise models, showing superior transfer performance compared to end-to-end alternatives. The representation acts as a stabilizer; even if the perceptual module's output degrades slightly in the real world, the policy operates on a more consistent and robust input domain.

Furthermore, these designs enhance **training efficiency**. Decomposing the problem into representation learning and policy learning allows for modular, potentially asynchronous, training. The representation can be pre-trained on large, unlabeled datasets (e.g., for occupancy prediction) or via self-supervised objectives, as in [270]. The policy module, now operating on a low-dimensional input, requires far fewer interactive samples to train. This is exemplified in [398], which shows that learning in latent state and action spaces facilitates policy generalization and sample efficiency. The framework [399] explicitly bridges model-free and model-based RL through a shared low-dimensional encoding, enabling efficient planning in the latent space.

Finally, the **interpretability** afforded by semantic and latent representations is critical for deployment and debugging. A policy that consumes a BEV occupancy grid allows developers to visualize exactly what the car "thinks" the world looks like before it makes a decision. The latent representations learned by methods like [400] are designed to associate reachable states together, creating an interpretable abstraction for hierarchical planning. This contrasts with black-box end-to-end policies where linking a failure to a specific perceptual error or reasoning flaw is extremely difficult. By designing policies around these intermediate representations, the autonomous system gains a measure of introspective capability, enabling safer and more trustworthy operation. In summary, policy designs leveraging semantic and latent representations offer a powerful middle ground, combining the strengths of data-driven learning with the safety, efficiency, and clarity of structured reasoning.

**Table: Comparison of approaches in 4.5 Policy Design with Semantic and Latent Representations**

| Method Category | Key Idea / Representation | Primary Benefits (as per text) | Example References (from Input 2) |
| :--- | :--- | :--- | :--- |
| Semantic Bird's-Eye-View (BEV) Grids | Predicts occupancy grid maps (OGMs) or semantic grids from camera images in a top-down, metric space. Disentangles perspective effects. | Interpretability, geometric consistency, simplifies learning (separates perception & action), enables safety checks. | [387], [315], [388] |
| Vectorized Scene Representations | Represents agents and map elements (lanes) as structured polylines or geometric primitives instead of dense grids. | Efficiency (compact), preserves instance-level info, explicit reasoning about constraints (lanes, interactions), aligns with traditional planners. | [389], [390] |
| Latent State Representations | Learns a low-dimensional embedding from high-dimensional observations that captures task-relevant information, often with formal guarantees (e.g., minimal sufficient). | Dramatically improves sample efficiency, enables generalization, reduces RL complexity, allows latent imagination/planning. | [391], [392], [393], [394], [395] |


## 5 Core Driving Applications and Task-Specific Formulations

This section surveys the application of DRL/IL to specific autonomous driving tasks. It includes operational control (longitudinal/lateral control, lane-keeping), tactical maneuvers (lane change, merging, intersection negotiation), and strategic tasks (route planning, eco-driving, fleet management), discussing their respective state/action spaces and reward designs.

### 5.1 Operational Control and Low-Level Motion Execution

At the foundational level of autonomous driving, operational control and low-level motion execution translate high-level decisions into precise, safe, and comfortable vehicle actuation. This domain primarily encompasses longitudinal control (e.g., car-following, speed adaptation) and lateral control (e.g., lane-keeping, path tracking), which are often learned separately before being integrated for holistic motion. Deep Reinforcement Learning (DRL) and Imitation Learning (IL) offer data-driven alternatives to classical control theory, capable of handling complex, non-linear dynamics and adapting to diverse driving styles and environmental conditions.

For **longitudinal control**, a canonical task is Adaptive Cruise Control (ACC) or car-following. DRL approaches formulate this as a continuous control problem, where the agent learns to modulate acceleration and braking to maintain a safe and efficient distance from a leading vehicle. The state space typically includes ego-vehicle speed, relative speed, and inter-vehicle spacing, as seen in studies like [19] and [401]. The latter work highlights a critical design choice: the discrepancy between simplified kinematic models used for training and the real vehicle's dynamic response (e.g., actuation delay). To bridge this gap, successful formulations augment the state with delayed control inputs and actual acceleration, enabling the DRL policy to learn a dynamic model implicitly and achieve near-optimal performance. Reward functions are meticulously crafted to balance competing objectives: maintaining a target headway (safety and efficiency), minimizing jerk (comfort), and reducing energy consumption. For instance, [133] explicitly incorporates all these factors into a multi-objective reward. Imitation Learning provides a complementary pathway, as demonstrated in [19], where a Deep Deterministic Policy Gradient (DDPG) agent is trained using the disparity between simulated and real human-driven speeds as a reward signal, effectively learning a human-like driving policy from naturalistic data.

**Lateral control**, primarily lane-keeping or path tracking, involves generating steering commands to follow a reference path. The state representation can vary from low-dimensional features (e.g., lateral offset, heading error) to high-dimensional raw sensor input like camera images. The action is typically a continuous steering angle. A key challenge is ensuring control smoothness to avoid dangerous oscillatory behavior and passenger discomfort. The paper [402] directly addresses this by applying a Conditioning for Action Policy Smoothness (CAPS) mechanism, which penalizes abrupt action changes and significantly improves lap times and stability. Similarly, [403] introduces smoothness rewards based on the minimization of trajectory derivatives to generate stable flight paths, a principle directly applicable to ground vehicles. For more robust and generalizable control, some works integrate domain knowledge. [404] proposes a hybrid architecture combining Q-learning with a PID controller, using a quadratic Q-function over actions and a PID-inspired action network to guide exploration within a continuous space, resulting in smooth lane-change and merge behaviors.

The ultimate goal is the **integrated control** of both longitudinal and lateral dynamics for complex maneuvers like lane changes or navigating curves. This requires policies that output multi-dimensional continuous actions (steering, acceleration, braking). Algorithms like DDPG, PPO, and SAC are frequently employed for this purpose. For example, [405] uses DDPG to learn a continuous lane-change policy from scratch, with rewards based on control values, position deviation, and maneuver time. The study [406] utilizes PPO for its sample efficiency and stability in learning safe lane-change decisions in dense traffic. A significant trend is moving towards **vision-based end-to-end control**, where policies map raw pixel inputs directly to control commands. This is exemplified by [407], which trains an agent to perform simultaneous lane-keeping and car-following using camera images and demonstrates successful transfer to a real-world platform. However, this approach intensifies the **Sim2Real transfer** challenge. Discrepancies in lighting, textures, and sensor physics between simulation and reality can cause severe performance degradation. Techniques to overcome this include domain randomization, used in [408], and the use of intermediate, platform-agnostic representations as proposed in [18], which extracts task-relevant features to minimize the domain gap.

Furthermore, **Imitation Learning** plays a vital role in low-level control by cloning expert demonstrations, which can be from human drivers or classical controllers. Behavior Cloning can provide a strong initial policy, but it often suffers from covariate shift. More advanced methods like Inverse Reinforcement Learning (IRL) learn the underlying reward function of the expert. [409] employs IRL to learn a spatiotemporal cost function from human driving, which is then used by a Model Predictive Controller (MPC) to generate control commands, effectively transferring human-like driving style to an optimization-based controller. Hybrid approaches that combine IL and RL, such as [26], leverage demonstrations to constrain the initial action space for RL, drastically improving exploration efficiency and final performance in vision-based tasks.

In summary, DRL and IL have proven highly effective for learning nuanced, adaptive, and integrated vehicle control policies. The core design considerations involve the careful formulation of state and action spaces, the balancing of multi-objective rewards for safety, efficiency, and comfort, and the incorporation of techniques—such as hybrid architectures, smoothness constraints, and domain adaptation—to ensure robustness and facilitate successful transfer from simulation to the real vehicle.

**Table: Comparison of approaches in 5.1 Operational Control and Low-Level Motion Execution**

| Method Category | Specific Method/Model | Key Contribution/Approach | Reference |
| :--- | :--- | :--- | :--- |
| Longitudinal Control (DRL) | DRL for Adaptive Cruise Control (ACC) | Formulates car-following as a continuous control problem. State includes ego speed, relative speed, spacing. Reward balances safety, efficiency, comfort, and energy consumption. | [401] |
| Longitudinal Control (IL) | Imitation Learning for Car-Following | Uses DDPG with reward based on disparity between simulated and real human-driven speeds to learn a human-like policy from naturalistic data. | [19] |
| Lateral Control (DRL) | DRL with Smoothness Constraint (CAPS) | Applies Conditioning for Action Policy Smoothness (CAPS) to penalize abrupt steering changes, improving lap times and stability in racing. | [402] |
| Lateral Control (Hybrid) | Quadratic Q-network with PID | Combines Q-learning with a PID controller, using a quadratic Q-function and a PID-inspired action network for smooth lane-change and merge behaviors. | [404] |
| Integrated Control (DRL) | DDPG for Lane Change | Learns a continuous lane-change policy from scratch with rewards based on control values, position deviation, and maneuver time. | [405] |
| Integrated Control (DRL) | PPO for Lane Change | Uses Proximal Policy Optimization for sample-efficient and stable learning of safe lane-change decisions in dense traffic. | [406] |
| Vision-based End-to-End Control | Vision-based DRL Agent | Trains an agent to perform simultaneous lane-keeping and car-following using raw camera images, with successful Sim2Real transfer. | [407] |
| Sim2Real Transfer | Platform-Agnostic DRL Framework | Uses platform-dependent perception to extract task-relevant features, minimizing the domain gap for effective Sim2Real transfer. | [18] |
| Imitation Learning (Advanced) | Inverse Reinforcement Learning (IRL) for MPC | Uses IRL to learn a spatiotemporal cost function from human driving, which is then used by an MPC to generate control commands. | [409] |
| Hybrid IL/RL | Controllable Imitative RL (CIRL) | Combines IL and RL, using demonstrations to constrain the initial action space for RL to improve exploration in vision-based tasks. | [26] |


### 5.2 Tactical Maneuvering in Structured Environments

Tactical maneuvering in structured environments, such as highways and arterial roads, involves discrete, high-level decisions that govern interactive maneuvers like lane changes, merging, and overtaking. These scenarios are characterized by predictable road geometry but highly uncertain interactions with human-driven vehicles (HDVs). Deep Reinforcement Learning (DRL) and Imitation Learning (IL) have emerged as powerful paradigms for learning these complex, socially-aware decision-making policies, moving beyond rigid rule-based systems.

**Lane-changing** is a quintessential tactical maneuver, subdivided into discretionary (DLC) and mandatory (MLC) types. DRL approaches formulate lane-changing as a sequential decision-making problem within a Markov Decision Process (MDP). For instance, proximal policy optimization (PPO) has been used to develop automated lane-change strategies that learn smooth and efficient policies in dense traffic [406]. A key challenge is the design of multi-objective reward functions that balance safety, efficiency (e.g., travel time), and passenger comfort (e.g., minimizing jerk). The Deep Deterministic Policy Gradient (DDPG) algorithm has been applied to continuous control for lane changes, with rewards defined by control values, position deviation, and maneuvering time [405]. To enhance safety, some works integrate model-based safety checks. A time-to-collision-aware lane-change strategy combines potential fields with polynomial trajectory optimization to generate shorter and safer paths [91]. Furthermore, modeling the social preferences of surrounding vehicles—whether courteous or rude—is critical, as human drivers utilize different environmental cues based on these inferred traits [410]. Imitation Learning offers a complementary path, where models learn directly from human demonstrations. A learning-based DLC model incorporating driving style awareness of both the ego and surrounding vehicles achieved high accuracy in replicating human decisions [411]. Similarly, personalized lane-change initiation can be learned via reinforcement learning from human feedback during autonomous driving, improving user acceptance [412].

**On-ramp and off-ramp merging** represents a mandatory lane-change scenario with intense interaction. The merging vehicle must identify a suitable gap and coordinate, often implicitly, with mainline traffic. DRL is well-suited for this due to its ability to optimize long-term outcomes. Algorithms like Soft Actor-Critic (SAC) have been employed, often augmented with safety controllers that predict collisions and substitute risky actions [413]. The Shielded Distributional Soft Actor-Critic (SDSAC) framework incorporates safety considerations through policy evaluation and a barrier function-based safety shield for online correction [414]. A significant research thrust focuses on explicitly modeling interaction. Methods propose inferring the internal states (intentions, traits) of other agents and estimating interactivity through counterfactual reasoning—predicting trajectories with and without the ego vehicle's influence—to make more explainable and robust decisions [359]. Game-theoretic models provide a formal framework for these interactions. Some approaches model merging as a Stackelberg game, where the merging vehicle's aggressiveness and the mainline vehicles' reactions are captured in payoff functions [415]. Others use a repeated game model to better predict human merging behavior by considering past interactions [416]. Hierarchical solutions are also prevalent, separating the high-level gap selection and interactive decision-making from low-level trajectory optimization. One framework combines game theory for behavior planning with Branch Model Predictive Control (BMPC) to handle the multi-modal behavior of surrounding vehicles [417].

**Highway overtaking** is a complex discretionary maneuver requiring assessment of oncoming traffic, relative speeds, and distances. DRL faces sample inefficiency challenges here. To address this, one method integrates fading guidance from an expert system (using constrained iterative LQR and PID controllers) into the DRL training loop, significantly improving learning efficiency and safety [418]. The overtaking decision-making process can also be modeled using a deep Q-network (DQN) or a dueling DQN (DDQN) architecture within a hierarchical control framework, where the high-level policy makes overtaking decisions and a low-level controller executes them [132].

A dominant architectural pattern across these tasks is the **hierarchical framework**, which decomposes the problem into a high-level tactical planner and a low-level motion controller. This separation enhances robustness, interpretability, and training stability. For example, one hierarchical automatic lane-changing algorithm uses a tactical layer to generate a local-optimum trajectory optimizing for comfort, efficiency, and safety of all affected vehicles, and an operational Model Predictive Control (MPC) layer for precise tracking [419]. Another hierarchical reinforcement learning method decomposes driving into maneuvers (lane-keeping, left/right change), learns sub-policies for each, and uses a master policy to select the appropriate maneuver [420]. Similarly, a multi-modal architecture uses an occupancy grid as input to a DRL agent for high-level command generation, which is then executed by lower-level controllers [421].

Finally, **multi-agent reinforcement learning (MARL)** is increasingly applied to model the cooperative and competitive dynamics in mixed traffic. In lane-changing, MARL frameworks enable multiple autonomous vehicles (AVs) to coordinate their actions, considering the motions of both AVs and HDVs to optimize for global traffic flow, safety, and fuel efficiency [368]. For on-ramp merging, MARL allows AVs on the ramp and mainline to collaboratively learn policies that adapt to HDVs and maximize traffic throughput, employing techniques like parameter sharing and action masking [369]. These approaches mark a shift from purely ego-centric planning to systems that reason about collective outcomes, paving the way for more harmonious and efficient integration of autonomous vehicles into existing traffic ecosystems.

**Table: Comparison of approaches in 5.2 Tactical Maneuvering in Structured Environments**

| **Method / Model** | **Task / Scenario** | **Key Idea / Approach** | **Reference** |
| :--- | :--- | :--- | :--- |
| Proximal Policy Optimization (PPO) | Automated Lane Change | Formulates lane-changing as an MDP; learns smooth and efficient policies in dense traffic. | [406] |
| Deep Deterministic Policy Gradient (DDPG) | Lane Change (Continuous Control) | Applies DDPG for continuous control; reward defined by control values, position deviation, and maneuvering time. | [405] |
| Time-to-Collision-Aware Strategy (PF + Cubic Polynomial) | Lane Change | Combines potential fields with cubic polynomial trajectory optimization, imposing TTC constraints for shorter, safer paths. | [91] |
| Learning-based DLC Model with Driving Style Awareness | Discretionary Lane Change (DLC) | Imitation Learning model incorporating driving style awareness of ego and surrounding vehicles for high-accuracy human decision replication. | [411] |
| Reinforcement Learning from Human Feedback | Personalized Lane-Change Initiation | Uses RL from human feedback during autonomous driving to learn personalized lane-change initiation, improving user acceptance. | [412] |
| Soft Actor-Critic (SAC) with Safety Controller | Highway On-Ramp Merging | Uses SAC for decision-making, augmented with a motion predictive safety controller to predict collisions and substitute risky actions. | [413] |
| Shielded Distributional Soft Actor-Critic (SDSAC) | On-Ramp Merging | Incorporates safety via policy evaluation and a barrier function-based safety shield for online correction within an offline training/online correction framework. | [414] |
| Internal State Inference & Interactivity Estimation | Interactive Navigation (e.g., Merging) | Infers internal states (traits, intentions) of others and estimates interactivity via counterfactual reasoning for explainable, robust decisions. | [359] |
| Stackelberg Game Theoretic Model | Lane Merging | Models merging as a Stackelberg game, capturing merging vehicle aggressiveness and mainline vehicle reactions in payoff functions. | [415] |
| Repeated Game Model | Lane Merging | Uses a repeated game model to predict human merging behavior by considering past interactions. | [416] |
| Game Theory + Branch Model Predictive Control (BMPC) | Automated Lane Merging | Combines game theory for high-level gap selection and interactive decision-making with BMPC to handle multi-modal behavior of surrounding vehicles. | [417] |
| DRL with Fading Expert Guidance | Highway Overtaking | Integrates fading guidance from an expert system (constrained iterative LQR & PID) into DRL training to improve sample efficiency and safety. | [418] |
| Dueling Deep Q-Network (DDQN) in Hierarchical Framework | Highway Overtaking | Uses a DDQN within a hierarchical control framework; high-level policy makes overtaking decisions, low-level controller executes them. | [132] |
| Hierarchical Automatic Lane-Changing Algorithm | Lane Change | Two-layer planner: tactical layer generates local-optimum trajectory optimizing comfort, efficiency, safety; operational MPC layer for tracking. | [419] |
| Hierarchical Reinforcement Learning (Maneuver Decomposition) | General Driving Decision-Making | Decomposes driving into maneuvers (lane-keep, left/right change), learns sub-policies for each, uses a master policy to select maneuver. | [420] |
| Multi-modal DRL with Occupancy Grid | Sequential Decision-Making | Uses occupancy grid as input to a DRL agent for high-level command generation, executed by lower-level controllers. | [421] |
| Multi-agent Advantage Actor-Critic (MA2C) | Cooperative Lane Changing | MARL framework for multiple AVs to coordinate lane changes, considering motions of AVs and HDVs; uses multi-objective reward for safety, efficiency, comfort. | [368] |
| Deep Multi-agent RL with Parameter Sharing & Action Masking | Highway On-Ramp Merging | MARL for AVs on ramp and mainline to collaboratively learn policies adapting to HDVs; uses parameter sharing, action masking, and a safety supervisor. | [369] |


### 5.3 Strategic Navigation in Complex Urban Scenarios

Strategic navigation in complex urban scenarios represents one of the most demanding frontiers for autonomous driving policy learning. Unlike structured highways, urban environments such as unsignalized intersections, roundabouts, and zones with mixed traffic (vehicles, pedestrians, cyclists) are characterized by a lack of explicit traffic control, intricate multi-agent interactions, partial observability due to occlusions, and a high degree of uncertainty regarding others' intentions. Successfully learning policies for these scenarios requires moving beyond reactive control to sophisticated, long-horizon strategic reasoning that balances safety, efficiency, and social compliance.

A primary focus of research is **unsignalized intersection negotiation**, particularly challenging maneuvers like unprotected left turns. Here, the ego vehicle must infer the intentions of oncoming and crossing traffic without the guidance of traffic signals. Deep Reinforcement Learning (DRL) has been extensively applied to learn such negotiation policies. For instance, work on [422] utilizes Deep Q-Learning to develop a decision-making framework that reduces collision rates. To handle the inherent uncertainty, many approaches frame the problem as a Partially Observable Markov Decision Process (POMDP). [423] employs Monte Carlo sampling to solve the POMDP, outperforming heuristic strategies. Similarly, [424] introduces a hierarchical method combining a high-level path generator with a POMDP-based planner, inspired by human driving behavior to enhance computational efficiency and safety.

A critical enabler for strategic navigation is advanced **multi-agent interaction modeling**. Simple prediction-then-plan pipelines often lead to overly conservative behavior. Instead, modern methods aim for *interaction-aware* planning, where the ego agent understands that its actions influence others' behavior. The paper [359] exemplifies this by using auxiliary tasks to infer the internal states (traits, intentions) of surrounding agents and estimate the degree of influence the ego vehicle has on them. This relational reasoning, often implemented with Graph Neural Networks (GNNs), provides explainable indicators for decision-making. Similarly, [2] uses reinforcement learning with an attention mechanism to learn a policy that can affect the actions of other cars, adapting to different road geometries and driver behaviors. For decentralized settings without communication, game-theoretic formulations offer a principled approach. [425] proposes an auction mechanism that assigns priority based on observable driving style, proving game-theoretically optimal for collision and deadlock avoidance. [426] further refines this by limiting game play to an agent's observational vicinity, making planning tractable for dense traffic.

To manage the complexity and long time horizons of urban navigation, **hierarchical and structured learning approaches** are prevalent. These methods decompose the problem into more manageable sub-tasks. [427] proposes a high-level policy that selects behavioral sub-policies and spatial regions of attention, while a low-level policy elaborates short-term goals within those regions. The survey context paper [428] demonstrates a practical integration where a trained DRL policy acts as a high-level behavior planner, populating an interface for established sampling-based motion planners to generate smooth trajectories, effectively bridging learning and traditional planning. Curriculum learning is another powerful technique to stage complexity. [429] presents a unique curriculum that progressively increases task difficulty, leading to faster training and better final performance. This idea is extended in [430], which automates curriculum selection to handle uncertainties in the number and intentions of surrounding vehicles.

Handling **mixed traffic flows and partial observability** is paramount for real-world deployment. Scenarios involve not just vehicles but also pedestrians and cyclists, each with distinct dynamics and behavioral patterns. [431] addresses this by developing a dynamic permutation state representation within an integrated decision and control framework, capable of processing varying numbers and types of traffic participants. When the view is occluded, agents must actively reason about what they cannot see. [432] explores learning active sensing behaviors to safely navigate despite occlusions. The challenge of simulating realistic, diverse interactions for training is tackled in [433], which learns a joint policy from real-world data to generate socially consistent and diverse traffic scenarios, providing valuable data for policy training and testing.

Finally, ensuring **safety and robustness** in these high-stakes, stochastic environments is a central concern. Many works incorporate safety constraints directly into the learning process. [434] adds a safety layer and social attention module to a multi-task RL framework to guarantee safe negotiation. [435] proposes a policy optimization method with interaction-aware constraints, using GNNs to model social context and create a feedback loop between prediction and control to enhance safety. Furthermore, [436] focuses on generalization by training a meta-policy for social vehicles that can generate diverse behaviors, thereby enhancing the robustness of the ego vehicle's policy when encountering unseen agent behaviors in challenging scenarios like uncontrolled T-intersections.

In summary, strategic navigation in complex urban scenarios demands a synthesis of advanced techniques from deep RL, interactive multi-agent modeling, hierarchical decomposition, and robust safety assurance. The progression is from learning reactive maneuvers to imbuing autonomous agents with the strategic foresight, social awareness, and adaptive negotiation skills necessary to operate safely and efficiently in the unstructured and unpredictable tapestry of urban traffic.

**Table: Comparison of approaches in 5.3 Strategic Navigation in Complex Urban Scenarios**

| Research Focus | Method/Model Name | Key Idea | Reference |
| :--- | :--- | :--- | :--- |
| Unsignalized Intersection Negotiation | Deep Q-Learning for Left-Turn Maneuver | Uses Deep Q-Learning to develop a decision-making framework for unprotected left turns, reducing collision rates. | [422] |
| Unsignalized Intersection Negotiation | POMDP with Monte Carlo Sampling | Frames intersection navigation as a POMDP and solves it using a Monte Carlo sampling method, outperforming heuristic strategies. | [423] |
| Unsignalized Intersection Negotiation | Hierarchical CTP-POMDP Approach | Proposes a hierarchical method combining a high-level path generator with a POMDP-based planner, inspired by human driving behavior for efficiency and safety. | [424] |
| Multi-Agent Interaction Modeling | Internal State Inference & Interactivity Estimation | Uses auxiliary tasks with spatio-temporal relational reasoning (GNNs) to infer internal states of surrounding agents and estimate the ego vehicle's influence on them. | [359] |
| Multi-Agent Interaction Modeling | MIDAS (RL with Attention) | Uses reinforcement learning with an attention mechanism to learn a policy that can affect the actions of other cars, adapting to different road geometries and driver behaviors. | [2] |
| Multi-Agent Interaction Modeling | GamePlan (Auction Mechanism) | Proposes a game-theoretic auction mechanism that assigns priority based on observable driving style, proving optimal for collision and deadlock avoidance. | [425] |
| Multi-Agent Interaction Modeling | Decentralized Game-Theoretic Planning | Limits game play to an agent's observational vicinity in a decentralized approach, making planning tractable for dense traffic like roundabouts. | [426] |
| Hierarchical & Structured Learning | Spatially & Seamlessly Hierarchical RL | Proposes a high-level policy that selects behavioral sub-policies and spatial regions of attention, with a low-level policy elaborating short-term goals. | [427] |
| Hierarchical & Structured Learning | DRL Integrated with Sampling-Based Motion Planning | Employs a trained DRL policy as a high-level behavior planner to populate an interface for sampling-based motion planners, bridging learning and traditional planning. | [428] |
| Hierarchical & Structured Learning | State Dropout-Based Curriculum RL | Presents a unique curriculum that progressively increases task difficulty (e.g., via state dropout) for faster training and better performance at intersections. | [429] |
| Hierarchical & Structured Learning | Reward-Driven Automated Curriculum Learning | Automates curriculum selection to handle uncertainties in the number and intentions of surrounding vehicles at unsignalized intersections. | [430] |
| Mixed Traffic & Partial Observability | Integrated Decision and Control with Dynamic Permutation State | Develops a dynamic permutation state representation within an integrated framework to process varying numbers and types of traffic participants (vehicles, cyclists, pedestrians). | [431] |
| Mixed Traffic & Partial Observability | Deep RL for Occluded Intersections | Explores learning active sensing behaviors using Deep RL to safely navigate intersections despite occlusions. | [432] |
| Mixed Traffic & Partial Observability | TrafficSim (Simulation of Realistic Behaviors) | Learns a joint policy from real-world data to generate socially consistent and diverse traffic scenarios for training and testing. | [433] |
| Safety & Robustness | Multi-task Safe RL with Social Attention | Adds a safety layer and social attention module to a multi-task RL framework to guarantee safe negotiation in dense traffic. | [434] |
| Safety & Robustness | GIN (Graph-based Interaction-aware Constraint Policy Optimization) | Proposes a policy optimization method with interaction-aware constraints, using GNNs to model social context and create a feedback loop between prediction and control. | [435] |
| Safety & Robustness | Guided Meta Reinforcement Learning | Trains a meta-policy for social vehicles to generate diverse behaviors, enhancing the robustness of the ego vehicle's policy to unseen agent behaviors. | [436] |


### 5.4 Fleet-Level and Network-Wide Optimization

The ultimate promise of autonomous driving extends beyond individual vehicle competence to the optimization of entire transportation ecosystems. Multi-agent deep reinforcement learning (MARL) provides the foundational framework for this leap, enabling the coordination of fleets of connected and autonomous vehicles (CAVs) to achieve network-wide objectives such as maximizing traffic throughput, minimizing fuel consumption, and ensuring systemic safety. This paradigm shift from ego-centric to system-centric optimization tackles problems where the optimal behavior of an individual is inextricably linked to the collective actions of many agents.

A canonical application is **cooperative platooning**, where CAVs form tightly coupled convoys to reduce aerodynamic drag, thereby improving fuel efficiency and road capacity. MARL frameworks are employed to learn decentralized control policies for acceleration and spacing that maintain string stability and safety. For instance, studies formulate Cooperative Adaptive Cruise Control (CACC) as a MARL problem, proposing fully decentralized frameworks with quantization-based communication to reduce overhead while maintaining efficacy [362]. The system-level reward often combines penalties for spacing error, acceleration jerk, and fuel consumption. Scalability is addressed through parameter sharing and local reward designs, as seen in frameworks for **scalable decentralized cooperative platooning** that utilize a "sharing and caring" communication protocol between predecessor and follower vehicles [437]. Beyond following, **cooperative lane-changing** in dense traffic, such as at highway weaving areas, is another critical target. Decentralized MARL controllers can learn policies that, when executed by multiple CAVs, yield superior traffic throughput and fuel efficiency compared to human drivers by reducing disruptive lane-change maneuvers [438]. The challenge here is designing a reward function that balances the ego vehicle's progress with the global smoothing of traffic flow, an approach taken by LCS-TF, which integrates local vehicle state with global traffic information from roadside units [439].

At the infrastructure level, **Traffic Signal Control (TSC)** represents a major MARL success story. The goal is to coordinate signals across a city to minimize average vehicle delay or queue length. Early MARL approaches treated each intersection as an independent agent, suffering from non-stationarity and poor coordination. Recent advances introduce sophisticated mechanisms for cooperation. **SocialLight** uses distributed actors with a locally centralized critic, allowing agents to estimate their individual marginal contribution to the neighborhood via counterfactual reasoning, improving scalability and performance [440]. To handle dynamic traffic patterns, **feudal MARL with adaptive network partition** dynamically groups intersections into regions based on real-time flow, using graph neural networks (GNNs) to inform the partitioning and manage cooperation within a hierarchical structure [441]. Similarly, **RegionLight** constrains partitions to star-network topologies and uses an adaptive branching dueling Q-network to decompose regional control into manageable joint sub-tasks [442]. Communication is pivotal in these systems. While some methods allow unrestricted messaging, others learn selective communication policies. One framework enables agents to learn "which" part of a message to send "to whom," significantly reducing channel usage while improving coordination [443].

**Autonomous Intersection Management (AIM)** is a signal-free paradigm for CAVs that requires high-precision coordination. Distributed MARL is attractive for its flexibility but faces challenges with convergence and safety due to multi-agent non-stationarity. Proposals like **D-HAL** replace traditional DRL with a hierarchical adversarial learning framework, using discriminators to evaluate immediate and final trajectory performance, which reportedly leads to safer and more efficient crossing [444]. Another hierarchical approach uses different RL levels with varying temporal scopes to balance long-term crossing goals with immediate collision avoidance [445]. These methods highlight the need for stable training paradigms in adversarial, multi-agent settings.

Underpinning all fleet-level coordination are two core technical challenges: **system-level reward design** and **scalable communication**. A global reward shared among all agents can lead to the "lazy agent" problem and credit assignment issues. Solutions include reward shaping with difference rewards, or value decomposition methods like QMIX. The **Shapley value** from cooperative game theory offers a principled way to reallocate the system's total reward to individual agents based on their marginal contributions, theoretically promoting stable and efficient cooperation if the game is convex [446]. For communication, bandwidth constraints are paramount. Approaches range from learning emergent, discrete communication protocols [363] to practical schemes like **quantization-based communication** that compresses shared data [362] and **regulated segment mixture** that reduces policy exchange overhead in fully distributed architectures [361]. The structure of communication is also optimized; some frameworks use **Graph Neural Networks (GNNs)** as a spatial-temporal encoder to effectively aggregate information from neighboring agents, enhancing cooperative policy learning [367] [366].

Finally, MARL enables **proactive network influence**, where automated vehicles are used not just to cooperate with each other, but to subtly guide surrounding human-driven traffic toward system-optimal patterns. This concept moves beyond prediction to strategic interaction. For example, autonomous vehicles can be trained to **influence human behavior** through local interactions to promote platooning and increase overall road capacity [447]. Similarly, policies can be learned to **affect the control actions of other cars** in urban driving scenarios using an attention mechanism to handle variable numbers of agents [2]. This line of research bridges MARL with human behavior modeling, aiming to create a harmonious and efficient mixed-autonomy traffic flow.

In summary, fleet-level and network-wide optimization via MARL represents the frontier of autonomous driving research, transforming the problem from one of perception and control to one of distributed intelligence and strategic coordination. Success hinges on innovative solutions for credit assignment, scalable and efficient communication, stable multi-agent learning algorithms, and reward structures that align individual actions with collective welfare. As connectivity becomes ubiquitous, these approaches hold the key to unlocking unprecedented levels of safety, efficiency, and sustainability in future transportation networks.

**Table: Comparison of approaches in 5.4 Fleet-Level and Network-Wide Optimization**

| Application / Domain | Method / Framework Name | Key Idea / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| Cooperative Adaptive Cruise Control (CACC) / Platooning | Communication-Efficient Decentralized MARL for CACC | Fully decentralized MARL framework with quantization-based communication to reduce overhead. | [362] |
| Cooperative Platooning | Scalable Decentralized Cooperative Platooning | Uses a "sharing and caring" communication protocol between predecessor and follower vehicles, with parameter sharing and local reward designs. | [437] |
| Cooperative Lane Changing | Decentralized Cooperative Lane Changing at Freeway Weaving Areas | Decentralized MARL controllers learn policies for multiple CAVs to improve throughput and fuel efficiency vs. human drivers. | [438] |
| Cooperative Lane Changing | LCS-TF | Integrates local vehicle state with global traffic information from roadside units (RSUs) in reward design. | [439] |
| Traffic Signal Control (TSC) | SocialLight | Uses distributed actors with a locally centralized critic and counterfactual reasoning to estimate individual marginal contribution. | [440] |
| Traffic Signal Control (TSC) | Feudal MARL with Adaptive Network Partition | Dynamically groups intersections into regions based on real-time flow using GNNs, within a hierarchical feudal structure. | [441] |
| Traffic Signal Control (TSC) | RegionLight | Constrains partitions to star-network topologies and uses an Adaptive Branching Dueling Q-network (ABDQ) to decompose regional control. | [442] |
| Traffic Signal Control (TSC) | MARL based on Representational Communication | Agents learn a communication policy dictating "which" part of a message to send "to whom", reducing channel usage. | [443] |
| Autonomous Intersection Management (AIM) | D-HAL | Distributed Hierarchical Adversarial Learning framework using discriminators to evaluate immediate and final trajectory performance. | [444] |
| Autonomous Intersection Management (AIM) | HARL | Hierarchical RL with different levels having varying temporal scopes to balance long-term goals with immediate collision avoidance. | [445] |
| Reward Design | Shapley Value-Based Reward Reallocation | Uses Shapley value from cooperative game theory to reallocate system reward based on agents' marginal contributions, promoting stable cooperation in convex games. | [446] |
| Communication | Networked MARL with Emergent Communication | Agents learn emergent, discrete communication protocols to coordinate. | [363] |
| Communication | RSM-MAPPO | Communication-efficient cooperative MARL via Regulated Segment Mixture in a fully distributed architecture. | [361] |
| Coordination & Policy Learning | Spatial-Temporal-Aware Safe MARL | Uses GNN-Transformer as a spatial-temporal encoder to aggregate information from neighboring agents. | [367] |
| Coordination & Policy Learning | Efficient CAV System with Multi-agent Graph RL | Employs graph reinforcement learning with attention mechanisms to capture agent interplay and boost cooperation. | [366] |
| Proactive Network Influence | Maximizing Road Capacity Using Influential Cars | Autonomous vehicles influence human behavior through local interactions to promote platooning and increase capacity. | [447] |
| Proactive Network Influence | MIDAS | RL-based method where an ego-agent learns to affect the control actions of other cars using an attention mechanism. | [2] |


### 5.5 Holistic and Integrated Task Formulations

A central ambition in autonomous driving research is the development of generalist agents capable of executing a wide array of tasks—from lane-keeping and intersection negotiation to complex interactive navigation—within a single, unified policy framework. This pursuit of holistic and integrated task formulations moves beyond isolated skill learning, aiming to create robust systems that can handle the long-horizon, multi-objective nature of real-world driving. A predominant architectural strategy to manage this complexity is Hierarchical Reinforcement Learning (HRL), which decomposes the driving problem into strategic, tactical, and operational layers. For instance, frameworks like the Diversity-Driven Extensible HRL (DEHRL) build multi-level hierarchies where a master policy selects among diverse, reusable sub-policies (skills), enabling efficient learning and transfer across tasks with highly abstract goals and primitive actions [344]. Similarly, the Imagination-Augmented HRL (IAHRL) integrates predictive "imagination" at the low-level, allowing policies to foresee consequences and enable safe, interactive behaviors in dynamic urban environments, with a high-level policy interpreting these imagined futures to infer interactions [352].

These hierarchical approaches are often coupled with modular designs that combine learned components with classical planning for stability and interpretability. The SG-RL framework exemplifies this by using a geometric planner (Simple Subgoal Graphs) to generate optimal abstract subgoal sequences, which are then executed by an RL-based motion planner (Least-Squares Policy Iteration) to produce kinematically feasible trajectories [448]. This decoupling allows the system to benefit from the global optimality of graph search and the adaptability of RL to uncertainties. Another modular paradigm is presented in Planning-oriented Autonomous Driving, which argues for a task cascade optimized for the ultimate planning objective. The Unified Autonomous Driving (UniAD) framework integrates perception, prediction, and planning modules within one network, with tasks communicating through unified queries to ensure all components contribute coherently to the driving plan [449]. This represents a significant shift from standalone models towards an integrated, planning-centric ecosystem.

A critical challenge in training such generalist policies is designing effective benchmarks and reward structures that encourage desired behaviors without catastrophic failures. Benchmarks like MetaDrive provide highly compositional simulation environments capable of generating an infinite number of diverse driving scenarios, from procedural generation to real-data import, enabling rigorous testing of generalization [450]. Similarly, Driver Dojo offers a configurable benchmark with randomized scenario generators to assess how well RL policies generalize across variations in road layout, traffic, and driver behavior [451]. These tools are essential for moving beyond overfitted, scenario-specific policies. Reward design in these complex settings is equally nuanced. The CIRL framework, for example, alleviates exploration challenges in large continuous action spaces by constraining exploration within a region informed by human demonstrations, while also specializing reward designs (e.g., for steering angle) based on different high-level control signals like "turn left" or "follow" [26]. This hybrid approach of reward shaping guided by imitation learning is a powerful method for achieving complex, goal-directed behavior.

The trade-off between specialization and generalization is a fundamental tension in policy design. Highly specialized policies may excel in specific conditions but fail catastrophically in novel situations. Conversely, overly general policies may lack the nuanced skill required for precise maneuvers. Several works address this by learning diverse repertoires of skills or policies that can be composed or selected as needed. The Diverse Policy Optimization (DPO) method models policies in structured action spaces as energy-based models and uses a GFlowNet as an efficient sampler to discover a wide array of diverse strategies, which can then be deployed or composed for robustness [452]. In a multi-agent context, ALMA learns a hierarchical policy where a high-level policy allocates agents to specific subtasks (e.g., handling different objects or zones), while low-level policies focus on their assigned subtask, promoting reuse and composition of skills across different task configurations [453]. This compositional approach is key to scalability.

Furthermore, the integration of large pre-trained models and language guidance is emerging as a powerful tool for creating more adaptable and instruction-following agents. The Read to Play (R2-Play) framework treats visual-based RL as a long-horizon vision task and incorporates multimodal game instructions (text and visual trajectories) into a Decision Transformer, significantly boosting its multitasking and generalization capabilities [454]. This points towards a future where driving policies can understand and execute high-level natural language commands, moving closer to true generalist agents. Similarly, Planning to Practice (PTP) uses a pre-trained conditional subgoal generator in latent space to propose intermediate goals for a low-level policy, facilitating efficient online fine-tuning for long-horizon tasks unseen in the offline data [455].

Ultimately, the goal of holistic formulations is to achieve robust performance in the face of the "long-tail" of rare but critical driving scenarios. As noted in an analysis of current planners, neither purely rule-based nor learning-based methods may safely navigate complex edge-case scenarios, suggesting a need for hybrid approaches that combine the reasoning of foundation models with the safety of classical planning [456]. The success of these integrated frameworks hinges on their ability to seamlessly blend strategic reasoning, tactical negotiation, and precise motion control, while maintaining safety and adaptability across an open-ended set of driving environments and conditions.

**Table: Comparison of approaches in 5.5 Holistic and Integrated Task Formulations**

| Method/Model Name | Core Idea / Approach | Key Components / Techniques | Reference |
| :--- | :--- | :--- | :--- |
| Diversity-Driven Extensible HRL (DEHRL) | Builds multi-level HRL frameworks for tasks with highly abstract goals and primitive actions, driven by a diversity assumption for sub-policies. | Extensible, levelwise learning; diversity-driven sub-policy discovery; master policy selecting among diverse, reusable sub-policies. | [344] |
| Imagination-Augmented HRL (IAHRL) | Integrates predictive "imagination" at the low-level to foresee consequences, enabling safe, interactive behaviors in dynamic urban environments. | Low-level policies imagine safe behaviors; high-level policy interprets imagined futures to infer interactions; permutation-invariant attention mechanism. | [352] |
| SG-RL (Subgoal Graphs-Reinforcement Learning) | Hierarchical path planning combining geometric planning (SSG) for optimal abstract subgoal sequences with RL (LSPI) for kinematically feasible motion planning. | Simple Subgoal Graphs (SSG) for high-level path planning; Least-Squares Policy Iteration (LSPI) for low-level motion planning; decouples global planning from local adaptation. | [448] |
| Unified Autonomous Driving (UniAD) | Planning-centric framework integrating perception, prediction, and planning modules within one network, optimized for the ultimate planning objective. | Full-stack task integration (perception, prediction, planning); tasks communicate via unified queries; complementary feature abstractions for agent interaction. | [449] |
| CIRL (Controllable Imitative Reinforcement Learning) | Hybrid approach combining RL exploration constrained by human demonstrations with specialized reward designs for different high-level control signals. | Exploration constrained within region from human demonstrations; specialized reward functions (e.g., for steering) per control signal (follow, turn left, etc.); built on DDPG. | [26] |
| Diverse Policy Optimization (DPO) | Models policies in structured action spaces as energy-based models and uses GFlowNet as an efficient sampler to discover diverse strategies. | Energy-based model (EBM) for policies; GFlowNet for diverse policy sampling; joint optimization framework for policy improvement and diversity. | [452] |
| ALMA (Hierarchical Learning for Composite Multi-Agent Tasks) | Learns a hierarchical policy where a high-level policy allocates agents to specific subtasks, promoting reuse and composition of skills. | High-level subtask allocation policy; low-level agent policies for assigned subtasks; structured inductive bias for composite tasks. | [453] |
| Read to Play (R2-Play) | Incorporates multimodal game instructions (text and visual trajectories) into a Decision Transformer, treating RL as a long-horizon vision task. | Decision Transformer backbone; multimodal instruction tuning (text + visual trajectories); "read-to-play" capability for generalization. | [454] |
| Planning to Practice (PTP) | Uses a pre-trained conditional subgoal generator in latent space to propose intermediate goals, facilitating efficient online fine-tuning for long-horizon tasks. | Hierarchical decomposition; conditional subgoal generator in latent space; hybrid offline pre-training and online fine-tuning. | [455] |


## 6 Critical Challenges: Safety, Robustness, and Evaluation

This section delves into the major hurdles for real-world deployment. It discusses safety assurance via formal methods, shielding, and control barrier functions; robustness to distribution shifts and adversarial conditions; sim-to-real transfer and domain adaptation techniques; and methodologies for rigorous offline evaluation and closed-loop benchmarking.

### 6.1 Formal Safety Assurance and Verification

The deployment of deep reinforcement learning (RL) and imitation learning (IL) in autonomous driving hinges on the ability to provide formal, verifiable safety guarantees. These learning-based policies, while powerful, are inherently opaque and can exhibit unpredictable, hazardous behaviors, especially when encountering out-of-distribution scenarios. To bridge this gap between high performance and safety-critical assurance, a suite of formal methods has been developed to act as protective layers around learned controllers. These methods, including runtime assurance (RTA) systems, shielding, and control barrier functions (CBFs), provide correctness-by-construction guarantees, actively mitigating risks during both the training and deployment phases.

Runtime Assurance (RTA) represents a foundational architecture where a safety-critical meta-controller monitors and, if necessary, overrides the actions of an untrusted primary controller (e.g., a neural network policy) to ensure system safety. The core challenge is designing RTA logic that is both safe and minimally invasive to preserve the performance of the primary controller. Frameworks like RTAEval have been proposed to systematically evaluate different RTA logics across various agents and scenarios [116]. Comparative studies categorize RTA approaches based on explicit vs. implicit monitoring and switching vs. optimization-based interventions, validating their feasibility in applications like spacecraft docking [118]. The design of optimal RTA can itself be framed as a learning problem, where reinforcement learning is used to create a meta-controller that maximizes the use of the experimental controller while guaranteeing safety, outperforming traditional reachability-based methods in complex 3D scenarios [457]. Furthermore, the integration of RTA into certification frameworks, such as MIL-HDBK-516C for aerospace, demonstrates how assurance arguments based on advanced RTA like Active Set Invariance Filtering (ASIF) can support compliance for neural network control systems [458].

Shielding is a closely related technique that synthesizes a correct-by-construction reactive system (the shield) to monitor and rectify unsafe actions proposed by a learning agent. Traditional shielding relies on a known model of the environment and a formal safety specification, often in Linear Temporal Logic (LTL). However, scaling shielding to complex, multi-agent, or partially unknown environments is non-trivial. To address this, **Model-based Dynamic Shielding (MBDS)** synthesizes distributive shields that can dynamically split, merge, and recompute based on agents' states, enabling safe and efficient Multi-Agent RL (MARL) without excessive coordination overhead [459]. For settings where a high-fidelity model or safety abstraction is unavailable, **approximate shielding** methods leverage learned world models. For instance, latent shielding verifies policy roll-outs in the latent space of a learned dynamics model, improving stability and reducing safety violations in environments like Atari games [460]. Similarly, **Probabilistic Logic Shields** integrate logical safety constraints as differentiable functions via probabilistic logic programming, enabling seamless integration with policy gradient algorithms for continuous control [461]. A significant challenge in real-world systems like autonomous driving is signal delay. **Delay-resilient shields** are synthesized to guarantee safety under worst-case assumptions on input signal delays, with heuristics designed to minimize future interference, a critical advancement for realistic deployment [462]. In black-box environments, **dynamic shielding** combines shielding with automata learning, iteratively constructing an approximate system model from agent traces to suppress unsafe explorations during training [463].

Control Barrier Functions (CBFs) have emerged as a powerful mathematical tool for constructing safety filters. A valid CBF defines a safe set of states (a superlevel set of the function) and provides a constraint—typically enforced via a quadratic program (QP)—that renders this set forward invariant. The primary challenge is synthesizing a valid and non-conservative CBF, especially for systems with high relative degree, actuation limits, and complex, non-convex safe sets. Recent research has focused on **learning CBFs from data**. One approach refines a handcrafted, conservative CBF using a prioritized data sampling strategy to recover a larger portion of the true safe set more efficiently [464]. Other works propose frameworks for the **simultaneous synthesis and verification of neural CBFs**, embedding branch-and-bound verification directly into the training loop to certify the network over the continuous state space [465]. For stochastic settings, algorithms exist to synthesize formally verified **Stochastic Neural CBFs (SNCBFs)** with guarantees across the entire state space from finite data [466]. To improve generalization, **differentiable safety-critical control** frameworks embed CBF-QP optimization as a differentiable layer, allowing the safety parameters to adapt to new environments [467]. Furthermore, CBFs can be combined with control Lyapunov functions (CLFs) in frameworks like **Barrier-Lyapunov Actor-Critic (BLAC)** to jointly enforce safety and stability constraints [164].

A critical advancement is the development of **Backup Control Barrier Functions (BCBFs)** and **predictive safety filters**, which address the conservatism of traditional CBFs by allowing temporary excursions from the safe set, provided a backup controller can guarantee recovery within a finite time horizon. This is essential for autonomous driving maneuvers that inherently require approaching the boundaries of safety (e.g., navigating tight spaces). Frameworks like **Reinforcement Learning Backup Shield (RLBUS)** integrate BCBFs with RL to learn better backup policies, enlarging the forward invariant set while guaranteeing zero training-time safety violations [468]. Similarly, **predictive control barrier functions** use a soft-constrained predictive control problem to provide a recovery mechanism, ensuring recursive feasibility and asymptotic stability of the safe set [469]. The connection between reachability analysis and CBFs is also exploited; for example, Hamilton-Jacobi (HJ) reach-avoid differential dynamic programming can be used in a receding-horizon framework to construct smooth, implicit CBFs with infinite-time safety guarantees [470]. Conversely, reachability analysis can be used to refine and improve candidate CBFs, as in the **refineCBF** framework, which uses dynamic programming to iteratively obtain provably safer CBFs [471].

Integrating these formal safety mechanisms with the learning process itself is a key research direction. Safe RL algorithms increasingly incorporate safety filters not just at deployment but during training to prevent catastrophic failures. Some approaches provide **probabilistic safety guarantees** under model uncertainty by using Gaussian Processes (GPs) to learn the dynamics, with event-triggered data collection ensuring recursive feasibility of the safety filter [472]. Others, like **Confidence-Based Safety Filters**, use probabilistic dynamics models to determine a safe backup policy and minimally adjust a nominal RL policy at each time step [166]. The **Projection-to-State Safety (PSSf)** concept quantifies how learning can improve safety guarantees by reducing uncertainty in the CBF's time derivative, enabling episodic learning to strengthen safety certificates [473]. For black-box systems where gradients are unavailable, novel methods like **SABLAS** redesign the loss function to enable gradient-based learning of safe policies and barrier certificates directly from interactions with the non-differentiable system [474].

Finally, the quest for **zero training-time violations** represents the ultimate goal for real-world robot learning. Algorithms like **Co-trained Barrier Certificate for Safe RL (CRABS)** iteratively learn barrier certificates, dynamics models, and policies through adversarial training, aiming to achieve high reward with zero safety violations during training, even from a trivial safe initial policy [475]. This highlights a paradigm shift from constraining the expected cumulative cost (as in Constrained MDPs) to explicitly enforcing hard, reachability-based safety constraints through barrier functions, which has been shown to significantly outperform CMDP-based methods in enforcing safety rates [476].

In summary, formal safety assurance for autonomous driving policies is rapidly evolving from external add-on filters to deeply integrated, learnable components. The synergy between formal methods (CBFs, shielding, reachability) and machine learning (RL, IL, dynamics learning) is creating a new generation of controllers that are both high-performing and verifiably safe. Future directions include improving the scalability and real-time performance of these methods for high-dimensional perception-action loops, handling multi-agent interactions with formal guarantees, and creating unified frameworks for end-to-end safe policy learning and certification.

**Table: Comparison of approaches in 6.1 Formal Safety Assurance and Verification**

| Method Category | Core Idea / Mechanism | Key Advantages / Innovations | Reference |
| :--- | :--- | :--- | :--- |
| Runtime Assurance (RTA) | A meta-controller monitors and overrides an untrusted primary controller to ensure safety. | Frameworks like RTAEval enable systematic evaluation; RL can be used to design optimal, minimally invasive meta-controllers; can be integrated into certification frameworks (e.g., MIL-HDBK-516C). | [116], [457], [458] |
| Shielding | Synthesizes a correct-by-construction reactive system (shield) to monitor and rectify unsafe actions from a learning agent. | Model-based Dynamic Shielding (MBDS) enables efficient, distributive shields for MARL; approximate shielding (e.g., latent shielding) works without high-fidelity models; delay-resilient shields handle real-world signal delays; dynamic shielding learns models in black-box environments. | [459], [460], [462], [463] |
| Control Barrier Functions (CBFs) | Mathematical functions defining a safe set, enforced via constraints (e.g., QP) to render it forward invariant. | Can be learned from data (e.g., refining handcrafted CBFs); frameworks for simultaneous synthesis and verification of neural CBFs; differentiable CBF layers enable generalization; can be combined with CLFs for stability (e.g., BLAC). | [464], [465], [467], [164] |
| Backup CBFs / Predictive Safety Filters | Extend CBFs by allowing temporary safety excursions if a backup controller guarantees recovery within a horizon. | Reduces conservatism of traditional CBFs; essential for complex maneuvers (e.g., tight spaces); RL can learn better backup policies (e.g., RLBUS); predictive formulations ensure recursive feasibility. | [468], [469] |
| Integrated Safe RL / Learning-based Safety | Integrates formal safety mechanisms (filters, CBFs) directly into the RL training process. | Provides probabilistic safety guarantees under model uncertainty (e.g., with GPs); confidence-based filters adjust nominal policies minimally; Projection-to-State Safety (PSSf) quantifies safety improvement via learning; methods like SABLAS learn safe policies for non-differentiable black-box systems. | [472], [166], [473], [474] |
| Zero Violation Learning | Aims to achieve safe RL with zero safety violations during the training process. | Algorithms like CRABS co-train barrier certificates, models, and policies via adversarial training to guarantee zero training-time violations from a trivial safe initial policy. | [475] |


### 6.2 Robustness to Distribution Shifts and Uncertainty

A fundamental challenge in deploying autonomous driving policies trained via deep reinforcement learning (RL) or imitation learning (IL) is their vulnerability to distribution shifts. These shifts occur when the statistical properties of the deployment environment differ from those of the training data, whether sourced from simulation or a limited set of real-world operational design domains (ODDs). Such discrepancies, known as covariate shifts or domain gaps, can lead to severe performance degradation and safety violations. Ensuring robustness against these shifts and the inherent uncertainty of real-world dynamics is therefore paramount. This subsection examines a spectrum of techniques designed to fortify driving policies, spanning domain adaptation, test-time adaptation, and formal frameworks for uncertainty quantification.

A primary line of defense is **Domain Adaptation (DA)**, which explicitly aims to align the feature distributions of the source (training) and target (deployment) domains. Traditional approaches often align second-order statistics, but as noted in [477], covariance matrices reside on a Riemannian manifold, making Euclidean alignment suboptimal. Using a theoretically sound geodesic distance on this manifold leads to more effective feature alignment. For autonomous driving, where source data may be synthetic, methods like domain randomization are a form of proactive DA, training on a wide distribution of simulated parameters to encourage robustness. However, more structured approaches are needed for known, specific shifts. The concept of **Distributionally Robust Optimization (DRO)** provides a strong theoretical foundation, where the policy is optimized for the worst-case performance within an uncertainty set of possible distributions. For instance, [478] encourages robustness over class-conditional distributions within Wasserstein uncertainty sets, a principle that can be extended to state-transition models in RL. Similarly, [479] connects transition kernel disturbances to state disturbances via the Wasserstein distance, enabling the design of risk-aware robust RL algorithms. Another perspective is offered by [480], which reduces differences in risk across multiple training domains (e.g., different weather conditions in simulation) to improve extrapolation to more extreme, unseen test-time shifts.

When the target domain is encountered only at deployment, **Test-Time Adaptation (TTA)** becomes crucial. TTA methods continuously adapt a pre-trained model using unlabeled data from the test stream. A common approach is entropy minimization on model predictions, but this can lead to overconfident errors and catastrophic forgetting of source knowledge. To address this, [481] proposes an active sample selection criterion to identify reliable, non-redundant test samples and uses a Fisher regularizer to constrain important model parameters. This idea is extended in [482], which separately exploits model and data uncertainty to avoid overconfident predictions, using divergence between sub-networks and a min-max entropy regularizer. For the highly dynamic, non-i.i.d. streams typical of driving, [483] introduces a resilient batch normalization with soft alignment and an entropy-driven memory bank to ensure stable adaptation. Furthermore, [484] enhances self-training with a memory buffer and dynamic adaptation based on the detected intensity of domain shift, showing improved robustness on autonomous driving benchmarks like CLAD-C and SHIFT. A significant challenge in TTA is hyperparameter tuning without target labels; [485] critically benchmarks validation criteria for DA and TTA, highlighting the over-optimism in literature when improper validation using test labels is employed and advocating for rigorous, label-free validation protocols.

Beyond point predictions, **quantifying uncertainty** is essential for safe fallback and informed decision-making. **Conformal Prediction (CP)** offers a distribution-free, model-agnostic framework for constructing prediction sets with guaranteed coverage under exchangeability. Its extension to covariate shift scenarios is vital for autonomous driving. [486] proposes Weighted Conformal Predictive Systems (WCPS), which use likelihood ratios between training and test covariate distributions to maintain calibration. Similarly, [487] constructs Probably Approximately Correct (PAC) prediction sets that satisfy coverage guarantees even under given or estimated importance weights encoding the shift. For sequential decision-making, [488] extends CP to provide joint prediction regions for multi-agent trajectories under policy-induced distribution shifts, which is directly relevant for interactive driving scenarios. To incorporate domain knowledge, [489] uses a physics-informed structural causal model (PI-SCM) to reduce the upper bound on coverage loss across distribution shifts, leveraging the invariance of physical laws.

Finally, robustness must be considered during the **policy evaluation and learning phase itself**. Off-policy evaluation (OPE) methods used to assess policies from historical data can be misled by distribution shifts. [490] introduces a framework, ROPE, which incorporates domain knowledge (e.g., which environmental aspects may plausibly change) to estimate worst-case policy utility under realistic shifts, resulting in less pessimistic and more useful evaluations. In the robust RL paradigm, [491] analyzes the fundamental hardness of learning with interactive data collection under support shift and proposes an algorithm with sample complexity guarantees under a vanishing minimal value assumption. For model-based RL, which is common in simulation-heavy autonomous driving pipelines, [492] proposes a method that introduces adaptive sampling of model-generated data to provide safety guarantees without unreliable uncertainty estimation, addressing distribution shift in offline settings.

In summary, achieving robustness for autonomous driving policies necessitates a multi-faceted approach. Proactive methods like distributionally robust training and domain generalization build inherent resilience. Reactive, efficient test-time adaptation mechanisms allow for continuous calibration to the encountered environment. Underpinning both, rigorous uncertainty quantification frameworks like conformal prediction provide safety assurances with statistical guarantees. The integration of these techniques—grounded in robust optimization, adaptive inference, and formal uncertainty quantification—is critical for developing autonomous driving systems that can reliably and safely generalize across the infinite variability of the real world.

**Table: Comparison of approaches in 6.2 Robustness to Distribution Shifts and Uncertainty**

| Category | Method Name | Key Idea / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| Domain Adaptation (DA) | Correlation Alignment via Riemannian Metric | Aligns feature distributions by using a theoretically sound geodesic distance on the Riemannian manifold of covariance matrices, rather than suboptimal Euclidean alignment. | [477] |
| Domain Adaptation (DA) | Distributionally Robust Optimization (DRO) / Wasserstein Distributional Robustness | Optimizes for worst-case performance within an uncertainty set of possible distributions. Encourages robustness over class-conditional distributions within Wasserstein uncertainty sets. | [478] |
| Robust Reinforcement Learning | Robust RL with Wasserstein Constraint | Connects transition kernel disturbances to state disturbances via the Wasserstein distance, enabling the design of risk-aware robust RL algorithms. | [479] |
| Domain Generalization | Risk Extrapolation (REx) | Reduces differences in risk across multiple training domains to improve extrapolation to more extreme, unseen test-time shifts. | [480] |
| Test-Time Adaptation (TTA) | Efficient Test-Time Model Adaptation without Forgetting | Uses an active sample selection criterion to identify reliable, non-redundant test samples and a Fisher regularizer to constrain important model parameters, preventing catastrophic forgetting. | [481] |
| Test-Time Adaptation (TTA) | Uncertainty-Calibrated Test-Time Adaptation without Forgetting | Separately exploits model and data uncertainty to avoid overconfident predictions, using divergence between sub-networks and a min-max entropy regularizer. | [482] |
| Test-Time Adaptation (TTA) | Resilient Practical Test-Time Adaptation | Introduces resilient batch normalization with soft alignment and an entropy-driven memory bank to ensure stable adaptation to non-i.i.d. test streams. | [483] |
| Test-Time Adaptation (TTA) | AR-TTA | Enhances self-training with a memory buffer and dynamic adaptation based on the detected intensity of domain shift. | [484] |
| Validation for DA/TTA | Better Practices for Domain Adaptation | Critically benchmarks validation criteria for DA and TTA, advocating for rigorous, label-free validation protocols to avoid over-optimism from improper test label use. | [485] |
| Uncertainty Quantification | Weighted Conformal Predictive Systems (WCPS) | Extends conformal prediction to covariate shift by using likelihood ratios between training and test covariate distributions to maintain calibration. | [486] |
| Uncertainty Quantification | PAC Prediction Sets Under Covariate Shift | Constructs Probably Approximately Correct (PAC) prediction sets that satisfy coverage guarantees under given or estimated importance weights encoding the shift. | [487] |
| Uncertainty Quantification | Conformal Off-Policy Prediction for Multi-Agent Systems | Extends conformal prediction to provide joint prediction regions for multi-agent trajectories under policy-induced distribution shifts. | [488] |
| Uncertainty Quantification | Robust Conformal Prediction via Physics-Informed SCM | Uses a physics-informed structural causal model (PI-SCM) to reduce the upper bound on coverage loss across distribution shifts, leveraging the invariance of physical laws. | [489] |
| Policy Evaluation | Robust Off-Policy Evaluation (ROPE) | Incorporates domain knowledge (e.g., which environmental aspects may plausibly change) to estimate worst-case policy utility under realistic shifts, resulting in less pessimistic evaluations. | [490] |
| Robust Reinforcement Learning | Distributionally Robust RL with Interactive Data Collection | Analyzes the fundamental hardness of learning with interactive data collection under support shift and proposes an algorithm with sample complexity guarantees under a vanishing minimal value assumption. | [491] |
| Offline Model-Based RL | DOMAIN | Introduces adaptive sampling of model-generated data to provide safety guarantees without unreliable uncertainty estimation, addressing distribution shift in offline settings. | [492] |


### 6.3 Adversarial Robustness and Stress Testing

The deployment of deep reinforcement learning (RL) and imitation learning (IL) policies in autonomous vehicles (AVs) introduces profound security and robustness challenges. These learning-based systems, particularly their perception and control modules, are vulnerable to adversarial attacks—maliciously crafted inputs designed to induce catastrophic failures. Ensuring robustness against such attacks is not merely an academic exercise but a prerequisite for safe real-world operation. This necessitates a two-pronged approach: developing defensive mechanisms to harden policies and employing proactive stress-testing methodologies to discover and mitigate vulnerabilities before deployment.

A primary line of defense is **adversarial training**, where policies are exposed to adversarial examples during the learning process. The canonical approach formulates a minimax optimization problem, where the policy (defender) is trained to minimize loss against an adversary that perturbs observations to maximize that loss. For instance, **Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations** [493] formalizes this as a State-Adversarial Markov Decision Process (SA-MDP) and introduces a theoretically principled policy regularization method applicable to algorithms like PPO and DDPG, significantly improving robustness against strong white-box attacks. Similarly, **Better Safe Than Sorry: Preventing Delusive Adversaries with Adversarial Training** [494] demonstrates that adversarial training can recover test accuracy degraded by delusive attacks on training data by preventing the model from overly relying on non-robust features. However, traditional adversarial training often assumes a uniform attack strategy, which may not reflect realistic threat models. **LAS-AT: Adversarial Training with Learnable Attack Strategy** [495] addresses this by introducing a framework where a strategy network learns to automatically produce adaptive attack strategies throughout training, dynamically challenging the target network and leading to superior robustness. Beyond perturbing inputs, **Robustifying Reinforcement Learning Agents via Action Space Adversarial Training** [496] shows that DRL agents susceptible to actuator attacks can be robustified through adversarial training in the action space, making the system inherently robust by design.

While adversarial training enhances robustness, it is often computationally expensive and may not generalize to unseen attack vectors. Therefore, complementary **detection and repair mechanisms** that operate at test-time are crucial. These methods aim to identify adversarial inputs and either reject them or transform them into benign ones. **Defending against Adversarial Attack towards Deep Neural Networks via Collaborative Multi-task Training** [497] exemplifies a hybrid defense, using encoded label pairs for adversarial training against black-box attacks and constructing a separate detector to identify and reject high-confidence adversarial examples that bypass the primary defense. For a more generic detection approach, **Revisiting Model's Uncertainty and Confidences for Adversarial Example Detection** [498] proposes an unsupervised ensemble detection mechanism (SFAD) that leverages model uncertainty and processes feature maps to generate new confidence metrics, showing strong performance against black- and gray-box attacks. **Test-time Detection and Repair of Adversarial Samples via Masked Autoencoder** (DRAM) [499] offers a novel detection-and-repair schema using Masked Autoencoder (MAE) losses to both detect adversarial samples via a statistical test and calculate reversal vectors to repair them, all without adapting the model weights, making it suitable for frozen models.

Proactive discovery of failures is equally critical, moving beyond static defenses to systematic **stress testing and falsification**. The goal is to actively search for scenarios—"corner cases" or adversarial policies—that cause the AV system to violate safety specifications. **Falsification-Based Robust Adversarial Reinforcement Learning** (FRARL) [500] integrates temporal logic falsification directly into adversarial learning. Instead of handcrafting an adversary's reward, it uses falsification methods to find disturbances (e.g., initial conditions, input sequences) that cause safety specification violations, thereby training a more robust policy against those failure modes. This connects to broader **search-based testing and red teaming** paradigms. **Behaviour-Diverse Automatic Penetration Testing: A Curiosity-Driven Multi-Objective Deep Reinforcement Learning Approach** [501] frames penetration testing as a Multi-Objective RL problem, seeking diverse attack strategies to provide comprehensive security assessments. In the context of AI systems, **Red Teaming with Mind Reading: White-Box Adversarial Policies Against RL Agents** [502] demonstrates that white-box access to a target agent's internal state allows for crafting more effective adversarial policies than black-box methods, highlighting the need to test under varying attacker knowledge assumptions. The concept is extended to automated, scalable evaluation with frameworks like **AART: AI-Assisted Red-Teaming with Diverse Data Generation** [503] and **MART: Improving LLM Safety with Multi-round Automatic Red-Teaming** [504], which use AI to generate diverse, adversarial evaluation datasets and iteratively improve safety through alternating attack generation and policy fine-tuning cycles. For autonomous driving specifically, **Targeted Attack on Deep RL-based Autonomous Driving with Learned Visual Patterns** [505] investigates a practical threat model where adversarial patterns placed on physical objects (like road signs or other cars) can hijack a pre-trained policy, necessitating stress tests that include such physically realizable attacks.

Ultimately, the adversarial landscape is a dynamic game between attackers and defenders. **Game Theory for Adversarial Attacks and Defenses** [506] provides a foundational perspective, modeling the competition where each player optimizes their strategy based on predicted opponent actions. Defenses must therefore be adaptive and evaluated against strategic, adaptive attackers. **Beyond Worst-case Attacks: Robust RL with Adaptive Defense via Non-dominated Policies** [124] argues that focusing solely on worst-case robustness can degrade nominal performance. Instead, it proposes refining the policy class to a set of "non-dominated" policies, enabling efficient test-time adaptation to various attack scenarios, balancing robustness and performance. This aligns with insights from **Are Adversarial Examples Created Equal? A Learnable Weighted Minimax Risk for Robustness under Non-uniform Attacks** [507], which emphasizes defending against non-uniform, targeted attacks by learning importance weights for different adversarial examples during training.

In conclusion, securing deep RL/IL driving policies demands an integrated strategy combining robust training, runtime monitoring, and proactive, exhaustive testing. Adversarial training and regularization build inherent resilience, while detection and repair mechanisms offer last-line defenses. However, the cornerstone of a safety case must be rigorous, automated stress-testing through falsification, red teaming, and search-based methods that relentlessly probe the policy's boundaries. Only through such a comprehensive and adversarial-aware development cycle can we hope to achieve the levels of robustness required for trustworthy autonomous deployment.

**Table: Comparison of approaches in 6.3 Adversarial Robustness and Stress Testing**

| Method Category | Specific Method / Framework | Key Idea / Mechanism | Reference |
| :--- | :--- | :--- | :--- |
| Adversarial Training | Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations | Formalizes State-Adversarial MDP (SA-MDP) and introduces a theoretically principled policy regularization method for algorithms like PPO and DDPG. | [493] |
| Adversarial Training | Better Safe Than Sorry: Preventing Delusive Adversaries with Adversarial Training | Uses adversarial training to recover test accuracy degraded by delusive attacks by preventing over-reliance on non-robust features. | [494] |
| Adversarial Training | LAS-AT: Adversarial Training with Learnable Attack Strategy | Introduces a framework where a strategy network learns to automatically produce adaptive attack strategies throughout training. | [495] |
| Adversarial Training | Robustifying Reinforcement Learning Agents via Action Space Adversarial Training | Robustifies DRL agents susceptible to actuator attacks through adversarial training in the action space. | [496] |
| Detection & Repair | Defending against Adversarial Attack towards Deep Neural Networks via Collaborative Multi-task Training | Uses encoded label pairs for adversarial training against black-box attacks and constructs a separate detector to identify/reject high-confidence adversarial examples. | [497] |
| Detection & Repair | Revisiting Model's Uncertainty and Confidences for Adversarial Example Detection | Proposes an unsupervised ensemble detection mechanism (SFAD) that leverages model uncertainty and processes feature maps to generate new confidence metrics. | [498] |
| Detection & Repair | Test-time Detection and Repair of Adversarial Samples via Masked Autoencoder (DRAM) | Uses Masked Autoencoder (MAE) losses to detect adversarial samples via a statistical test and calculate reversal vectors to repair them, without adapting model weights. | [499] |
| Stress Testing & Falsification | Falsification-Based Robust Adversarial Reinforcement Learning (FRARL) | Integrates temporal logic falsification into adversarial learning to find disturbances that cause safety specification violations, training a more robust policy. | [500] |
| Stress Testing & Red Teaming | Behaviour-Diverse Automatic Penetration Testing: A Curiosity-Driven Multi-Objective Deep Reinforcement Learning Approach | Frames penetration testing as a Multi-Objective RL problem to find diverse attack strategies for comprehensive security assessments. | [501] |
| Stress Testing & Red Teaming | Red Teaming with Mind Reading: White-Box Adversarial Policies Against RL Agents | Demonstrates that white-box access to a target agent's internal state allows for crafting more effective adversarial policies than black-box methods. | [502] |
| Stress Testing & Red Teaming | AART: AI-Assisted Red-Teaming with Diverse Data Generation | Uses AI to generate diverse, adversarial evaluation datasets for new LLM-powered applications. | [503] |
| Stress Testing & Red Teaming | MART: Improving LLM Safety with Multi-round Automatic Red-Teaming | Uses alternating attack generation and policy fine-tuning cycles to iteratively improve LLM safety. | [504] |
| Stress Testing & Red Teaming | Targeted Attack on Deep RL-based Autonomous Driving with Learned Visual Patterns | Investigates adversarial patterns placed on physical objects to hijack a pre-trained policy, necessitating stress tests for physically realizable attacks. | [505] |
| Game-Theoretic & Adaptive Defense | Game Theory for Adversarial Attacks and Defenses | Provides a foundational perspective, modeling the competition where each player optimizes their strategy based on predicted opponent actions. | [506] |
| Game-Theoretic & Adaptive Defense | Beyond Worst-case Attacks: Robust RL with Adaptive Defense via Non-dominated Policies | Proposes refining the policy class to a set of "non-dominated" policies for efficient test-time adaptation to various attack scenarios. | [124] |
| Game-Theoretic & Adaptive Defense | Are Adversarial Examples Created Equal? A Learnable Weighted Minimax Risk for Robustness under Non-uniform Attacks | Emphasizes defending against non-uniform, targeted attacks by learning importance weights for different adversarial examples during training. | [507] |


### 6.4 Sim-to-Real Transfer and Domain Adaptation

The ability to train policies in simulation before deployment is a cornerstone of modern autonomous driving research, offering a scalable, safe, and cost-effective alternative to prohibitively expensive real-world data collection. However, the inevitable discrepancies between simulation and reality—the "reality gap"—pose a significant barrier to the direct transfer of learned behaviors, potentially leading to catastrophic failures. Bridging this gap through effective sim-to-real transfer and domain adaptation is therefore a critical challenge for ensuring the robustness and safety of learned driving policies.

A dominant and empirically successful strategy is **Domain Randomization (DR)**, which trains policies under a wide distribution of randomized simulation parameters (e.g., lighting, textures, vehicle dynamics, friction). The core hypothesis is that a policy robust to this broad variability will generalize to the unseen real world. As demonstrated in [84], randomizing dynamics parameters during training can produce policies that adapt to real-world dynamics without any fine-tuning. However, the success of DR is highly sensitive to the design of the randomization distribution. Naïve, overly broad randomization can impede learning or lead to overly conservative policies, while insufficient randomization fails to cover the target domain. This has spurred research into more sophisticated, adaptive approaches. Methods like **Bayesian Domain Randomization (BayRn)** [508] and **AdaptSim** [509] move beyond fixed heuristics. They treat the simulator's parameter distribution as an optimization variable, using limited real-world data to adapt it, either to match real-world dynamics or, more effectively, to directly maximize task performance in reality. Similarly, **Adversarial Domain Randomization** [510] frames the search for simulation parameters as a game, generating challenging, adversarial scenarios that are most informative for the learner, thereby improving data efficiency.

Complementary to DR is **System Identification (Sys-ID)**, which aims to precisely calibrate the simulator to match the dynamics of a specific target platform or environment. Traditional Sys-ID can be data-hungry and ill-posed. Recent learning-based approaches seek to automate and improve this process. For instance, **DROID** [511] uses a single human demonstration to identify the distribution of dynamics parameters that minimizes the reality gap. **COMPASS** [512] introduces a differentiable causal discovery framework to automatically identify which environment parameters are causally linked to the sim-to-real performance gap, pruning the search space and improving interpretability. However, a fundamental limitation of perfect Sys-ID is that it may be impossible or unnecessary to match all aspects of reality; the goal should be task-aligned adaptation. This insight underpins frameworks like **Universal Policy with Embedding System Identification (UPESI)** [513], which performs implicit Sys-ID in a learned embedding space to enable a single universal policy to adapt optimally to various dynamics.

The concept of **Digital Twins (DTs)** represents a paradigm shift, moving from one-off transfer to continuous alignment. A DT is a high-fidelity, executable virtual counterpart of a physical system that is continuously updated with real-world data. As surveyed in [108], DTs enable a closed-loop where policies can be safely tested, optimized, and validated against a constantly evolving model of reality. For autonomous driving, this allows for testing in rare "corner-case" scenarios synthesized in the twin and for adapting controllers to changing conditions, as explored in [514]. The DT framework naturally integrates with **Domain Adaptation** techniques at the perception level. Since visual discrepancies are a major component of the reality gap, methods like **AptSim2Real** [515] and **Randomized-to-Canonical Adaptation Networks (RCAN)** [516] learn to translate synthetic images into a canonical or real-like style, enabling vision-based policies trained on adapted images to work with real camera feeds.

A crucial, often counter-intuitive, consideration is **simulation fidelity**. The instinct is to minimize the reality gap by building ever more high-fidelity simulators. However, research suggests this is not always optimal. High-fidelity simulators are computationally expensive, limiting the scale of training, and may introduce their own hard-to-model inaccuracies that policies can overfit to. As argued in [85], a lower-fidelity simulator that is fast and captures the task-relevant dynamics can sometimes yield better transfer performance. The key is to inject the right kind of randomness or to learn simple, data-driven models that capture essential real-world variability, as seen in [517], which leverages the inherent stochasticity of real-time physics engines as a natural form of randomization.

Ultimately, the **quantification and mitigation of the sim2real performance gap** is essential for safe deployment. This involves developing better metrics and protocols for assessing transfer readiness. **Simulation-based Policy Optimization with Transferability Assessment (SPOTA)** [518] uses an estimator of simulation optimization bias to decide when to stop training. **Validate on Sim, Detect on Real (VSDR)** [519] proposes a policy selection method that combines in-simulation validation with out-of-distribution detection scores on a small set of real data, reducing the need for exhaustive real-world policy rollouts. Furthermore, **hybrid offline-and-online** approaches like **H2O** [520] dynamically balance learning from limited real-world offline data and a potentially imperfect simulator, penalizing Q-learning on simulated transitions with large dynamics gaps.

In conclusion, overcoming the sim-to-real challenge in autonomous driving requires a multifaceted toolkit. No single technique is sufficient; instead, the most promising path forward lies in the integrated application of adaptive domain randomization, causal system identification, digital twin frameworks for continuous learning, and task-aware fidelity design, all underpinned by rigorous transferability assessment. This holistic approach is vital for developing driving policies that are not only high-performing in simulation but also robustly safe and reliable in the unpredictable physical world.

**Table: Comparison of approaches in 6.4 Sim-to-Real Transfer and Domain Adaptation**

| Method / Concept | Core Idea / Strategy | Key Advantages / Insights | Limitations / Challenges | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Domain Randomization (DR) | Trains policies under a wide distribution of randomized simulation parameters (e.g., lighting, textures, dynamics). | Can produce policies that generalize to the real world without fine-tuning; simple and effective. | Success is highly sensitive to the design of the randomization distribution; naïve randomization can impede learning or lead to overly conservative policies. | [84] |
| Bayesian Domain Randomization (BayRn) | Treats the simulator's parameter distribution as an optimization variable, using limited real-world data to adapt it to maximize task performance. | More data-efficient than fixed DR; adapts the randomization distribution based on real-world feedback. | Requires some real-world data for the optimization process; computational overhead for the Bayesian optimization loop. | [508] |
| AdaptSim | Task-driven adaptation that optimizes simulation parameters to directly maximize task performance in the target (real) environment. | Focuses on task-relevant adaptation rather than general dynamics matching; can be more efficient and effective for specific tasks. | Requires an iterative adaptation process with real-world rollouts; meta-learning the adaptation policy adds complexity. | [509] |
| Adversarial Domain Randomization | Frames the search for simulation parameters as a game, generating challenging, adversarial scenarios informative for the learner. | Improves data efficiency by generating informative samples; can surface corner cases. | Requires training an adversarial policy; may be computationally intensive. | [510] |
| System Identification (Sys-ID) | Aims to precisely calibrate the simulator to match the dynamics of a specific target platform or environment. | Can lead to high-fidelity simulation for a specific setup if accurate. | Can be data-hungry and ill-posed; perfect matching of all reality aspects may be impossible or unnecessary for the task. | General concept, not a single paper. |
| DROID | Uses a single human demonstration to identify the distribution of dynamics parameters that minimizes the reality gap. | Data-efficient (single demonstration); optimizes DR ranges based on real-world data. | Relies on the quality and representativeness of the single demonstration; may not capture full parameter distribution. | [511] |
| COMPASS | Differentiable causal discovery framework to identify which environment parameters are causally linked to the sim-to-real performance gap. | Automates parameter tuning; prunes search space and improves interpretability via causal graphs. | Requires learning a differentiable mapping and causal structure; complexity may scale with number of parameters. | [512] |
| Universal Policy with Embedding System Identification (UPESI) | Performs implicit system identification in a learned embedding space to enable a single universal policy to adapt to various dynamics. | Combines benefits of DR and adaptive policies; more efficient than explicit Sys-ID. | Requires training a dynamics model and performing Bayesian optimization in embedding space. | [513] |
| Digital Twins (DTs) | A high-fidelity, executable virtual counterpart continuously updated with real-world data for closed-loop testing and adaptation. | Enables safe testing of corner cases and continuous adaptation to changing real-world conditions. | Requires significant effort to build and maintain a high-fidelity model; relies on continuous data streaming. | [108], [514] |
| AptSim2Real | Approximately-paired sim-to-real image translation that exploits loosely resembling scenes between sim and real. | Does not require perfect pixel-wise pairing; shown to improve over unpaired translation methods. | Still requires loosely corresponding scene pairs; performance depends on the quality of scene generation. | [515] |
| Randomized-to-Canonical Adaptation Networks (RCAN) | Translates randomized rendered images into canonical sim images, enabling real images to be translated for policy transfer. | Enables zero-shot sim-to-real transfer for vision-based policies without real-world data for adaptation. | Requires training the translation network; may not handle all real-world visual variations. | [516] |
| Simulation Fidelity Consideration | Argues that lower-fidelity, fast simulators capturing task-relevant dynamics can sometimes yield better transfer than high-fidelity ones. | Faster simulation enables larger-scale training; avoids overfitting to inaccurate high-fidelity details. | Requires careful design to ensure essential dynamics are captured; counter-intuitive approach. | [85] |
| Intrinsic Stochasticity of Real-Time Simulation (RT-IS) | Leverages the inherent stochasticity of off-the-shelf real-time physics engines as a natural form of randomization. | Less heuristic than conventional DR; not task-dependent; improves robustness to model imprecision. | Dependent on the specific properties of the physics engine's real-time solver. | [517] |
| Simulation-based Policy Optimization with Transferability Assessment (SPOTA) | Uses an estimator of Simulation Optimization Bias (SOB) to decide when to stop training in randomized simulators. | Provides a quantifiable stopping criterion to prevent overfitting to the simulation distribution. | Requires defining and estimating the SOB, which may be non-trivial. | [518] |
| Validate on Sim, Detect on Real (VSDR) | Policy selection method combining in-simulation validation with out-of-distribution detection scores on a small real dataset. | Reduces need for exhaustive real-world policy rollouts for model selection. | Relies on the accuracy of the OOD detection method and its correlation with policy performance. | [519] |
| H2O (Hybrid Offline-and-Online RL) | Dynamics-aware framework that balances learning from limited real-world offline data and an imperfect simulator, penalizing Q-learning on simulated transitions with large dynamics gaps. | Leverages strengths of both offline and online RL; adaptively trusts the simulator based on estimated dynamics gap. | Requires estimating the dynamics gap, which adds complexity; needs some real-world offline data. | [520] |


### 6.5 Evaluation Methodologies and Benchmarking

Rigorous evaluation is paramount for the deployment of learning-based autonomous driving (AD) policies, moving beyond simple performance metrics to encompass safety, robustness, and real-world readiness. A cornerstone of modern evaluation is **scenario-based testing**, which structures the infinite space of possible driving situations into manageable, semantically meaningful units for systematic assessment. This paradigm is widely recognized as essential for verification and validation, as it focuses testing effort on relevant and potentially critical situations [521]. Ontologies provide the formal scaffolding for these scenarios, defining entities, relations, and dynamic aspects to ensure test scenarios are both meaningful and reproducible [521]. The process typically operates at different levels of abstraction: *functional scenarios* describe a class of situations (e.g., cut-in on a highway), *logical scenarios* parameterize them (e.g., ranges for relative speed, distance), and *concrete scenarios* are fully instantiated test cases. A significant challenge is the efficient generation and selection of these concrete scenarios from the vast parameter space of logical scenarios.

To ground testing in reality, methodologies for **test synthesis from real-world data** have become crucial. The goal is to mine naturalistic driving data to extract common and, more importantly, challenging scenarios. Unsupervised learning techniques, such as clustering trajectory data from datasets like *highD* or *inD*, can automatically discover recurring scenario patterns without heavy reliance on predefined expert rules, potentially revealing unforeseen critical situations [522] [523]. Once identified, these scenarios must be parameterized and reconstructed in simulation. Frameworks exist to automatically extract lane-change or intersection scenarios and encode them into standardized formats like OpenSCENARIO for use in simulators such as CARLA, creating a direct pipeline from real-world observation to simulated test [524] [525]. This enables the creation of large, realistic test libraries. However, naturalistic data is inherently skewed towards safe, nominal driving, making safety-critical events extremely rare. Therefore, methods to **intelligently generate adversarial or edge-case scenarios** are necessary to probe the boundaries of an AD system's capabilities.

This leads to the domain of **black-box safety validation**, where the system under test (SUT) is treated as an opaque component, and the environment or other agents are controlled to stress it. Reinforcement Learning (RL) has emerged as a powerful tool for this adversarial search. RL agents can be trained to learn policies for background vehicles that maximize some notion of "failure" or "criticality" for the ego vehicle. For instance, frameworks like STARS use multi-agent RL with a Hazard Arbitration Reward to specifically generate autonomous-vehicle-responsible hazardous scenarios, ensuring the discovered flaws are relevant to the policy's vulnerabilities [526]. Similarly, other approaches frame the problem as a falsification task, using RL to find scenario parameters that cause the SUT to violate a safety requirement, such as those defined by Responsibility-Sensitive Safety (RSS) [527] [528]. The core advantage is sample efficiency; instead of random Monte Carlo sampling, RL actively explores the parameter space towards high-risk regions. Advanced techniques like adaptive stress testing (AST) formalize this as a Markov decision process solved with deep RL to discover crash scenarios [94]. To accelerate this search further, **active learning and metamodeling** techniques are employed. Methods like HiddenGems use active learning to efficiently map the compliance boundary of a scenario—the frontier between safe and unsafe parameter regions—with far fewer simulations than exhaustive sweeps [529]. Gaussian Processes and other probabilistic metamodels can predict system performance across the scenario space, guiding the selection of the most informative test cases [530] [531].

The development of **closed-loop benchmarks and unified platforms** is critical for fair and reproducible comparison of different AD policies and testing algorithms. Platforms like SafeBench integrate diverse safety-critical scenarios, multiple scenario generation algorithms, and various AD models with different sensor inputs into a unified benchmarking environment [532]. This allows for apples-to-apples comparisons and reveals trade-offs, such as an agent's performance in benign versus adversarial settings. The move towards photorealistic, closed-loop evaluation is also evident in tools like NeuroNCAP, which uses Neural Radiance Fields (NeRF) to create high-fidelity, reconfigurable simulations from real-world data for testing against safety protocols like Euro NCAP [533]. These benchmarks shift evaluation from open-loop prediction accuracy to closed-loop interaction competence, which is essential for assessing real-world viability.

Underpinning all these methodologies are **metrics for safety performance boundary identification and probabilistic risk estimation**. Simple binary pass/fail outcomes are insufficient for statistical validation. Frameworks distinguish between prescriptive rules (e.g., "must not cross solid line") and risk-based rules (e.g., "must not have a collision"), where the latter requires aggregation over many tests to make a probabilistic safety claim [534]. The concept of a **counterfactual safety margin** quantifies risk by simulating the minimum behavioral deviation of other agents needed to cause a collision, providing a continuous measure of how close the ego vehicle's behavior was to a failure [535]. Similarly, **probabilistic risk indices** extend models like RSS to quantify the likelihood of a collision when safe distances are violated, moving from a binary safe/unsafe judgment to a graduated risk spectrum [536]. For overall system assessment, **statistical validation techniques** like Conservative Bayesian Inference (CBI) are proposed to combine limited operational test data with prior knowledge (e.g., from simulation or design) to support rigorous reliability claims without optimistic bias [537]. Finally, evaluation must consider **scenario coverage and criticality**. Metrics are needed to assess not just if a test fails, but how thoroughly the space of possible scenarios has been exercised. Tree-based formal classifiers can measure coverage of scenario sets in recorded test drives [538]. Furthermore, methods to describe the "tactical challenge" of a scenario—such as the minimum required lane changes and their difficulty—provide interpretable insights beyond a single metric value, helping engineers select a diverse and challenging test suite [539]. Together, these evolving methodologies form a multifaceted toolkit for rigorously evaluating the safety and robustness of deep RL and IL driving policies, bridging the gap from simulation to credible real-world deployment assurances.

**Table: Comparison of approaches in 6.5 Evaluation Methodologies and Benchmarking**

| Method Category | Key Idea / Approach | Specific Techniques / Frameworks Mentioned | Reference(s) |
| :--- | :--- | :--- | :--- |
| **Scenario-based Testing & Ontologies** | Structures infinite driving situations into manageable, semantically meaningful units (functional, logical, concrete scenarios) using formal ontologies to ensure meaningful and reproducible tests. | Ontologies for entity/relation definition; Abstraction levels (functional, logical, concrete scenarios). | [521] |
| **Test Synthesis from Real-World Data** | Mines naturalistic driving data to extract common and challenging scenarios, creating a pipeline from real-world observation to simulated test. | Unsupervised clustering (e.g., K-Means, hierarchical clustering, DBSCAN) on datasets like *highD*, *inD*; Automatic extraction and encoding into OpenSCENARIO for simulators like CARLA. | [522], [523], [524], [525] |
| **Black-box Safety Validation / Adversarial Generation** | Treats the System Under Test (SUT) as opaque and uses controlled agents to stress it, often framing the problem as a falsification task to find failure-inducing scenarios. | Reinforcement Learning (RL) with adversarial reward functions (e.g., Hazard Arbitration Reward in STARS); Adaptive Stress Testing (AST) formalized as an MDP; Falsification using metrics like Responsibility-Sensitive Safety (RSS). | [526], [527], [528], [94] |
| **Active Learning & Metamodeling** | Uses efficient sampling and probabilistic models to map the performance boundary (safe/unsafe regions) in the scenario parameter space, guiding informative test case selection. | Active learning (e.g., HiddenGems); Probabilistic metamodels like Gaussian Processes (GP) and Bayesian Neural Networks (BNN) for performance prediction. | [529], [530], [531] |
| **Closed-loop Benchmarks & Unified Platforms** | Provides integrated environments for fair, reproducible, and photorealistic closed-loop evaluation of different AD policies and testing algorithms. | Platforms like SafeBench; Photorealistic simulation using Neural Radiance Fields (NeRF) in tools like NeuroNCAP for protocol-based testing (e.g., Euro NCAP). | [532], [533] |
| **Safety Metrics & Risk Estimation** | Moves beyond binary pass/fail to probabilistic risk assessment and statistical validation, quantifying how close behavior is to failure and estimating failure likelihood. | Counterfactual safety margin; Probabilistic risk indices extending RSS; Statistical validation techniques like Conservative Bayesian Inference (CBI); Scenario coverage analysis via formal classifiers. | [534], [535], [536], [537], [538], [539] |


## 7 Emerging Trends, Open Frontiers, and Conclusion

This section outlines future research directions, including causal and explainable AI, lifelong and meta-learning, ethical decision-making, human-AI collaboration, and the ecosystem of tools and datasets. It concludes by synthesizing the evolution of the field, summarizing key insights, and highlighting the most pressing open problems on the path to robust and trustworthy autonomous driving agents.

### 7.1 The Rise of Foundation Models and Knowledge-Driven Autonomy

A fundamental paradigm shift is underway in autonomous driving (AD), moving beyond purely data-driven, pattern-matching approaches towards systems endowed with human-like reasoning, common sense, and open-world understanding. This shift is propelled by the advent of foundation models, particularly Large Language Models (LLMs) and Vision-Language Models (VLMs). These models, pre-trained on vast, diverse corpora, encapsulate a rich repository of world knowledge, semantic relationships, and reasoning capabilities. Their integration into the AD stack promises to address core limitations of traditional Deep Reinforcement Learning (RL) and Imitation Learning (IL) pipelines, such as poor generalization to long-tail scenarios, lack of interpretability, and the inability to follow complex natural language instructions or leverage experiential knowledge [540].

The core proposition is to treat the driving agent not merely as a policy optimizing a reward function or mimicking demonstrations, but as a **cognitive agent** that can reason about its environment. Frameworks like **Agent-Driver** and **DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models** exemplify this. They re-architect the traditional pipeline by employing an LLM as a central reasoning engine. This engine accesses a tool library (for perception, prediction, and control), a cognitive memory of driving rules and common sense, and performs chain-of-thought reasoning to interpret scenes, plan tasks, and reflect on decisions [541] [542]. This approach enables the system to handle ambiguous situations by explicitly reasoning about the intentions of other road users, physical constraints, and social norms, moving closer to the ideal of systems that **Drive Like a Human** [374].

A critical advantage of this knowledge-driven paradigm is **inherent interpretability**. Unlike black-box RL/IL policies, LLM-based agents can generate natural language explanations for their decisions. For instance, **DriveGPT4** and **DriveMLM** are end-to-end systems that not only predict control signals but also provide reasoning for vehicle actions and answer user queries about the driving scene [372] [373]. This aligns with the broader need for **Faithful Explainers** in complex AI systems, ensuring that the provided explanations accurately reflect the model's decision-making process [543]. Benchmarks like **Reason2Drive** are being developed specifically to evaluate such chain-based reasoning capabilities in driving contexts, providing datasets with annotated reasoning chains spanning perception, prediction, and planning [378].

Furthermore, foundation models enable **open-vocabulary instruction following and personalization**. Systems like **Talk2Drive** and **Receive, Reason, and React: Drive as You Say with Large Language Models in Autonomous Vehicles** demonstrate that LLMs can process verbal commands from passengers (e.g., "follow that red car, but keep a safe distance" or "drive more smoothly") and translate them into contextualized driving policies. This facilitates a human-centric collaboration where the vehicle adapts to personalized preferences for safety, efficiency, and comfort [544] [15]. The LLM acts as an interface that **Human-Centric Autonomous Systems** can use to infer system requirements directly from natural language, enhancing user trust and adaptability [545].

The evolution is also marked by a push towards **grounded, embodied understanding**. Pure LLMs lack a connection to the 3D physical world. Research is thus rapidly advancing into **Multimodal Large Language Models (MLLMs)** and **3D-aware foundation models** that fuse visual, linguistic, and spatial reasoning. Works like **LEO (An Embodied Generalist Agent in 3D World)**, **3D-LLM: Injecting the 3D World into Large Language Models**, and **3D-VLA: A 3D Vision-Language-Action Generative World Model** aim to build agents that perceive, reason, plan, and act within 3D environments [546] [380] [547]. For driving, this means moving from 2D image captioning to 3D spatial reasoning about object permanence, occlusion, and affordances. The **Embodied Understanding of Driving Scenarios** framework (ELM) explicitly incorporates space-aware pre-training and time-aware reasoning to handle the large spatial and temporal spans characteristic of driving [548].

This trend also intersects with the development of **generative world models**. The paradigm of **Reasoning with Language Model is Planning with World Model** (RAP) repurposes the LLM itself as a world model to simulate future states and perform strategic planning via algorithms like Monte Carlo Tree Search [549]. Similarly, other research explores how **Language Models Meet World Models** through fine-tuning on embodied experiences gained in simulators, thereby teaching LMs physical commonsense like object permanence and planning [550]. These approaches address a key shortcoming of traditional model-free RL: the lack of an internal model for counterfactual reasoning and long-horizon prediction.

However, significant challenges remain on the path to knowledge-driven autonomy. **Evaluation** is paramount; new benchmarks like **CODA-LM** and **EgoPlan-Bench** are emerging to quantitatively assess LVLMs on corner-case reasoning and embodied task planning in realistic scenarios [551] [552]. There are also concerns about **semantic grounding**—ensuring the model's linguistic outputs are correctly anchored to visual entities in the scene—and **reliability**, as LLMs are prone to hallucination [384] [553]. Furthermore, the **ethical frameworks** of LLMs, as explored in studies like **The Moral Machine Experiment on Large Language Models**, may not fully align with nuanced human moral judgments, necessitating careful alignment for safety-critical decisions [554].

In conclusion, the rise of foundation models is catalyzing a transformative leap from data-driven reactivity to knowledge-driven cognition in autonomous driving. By embedding common sense, enabling interpretable reasoning, and facilitating natural interaction, LLMs and VLMs are poised to overcome the generalization and explainability barriers of conventional Deep RL and IL. The future lies in hybrid architectures that combine the robust, low-level control learned through RL/IL with the high-level, contextual intelligence and planning capabilities of foundation models, ultimately creating safer, more adaptable, and more trustworthy autonomous vehicles [49] [555].

**Table: Comparison of approaches in 7.1 The Rise of Foundation Models and Knowledge-Driven Autonomy**

| Method/Model Name | Key Idea/Contribution | Reference |
| :--- | :--- | :--- |
| Agent-Driver | Employs an LLM as a central reasoning engine with a tool library and cognitive memory for chain-of-thought reasoning, task planning, and self-reflection. | [541] |
| DiLu | A knowledge-driven framework combining Reasoning and Reflection modules, enabling decision-making based on common-sense knowledge and continuous evolution. | [542] |
| DriveGPT4 | An interpretable end-to-end autonomous driving system based on MLLMs that processes video and text to explain actions, answer questions, and predict control signals. | [372] |
| DriveMLM | An MLLM-based framework aligned with behavioral planning states for close-loop driving, providing decisions and explanations. | [373] |
| Talk2Drive | An LLM-based framework that processes verbal commands from passengers to generate contextualized driving policies for personalization. | [544] |
| Receive, Reason, and React | A framework leveraging LLMs for decision-making, enabling verbal command interpretation and personalized driving behavior adaptation. | [15] |
| LEO | An embodied multi-modal, multi-task generalist agent trained for 3D vision-language alignment and action instruction tuning for 3D world interaction. | [546] |
| 3D-LLM | Injects 3D world representations (point clouds) into LLMs to enable a diverse set of 3D-related tasks like captioning, QA, and grounding. | [380] |
| 3D-VLA | A 3D Vision-Language-Action generative world model that links 3D perception, reasoning, and action through a generative world model. | [547] |
| RAP (Reasoning via Planning) | Repurposes the LLM as both a world model and a reasoning agent, using planning algorithms (e.g., MCTS) for strategic exploration in reasoning tasks. | [549] |
| Language Models Meet World Models | Enhances LMs by fine-tuning them with embodied experiences from simulators to teach physical commonsense and planning. | [550] |
| ELM (Embodied Language Model) | A framework for embodied understanding of driving scenes with space-aware pre-training and time-aware reasoning for large spatial/temporal spans. | [548] |
| xLLM | A generative explanation framework with an iterative optimization process to improve the faithfulness of natural language explanations for LLM decisions. | [543] |


### 7.2 Towards Causal, Explainable, and Trustworthy AI

The deployment of autonomous vehicles (AVs) in open-world environments represents one of the most challenging applications of artificial intelligence, demanding not only exceptional performance but also rigorous safety, transparency, and accountability. The inherent opacity of deep reinforcement and imitation learning models, often referred to as "black boxes," poses a significant barrier to public trust and regulatory approval. Consequently, the development of causal, explainable, and trustworthy AI is not merely an optional enhancement but a foundational requirement for the safe and ethical integration of AVs into society. This subsection explores the convergence of Explainable AI (XAI) and causal inference as critical pathways to build interpretable, robust, and ethically aligned driving policies.

The primary objective of XAI in autonomous driving is to make the decision-making process of AI models comprehensible to a diverse set of stakeholders, including engineers, regulators, end-users, and the general public. As highlighted in [556], XAI is fundamental to meeting core requirements for data transparency, model auditability, and clear agency. However, a fundamental challenge lies in the ambiguity of what constitutes an effective "explanation." As argued in [557], an explanation's utility is defined by its functional role, the knowledge state of the user, and the availability of necessary information. A one-size-fits-all approach is insufficient. For instance, a safety engineer may require a detailed, causal account of a near-miss event to debug the system, while a passenger might benefit from a simple, teleological explanation like "the car slowed down to maintain a safe distance from the cyclist ahead," a form of reasoning people naturally attribute to both humans and machines as shown in [558]. This underscores the need for **user-centric XAI** design, moving beyond algorithm-centered techniques to incorporate socio-organizational context, a concept explored as Social Transparency in [559].

Technical approaches to XAI can be broadly categorized into *intrinsic* (interpretable-by-design) and *post-hoc* methods. Intrinsic interpretability involves designing models whose decision logic is inherently transparent, such as decision trees or rule-based systems integrated within a broader learning framework. The survey [125] details progress in this area for RL. However, the high complexity of driving environments often necessitates the use of powerful, opaque deep networks. For these, post-hoc explanation techniques are employed. Saliency maps and feature attribution methods (e.g., variants of SHAP or LIME) highlight which input pixels or features (e.g., a pedestrian, a traffic sign) were most influential for a particular decision. Frameworks like [560] demonstrate model-agnostic approaches for generating such explanations. Yet, these methods have limitations; they can be unstable, fail to capture true causal relationships, and as noted in [561], may provide marginal or even detrimental utility if not carefully evaluated within a human decision-making loop.

A more advanced and promising direction is the generation of **counterfactual explanations**. These explanations answer "what-if" questions: "What minimal change to the scene would have led to a different decision?" For example, "If the oncoming car had been 2 meters further away, a lane change would have been deemed safe." Such explanations are intuitively aligned with human reasoning and can offer actionable recourse. However, generating feasible and causally consistent counterfactuals is non-trivial. Simple perturbation-based methods may suggest physically impossible scenarios. Recent work, such as [562] and [563], integrates causal graphs and domain knowledge to ensure the proposed changes respect real-world constraints. A significant concern, however, is the **disagreement problem**: different counterfactual algorithms can generate vastly different explanations for the same instance, which a malicious actor could exploit to "fairwash" an unfair model or obscure its true rationale, as empirically demonstrated in [564]. This calls for standardization and robustness in explanation generation.

The pursuit of true robustness and trustworthiness necessitates moving beyond correlation to **causality**. Causal inference allows models to understand the underlying data-generating processes and mechanisms. In driving, this means distinguishing between spurious correlations (e.g., braking when seeing a red billboard because it was often co-located with stop signs in training) and true cause-effect relationships (e.g., braking due to a pedestrian's trajectory). Causal models can improve robustness to distributional shifts and adversarial perturbations by focusing on invariant causal features. They also enable better **sim-to-real transfer** by modeling the fundamental dynamics of the driving environment rather than its superficial visual features. Furthermore, causal reasoning is indispensable for ethical decision-making. In a complex, unavoidable accident scenario, an AV's choice must be justifiable based on a causal model of outcomes, not just statistical patterns. Frameworks that embed ethical principles into a causal decision-making structure, as alluded to in works like [101], are essential for aligning AI with societal values.

Building trustworthy AI ultimately requires a holistic framework that integrates technical explainability with **validation, governance, and human-AI collaboration**. As emphasized in [565], explainability and high performance are not mutually exclusive but are co-requisites for trustworthy systems. Effective evaluation is critical; metrics must go beyond algorithmic fidelity to assess the explanation's impact on human understanding, appropriate trust calibration, and decision-making quality, as discussed in [566] and [567]. Regulatory perspectives, such as those examined in [568], highlight a potential disparity between the explainability desired by regulators and that provided by developers, indicating a need for clear, context-dependent standards. Finally, the human must remain in the loop, not just as a passive recipient of explanations but as an active collaborator. Systems should support **interactive explanation**, allowing users to query, explore alternative scenarios, and provide feedback, fostering a collaborative human-AI relationship as envisioned in [569] and [570].

In conclusion, the path towards widespread adoption of RL/IL-based autonomous driving is inextricably linked to advances in causal and explainable AI. The field must evolve from producing post-hoc justifications for black-box models to engineering intrinsically more interpretable and causally-aware learning systems. This requires a multidisciplinary effort, combining robust XAI algorithms, causal discovery methods, rigorous human-centered evaluation, and ethical governance frameworks. By making AI decisions transparent, auditable, and aligned with human reasoning, we can build the foundation of trust necessary for autonomous vehicles to become a safe and integral part of our future transportation ecosystem.

### 7.3 Lifelong, Continual, and Meta-Learning

A core aspiration for autonomous driving is the development of agents that, like human drivers, can learn and adapt continuously throughout their operational lifetime. This requires overcoming the fundamental challenge of *catastrophic forgetting*, where learning new skills or adapting to new environments causes the abrupt degradation of previously acquired knowledge. The paradigms of lifelong learning, continual learning, and meta-learning offer promising pathways to create such adaptive and scalable driving intelligence, enabling systems to handle the long-tailed distribution of rare but critical driving events.

**Lifelong and Continual Learning for Non-Stationary Roads.** The real-world driving environment is inherently non-stationary, with continuous changes in geography, traffic rules, vehicle models, and agent behaviors. A model trained on a fixed dataset from one city may fail catastrophically when deployed in another, a phenomenon exacerbated by distribution shifts. Continual learning (CL) directly addresses this by enabling sequential learning from streams of tasks or data without forgetting. In trajectory prediction, for instance, a model must adapt to new intersection layouts or driving cultures without losing accuracy on previously learned scenarios. Approaches like *Generative Negative Replay for Continual Learning* [571] demonstrate that generated data from old tasks can serve as effective negative examples to learn new classes, a strategy applicable to distinguishing novel dangerous maneuvers from safe ones. Similarly, *Lifelong Learning of Spatiotemporal Representations with Dual-Memory Recurrent Self-Organization* [572] proposes a neuro-inspired architecture with separate episodic and semantic memories, where the episodic memory learns fine-grained instances and replays trajectories to consolidate knowledge, showing strong performance on continuous object recognition benchmarks relevant to perception. For direct policy learning, *Continual Interactive Behavior Learning With Traffic Divergence Measurement* [573] introduces a dynamic gradient scenario memory that measures traffic divergence to selectively retain experiences, effectively mitigating forgetting across different driving locations. The challenge extends to visual domains, as seen in *Distribution-Aware Continual Test-Time Adaptation for Semantic Segmentation* [574], which dynamically selects and updates small sets of domain-specific and task-relevant parameters to enable efficient and practical long-term adaptation for perception systems.

**Meta-Learning for Fast Adaptation and Generalization.** While continual learning focuses on sequential knowledge accumulation, meta-learning (or "learning to learn") aims to equip an agent with the innate ability to adapt rapidly to new tasks with minimal data. This is crucial for autonomous vehicles encountering entirely novel scenarios (e.g., unseen road layouts, extreme weather) where extensive retraining is impossible. Meta-learning frameworks typically involve a two-loop process: an outer loop learns a good initialization or prior across a distribution of tasks, and an inner loop quickly fine-tunes this prior on a new task. *Expanding the Deployment Envelope of Behavior Prediction via Adaptive Meta-Learning* [575] leverages Bayesian regression to augment prediction models with an adaptive layer, enabling efficient domain transfer to new cities via offline fine-tuning or online adaptation. In a control setting, *Meta Learning MPC using Finite-Dimensional Gaussian Process Approximations* [576] meta-trains a dynamics model using data from related tasks, allowing for fast online Bayesian adaptation to new road conditions, such as varying friction in autonomous racing. The *Online Meta-Learning* [577] framework merges online and meta-learning to capture continual lifelong learning, providing algorithms with sub-linear regret guarantees for changing environments. This is directly applicable to driving, where an agent must both leverage prior experience and adapt online to dynamic traffic. *Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning* [578] showcases this principle in navigation, where an agent learns a self-supervised interaction loss that allows it to quickly adapt to novel indoor scenes, a concept transferable to unfamiliar road networks.

**Curriculum Learning and Strategic Experience Management.** Mimicking the progressive learning of humans, curriculum learning strategically sequences training scenarios from simple to complex, which can dramatically improve learning speed, stability, and final performance. In autonomous driving, this is vital for safely learning high-risk maneuvers and for tackling the long-tail problem where catastrophic events are rare. *Safe Reinforcement Learning via Curriculum Induction* [579] draws inspiration from human teaching by employing an automated "monitor" that intervenes with reset controllers when the agent acts dangerously. This teacher itself learns a curriculum—a policy for choosing interventions—to optimize the agent's final performance, ensuring safety *during* training. A more autonomous approach is presented in *Continual Driving Policy Optimization with Closed-Loop Individualized Curricula* [580], which frames curriculum generation as a closed-loop process. It evaluates an AV's failure probability in a library of historical scenarios and then tailors an individualized training curriculum by sampling more challenging cases, thereby maximizing the utility of existing data for iterative policy improvement. Furthermore, *Rethinking Closed-loop Training for Autonomous Driving* [30] highlights that the design of the training benchmark itself—the scaling and composition of traffic scenarios—is a critical form of curriculum that significantly impacts agent success. Their proposed method, Trajectory Value Learning (TRAVL), exploits cheaply generated imagined data for efficient learning, which can be seen as a form of internally generated, progressive experience.

**Integration and Open Challenges.** The ultimate goal is the seamless integration of these paradigms into a cohesive lifelong learning system. An agent would use meta-learning to acquire a prior for fast adaptation, employ continual learning techniques to accumulate and retain knowledge over its lifetime, and leverage curriculum learning to safely and efficiently master increasingly complex skills. Promising steps include *Online Fast Adaptation and Knowledge Accumulation (OSAKA)* [581], which proposes a scenario demanding both quick solving of new tasks and fast remembering, and *Continual-MAML* as a baseline combining online adaptation with meta-learning. However, significant challenges remain. The *trade-off between stability (retaining old knowledge) and plasticity (learning new things)* is delicate, especially under strict safety constraints. *Evaluating* such lifelong agents is non-trivial, as highlighted in *Rigorous Agent Evaluation: An Adversarial Approach to Uncover Catastrophic Failures* [582], which argues that standard evaluation can miss rare failures and proposes adversarial methods to stress-test agents. Furthermore, most current research operates in simplified settings. Bridging these techniques to the *high-dimensional, multi-agent, and safety-critical* domain of real-world autonomous driving, as discussed in *Exiting the Simulation: The Road to Robust and Resilient Autonomous Vehicles at Scale* [9], requires advances in simulation-to-reality transfer and the development of comprehensive benchmarks like *MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning* [450] and *Continual World: A Robotic Benchmark For Continual Reinforcement Learning* [583]. Success in this frontier will be key to deploying autonomous vehicles that are not only competent in a fixed domain but are truly robust, resilient, and capable of lifelong learning in the face of an ever-evolving world.

**Table: Comparison of approaches in 7.3 Lifelong, Continual, and Meta-Learning**

| Paradigm | Key Method / Framework | Core Idea / Mechanism | Application / Task in Autonomous Driving | Reference |
| :--- | :--- | :--- | :--- | :--- |
| Continual Learning | Generative Negative Replay for Continual Learning | Uses generated data from old tasks as effective negative examples to learn new classes, helping distinguish novel dangerous maneuvers from safe ones. | Trajectory prediction, adapting to new scenarios without forgetting old ones. | [571] |
| Continual Learning | Lifelong Learning of Spatiotemporal Representations with Dual-Memory Recurrent Self-Organization | Neuro-inspired architecture with separate episodic (fine-grained instances) and semantic (compact categories) memories; episodic memory replays trajectories to consolidate knowledge. | Continuous object recognition for perception systems. | [572] |
| Continual Learning | Continual Interactive Behavior Learning With Traffic Divergence Measurement: A Dynamic Gradient Scenario Memory Approach | Uses a dynamic gradient scenario memory that measures traffic divergence to selectively retain experiences, mitigating forgetting across different driving locations. | Vehicle trajectory prediction in interactive scenarios. | [573] |
| Continual Learning | Distribution-Aware Continual Test-Time Adaptation for Semantic Segmentation | Dynamically selects and updates small sets of domain-specific and task-relevant parameters for efficient long-term adaptation. | Semantic segmentation for perception in changing environments. | [574] |
| Meta-Learning | Expanding the Deployment Envelope of Behavior Prediction via Adaptive Meta-Learning | Leverages Bayesian regression to augment prediction models with an adaptive layer for efficient domain transfer to new cities via offline fine-tuning or online adaptation. | Behavior prediction for domain transfer. | [575] |
| Meta-Learning | Meta Learning MPC using Finite-Dimensional Gaussian Process Approximations | Meta-trains a dynamics model using data from related tasks for fast online Bayesian adaptation to new conditions (e.g., road friction). | Model Predictive Control (MPC) for autonomous racing. | [576] |
| Meta-Learning | Online Meta-Learning | Merges online and meta-learning to capture continual lifelong learning with sub-linear regret guarantees for changing environments. | General driving adaptation to dynamic traffic. | [577] |
| Meta-Learning | Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning | Learns a self-supervised interaction loss that allows an agent to quickly adapt to novel scenes (e.g., indoor navigation). | Visual navigation, transferable to unfamiliar road networks. | [578] |
| Curriculum Learning | Safe Reinforcement Learning via Curriculum Induction | Employs an automated "monitor" that intervenes with reset controllers when the agent acts dangerously; the teacher learns a curriculum policy to optimize final performance. | Safely learning high-risk maneuvers during training. | [579] |
| Curriculum Learning | Continual Driving Policy Optimization with Closed-Loop Individualized Curricula | Frames curriculum generation as a closed-loop process: evaluates AV failure probability in historical scenarios and tailors an individualized training curriculum by sampling more challenging cases. | Iterative driving policy improvement using scenario libraries. | [580] |
| Curriculum Learning | Rethinking Closed-loop Training for Autonomous Driving | Highlights that training benchmark design (scaling/composition of traffic scenarios) is a critical curriculum; proposes Trajectory Value Learning (TRAVL) exploiting imagined data. | Efficient closed-loop training for autonomous driving agents. | [30] |
| Integration & Evaluation | Online Fast Adaptation and Knowledge Accumulation (OSAKA) | Proposes a scenario demanding both quick solving of new tasks and fast remembering. | Continual learning baseline. | [581] |
| Integration & Evaluation | Rigorous Agent Evaluation: An Adversarial Approach to Uncover Catastrophic Failures | Proposes adversarial evaluation methods to stress-test agents and uncover rare failures missed by standard evaluation. | Evaluating safety and robustness of autonomous driving agents. | [582] |
| Integration & Evaluation | Exiting the Simulation: The Road to Robust and Resilient Autonomous Vehicles at Scale | Discusses advances needed in simulation-to-reality transfer and comprehensive benchmarks for real-world deployment. | Bridging simulation and real-world autonomous driving. | [9] |
| Integration & Evaluation | MetaDrive: Composing Diverse Driving Scenarios for Generalizable Reinforcement Learning | A benchmark for composing diverse driving scenarios to study generalizability. | Benchmark for generalizable RL in autonomous driving. | [450] |
| Integration & Evaluation | Continual World: A Robotic Benchmark For Continual Reinforcement Learning | A robotic benchmark for continual reinforcement learning, prioritizing forward transfer. | Benchmark for continual RL in robotics/autonomous driving. | [583] |


### 7.4 Human-AI Collaboration and Personalized Driving

The paradigm of autonomous driving is undergoing a profound transformation, moving from a purely technical problem of sensorimotor control to a complex socio-technical system where human intelligence, preference, and trust are central. This evolution necessitates a shift from opaque, monolithic AI drivers towards collaborative and personalized systems that can communicate, adapt, and co-exist with human users—both inside and outside the vehicle. The integration of Deep Reinforcement Learning (RL) and Imitation Learning (IL) is pivotal in enabling this new generation of human-centric autonomous vehicles (AVs), focusing on explainable communication interfaces, human-in-the-loop policy refinement, and personalized driving behavior.

A foundational requirement for effective human-AI collaboration is transparent and interpretable decision-making. Opaque AV actions can erode trust and situational awareness, particularly in safety-critical or unexpected scenarios. Research consistently shows that providing explanations for an AV's actions can significantly impact passenger perceptions of safety, trust, and the desire to take over control [584]. The necessity and optimal content of these explanations are highly context-dependent, varying with driving scenarios and individual user types. For instance, studies indicate that while both abstract and specific natural language explanations can alleviate passenger anxiety, specific explanations more strongly influence the desire to resume manual control [585]. Effective explanatory interfaces, therefore, must be dynamic and tailored. This aligns with frameworks for developing situational awareness in joint human-AV action, which argue that communications should be sensitive to AV traits, user states, action goals, and the driving context [586]. Beyond passengers, explainability is also crucial for interaction with other road users. Human-Machine Interfaces (HMIs), both internal (iHMIs) and external (eHMIs), are being designed to foster communication between AVs and conventional vehicle (CV) drivers, with studies showing iHMIs can improve CV drivers' situation awareness and trust in AVs at intersections [587]. The move towards generating automated driving commentary, inspired by human "think-aloud" protocols, represents a promising direction for creating intelligible, real-time explanations of AV perception and planning [588].

Building upon transparent communication, the next frontier is the active incorporation of human feedback into the learning loop itself. Rather than treating the policy learning process as a one-off training event, emerging paradigms leverage humans as mentors or guides for continuous improvement. Human-in-the-loop RL and IL frameworks allow for the fine-tuning of pre-trained models based on direct human intervention, demonstration, or reward shaping. For example, one approach integrates a Transformer-based policy network pre-trained via Behavior Cloning, which is subsequently fine-tuned through reinforcement learning with human guidance (RLHG), where human feedback directly shapes the reward function to achieve safer and more efficient behaviors [589]. Similarly, shared control paradigms aim to balance human authority with autonomous safety guarantees. A highly parallelized, data-driven Model Predictive Control (MPC) scheme can evaluate thousands of potential human inputs to minimally intervene only when necessary to maintain safety, thereby preserving the human's sense of agency while preventing dangerous outcomes [590]. This philosophy of "meaningful human control" is critical for partially automated systems, where ensuring the system tracks the user's intentions is directly linked to perceived safety and trust [591].

Personalization is the logical culmination of human-AI collaboration, transforming the AV from a generic chauffeur into an adaptive agent that aligns with individual passenger preferences and verbal instructions. Deep RL and IL are key to learning and encoding these preferences. Personalization can operate at multiple levels: from adjusting driving style (e.g., assertive vs. conservative) to interpreting and executing high-level natural language commands. Learning latent representations of driver behavior from data is a powerful technique for this purpose. By imposing an information bottleneck, models can extract compact, generalizable representations of driving traits that can then inform a policy, allowing it to adapt to different driver types [393]. Furthermore, cognitive factors like impulsivity and inhibitory control, inferred from driving behavior via recurrent neural networks, can be used to trigger personalized safety interfaces, such as discouraging running yellow lights [592]. The most significant leap in personalization, however, is enabled by Large Language Models (LLMs). Frameworks like "Agent-Driver" and "Talk2Drive" leverage LLMs as cognitive engines that can understand natural language instructions, reason about context using chain-of-thought processes, access tool libraries for planning, and generate personalized driving policies [541] [544]. This allows passengers to verbally specify preferences for safety, efficiency, or comfort, or to give conditional navigation instructions (e.g., "follow that truck for now"), with the LLM translating these commands into actionable plans for the vehicle's control system [15] [593].

However, this drive towards personalized, human-collaborative AVs raises significant societal and ethical questions that must be addressed proactively. A primary concern is the impact on professional drivers, whose livelihoods may be threatened by automation. Qualitative studies reveal that drivers themselves are apprehensive about this future and challenge narratives that their jobs are unsatisfying or unworthy of protection [594]. This highlights a critical gap between expert discourse and the perspectives of directly affected stakeholders, underscoring the need for inclusive ethical frameworks and just transition policies. Furthermore, the personalization of driving behavior must be bounded by social and legal norms. An AV that drives overly aggressively to suit one passenger's preference could endanger others and disrupt traffic flow. Therefore, personalization algorithms must operate within safe, socially compatible, and legally compliant envelopes. Concepts like Social Value Orientation (SVO) and altruism are being integrated into RL frameworks to ensure AVs do not become purely egoistic but consider the welfare of other road users, leading to smoother and safer mixed traffic flow [595] [596]. Ultimately, the goal is not to replace human judgment and social nuance but to augment it with AI capabilities, creating a transportation ecosystem that is not only efficient and safe but also equitable, trustworthy, and respectful of human dignity.

**Table: Comparison of approaches in 7.4 Human-AI Collaboration and Personalized Driving**

| Method/Model Name | Core Idea / Purpose | Key Techniques / Components | Reference |
| :--- | :--- | :--- | :--- |
| Agent-Driver (LLM-based) | Leverage LLMs as a cognitive agent for human-like reasoning, understanding, and planning in autonomous driving. | Large Language Models (LLMs), tool library, cognitive memory, chain-of-thought reasoning, task/motion planning, self-reflection. | [541] |
| Talk2Drive (LLM-based) | Process verbal commands to make personalized driving decisions based on safety, efficiency, and comfort preferences. | Large Language Models (LLMs), speech recognition, contextual reasoning, command generation for ECU. | [544] |
| Pre-trained Transformer with Human-Guided Fine-Tuning | Enhance end-to-end navigation by pre-training with Behavior Cloning and fine-tuning via human-guided reinforcement learning. | Transformer-based policy network, Behavior Cloning (BC), Reinforcement Learning with Human Guidance (RLHG), human supervision/intervention/demonstration. | [589] |
| Highly Parallelized Data-driven MPC for Shared Control | Enable minimal intervention shared control by evaluating thousands of potential human inputs to maintain safety while preserving user agency. | Data-driven Model Predictive Control (MPC), parallel trajectory evaluation, safety prediction, goal-agnostic intervention. | [590] |
| Learning from Restricted Latent Representations | Learn generalizable driving policies by extracting compact, scenario-invariant latent representations of driving behavior. | Information bottleneck, latent representation learning, Q-learning, distance metric for scenario similarity. | [393] |
| Personalized Safety Interfaces via Cognitive Factors Inference | Personalize driver safety interventions (e.g., discouraging running yellow lights) by inferring cognitive factors like impulsivity from driving behavior. | Recurrent Neural Network (RNN), inference of impulsivity/inhibitory control, real-time interface triggering. | [592] |
| Conditional Driving from Natural Language Instructions | Enable AVs to understand and safely follow high-level natural language instructions that alter the pre-planned route. | Hierarchical policy, recurrent layers, gated attention, conditional imitation learning from human language data. | [593] |
| Receive, Reason, and React (LLM Framework) | Integrate LLMs for linguistic understanding and reasoning to enable personalized driving based on verbal commands and feedback. | Large Language Models (LLMs), chain-of-thought prompting, specialized tools, real-time personalization. | [15] |
| Socially Compatible Control (Altruistic AV) | Design AV control to be socially compatible by optimizing for both ego reward and courtesy to other drivers (e.g., in car-following). | Social Value Orientation (SVO), altruism integration into decision-making, optimization of combined reward. | [595] |
| Cooperative Autonomous Vehicles with Sympathy | Induce altruistic behavior in AVs using Social Value Orientation (SVO) to improve safety and traffic flow in competitive scenarios. | Social Value Orientation (SVO), reinforcement learning, experiential learning without explicit coordination. | [596] |


### 7.5 The Data-Centric Ecosystem: Simulation, Datasets, and Closed-Loop Development

The advancement of deep reinforcement and imitation learning for autonomous driving is inextricably linked to the parallel evolution of a sophisticated data-centric infrastructure. This ecosystem, comprising large-scale datasets, high-fidelity simulators, and closed-loop development frameworks, forms the essential substrate for training, validating, and continuously improving driving policies. The trend is moving beyond static datasets and fixed simulation environments towards dynamic, generative, and interactive systems that can synthesize the long-tail of safety-critical scenarios essential for robust autonomy.

The foundation of this ecosystem is the proliferation of large-scale, open-source driving datasets such as Waymo Open Dataset, nuScenes, and Lyft L5. These datasets provide not just perception data but, crucially, detailed object trajectories and HD maps that accurately reflect real-world complexity. Platforms like **ScenarioNet** [597] leverage this wealth of information by defining a unified scenario description format and aggregating scenarios from heterogeneous datasets, creating massive repositories of real-world traffic interactions. These "digital twin" scenarios can be replayed in simulators, providing a benchmark for safety evaluation that is grounded in reality rather than hand-crafted designs. This shift from scripted to data-driven scenarios is pivotal, as it facilitates research in imitation learning, where policies can be trained on vast amounts of human driving behavior, and in reinforcement learning, where agents can be evaluated in environments that mirror the stochastic nature of real traffic.

To utilize these datasets effectively and conduct safe, scalable training, the field has seen significant innovation in simulation frameworks. High-fidelity simulators like CARLA and **AutoVRL** [598], built on physics engines like Bullet, provide realistic sensor simulation (LiDAR, cameras) and vehicle dynamics, which are critical for sim-to-real transfer. Beyond visual and physical realism, a key advancement is the focus on *compositional diversity* to combat overfitting and improve generalization. **MetaDrive** [450] exemplifies this with its emphasis on procedural generation, creating an infinite number of diverse driving scenes through configurable road networks and traffic flows. Similarly, **PGDrive** [599] uses procedural generation to create open-ended environments, demonstrating that training on an expanding set of generated scenes significantly improves an agent's ability to generalize to unseen scenarios. This capability is vital for preparing agents for the infinite variability of the real world.

A paramount challenge within this ecosystem is the efficient generation of *safety-critical scenarios*. Naturalistic driving data is overwhelmingly composed of safe, routine situations, making collisions and near-misses extremely rare. To evaluate and improve the robustness of autonomous systems, methods to artificially generate these high-risk scenarios are essential. Early approaches included adversarial generation and sampling-based optimization, but recent trends heavily leverage generative models and deep reinforcement learning. For instance, **Safety-Critical Scenario Generation Via Reinforcement Learning Based Editing** [600] frames generation as a sequential editing process guided by a reward function that balances risk and plausibility, the latter often learned by a generative model like a VAE. Frameworks like **BridgeGen** [601] seek a hybrid approach, bridging data-driven and knowledge-driven methods by using ontologies for broad coverage and optimization/RL for efficient critical scenario generation. Furthermore, **CaDRE** [602] focuses on generating *controllable and diverse* safety-critical scenarios using real-world trajectories and black-box optimization, while **CausalAF** [603] integrates causal relationships as a prior into a flow-based generative model, improving the efficiency of learning the cause-and-effect mechanisms behind risk. The **Closed-loop Adversarial Training (CAT)** framework [604] introduces a resampling technique to turn logged real-world scenarios into safety-critical ones efficiently, creating a dynamic training environment that continuously challenges the agent. These methods collectively represent a move towards a generative, on-demand synthesis of the edge cases that define the safety envelope of an autonomous system.

This capability feeds directly into the emerging paradigm of *closed-loop development*. The vision is a continuous cycle where an agent's performance is evaluated, its weaknesses are identified, and targeted scenarios are generated to retrain and improve it. **Continual Driving Policy Optimization with Closed-Loop Individualized Curricula (CLIC)** [580] operationalizes this by framing autonomous vehicle evaluation as a collision prediction task. It uses failure probabilities to tailor individualized training curricula from a vast pre-collected scenario library, ensuring the agent focuses on its specific weaknesses. The **CRITICAL** framework [605] formalizes this closed-loop feedback between data generation and training, using safety measures and even large language models to analyze and generate scenarios targeting specific performance gaps. This mirrors a broader "data engine" philosophy, where the training process itself is augmented by intelligent systems that curate and synthesize the most informative data. The concept extends to sim-to-real pipelines, where frameworks like **SafeAPT** [606] and **Sim-to-Lab-to-Real** [607] emphasize safe adaptation. They use diverse policies evolved in simulation or safety-aware policy distributions with shielding to minimize real-world violations during the transfer phase, ensuring that the learning loop can be closed safely outside the simulation.

Underpinning these advances is the growing role of *generative world models*. Projects like **GAIA-1** [608] and **Learning Interactive Real-World Simulators** [609] aim to create foundational models that can simulate realistic visual outcomes and physical interactions in response to actions. By learning from vast, diverse datasets (video, text, actions), these models promise to become universal simulators capable of generating highly realistic and varied driving scenarios for training and testing. This represents the next frontier in the data-centric ecosystem: moving from simulators with pre-defined rules and assets to generative environments that can imagine and render novel, plausible situations on the fly.

In conclusion, the infrastructure for autonomous driving policy learning is undergoing a profound transformation. It is evolving from a collection of static tools into an integrated, intelligent, and generative ecosystem. The synergy between large-scale real-world datasets, diverse and programmable simulators, generative models for scenario synthesis, and closed-loop development frameworks creates a virtuous cycle. This data-centric foundation is crucial for overcoming the fundamental challenges of robustness and safety, enabling the iterative and scalable improvement required to "exit the simulation" [9] and deploy autonomous vehicles that are truly prepared for the complexity of the real world.

**Table: Comparison of approaches in 7.5 The Data-Centric Ecosystem: Simulation, Datasets, and Closed-Loop Development**

| Method/Model Name | Category | Key Idea/Approach | Reference |
| :--- | :--- | :--- | :--- |
| ScenarioNet | Dataset & Simulation Platform | Defines a unified scenario description format and aggregates real-world traffic scenarios from heterogeneous datasets (Waymo, nuScenes, Lyft L5, nuPlan) to create a large-scale repository of "digital twin" scenarios for simulation and benchmarking. | [597] |
| AutoVRL | High-Fidelity Simulator | A high-fidelity simulator built on the Bullet physics engine for sim-to-real deep reinforcement learning, providing realistic sensor simulation (LiDAR, camera, GPS, IMU) and vehicle dynamics. | [598] |
| MetaDrive | Driving Simulator | A compositional driving simulator emphasizing procedural generation to create an infinite number of diverse driving scenarios, improving the generalizability of RL agents. | [450] |
| PGDrive | Driving Simulator | An open-ended, highly configurable driving simulator using procedural generation to create diverse road networks and traffic flows, demonstrating improved agent generalization. | [599] |
| Safety-Critical Scenario Generation Via Reinforcement Learning Based Editing | Scenario Generation | Frames safety-critical scenario generation as a sequential editing process guided by a reward function balancing risk and plausibility, the latter learned by a generative model like a VAE. | [600] |
| BridgeGen | Scenario Generation | A hybrid framework bridging data-driven and knowledge-driven methods. It uses ontology-based techniques for broad coverage and optimization/RL for efficient safety-critical scenario generation. | [601] |
| CaDRE | Scenario Generation | Generates controllable and diverse safety-critical scenarios using real-world trajectories and black-box optimization techniques. | [602] |
| CausalAF | Scenario Generation | A flow-based generative framework that integrates causal relationships as a prior via causal masking operations to improve the efficiency of learning the cause-and-effect mechanisms behind risk. | [603] |
| CAT (Closed-loop Adversarial Training) | Training Framework | A closed-loop adversarial training framework using a novel resampling technique to efficiently turn logged real-world scenarios into safety-critical ones for dynamic agent training. | [604] |
| CLIC (Continual Driving Policy Optimization with Closed-Loop Individualized Curricula) | Training Framework | Frames AV evaluation as a collision prediction task and uses failure probabilities to tailor individualized training curricula from a pre-collected scenario library, focusing on agent weaknesses. | [580] |
| CRITICAL | Training Framework | A closed-loop framework integrating real-world traffic dynamics, safety measures, and optional LLMs to generate critical scenarios targeting specific performance gaps in the RL agent. | [605] |
| SafeAPT | Sim-to-Real Transfer | A safe sim-to-real algorithm that leverages a diverse repertoire of policies evolved in simulation and transfers the most promising safe policy to the real robot using Bayesian optimization with learned reward and safety models. | [606] |
| Sim-to-Lab-to-Real | Sim-to-Real Transfer | Uses a dual-policy setup (performance + safety) with shielding and PAC-Bayes theory to provide safety and generalization guarantees for policy transfer from simulation to lab to real world. | [607] |
| GAIA-1 | Generative World Model | A generative world model for autonomy that uses video, text, and action inputs to generate realistic driving scenarios and predict potential outcomes, learning high-level scene dynamics and structure. | [608] |
| Learning Interactive Real-World Simulators | Generative World Model | Aims to learn a universal simulator of real-world interaction through generative modeling on diverse datasets (video, robotics, navigation), simulating visual outcomes in response to high and low-level instructions. | [609] |


### 7.6 Systemic Challenges: Governance, Certification, and Societal Integration

The successful deployment of learning-based autonomous vehicles (AVs) extends far beyond achieving technical benchmarks in simulation. It necessitates navigating a complex landscape of systemic challenges encompassing governance, certification, and societal integration. These non-technical frontiers are critical for ensuring that AVs are not only capable but also trustworthy, legally compliant, and beneficial to society at large. Addressing them requires a paradigm shift from isolated algorithmic development to a holistic, multidisciplinary approach that intertwines computer science with ethics, law, policy, and social sciences.

A primary challenge lies in establishing robust and adaptive **AI governance frameworks**. As highlighted in surveys of the field, the ethical implications of AI are multifaceted, including fairness, accountability, safety, and transparency [610]. For AVs, these principles must be translated into concrete, operational requirements throughout the system lifecycle. This involves moving from high-level ethical charters to implementable technical standards and organizational processes. Frameworks like the "hourglass model" of organizational AI governance are emerging, which structure requirements at environmental, organizational, and AI system levels to ensure ethical principles are baked into development and deployment [611]. Furthermore, the management-based regulatory paradigm, gaining traction in regions like the EU and US, emphasizes the necessity of human oversight during the training and development phases of AI systems [612]. This aligns with technical needs in RL and IL for human-in-the-loop training and validation. Effective governance must also be **multilevel**, coordinating actions across international bodies, national regulators, corporations, and citizens to build trust through competence, integrity, and benevolence [613]. The dynamic nature of AI risk, especially from "frontier" systems with potentially dangerous capabilities, calls for proactive governance functions such as standard-setting, registration, and compliance mechanisms for advanced models [614]. International institutions may be crucial for coordinating these efforts, managing global externalities, and setting safety standards [615].

Closely tied to governance is the urgent need for standardized **testing and certification methodologies** for learning-based driving policies. Current vehicle safety standards (e.g., NCAP, FMVSS) are ill-suited for evaluating the performance of AI systems that learn and may behave non-deterministically. New, rigorous evaluation frameworks are required. This includes standardized simulation-based testing protocols using high-fidelity digital twins and scenario databases to assess performance across a long tail of rare but critical events. More importantly, there is a push towards **safety assurance** frameworks that go beyond statistical testing. Techniques like runtime assurance (RTA) and conformal safety filters provide formal guarantees on system behavior during deployment, acting as a last line of defense. The development of benchmarks like GUARD for safe RL is a step towards standardizing the evaluation of safety-critical learning algorithms. Certification will likely evolve into a continuous process, akin to "data-centric governance," where compliance is assured through curated datasets and algorithmic evaluations applied throughout the product lifecycle, rather than a one-time audit [616]. This approach systematizes governance requirements, enabling reproducible evaluation of system behavior and outcomes.

**Cybersecurity** presents a profound and escalating systemic risk. AVs are complex cyber-physical systems, and their learning-based components are vulnerable to adversarial attacks on sensors, data, and models. Ensuring robustness against such attacks is not just a technical problem but a cornerstone of public safety and trust. Research into adversarial robustness for RL policies, such as training with observation perturbations, is vital. Furthermore, the cybersecurity of the broader AV ecosystem—including V2X communication, fleet management, and software update pipelines—must be governed by stringent standards and proactive "violet teaming" practices that combine offensive security testing with defensive design [617]. A breach in this ecosystem could have catastrophic consequences, making cybersecurity a non-negotiable pillar of AV certification.

Finally, the **socio-economic impact and societal integration** of AVs constitute a vast area of necessary inquiry. Widespread AV deployment will reshape labor markets (e.g., professional drivers), urban design, traffic patterns, and energy consumption. It also raises critical questions about equity, access, and environmental sustainability. A purely techno-centric development risks exacerbating existing inequalities or creating new ones. For instance, ethical AI frameworks must be inclusive and consider global perspectives, moving beyond principles dominated by the Global North to incorporate local knowledge and values [618] [619]. Tools like Multi-Criteria Decision Analysis (MCDA) can help formally assess the social and ethical trade-offs of AV integration [620]. Public perception and trust are also pivotal; studies show that ethical concerns are not salient for most of the public unless directly prompted, indicating a need for public engagement and education to foster informed societal discourse [621]. Participatory frameworks like Particip-AI, which gather public input on AI use cases and harms, are essential for democratic governance [622].

In conclusion, the path to trustworthy and ubiquitous autonomous driving is paved with systemic challenges that demand deep collaboration across disciplines. Computer scientists must work with ethicists to design auditable and fair algorithms, with lawyers to define liability and compliance frameworks, with policymakers to craft agile regulations, and with social scientists to understand and mitigate unintended societal consequences. The ultimate goal is to develop not just a functional technology, but a **responsible AI system**—lawful, ethical, and robust—that earns public trust and contributes positively to a sustainable and equitable future [623]. The maturation of the AV field will be measured not only by miles driven without intervention but by the strength of the governance, certification, and social contracts that enable its safe and beneficial integration into the fabric of human society.

**Table: Comparison of approaches in 7.6 Systemic Challenges: Governance, Certification, and Societal Integration**

| Challenge Category | Key Concepts / Frameworks | Proposed Solutions / Approaches | Reference |
| :--- | :--- | :--- | :--- |
| AI Governance Frameworks | Hourglass model of organizational AI governance; Management-based regulatory paradigm; Multilevel governance (international, national, organizational, citizen). | Translating ethical principles into technical standards and organizational processes; Human-in-the-loop oversight during training; Coordinated action across governance levels based on trust (competence, integrity, benevolence). | [611]; [612]; [613] |
| Testing & Certification | Standardized simulation-based testing; Runtime assurance (RTA) and conformal safety filters; Data-centric governance; Continuous compliance processes. | Developing high-fidelity digital twins and scenario databases; Implementing safety filters for formal behavioral guarantees; Using curated datasets and algorithmic evaluations throughout the system lifecycle for reproducible compliance. | [616] |
| Cybersecurity | Adversarial robustness for RL/IL; Violet teaming; Ecosystem security (V2X, software updates). | Training with observation perturbations; Proactive combination of offensive security testing (red teaming) with defensive design (blue teaming) and ethical prioritization (violet teaming). | [617] |
| Socio-Economic & Societal Integration | Multi-Criteria Decision Analysis (MCDA); Participatory frameworks (e.g., Particip-AI); Inclusive, global ethical frameworks. | Using formal impact assessment tools (e.g., MAIA questionnaire) to evaluate social/ethical trade-offs; Gathering public input on AI use cases and harms to inform democratic governance; Incorporating local knowledge and values beyond Global North perspectives. | [620]; [622]; [618]; [619] |
| Foundational Ethical Principles & Trustworthy AI | Multifaceted ethical concerns (fairness, accountability, safety, transparency); Trustworthy AI as lawful, ethical, and robust. | Holistic, multidisciplinary approach integrating computer science with ethics, law, policy, and social sciences; Implementing the seven key requirements for trustworthy AI throughout the system lifecycle. | [610]; [623] |


### 7.7 Synthesis and Concluding Remarks

The journey of autonomous driving policy learning, as chronicled in this survey, reflects a broader evolution in artificial intelligence: a quest for systems that are not only performant but also robust, safe, and trustworthy. This trajectory has progressed from meticulously engineered modular pipelines, through the data-hungry promise of end-to-end learning, and is now converging towards a paradigm of knowledge-integrated autonomy. Each phase has brought critical insights and exposed fundamental challenges that define the current frontier.

The modular approach, decomposing driving into perception, prediction, planning, and control, established a foundation of interpretability and safety-by-design, allowing for verification of individual components. However, its limitations—error propagation, compounding uncertainties, and a struggle to capture the nuanced, closed-loop nature of human driving interaction—became apparent. This spurred the rise of end-to-end methods, particularly those leveraging Deep Reinforcement Learning (RL) and Imitation Learning (IL). These approaches promised joint optimization and direct learning of complex behaviors from data, demonstrating remarkable performance in controlled settings. Deep RL, through trial-and-error in simulation, learned sophisticated negotiation and planning strategies, as seen in works exploring multi-agent cooperation in mixed traffic [356]. IL, especially behavior cloning, provided a data-efficient path to replicating human driving, with advanced variants like the spatial-temporal heatmap method achieving high competition scores [624].

Yet, the end-to-end paradigm unveiled its own profound set of challenges. The "black box" nature of these models clashes with the non-negotiable demand for safety assurance and interpretability in safety-critical systems [556]. The sim-to-real gap remains a formidable obstacle, where policies excelling in simulation can fail unpredictably in the real world due to distribution shifts in perception, dynamics, and agent behaviors [9]. Furthermore, pure data-driven methods are inherently limited by their training distribution, struggling with long-tail, unforeseen scenarios that are rare in collected datasets but paramount for safety [7]. The quest for robustness against adversarial perturbations and natural distribution shifts is ongoing, as highlighted by benchmarking efforts like [532].

This recognition has catalyzed the current, integrative trend: moving beyond purely reactive pattern matching towards systems infused with knowledge, reasoning, and explicit safety architectures. Several key strands define this frontier. First, there is a concerted effort to **re-integrate safety and planning**, not as separate modules but through formal methods that provide guarantees. Techniques like reachability analysis are being infused within planning frameworks to ensure the existence of safe fallback maneuvers in real-time, creating minimally interventional safety controllers [10]. Second, the field is embracing **interactive and game-theoretic models** that explicitly account for the mutual influence between the ego vehicle and other agents, moving beyond passive prediction to strategic planning [625]. Third, and perhaps most transformative, is the emergence of **knowledge-driven and foundation model-enhanced autonomy**. Large Language Models (LLMs) and other pre-trained models are being leveraged not as direct controllers, but as reasoning engines for high-level scene understanding, causal inference, and behavior planning. They offer potential breakthroughs in generalization, interpretability, and handling of corner cases by encoding commonsense and contextual knowledge [626], [627]. This leads to hybrid architectures where neural networks handle perception and low-level control, while symbolic or semantic reasoning guides high-level strategy.

Despite these advances, the most pressing open problems lie at the confluence of safety, robustness, and societal trust. **Certifiable Safety in Learning-Based Systems** remains unsolved at scale. While runtime assurance frameworks and safety filters provide a pragmatic path [628], providing end-to-end guarantees for complex deep policies in open-world environments is a fundamental research challenge. **Scalable and Faithful Simulation-to-Real Transfer** is equally critical. The community must move beyond domain randomization to develop simulation frameworks and learning algorithms that capture the causal structure of driving and enable efficient adaptation to the real world, a concept central to [9]. Furthermore, **Explainability and Trust** must evolve from post-hoc visualization to integral components of the decision-making process. Explanations must be actionable, timely, and tailored to different stakeholders—from engineers validating systems to passengers and regulatory bodies [14]. Finally, the **Ethical and Social Dimension** of learned policies—ensuring fairness, defining accountable behavior in moral dilemmas, and designing for productive human-AI collaboration—requires interdisciplinary engagement beyond pure engineering [629].

Looking forward, the path to robust and socially beneficial autonomous driving agents will not be found in a single algorithmic breakthrough but in a holistic synthesis. The future stack will likely be a hybrid, adaptive, and introspective system. It will combine the perceptual prowess and behavioral flexibility of deep learning with the rigorous safety guarantees of formal methods, the causal and contextual reasoning of knowledge models, and the strategic foresight of game theory. Continual and meta-learning frameworks will allow agents to adapt efficiently to new environments and learn from rare events [580]. Crucially, the development and validation ecosystem—encompassing high-fidelity simulation, scenario generation [7], and comprehensive benchmarking—must co-evolve with the algorithms themselves. The ultimate goal is to create autonomous drivers that are not merely competent mimics of human behavior but cooperative, predictable, and resilient entities that enhance overall traffic safety and efficiency. By embracing this integrated, safety-first, and knowledge-aware paradigm, the field can transition from solving the driving problem in isolation to engineering trustworthy agents capable of exiting the simulation and navigating the immense complexity of the real world.

**Table: Comparison of approaches in 7.7 Synthesis and Concluding Remarks**

| Paradigm / Method | Key Characteristics / Approach | Key Challenges / Limitations | Reference(s) |
| :--- | :--- | :--- | :--- |
| Modular Pipelines | Decomposes driving into perception, prediction, planning, and control. Establishes interpretability and safety-by-design, allowing verification of individual components. | Error propagation, compounding uncertainties, struggle to capture nuanced, closed-loop nature of human driving interaction. | [630], [42] |
| End-to-End Learning (Deep RL & Imitation Learning) | Joint optimization and direct learning of complex behaviors from data. Deep RL learns sophisticated negotiation/planning in simulation. IL (e.g., Behavior Cloning) replicates human driving efficiently. | "Black box" nature clashes with safety/interpretability demands. Sim-to-real gap due to distribution shifts. Limited by training distribution, struggles with long-tail/unforeseen scenarios. | [356], [624], [328], [631] |
| Knowledge-Integrated Autonomy (Current Frontier) | Moves beyond reactive pattern matching towards systems infused with knowledge, reasoning, and explicit safety architectures. | Integrating diverse knowledge sources, ensuring real-time performance with complex reasoning, achieving certifiable safety guarantees. | [626], [627], [555] |
| Formal Methods & Safety Assurance (Sub-strand) | Re-integrates safety and planning via formal methods (e.g., reachability analysis) to provide guarantees and minimally interventional safety controllers. | Scalability to complex, multi-agent scenarios; integration with learning-based components; computational complexity for real-time use. | [10], [628], [632] |
| Interactive & Game-Theoretic Models (Sub-strand) | Explicitly accounts for mutual influence between ego vehicle and other agents using game theory, moving beyond passive prediction to strategic planning. | Modeling human behavior and intent uncertainty; computational demands of solving games in real-time; non-stationarity of human policies. | [625], [291], [596] |
| Foundation Model-Enhanced Autonomy (Sub-strand) | Leverages LLMs and pre-trained models as reasoning engines for high-level scene understanding, causal inference, and behavior planning, not as direct controllers. | Reliability and hallucination of LLMs; grounding symbolic knowledge in perceptual reality; latency and resource constraints. | [627], [626], [633], [15] |



## References
[1] aiMotive Dataset  A Multimodal Dataset for Robust Autonomous Driving   with Long-Range Perception

[2] MIDAS  Multi-agent Interaction-aware Decision-making with Adaptive   Strategies for Urban Autonomous Navigation

[3] Enhancing Social Decision-Making of Autonomous Vehicles  A   Mixed-Strategy Game Approach With Interaction Orientation Identification

[4] Potential Game-Based Decision-Making for Autonomous Driving

[5] IR-STP  Enhancing Autonomous Driving with Interaction Reasoning in   Spatio-Temporal Planning

[6] Towards Socially Responsive Autonomous Vehicles  A Reinforcement   Learning Framework with Driving Priors and Coordination Awareness

[7] A Survey on Safety-Critical Driving Scenario Generation -- A   Methodological Perspective

[8] (Re)$^2$H2O  Autonomous Driving Scenario Generation via Reversely   Regularized Hybrid Offline-and-Online Reinforcement Learning

[9] Exiting the Simulation  The Road to Robust and Resilient Autonomous   Vehicles at Scale

[10] On Infusing Reachability-Based Safety Assurance within Planning   Frameworks for Human-Robot Vehicle Interactions

[11] Refining Obstacle Perception Safety Zones via Maneuver-Based   Decomposition

[12] Ethical Decision-making for Autonomous Driving based on LSTM Trajectory   Prediction Network

[13] Legal Decision-making for Highway Automated Driving

[14] Incorporating Explanations into Human-Machine Interfaces for Trust and   Situation Awareness in Autonomous Vehicles

[15] Receive, Reason, and React  Drive as You Say with Large Language Models   in Autonomous Vehicles

[16] Human-Vehicle Cooperation on Prediction-Level  Enhancing Automated   Driving with Human Foresight

[17] DQ-GAT  Towards Safe and Efficient Autonomous Driving with Deep   Q-Learning and Graph Attention Networks

[18] A Platform-Agnostic Deep Reinforcement Learning Framework for Effective   Sim2Real Transfer in Autonomous Driving

[19] Human-Like Autonomous Car-Following Model with Deep Reinforcement   Learning

[20] Safe Decision-making for Lane-change of Autonomous Vehicles via Human   Demonstration-aided Reinforcement Learning

[21] Human-Like Autonomous Driving on Dense Traffic

[22] Evaluation of MPC-based Imitation Learning for Human-like Autonomous   Driving

[23] Modeling Human Driving Behavior through Generative Adversarial Imitation   Learning

[24] Imitation Is Not Enough  Robustifying Imitation with Reinforcement   Learning for Challenging Driving Scenarios

[25] Imitation Bootstrapped Reinforcement Learning

[26] CIRL  Controllable Imitative Reinforcement Learning for Vision-based   Self-driving

[27] Integrating Imitation Learning with Human Driving Data into   Reinforcement Learning to Improve Training Efficiency for Autonomous Driving

[28] Towards Learning Multi-agent Negotiations via Self-Play

[29] Hybrid Reinforcement Learning-Based Eco-Driving Strategy for Connected   and Automated Vehicles at Signalized Intersections

[30] Rethinking Closed-loop Training for Autonomous Driving

[31] Self-Awareness Safety of Deep Reinforcement Learning in Road Traffic   Junction Driving

[32] Improved Deep Reinforcement Learning with Expert Demonstrations for   Urban Autonomous Driving

[33] Efficient Deep Reinforcement Learning with Imitative Expert Priors for   Autonomous Driving

[34] Human as AI Mentor  Enhanced Human-in-the-loop Reinforcement Learning   for Safe and Efficient Autonomous Driving

[35] Reinforcement Learning based Control of Imitative Policies for   Near-Accident Driving

[36] Fine-grained acceleration control for autonomous intersection management   using deep reinforcement learning

[37] Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery

[38] LEAF  Latent Exploration Along the Frontier

[39] A Survey on Robotics with Foundation Models  toward Embodied AI

[40] Scalable Interactive Machine Learning for Future Command and Control

[41] Learning Neuro-Symbolic Skills for Bilevel Planning

[42] Milestones in Autonomous Driving and Intelligent Vehicles Part II    Perception and Planning

[43] Deep Model-Based Reinforcement Learning for High-Dimensional Problems, a   Survey

[44] IR-VIC  Unsupervised Discovery of Sub-goals for Transfer in RL

[45] Subgoal-based Reward Shaping to Improve Efficiency in Reinforcement   Learning

[46] Constrained Policy Optimization via Bayesian World Models

[47] Categories from scratch

[48] Big Learning

[49] Foundation Models for Decision Making  Problems, Methods, and   Opportunities

[50] A Compositional Approach to Creating Architecture Frameworks with an   Application to Distributed AI Systems

[51] Beyond the Leaderboard  Insight and Deployment Challenges to Address   Research Problems

[52] On the Opportunities and Risks of Foundation Models

[53] Towards Responsible AI in the Era of Generative AI  A Reference   Architecture for Designing Foundation Model based Systems

[54] Delving into Multi-modal Multi-task Foundation Models for Road Scene   Understanding  From Learning Paradigm Perspectives

[55] Grounding Foundation Models through Federated Transfer Learning  A   General Framework

[56] Proximal Policy Optimization Algorithms

[57] Beyond Stationarity  Convergence Analysis of Stochastic Softmax Policy   Gradient Methods

[58] Zeroth-Order Actor-Critic

[59] Modified DDPG car-following model with a real-world human driving   experience with CARLA simulator

[60] Combining policy gradient and Q-learning

[61] Secure Federated Transfer Learning

[62] Conformal Predictive Safety Filter for RL Controllers in Dynamic   Environments

[63] Safe Reinforcement Learning via Hierarchical Adaptive Chance-Constraint   Safeguards

[64] Safe Reinforcement Learning Using Robust Control Barrier Functions

[65] DDM-Lag   A Diffusion-based Decision-making Model for Autonomous   Vehicles with Lagrangian Safety Enhancement

[66] Internet of Autonomous Vehicles  Architecture, Features, and   Socio-Technological Challenges

[67] Prompt-Augmented Linear Probing  Scaling beyond the Limit of Few-shot   In-Context Learners

[68] Towards Task Sampler Learning for Meta-Learning

[69] Curiosity-driven Exploration for Mapless Navigation with Deep   Reinforcement Learning

[70] Waymax  An Accelerated, Data-Driven Simulator for Large-Scale Autonomous   Driving Research

[71] Active Deep Q-learning with Demonstration

[72] Integrating Behavior Cloning and Reinforcement Learning for Improved   Performance in Dense and Sparse Reward Environments

[73] Data Quality in Imitation Learning

[74] Decision Making for Autonomous Driving in Interactive Merge Scenarios   via Learning-based Prediction

[75] Inverse Reward Design

[76] Sample-efficient Adversarial Imitation Learning

[77] Kernel-based diffusion approximated Markov decision processes for   autonomous navigation and control on unstructured terrains

[78] Gradient Informed Proximal Policy Optimization

[79] Direct and indirect reinforcement learning

[80] On-the-fly Denoising for Data Augmentation in Natural Language   Understanding

[81] Approximate Model-Based Shielding for Safe Reinforcement Learning

[82] Constraint-Conditioned Policy Optimization for Versatile Safe   Reinforcement Learning

[83] Bridging the Domain Gap between Synthetic and Real-World Data for   Autonomous Driving

[84] Sim-to-Real Transfer of Robotic Control with Dynamics Randomization

[85] Rethinking Sim2Real  Lower Fidelity Simulation Leads to Higher Sim2Real   Transfer in Navigation

[86] Barrier Functions Inspired Reward Shaping for Reinforcement Learning

[87] Learning to Shape Rewards using a Game of Two Partners

[88] Relational Self-Supervised Learning

[89] Vehicle Lane Change Prediction based on Knowledge Graph Embeddings and   Bayesian Inference

[90] Lane Change Decision-Making through Deep Reinforcement Learning

[91] Time-to-Collision-Aware Lane-Change Strategy Based on Potential Field   and Cubic Polynomial for Autonomous Vehicles

[92] Offline Imitation Learning with Suboptimal Demonstrations via Relaxed   Distribution Matching

[93] Barrier-Enhanced Homotopic Parallel Trajectory Optimization for   Safety-Critical Autonomous Driving

[94] A novel framework for adaptive stress testing of autonomous vehicles in   highways

[95] Graph Attention Network for Lane-Wise and Topology-Invariant   Intersection Traffic Simulation

[96] DimCL  Dimensional Contrastive Learning For Improving Self-Supervised   Learning

[97] SDGym  Low-Code Reinforcement Learning Environments using System   Dynamics Models

[98] Towards Safe Load Balancing based on Control Barrier Functions and Deep   Reinforcement Learning

[99] Do Androids Dream of Electric Fences  Safety-Aware Reinforcement   Learning with Latent Shielding

[100] Towards Goal-oriented Intelligent Tutoring Systems in Online Education

[101] Ethical Decision Making During Automated Vehicle Crashes

[102] Learning-based Ecological Adaptive Cruise Control of Autonomous Electric   Vehicles  A Comparison of ADP, DQN and DDPG Approaches

[103] Real-time Ecological Velocity Planning for Plug-in Hybrid Vehicles with   Partial Communication to Traffic Lights

[104] Safe Offline Reinforcement Learning with Feasibility-Guided Diffusion   Model

[105] Exploring the Lottery Ticket Hypothesis with Explainability Methods    Insights into Sparse Network Performance

[106] High-speed Autonomous Racing using Trajectory-aided Deep Reinforcement   Learning

[107] Smart Roads  Roadside Perception, Vehicle-Road Cooperation and Business   Model

[108] How Simulation Helps Autonomous Driving A Survey of Sim2real, Digital   Twins, and Parallel Intelligence

[109] Continual Domain Randomization

[110] Robot Fine-Tuning Made Easy  Pre-Training Rewards and Policies for   Autonomous Real-World Reinforcement Learning

[111] SafeShift  Safety-Informed Distribution Shifts for Robust Trajectory   Prediction in Autonomous Driving

[112] Benchmarking Data Science Agents

[113] Weathering Ongoing Uncertainty  Learning and Planning in a Time-Varying   Partially Observable Environment

[114] Adapting to Continuous Covariate Shift via Online Density Ratio   Estimation

[115] Introspective Experience Replay  Look Back When Surprised

[116] RTAEval  A framework for evaluating runtime assurance logic

[117] GUARD  A Safe Reinforcement Learning Benchmark

[118] Comparing Run Time Assurance Approaches for Safe Spacecraft Docking

[119] Why Guided Dialog Policy Learning performs well  Understanding the role   of adversarial learning and its alternative

[120] Adversarial Unlearning  Reducing Confidence Along Adversarial Directions

[121] On the Robustness of Safe Reinforcement Learning under Observational   Perturbations

[122] FL-GUARD  A Holistic Framework for Run-Time Detection and Recovery of   Negative Federated Learning

[123] Computation of Nash Equilibria of Attack and Defense Games on Networks

[124] Beyond Worst-case Attacks  Robust RL with Adaptive Defense via   Non-dominated Policies

[125] A Survey on Interpretable Reinforcement Learning

[126] POLICEd RL  Learning Closed-Loop Robot Control Policies with Provable   Satisfaction of Hard Constraints

[127] AdaLoRA  Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning

[128] Triple Regression for Camera Agnostic Sim2Real Robot Grasping and   Manipulation Tasks

[129] Comparison of Waymo Rider-Only Crash Data to Human Benchmarks at 7.1   Million Miles

[130] Privacy-Preserving in Blockchain-based Federated Learning Systems

[131] Muffin  A Framework Toward Multi-Dimension AI Fairness by Uniting   Off-the-Shelf Models

[132] Decision-making Strategy on Highway for Autonomous Vehicles using Deep   Reinforcement Learning

[133] Safe, Efficient, Comfort, and Energy-saving Automated Driving through   Roundabout Based on Deep Reinforcement Learning

[134] Comprehensive Training and Evaluation on Deep Reinforcement Learning for   Automated Driving in Various Simulated Driving Maneuvers

[135] A Deep Reinforcement Learning Framework for Eco-driving in Connected and   Automated Hybrid Electric Vehicles

[136] Improving Generalization of Reinforcement Learning with Minimax   Distributional Soft Actor-Critic

[137] Encoding Distributional Soft Actor-Critic for Autonomous Driving in   Multi-lane Scenarios

[138] Addressing Action Oscillations through Learning Policy Inertia

[139] Actor-Critic Reinforcement Learning with Phased Actor

[140] Rethinking ValueDice  Does It Really Improve Performance 

[141] Inverse Reinforcement Learning by Estimating Expertise of Demonstrators

[142] Imitation Learning from Imperfect Demonstration

[143] Exploring Beyond-Demonstrator via Meta Learning-Based Reward   Extrapolation

[144] Inverse Reinforcement Learning without Reinforcement Learning

[145] Distance-rank Aware Sequential Reward Learning for Inverse Reinforcement   Learning with Sub-optimal Demonstrations

[146] Context-Hierarchy Inverse Reinforcement Learning

[147] Robust Learning from Observation with Model Misspecification

[148] Wasserstein Distance guided Adversarial Imitation Learning with Reward   Shape Exploration

[149] Discriminator-Guided Model-Based Offline Imitation Learning

[150] Non-Adversarial Imitation Learning and its Connections to Adversarial   Methods

[151] Energy-Based Imitation Learning

[152] DiffAIL  Diffusion Adversarial Imitation Learning

[153] When Will Generative Adversarial Imitation Learning Algorithms Attain   Global Convergence

[154] CLARE  Conservative Model-Based Reward Learning for Offline Inverse   Reinforcement Learning

[155] State-only Imitation with Transition Dynamics Mismatch

[156] Coherent Soft Imitation Learning

[157] Fast Policy Learning through Imitation and Reinforcement

[158] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods

[159] Separated Proportional-Integral Lagrangian for Chance Constrained   Reinforcement Learning

[160] Constrained Variational Policy Optimization for Safe Reinforcement   Learning

[161] Trust Region-Based Safe Distributional Reinforcement Learning for   Multiple Constraints

[162] Policy Bifurcation in Safe Reinforcement Learning

[163] Leveraging Approximate Model-based Shielding for Probabilistic Safety   Guarantees in Continuous Environments

[164] Stable and Safe Reinforcement Learning via a Barrier-Lyapunov   Actor-Critic Approach

[165] NLBAC  A Neural Ordinary Differential Equations-based Framework for   Stable and Safe Reinforcement Learning

[166] Safe Reinforcement Learning via Confidence-Based Filters

[167] Safety Filtering for Reinforcement Learning-based Adaptive Cruise   Control

[168] ISAACS  Iterative Soft Adversarial Actor-Critic for Safety

[169] Certifying Safety in Reinforcement Learning under Adversarial   Perturbation Attacks

[170] Robust Policy Learning over Multiple Uncertainty Sets

[171] SafeRL-Kit  Evaluating Efficient Reinforcement Learning Methods for Safe   Autonomous Driving

[172] DEIR  Efficient and Robust Exploration through   Discriminative-Model-Based Episodic Intrinsic Rewards

[173] Redeeming Intrinsic Rewards via Constrained Optimization

[174] Goal-conditioned Offline Planning from Curious Exploration

[175] Efficient Online Reinforcement Learning with Offline Data

[176] Offline Data Enhanced On-Policy Policy Gradient with Provable Guarantees

[177] Active Policy Improvement from Multiple Black-box Oracles

[178] The Challenges of Exploration for Offline Reinforcement Learning

[179] Evolution-Guided Policy Gradient in Reinforcement Learning

[180] ERL-Re$^2$  Efficient Evolutionary Reinforcement Learning with Shared   State Representation and Individual Policy Representation

[181] CEM-RL  Combining evolutionary and gradient-based methods for policy   search

[182] Decoupled Exploration and Exploitation Policies for Sample-Efficient   Reinforcement Learning

[183] MAME   Model-Agnostic Meta-Exploration

[184] First-Explore, then Exploit  Meta-Learning Intelligent Exploration

[185] Careful at Estimation and Bold at Exploration

[186] Designing Rewards for Fast Learning

[187] Deep Reinforcement Learning for 2D Physics-Based Object Manipulation in   Clutter

[188] Useful Policy Invariant Shaping from Arbitrary Advice

[189] Magnetic Field-Based Reward Shaping for Goal-Conditioned Reinforcement   Learning

[190] Reward Uncertainty for Exploration in Preference-based Reinforcement   Learning

[191] Symbol Guided Hindsight Priors for Reward Learning from Human   Preferences

[192] RL-VLM-F  Reinforcement Learning from Vision Language Foundation Model   Feedback

[193] Towards Socially and Morally Aware RL agent  Reward Design With LLM

[194] Utility-Based Reinforcement Learning  Unifying Single-objective and   Multi-objective Reinforcement Learning

[195] A Risk-Sensitive Approach to Policy Optimization

[196] Risk-sensitive Markov Decision Process and Learning under General   Utility Functions

[197] Reward Machines  Exploiting Reward Function Structure in Reinforcement   Learning

[198] DrS  Learning Reusable Dense Rewards for Multi-Stage Tasks

[199] Sample Efficient Reinforcement Learning by Automatically Learning to   Compose Subtasks

[200] Behavior Alignment via Reward Function Optimization

[201] Reward Tampering Problems and Solutions in Reinforcement Learning  A   Causal Influence Diagram Perspective

[202] Choices, Risks, and Reward Reports  Charting Public Policy for   Reinforcement Learning Systems

[203] Jump-Start Reinforcement Learning

[204] Launchpad  Learning to Schedule Using Offline and Online RL Methods

[205] How to Spend Your Robot Time  Bridging Kickstarting and Offline   Reinforcement Learning for Vision-based Robotic Manipulation

[206] MOORe  Model-based Offline-to-Online Reinforcement Learning

[207] PROTO  Iterative Policy Regularized Offline-to-Online Reinforcement   Learning

[208] Uni-O4  Unifying Online and Offline Deep Reinforcement Learning with   Multi-Step On-Policy Optimization

[209] A Simple Unified Uncertainty-Guided Framework for Offline-to-Online   Reinforcement Learning

[210] Planning to Go Out-of-Distribution in Offline-to-Online Reinforcement   Learning

[211] Offline Retraining for Online RL  Decoupled Policy Learning to Mitigate   Exploration Bias

[212] Dual RL  Unification and New Methods for Reinforcement and Imitation   Learning

[213] Behavior Proximal Policy Optimization

[214] P3O  Policy-on Policy-off Policy Optimization

[215] Hundreds Guide Millions  Adaptive Offline Reinforcement Learning with   Expert Guidance

[216] Train Once, Get a Family  State-Adaptive Balances for Offline-to-Online   Reinforcement Learning

[217] Optimistic Model Rollouts for Pessimistic Offline Policy Optimization

[218] Conservative Q-Learning for Offline Reinforcement Learning

[219] Mildly Conservative Q-Learning for Offline Reinforcement Learning

[220] Pessimistic Bootstrapping for Uncertainty-Driven Offline Reinforcement   Learning

[221] Confidence-Conditioned Value Functions for Offline Reinforcement   Learning

[222] A Minimalist Approach to Offline Reinforcement Learning

[223] BRAC+  Improved Behavior Regularized Actor Critic for Offline   Reinforcement Learning

[224] Advantage-Aware Policy Optimization for Offline Reinforcement Learning

[225] Offline Reinforcement Learning with Soft Behavior Regularization

[226] Offline Reinforcement Learning with Implicit Q-Learning

[227] Offline RL with No OOD Actions  In-Sample Learning via Implicit Value   Regularization

[228] Critic Regularized Regression

[229] When Should We Prefer Offline Reinforcement Learning Over Behavioral   Cloning 

[230] Harnessing Mixed Offline Reinforcement Learning Datasets via Trajectory   Weighting

[231] Offline RL With Realistic Datasets  Heteroskedasticity and Support   Constraints

[232] Beyond Uniform Sampling  Offline Reinforcement Learning with Imbalanced   Datasets

[233] Curriculum Offline Imitation Learning

[234] Cal-QL  Calibrated Offline RL Pre-Training for Efficient Online   Fine-Tuning

[235] Adaptive Policy Learning for Offline-to-Online Reinforcement Learning

[236] MOPO  Model-based Offline Policy Optimization

[237] Representation Matters  Offline Pretraining for Sequential Decision   Making

[238] Action-Quantized Offline Reinforcement Learning for Robotic Skill   Learning

[239] LIDAR-Camera Fusion for Road Detection Using Fully Convolutional Neural   Networks

[240] HYDRA -- Hyper Dependency Representation Attentions

[241] Deep Tempering

[242] Deep Sensor Fusion with Pyramid Fusion Networks for 3D Semantic   Segmentation

[243] Conformal calibrators

[244] From One to Many  Dynamic Cross Attention Networks for LiDAR and Camera   Fusion

[245] Cognitive TransFuser  Semantics-guided Transformer-based Sensor Fusion   for Improved Waypoint Prediction

[246] Sensor Fusion by Spatial Encoding for Autonomous Driving

[247] Selective Sensor Fusion for Neural Visual-Inertial Odometry

[248] Learning Selective Sensor Fusion for States Estimation

[249] UNO  Uncertainty-aware Noisy-Or Multimodal Fusion for Unanticipated   Input Degradation

[250] 2DPASS  2D Priors Assisted Semantic Segmentation on LiDAR Point Clouds

[251] MaskedFusion360  Reconstruct LiDAR Data by Querying Camera Features

[252] Shared Cross-Modal Trajectory Prediction for Autonomous Driving

[253] Object Detection and Classification in Occupancy Grid Maps using Deep   Convolutional Networks

[254] FISHING Net  Future Inference of Semantic Heatmaps In Grids

[255] PolarNet  Accelerated Deep Open Space Segmentation Using Automotive   Radar in Polar Domain

[256] Rules of the Road  Predicting Driving Behavior with a Convolutional   Model of Semantic Interactions

[257] CalibFormer  A Transformer-based Automatic LiDAR-Camera Calibration   Network

[258] HydraFusion  Context-Aware Selective Sensor Fusion for Robust and   Efficient Autonomous Vehicle Perception

[259] Towards holistic scene understanding  Semantic segmentation and beyond

[260] Predicting Semantic Map Representations from Images using Pyramid   Occupancy Networks

[261] Monocular Semantic Occupancy Grid Mapping with Convolutional Variational   Encoder-Decoder Networks

[262] Dynamic Semantic Occupancy Mapping using 3D Scene Flow and Closed-Form   Bayesian Inference

[263] Neural Map Prior for Autonomous Driving

[264] Neural Groundplans  Persistent Neural Scene Representations from a   Single Image

[265] Multi-Object Navigation with dynamically learned neural implicit   representations

[266] OccFlowNet  Towards Self-supervised Occupancy Estimation via   Differentiable Rendering and Occupancy Flow

[267] Hierarchical Representations and Explicit Memory  Learning Effective   Navigation Policies on 3D Scene Graphs using Graph Neural Networks

[268] Simultaneous Mapping and Target Driven Navigation

[269] Generalized Label-Efficient 3D Scene Parsing via Hierarchical Feature   Aligned Pre-Training and Region-Aware Fine-tuning

[270] Learning Navigational Visual Representations with Semantic Map   Supervision

[271] Texture Underfitting for Domain Adaptation

[272] Social-DualCVAE  Multimodal Trajectory Forecasting Based on Social   Interactions Pattern Aware and Dual Conditional Variational Auto-Encoder

[273] SoPhie  An Attentive GAN for Predicting Paths Compliant to Social and   Physical Constraints

[274] Trajectron++  Dynamically-Feasible Trajectory Forecasting With   Heterogeneous Data

[275] Multiple Futures Prediction

[276] Social-WaGDAT  Interaction-aware Trajectory Prediction via Wasserstein   Graph Double-Attention Network

[277] Spatio-Temporal Graph Dual-Attention Network for Multi-Agent Prediction   and Tracking

[278] Polar Collision Grids  Effective Interaction Modelling for Pedestrian   Trajectory Prediction in Shared Space Using Collision Checks

[279] M2I  From Factored Marginal Trajectory Prediction to Interactive   Prediction

[280] SIMMF  Semantics-aware Interactive Multiagent Motion Forecasting for   Autonomous Vehicle Driving

[281] ProIn  Learning to Predict Trajectory Based on Progressive Interactions   for Autonomous Driving

[282] GET-DIPP  Graph-Embedded Transformer for Differentiable Integrated   Prediction and Planning

[283] TNT  Target-driveN Trajectory Prediction

[284] PePScenes  A Novel Dataset and Baseline for Pedestrian Action Prediction   in 3D

[285] LOKI  Long Term and Key Intentions for Trajectory Prediction

[286] VRUNet  Multi-Task Learning Model for Intent Prediction of Vulnerable   Road Users

[287] PedFormer  Pedestrian Behavior Prediction via Cross-Modal Attention   Modulation and Gated Multitask Learning

[288] Learning Interaction-aware Motion Prediction Model for Decision-making   in Autonomous Driving

[289] What-If Motion Prediction for Autonomous Driving

[290] ScePT  Scene-consistent, Policy-based Trajectory Predictions for   Planning

[291] Prediction-aware and Reinforcement Learning based Altruistic Cooperative   Driving

[292] Towards trustworthy multi-modal motion prediction  Holistic evaluation   and interpretability of outputs

[293] Behavioral Intention Prediction in Driving Scenes  A Survey

[294] ProphNet  Efficient Agent-Centric Motion Forecasting with   Anchor-Informed Proposals

[295] World Models

[296] Dream to Control  Learning Behaviors by Latent Imagination

[297] Separating the World and Ego Models for Self-Driving

[298] Iso-Dream  Isolating and Leveraging Noncontrollable Visual Dynamics in   World Models

[299] Model-Based Reinforcement Learning with Isolated Imaginations

[300] OccWorld  Learning a 3D Occupancy World Model for Autonomous Driving

[301] Copilot4D  Learning Unsupervised World Models for Autonomous Driving via   Discrete Diffusion

[302] Facing Off World Model Backbones  RNNs, Transformers, and S4

[303] Mastering Atari with Discrete World Models

[304] Model-Based Imitation Learning for Urban Driving

[305] Forecaster  Towards Temporally Abstract Tree-Search Planning from Pixels

[306] Hieros  Hierarchical Imagination on Structured State Space Sequence   World Models

[307] Tree-structured Policy Planning with Learned Behavior Models

[308] Interactive Joint Planning for Autonomous Vehicles

[309] Graph networks as learnable physics engines for inference and control

[310] World Models via Policy-Guided Trajectory Diffusion

[311] Continual Learning Using World Models for Pseudo-Rehearsal

[312] The Effectiveness of World Models for Continual Reinforcement Learning

[313] Informal Safety Guarantees for Simulated Optimizers Through   Extrapolation from Partial Simulations

[314] Causal World Models by Unsupervised Deconfounding of Physical Dynamics

[315] Perceive, Predict, and Plan  Safe Motion Planning Through Interpretable   Semantic Representations

[316] Pixel State Value Network for Combined Prediction and Planning in   Interactive Environments

[317] Occupancy Prediction-Guided Neural Planner for Autonomous Driving

[318] Hybrid-Prediction Integrated Planning for Autonomous Driving

[319] InteractionNet  Joint Planning and Prediction for Autonomous Driving   with Transformers

[320] DTPP  Differentiable Joint Conditional Prediction and Cost Evaluation   for Tree Policy Planning in Autonomous Driving

[321] Long-Horizon Visual Planning with Goal-Conditioned Hierarchical   Predictors

[322] Neural Modular Control for Embodied Question Answering

[323] Entity Abstraction in Visual Model-Based Reinforcement Learning

[324] Reasoning About Physical Interactions with Object-Oriented Prediction   and Planning

[325] Active Predictive Coding  A Unified Neural Framework for Learning   Hierarchical World Models for Perception and Planning

[326] Grid-Centric Traffic Scenario Perception for Autonomous Driving  A   Comprehensive Review

[327] Towards Explainability in Modular Autonomous Vehicle Software

[328] End-to-end Autonomous Driving  Challenges and Frontiers

[329] Level 2 Autonomous Driving on a Single Device  Diving into the Devils of   Openpilot

[330] Safety Implications of Explainable Artificial Intelligence in End-to-End   Autonomous Driving

[331] Navigating to Objects in the Real World

[332] Self-Supervised Simultaneous Multi-Step Prediction of Road Dynamics and   Cost Map

[333] DriveAdapter  Breaking the Coupling Barrier of Perception and Planning   in End-to-End Autonomous Driving

[334] DiffStack  A Differentiable and Modular Control Stack for Autonomous   Vehicles

[335] DriveCoT  Integrating Chain-of-Thought Reasoning with End-to-End Driving

[336] What Matters to Enhance Traffic Rule Compliance of Imitation Learning   for Automated Driving

[337] Action and Trajectory Planning for Urban Autonomous Driving with   Hierarchical Reinforcement Learning

[338] State-Conditioned Adversarial Subgoal Generation

[339] Hierarchical Reinforcement Learning with Timed Subgoals

[340] CRISP  Curriculum inducing Primitive Informed Subgoal Prediction

[341] Landmark-Guided Subgoal Generation in Hierarchical Reinforcement   Learning

[342] Adjacency constraint for efficient hierarchical reinforcement learning

[343] Generating Adjacency-Constrained Subgoals in Hierarchical Reinforcement   Learning

[344] Diversity-Driven Extensible Hierarchical Reinforcement Learning

[345] Hierarchical Reinforcement Learning with AI Planning Models

[346] Hierarchical Program-Triggered Reinforcement Learning Agents For   Automated Driving

[347] LLM Augmented Hierarchical Agents

[348] Hierarchical Reinforcement Learning By Discovering Intrinsic Options

[349] Value Function Spaces  Skill-Centric State Abstractions for Long-Horizon   Reasoning

[350] ReLMoGen  Leveraging Motion Generation in Reinforcement Learning for   Mobile Manipulation

[351] Emergency action termination for immediate reaction in hierarchical   reinforcement learning

[352] Imagination-Augmented Hierarchical Reinforcement Learning for Safe and   Interactive Autonomous Driving in Urban Environments

[353] Multi-Agent Reinforcement Learning for Connected and Automated Vehicles   Control  Recent Advancements and Future Prospects

[354] On Multi-Agent Deep Deterministic Policy Gradients and their   Explainability for SMARTS Environment

[355] Social Coordination and Altruism in Autonomous Driving

[356] Robustness and Adaptability of Reinforcement Learning based Cooperative   Autonomous Driving in Mixed-autonomy Traffic

[357] The Synergy Between Optimal Transport Theory and Multi-Agent   Reinforcement Learning

[358] Formal Contracts Mitigate Social Dilemmas in Multi-Agent RL

[359] Interactive Autonomous Navigation with Internal State Inference and   Interactivity Estimation

[360] A Multi-Agent Reinforcement Learning Approach For Safe and Efficient   Behavior Planning Of Connected Autonomous Vehicles

[361] Communication-Efficient Cooperative Multi-Agent PPO via Regulated   Segment Mixture in Internet of Vehicles

[362] Communication-Efficient Decentralized Multi-Agent Reinforcement Learning   for Cooperative Adaptive Cruise Control

[363] Networked Multi-Agent Reinforcement Learning with Emergent Communication

[364] Effective Communications  A Joint Learning and Communication Framework   for Multi-Agent Reinforcement Learning over Noisy Channels

[365] Graph Reinforcement Learning Application to Co-operative Decision-Making   in Mixed Autonomy Traffic  Framework, Survey, and Challenges

[366] Efficient Connected and Automated Driving System with Multi-agent Graph   Reinforcement Learning

[367] Spatial-Temporal-Aware Safe Multi-Agent Reinforcement Learning of   Connected Autonomous Vehicles in Challenging Scenarios

[368] Multi-agent Reinforcement Learning for Cooperative Lane Changing of   Connected and Autonomous Vehicles in Mixed Traffic

[369] Deep Multi-agent Reinforcement Learning for Highway On-Ramp Merging in   Mixed Traffic

[370] Interaction-aware Decision Making with Adaptive Strategies under Merging   Scenarios

[371] iPLAN  Intent-Aware Planning in Heterogeneous Traffic via Distributed   Multi-Agent Reinforcement Learning

[372] DriveGPT4  Interpretable End-to-end Autonomous Driving via Large   Language Model

[373] DriveMLM  Aligning Multi-Modal Large Language Models with Behavioral   Planning States for Autonomous Driving

[374] Drive Like a Human  Rethinking Autonomous Driving with Large Language   Models

[375] LanguageMPC  Large Language Models as Decision Makers for Autonomous   Driving

[376] Igniting Language Intelligence  The Hitchhiker's Guide From   Chain-of-Thought Reasoning to Language Agents

[377] DriveVLM  The Convergence of Autonomous Driving and Large   Vision-Language Models

[378] Reason2Drive  Towards Interpretable and Chain-based Reasoning for   Autonomous Driving

[379] Look Before You Leap  Unveiling the Power of GPT-4V in Robotic   Vision-Language Planning

[380] 3D-LLM  Injecting the 3D World into Large Language Models

[381] Using Left and Right Brains Together  Towards Vision and Language   Planning

[382] LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

[383] LLM-Assist  Enhancing Closed-Loop Planning with Language-Based Reasoning

[384] Evaluation and Enhancement of Semantic Grounding in Large   Vision-Language Models

[385] RePLan  Robotic Replanning with Perception and Language Models

[386] Inner Monologue  Embodied Reasoning through Planning with Language   Models

[387] Driving among Flatmobiles  Bird-Eye-View occupancy grids from a   monocular camera for holistic trajectory planning

[388] LOPR  Latent Occupancy PRediction using Generative Models

[389] VAD  Vectorized Scene Representation for Efficient Autonomous Driving

[390] Social Occlusion Inference with Vectorized Representation for Autonomous   Driving

[391] Embed to Control Partially Observed Systems  Representation Learning   with Provable Sample Efficiency

[392] Action-Sufficient State Representation Learning for Control with   Structural Constraints

[393] Towards Learning Generalizable Driving Policies from Restricted Latent   Representations

[394] Interpretable End-to-end Urban Autonomous Driving with Latent Deep   Reinforcement Learning

[395] Cycle-Consistent World Models for Domain Independent Latent Imagination

[396] Driving Policy Transfer via Modularity and Abstraction

[397] Learning to Navigate from Simulation via Spatial and Semantic   Information Synthesis with Noise Model Embedding

[398] Representation Learning for Continuous Action Spaces is Beneficial for   Efficient Policy Learning

[399] Combined Reinforcement Learning via Abstract Representations

[400] PcLast  Discovering Plannable Continuous Latent States

[401] Longitudinal Dynamic versus Kinematic Models for Car-Following Control   Using Deep Reinforcement Learning

[402] Image-Based Conditioning for Action Policy Smoothness in Autonomous   Miniature Car Racing with Reinforcement Learning

[403] Smooth Trajectory Collision Avoidance through Deep Reinforcement   Learning

[404] Quadratic Q-network for Learning Continuous Control for Autonomous   Vehicles

[405] Continuous Control for Automated Lane Change Behavior Based on Deep   Deterministic Policy Gradient Algorithm

[406] Automated Lane Change Strategy using Proximal Policy Optimization-based   Deep Reinforcement Learning

[407] Vision-based DRL Autonomous Driving Agent with Sim2Real Transfer

[408] Reinforcement Learning from Simulation to Real World Autonomous Driving   using Digital Twin

[409] Spatiotemporal Costmap Inference for MPC via Deep Inverse Reinforcement   Learning

[410] On Social Interactions of Merging Behaviors at Highway On-Ramps in   Congested Traffic

[411] A Learning-based Discretionary Lane-Change Decision-Making Model with   Driving Style Awareness

[412] Learning Personalized Discretionary Lane-Change Initiation for Fully   Autonomous Driving Based on Reinforcement Learning

[413] Autonomous Highway Merging in Mixed Traffic Using Reinforcement Learning   and Motion Predictive Safety Controller

[414] Decision-Making under On-Ramp merge Scenarios by Distributional Soft   Actor-Critic Algorithm

[415] A Stackelberg Game Theoretic Model of Lane-Merging

[416] A Repeated Game Freeway Lane Changing Model

[417] Automated Lane Merging via Game Theory and Branch Model Predictive   Control

[418] Integrating Expert Guidance for Efficient Learning of Safe Overtaking in   Autonomous Driving Using Deep Reinforcement Learning

[419] Hierarchical automatic lane-changing motion planning  from self-optimum   to local-optimum

[420] Hierarchical Reinforcement Learning for Self-Driving Decision-Making   without Reliance on Labeled Driving Data

[421] A Hierarchical Architecture for Sequential Decision-Making in Autonomous   Driving using Deep Reinforcement Learning

[422] Decision-making at Unsignalized Intersection for Autonomous Vehicles    Left-turn Maneuver with Deep Reinforcement Learning

[423] Belief State Planning for Autonomously Navigating Urban Intersections

[424] Autonomous Driving at Intersections  A Critical-Turning-Point Approach   for Left Turns

[425] GamePlan  Game-Theoretic Multi-Agent Planning with Human Drivers at   Intersections, Roundabouts, and Merging

[426] Multi-Vehicle Control in Roundabouts using Decentralized Game-Theoretic   Planning

[427] Spatially and Seamlessly Hierarchical Reinforcement Learning for State   Space and Policy space in Autonomous Driving

[428] Integration of Reinforcement Learning Based Behavior Planning With   Sampling Based Motion Planning for Automated Driving

[429] State Dropout-Based Curriculum Reinforcement Learning for Self-Driving   at Unsignalized Intersections

[430] Reward-Driven Automated Curriculum Learning for Interaction-Aware   Self-Driving at Unsignalized Intersections

[431] Integrated Decision and Control at Multi-Lane Intersections with Mixed   Traffic Flow

[432] Navigating Occluded Intersections with Autonomous Vehicles using Deep   Reinforcement Learning

[433] TrafficSim  Learning to Simulate Realistic Multi-Agent Behaviors

[434] Multi-task Safe Reinforcement Learning for Navigating Intersections in   Dense Traffic

[435] GIN  Graph-based Interaction-aware Constraint Policy Optimization for   Autonomous Driving

[436] Robust Driving Policy Learning with Guided Meta Reinforcement Learning

[437] Scalable Decentralized Cooperative Platoon using Multi-Agent Deep   Reinforcement Learning

[438] Decentralized Cooperative Lane Changing at Freeway Weaving Areas Using   Multi-Agent Deep Reinforcement Learning

[439] LCS-TF  Multi-Agent Deep Reinforcement Learning-Based Intelligent   Lane-Change System for Improving Traffic Flow

[440] SocialLight  Distributed Cooperation Learning towards Network-Wide   Traffic Signal Control

[441] Feudal Multi-Agent Reinforcement Learning with Adaptive Network   Partition for Traffic Signal Control

[442] Large-Scale Traffic Signal Control Using Constrained Network Partition   and Adaptive Deep Reinforcement Learning

[443] Multi-Agent Reinforcement Learning Based on Representational   Communication for Large-Scale Traffic Signal Control

[444] D-HAL  Distributed Hierarchical Adversarial Learning for Multi-Agent   Interaction in Autonomous Intersection Management

[445] HARL  A Novel Hierachical Adversary Reinforcement Learning for   Automoumous Intersection Management

[446] Stable and Efficient Shapley Value-Based Reward Reallocation for   Multi-Agent Reinforcement Learning of Autonomous Vehicles

[447] Maximizing Road Capacity Using Cars that Influence People

[448] Combining Subgoal Graphs with Reinforcement Learning to Build a Rational   Pathfinder

[449] Planning-oriented Autonomous Driving

[450] MetaDrive  Composing Diverse Driving Scenarios for Generalizable   Reinforcement Learning

[451] Driver Dojo  A Benchmark for Generalizable Reinforcement Learning for   Autonomous Driving

[452] Diverse Policy Optimization for Structured Action Space

[453] ALMA  Hierarchical Learning for Composite Multi-Agent Tasks

[454] Read to Play (R2-Play)  Decision Transformer with Multimodal Game   Instruction

[455] Planning to Practice  Efficient Online Fine-Tuning by Composing Goals in   Latent Space

[456] Can Vehicle Motion Planning Generalize to Realistic Long-tail Scenarios 

[457] Searching for Optimal Runtime Assurance via Reachability and   Reinforcement Learning

[458] Bridging the Gap  Applying Assurance Arguments to MIL-HDBK-516C   Certification of a Neural Network Control System with ASIF Run Time Assurance   Architecture

[459] Model-based Dynamic Shielding for Safe and Efficient Multi-Agent   Reinforcement Learning

[460] Approximate Shielding of Atari Agents for Safe Exploration

[461] Safe Reinforcement Learning via Probabilistic Logic Shields

[462] Safety Shielding under Delayed Observation

[463] Dynamic Shielding for Reinforcement Learning in Black-Box Environments

[464] Data-Efficient Control Barrier Function Refinement

[465] Simultaneous Synthesis and Verification of Neural Control Barrier   Functions through Branch-and-Bound Verification-in-the-loop Training

[466] Learning a Formally Verified Control Barrier Function in Stochastic   Environment

[467] Learning Differentiable Safety-Critical Control using Control Barrier   Functions for Generalization to Novel Environments

[468] Safe Exploration in Reinforcement Learning  Training Backup Control   Barrier Functions with Zero Training Time Safety Violations

[469] Predictive control barrier functions  Enhanced safety mechanisms for   learning-based control

[470] Fast, Smooth, and Safe  Implicit Control Barrier Functions through   Reach-Avoid Differential Dynamic Programming

[471] Refining Control Barrier Functions through Hamilton-Jacobi Reachability

[472] Recursively Feasible Probabilistic Safe Online Learning with Control   Barrier Functions

[473] A Control Barrier Perspective on Episodic Learning via   Projection-to-State Safety

[474] SABLAS  Learning Safe Control for Black-box Dynamical Systems

[475] Learning Barrier Certificates  Towards Safe Reinforcement Learning with   Zero Training-time Violations

[476] Enforcing Hard Constraints with Soft Barriers  Safe Reinforcement   Learning in Unknown Stochastic Environments

[477] Correlation Alignment by Riemannian Metric for Domain Adaptation

[478] Generalizing to Unseen Domains with Wasserstein Distributional   Robustness under Limited Source Knowledge

[479] Robust Reinforcement Learning with Wasserstein Constraint

[480] Out-of-Distribution Generalization via Risk Extrapolation (REx)

[481] Efficient Test-Time Model Adaptation without Forgetting

[482] Uncertainty-Calibrated Test-Time Model Adaptation without Forgetting

[483] Resilient Practical Test-Time Adaptation  Soft Batch Normalization   Alignment and Entropy-driven Memory Bank

[484] AR-TTA  A Simple Method for Real-World Continual Test-Time Adaptation

[485] Better Practices for Domain Adaptation

[486] Conformal Predictive Systems Under Covariate Shift

[487] PAC Prediction Sets Under Covariate Shift

[488] Conformal Off-Policy Prediction for Multi-Agent Systems

[489] Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model

[490] Towards Robust Off-Policy Evaluation via Human Inputs

[491] Distributionally Robust Reinforcement Learning with Interactive Data   Collection  Fundamental Hardness and Near-Optimal Algorithm

[492] DOMAIN  MilDly COnservative Model-BAsed OfflINe Reinforcement Learning

[493] Robust Deep Reinforcement Learning against Adversarial Perturbations on   State Observations

[494] Better Safe Than Sorry  Preventing Delusive Adversaries with Adversarial   Training

[495] LAS-AT  Adversarial Training with Learnable Attack Strategy

[496] Robustifying Reinforcement Learning Agents via Action Space Adversarial   Training

[497] Defending against Adversarial Attack towards Deep Neural Networks via   Collaborative Multi-task Training

[498] Revisiting Model's Uncertainty and Confidences for Adversarial Example   Detection

[499] Test-time Detection and Repair of Adversarial Samples via Masked   Autoencoder

[500] Falsification-Based Robust Adversarial Reinforcement Learning

[501] Behaviour-Diverse Automatic Penetration Testing  A Curiosity-Driven   Multi-Objective Deep Reinforcement Learning Approach

[502] Red Teaming with Mind Reading  White-Box Adversarial Policies Against RL   Agents

[503] AART  AI-Assisted Red-Teaming with Diverse Data Generation for New   LLM-powered Applications

[504] MART  Improving LLM Safety with Multi-round Automatic Red-Teaming

[505] Targeted Attack on Deep RL-based Autonomous Driving with Learned Visual   Patterns

[506] Game Theory for Adversarial Attacks and Defenses

[507] Are Adversarial Examples Created Equal  A Learnable Weighted Minimax   Risk for Robustness under Non-uniform Attacks

[508] Data-efficient Domain Randomization with Bayesian Optimization

[509] AdaptSim  Task-Driven Simulation Adaptation for Sim-to-Real Transfer

[510] Adversarial Domain Randomization

[511] DROID  Minimizing the Reality Gap using Single-Shot Human Demonstration

[512] What Went Wrong  Closing the Sim-to-Real Gap via Differentiable Causal   Discovery

[513] Not Only Domain Randomization  Universal Policy with Embedding System   Identification

[514] Sim2real for Autonomous Vehicle Control using Executable Digital Twin

[515] AptSim2Real  Approximately-Paired Sim-to-Real Image Translation

[516] Sim-to-Real via Sim-to-Sim  Data-efficient Robotic Grasping via   Randomized-to-Canonical Adaptation Networks

[517] Facilitating Sim-to-real by Intrinsic Stochasticity of Real-Time   Simulation in Reinforcement Learning for Robot Manipulation

[518] Assessing Transferability from Simulation to Reality for Reinforcement   Learning

[519] Validate on Sim, Detect on Real -- Model Selection for Domain   Randomization

[520] When to Trust Your Simulator  Dynamics-Aware Hybrid Offline-and-Online   Reinforcement Learning

[521] A Comprehensive Review on Ontologies for Scenario-based Testing in the   Context of Autonomous Driving

[522] Toward Unsupervised Test Scenario Extraction for Automated Driving   Systems from Urban Naturalistic Road Traffic Data

[523] The highD Dataset  A Drone Dataset of Naturalistic Vehicle Trajectories   on German Highways for Validation of Highly Automated Driving Systems

[524] Parameterisation of lane-change scenarios from real-world data

[525] Automatic lane change scenario extraction and generation of scenarios in   OpenX format from real-world data

[526] Multi-Agent Vulnerability Discovery for Autonomous Driving with Hazard   Arbitration Reward

[527] Critical concrete scenario generation using scenario-based falsification

[528] Efficient falsification approach for autonomous vehicle validation using   a parameter optimisation technique based on reinforcement learning

[529] HiddenGems  Efficient safety boundary detection with active learning

[530] Probabilistic Metamodels for an Efficient Characterization of Complex   Driving Scenarios

[531] Performance Boundary Identification for the Evaluation of Automated   Vehicles using Gaussian Process Classification

[532] SafeBench  A Benchmarking Platform for Safety Evaluation of Autonomous   Vehicles

[533] NeuroNCAP  Photorealistic Closed-loop Safety Testing for Autonomous   Driving

[534] Pass-Fail Criteria for Scenario-Based Testing of Automated Driving   Systems

[535] A Counterfactual Safety Margin Perspective on the Scoring of Autonomous   Vehicles' Riskiness

[536] Quantitative Risk Indices for Autonomous Vehicle Training Systems

[537] Assessing Safety-Critical Systems from Operational Testing  A Study on   Autonomous Vehicles

[538] Tree-Based Scenario Classification  A Formal Framework for Coverage   Analysis on Test Drives of Autonomous Vehicles

[539] Determining the Tactical Challenge of Scenarios to Efficiently Test   Automated Driving Systems

[540] A Survey on Multimodal Large Language Models for Autonomous Driving

[541] A Language Agent for Autonomous Driving

[542] DiLu  A Knowledge-Driven Approach to Autonomous Driving with Large   Language Models

[543] Large Language Models As Faithful Explainers

[544] Large Language Models for Autonomous Driving  Real-World Experiments

[545] Human-Centric Autonomous Systems With LLMs for User Command Reasoning

[546] An Embodied Generalist Agent in 3D World

[547] 3D-VLA  A 3D Vision-Language-Action Generative World Model

[548] Embodied Understanding of Driving Scenarios

[549] Reasoning with Language Model is Planning with World Model

[550] Language Models Meet World Models  Embodied Experiences Enhance Language   Models

[551] Automated Evaluation of Large Vision-Language Models on Self-driving   Corner Cases

[552] EgoPlan-Bench  Benchmarking Egocentric Embodied Planning with Multimodal   Large Language Models

[553] Tuning-Free Accountable Intervention for LLM Deployment -- A   Metacognitive Approach

[554] The Moral Machine Experiment on Large Language Models

[555] LLM4Drive  A Survey of Large Language Models for Autonomous Driving

[556] Explainable AI for Safe and Trustworthy Autonomous Driving  A Systematic   Review

[557]  Explanation  is Not a Technical Term  The Problem of Ambiguity in XAI

[558] People Attribute Purpose to Autonomous Vehicles When Explaining Their   Behavior

[559] Expanding Explainability  Towards Social Transparency in AI systems

[560] TRUST XAI  Model-Agnostic Explanations for AI With a Case Study on IIoT   Security

[561] Challenging common interpretability assumptions in feature attribution   explanations

[562] Counterfactual Explanations as Interventions in Latent Space

[563] Counterfactual Explanations of Black-box Machine Learning Models using   Causal Discovery with Applications to Credit Rating

[564] Disagreement amongst counterfactual explanations  How transparency can   be deceptive

[565] It is not  accuracy vs. explainability  -- we need both for trustworthy   AI systems

[566] Measure Utility, Gain Trust  Practical Advice for XAI Researcher

[567] Roadmap of Designing Cognitive Metrics for Explainable Artificial   Intelligence (XAI)

[568] Exploring Explainable AI in the Financial Sector  Perspectives of Banks   and Supervisory Authorities

[569] The human-AI relationship in decision-making  AI explanation to support   people on justifying their decisions

[570] Towards Directive Explanations  Crafting Explainable AI Systems for   Actionable Human-AI Interactions

[571] Generative Negative Replay for Continual Learning

[572] Lifelong Learning of Spatiotemporal Representations with Dual-Memory   Recurrent Self-Organization

[573] Continual Interactive Behavior Learning With Traffic Divergence   Measurement  A Dynamic Gradient Scenario Memory Approach

[574] Distribution-Aware Continual Test-Time Adaptation for Semantic   Segmentation

[575] Expanding the Deployment Envelope of Behavior Prediction via Adaptive   Meta-Learning

[576] Meta Learning MPC using Finite-Dimensional Gaussian Process   Approximations

[577] Online Meta-Learning

[578] Learning to Learn How to Learn  Self-Adaptive Visual Navigation Using   Meta-Learning

[579] Safe Reinforcement Learning via Curriculum Induction

[580] Continual Driving Policy Optimization with Closed-Loop Individualized   Curricula

[581] Online Fast Adaptation and Knowledge Accumulation  a New Approach to   Continual Learning

[582] Rigorous Agent Evaluation  An Adversarial Approach to Uncover   Catastrophic Failures

[583] Continual World  A Robotic Benchmark For Continual Reinforcement   Learning

[584] To Explain or Not to Explain  A Study on the Necessity of Explanations   for Autonomous Vehicles

[585] Effects of Explanation Specificity on Passengers in Autonomous Driving

[586] Developing Situational Awareness for Joint Action with Autonomous   Vehicles

[587] Investigating HMIs to Foster Communications between Conventional   Vehicles and Autonomous Vehicles in Intersections

[588] From Spoken Thoughts to Automated Driving Commentary  Predicting and   Explaining Intelligent Vehicles' Actions

[589] Pre-trained Transformer-Enabled Strategies with Human-Guided Fine-Tuning   for End-to-end Navigation of Autonomous Vehicles

[590] Highly Parallelized Data-driven MPC for Minimal Intervention Shared   Control

[591] User Perception of Partially Automated Driving Systems  A Meaningful   Human Control Perspective on the Perception among Tesla Users

[592] Personalizing Driver Safety Interfaces via Driver Cognitive Factors   Inference

[593] Conditional Driving from Natural Language Instructions

[594] Moral and Social Ramifications of Autonomous Vehicles

[595] Socially Compatible Control Design of Automated Vehicle in Mixed Traffic

[596] Cooperative Autonomous Vehicles that Sympathize with Human Drivers

[597] ScenarioNet  Open-Source Platform for Large-Scale Traffic Scenario   Simulation and Modeling

[598] AutoVRL  A High Fidelity Autonomous Ground Vehicle Simulator for   Sim-to-Real Deep Reinforcement Learning

[599] Improving the Generalization of End-to-End Driving through Procedural   Generation

[600] Safety-Critical Scenario Generation Via Reinforcement Learning Based   Editing

[601] Bridging Data-Driven and Knowledge-Driven Approaches for Safety-Critical   Scenario Generation in Automated Vehicle Validation

[602] CaDRE  Controllable and Diverse Generation of Safety-Critical Driving   Scenarios using Real-World Trajectories

[603] CausalAF  Causal Autoregressive Flow for Safety-Critical Driving   Scenario Generation

[604] CAT  Closed-loop Adversarial Training for Safe End-to-End Driving

[605] Enhancing Autonomous Vehicle Training with Language Model Integration   and Critical Scenario Generation

[606] SafeAPT  Safe Simulation-to-Real Robot Learning using Diverse Policies   Learned in Simulation

[607] Sim-to-Lab-to-Real  Safe Reinforcement Learning with Shielding and   Generalization Guarantees

[608] GAIA-1  A Generative World Model for Autonomous Driving

[609] Learning Interactive Real-World Simulators

[610] Survey on AI Ethics  A Socio-technical Perspective

[611] Putting AI Ethics into Practice  The Hourglass Model of Organizational   AI Governance

[612] Taking Training Seriously  Human Guidance and Management-Based   Regulation of Artificial Intelligence

[613] A multilevel framework for AI governance

[614] Frontier AI Regulation  Managing Emerging Risks to Public Safety

[615] International Institutions for Advanced AI

[616] Data-Centric Governance

[617] The Promise and Peril of Artificial Intelligence -- Violet Teaming   Offers a Balanced Path Forward

[618] The Different Faces of AI Ethics Across the World  A   Principle-Implementation Gap Analysis

[619] FATE in AI  Towards Algorithmic Inclusivity and Accessibility

[620] Toward a Rational and Ethical Sociotechnical System of Autonomous   Vehicles  A Novel Application of Multi-Criteria Decision Analysis

[621] Ever heard of ethical AI  Investigating the salience of ethical AI   issues among the German population

[622] Particip-AI  A Democratic Surveying Framework for Anticipating Future AI   Use Cases, Harms and Benefits

[623] Connecting the Dots in Trustworthy Artificial Intelligence  From AI   Principles, Ethics, and Key Requirements to Responsible AI Systems and   Regulation

[624] Imitation with Spatial-Temporal Heatmap  2nd Place Solution for NuPlan   Challenge

[625] Hierarchical Game-Theoretic Planning for Autonomous Vehicles

[626] Towards Knowledge-driven Autonomous Driving

[627] Empowering Autonomous Driving with Large Language Models  A Safety   Perspective

[628] An Empirical Analysis of the Use of Real-Time Reachability for the   Safety Assurance of Autonomous Vehicles

[629] Ensuring Safe Autonomy  Navigating the Future of Autonomous Vehicles

[630] Milestones in Autonomous Driving and Intelligent Vehicles Part I    Control, Computing System Design, Communication, HD Map, Testing, and Human   Behaviors

[631] Recent Advancements in End-to-End Autonomous Driving using Deep   Learning  A Survey

[632] Comprehensive Reactive Safety  No Need For A Trajectory If You Have A   Strategy

[633] Drive Anywhere  Generalizable End-to-end Autonomous Driving with   Multi-modal Foundation Models


