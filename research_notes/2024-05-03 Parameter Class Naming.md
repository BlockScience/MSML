# Parameter Class Naming Research Note

## Problem Statement

The MSML currently has the ability to add a parameter class attribute to parameters which describes the use of the parameter. These three, explained below, are behavioral, functional and system. The goals are to:

1. Align the vocabulary used so that is easily understood for most audiences
2. Define out any missing parameter classes
3. Figure out any changes to the functionalities listed

## Current MSML Method

The following are the three tags to be used:

### Behavioral

- These parameters would NOT be seen in a production system but instead denote any behavioral assumptions that would impact a simulation
- The purpose of segmenting them like this is easier views when working with the simulation and also an ability to filter them out if the MSML is being used for implementation of production software instead of a simulation
- An example would be parameters for the random return distribution for a given price

### System

- These are parameters that MUST be in a production system as they relate to certain system parameters set
- An example would be a parameter that denotes a fixed exchange rate between two assets (although if this exchange rate changes it is probably better put as a state variable)
- Another example might be something like maximum capacity of workers for a power plant, there might be a hard upper limit due to regulation and this would be put in to act as the boundary on a policy of adding more workers

### Functional

- These are parameters that impact the functional form in two ways:
    - Functional parameters that map which policy option or boundary action option is implemented in a simulation or production system
    - Possibly specific functions used such as what return distribution to use (by being a string representing normal distribution, normal distribution with a skew, etc.)
- These MAY OR MAY NOT be in a production system
- Part of the purpose is to extend modularity, if we have three implementations of a policy, the functional parameterization can allow for easy switching of the functions to be used in a simulation (or possibly production software)
- MSML has built in functions for the metaprogramming that allow for combining through all policies, boundary actions, and other components that contain "options" and creating the functional parameters for those which have more than one option, ensuring users know which functions are modifiable and need to be specified for specific implementations


## BlockScience KMS Conversation

The following is a conversation between Sean McOwen, the BlockScience KMS LLM and Michael Zargham.

Sean: @KMS What different classes of parameters might exist in a systems engineering context?

KMS: In a systems engineering context, parameters can be broadly categorized into several classes based on their nature and the role they play within the system design and operation. While the specific article or source you're referring to might not explicitly list these classes, based on general knowledge in systems engineering, we can infer the following potential classes of parameters:
1. **Physical Parameters:** These include dimensions, materials properties, physical constants, and environmental conditions that the system will operate under. They are often determined through empirical measurements and are critical for the design and analysis of physical systems.
2. **Performance Parameters:** These parameters define the desired outcomes or performance metrics that the system should achieve. Examples include speed, efficiency, capacity, and reliability metrics. Performance parameters are crucial for evaluating whether a system meets its intended goals.
3. **Operational Parameters:** These parameters are related to the operation of the system, including user inputs, control settings, and operational modes. They can vary during the system's life cycle and are essential for ensuring the system operates within its intended parameters.
4. **Economic Parameters:** Cost, budget, and economic impact parameters fall into this category. They are vital for assessing the economic feasibility and sustainability of the system throughout its lifecycle.
5. **Environmental Parameters:** These involve external conditions and environmental impact considerations, such as emissions, energy consumption, and resource utilization. Environmental parameters are increasingly important in the context of sustainable design and regulatory compliance.
6. **Social Parameters:** User satisfaction, societal impact, and ethical considerations can also be viewed as parameters in systems design, especially for systems that interact closely with the public or have significant societal implications.
7. **Uncertainty Parameters:** These parameters account for the variability and uncertainty in system models and real-world operations. They are crucial for risk assessment and for designing systems that are robust and resilient under varying conditions.
In the Parameter Selection Under Uncertainty (PSuU) process, it's essential to identify and categorize these parameters appropriately to ensure a comprehensive analysis that covers all critical aspects of the system's design and operation. This helps in making informed decisions even under conditions of uncertainty.


Sean: @Zargham If you have a second, I believe you mentioned something before on this prior but I can't recall exactly.
I also thought the KMS response had some interesting possible name changes:
I like operational parameters instead of system parameters potentially or maybe it actually sounds more like functional. Perhaps environmental or uncertainty parameters instead of behavioral.

Zargham: @KMS the parameters as described are pretty "zoomed out" taxonomy with an emphasis on physical systems. While i find physical systems analogies very helpful for intuition, this kind of breakdown may not be helpful in developing a specific computational model of a digital infrastructure, such as a market. Our models are discrete event simulations which demonstrate potential behavior based on the interactions of subsystems. Generally: there are some mechanisms for which we have direct control such as tuning gains on a control system or market parameters like the size of a transaction fee; there are some mechanisms which are environmental in nature -- these are non-deterministic but also non-strategic, this can include noise on an actuator or other sources of uncertainty which can be parameterized by stochastic processes. there are some mechanisms which are behavioral in nature, are often strategic behaviors which adapt to changes in the systems behavior, they can be individuals or subpopulations or populations and the parameters of these behavioral models can include things like preference vectors, time discounting factors or full utility functions. All these parameters are defined locally within the context of such a model. the things which are called parameters, are precisely the assumptions within the model that we need to evaluate sensitivity to. as engineers we must find subsets of the potential values of the controllable parameters which reliably produce desirable outcomes (where what is desirable is itself a multicriterion optimization defined over the trajectories generated by executing this system). The final, and often most critical parameters for such a model are the metrics defining "desirable" and their relative priorities. All together these "parameters" allow us to do model based systems engineering workflows for digital infrastructures such as markets.

KMS: How can the broad taxonomy of parameters in systems engineering, which emphasizes physical systems, be adapted or applied to develop a specific computational model for a digital infrastructure like a market, considering the model involves discrete event simulations and parameters that include controllable mechanisms, environmental uncertainties, behavioral strategies, and critical metrics defining desirable outcomes?
1. In the context of systems engineering, which traditionally focuses on physical systems, what strategies can be implemented to modify its extensive taxonomy of parameters for creating a computational model tailored to a digital market infrastructure, especially when the model requires discrete event simulations and encompasses variables such as adjustable controls, external uncertainties, behavioral tactics, and key performance indicators?
2. How can we adjust the comprehensive parameter taxonomy used in systems engineering, primarily designed for physical systems, to suit the development of a computational model for a digital marketplace, taking into account the need for discrete event simulations and the inclusion of factors like manipulable controls, environmental unpredictability, strategic behaviors, and essential success metrics?
3. What approach can be taken to adapt the wide-ranging set of parameters identified in systems engineering for physical systems, to the crafting of a specific computational model for digital platforms like markets, where the model must incorporate discrete event simulations and account for variables such as control mechanisms, uncertainty from the environment, decision-making strategies, and critical measures for desired outcomes?Adapting the broad taxonomy of parameters from systems engineering, which traditionally emphasizes physical systems, to develop a specific computational model for a digital infrastructure like a market involves several key steps. This adaptation process requires a nuanced understanding of both the physical systems' engineering principles and the unique characteristics of digital systems and markets. Here's how the adaptation can be approached, especially when the model involves discrete event simulations and parameters that include controllable mechanisms, environmental uncertainties, behavioral strategies, and critical metrics defining desirable outcomes:
1. **Define System Goals and Objectives**: Start by clearly defining the goals and objectives of the digital market. This includes understanding the desired outcomes, such as efficiency, fairness, liquidity, or stability. These goals will guide the selection and definition of key performance indicators (KPIs) that will be used to measure the system's performance.
2. **Identify Control Parameters**: In a digital market, control parameters are variables that can be directly manipulated to influence the system's behavior. These could include pricing algorithms, matching algorithms, or rules for participant interaction. The identification of these parameters requires a deep understanding of the market's operational mechanisms and how they can be engineered or adjusted.
3. **Specify Environmental Parameters**: Environmental parameters represent external factors that cannot be controlled but must be accounted for in the model. In a digital market, these could include market volatility, regulatory changes, or shifts in user behavior. Modeling these parameters involves identifying relevant external variables and incorporating them into the simulation, often as inputs or boundary conditions.
4. **Characterize Behavioral Strategies**: Behavioral strategies reflect the actions and decisions of participants within the market. This involves modeling the decision-making processes of users, which can be based on rational, bounded rational, or other behavioral economics principles. Understanding these strategies is crucial for accurately simulating interactions within the market and

~ KMS Timed Out, Sean re-tried with same prompt ~

KMS: How can the concept of parameters in systems engineering be adapted to specifically suit the development of computational models for digital infrastructures like markets, considering the distinctions between controllable mechanisms, environmental uncertainties, behavioral strategies, and the critical role of defining desirable outcomes within the context of discrete event simulations?1. What strategies can be applied in systems engineering to tailor parameter concepts for building computational models in digital market infrastructures, with a focus on differentiating between controllable mechanisms, environmental uncertainties, behavioral strategies, and effectively setting desired outcomes in discrete event simulations?
2. In the context of systems engineering, how can parameterization be specifically adapted for the creation of computational models for digital infrastructures, such as markets, by addressing the nuances of controllable mechanisms, environmental uncertainties, behavioral strategies, and the importance of defining target outcomes in discrete event simulations?
3. How can systems engineering principles of parameter management be customized for developing computational models tailored to digital market infrastructures, taking into account the challenges of controllable mechanisms, environmental uncertainties, behavioral strategies, and the significance of establishing clear goals within discrete event simulations?Adapting the concept of parameters in systems engineering to suit the development of computational models for digital infrastructures, such as markets, involves a nuanced approach that accounts for the various facets of the system including controllable mechanisms, environmental uncertainties, behavioral strategies, and the definition of desirable outcomes. This adaptation can be achieved through a structured methodology that emphasizes the following aspects:
1. **Defining System Goals and Objectives**: Clearly articulate the desirable outcomes for the digital infrastructure. This involves identifying the key performance indicators (KPIs) that will measure the success of the system, such as efficiency, fairness, stability, and resilience. These goals provide a foundation for the entire model development process.
2. **Identification of Controllable Mechanisms**: Delineate the components or mechanisms within the system that can be directly controlled or manipulated. In the context of digital markets, this could include aspects like transaction fees, matching algorithms, liquidity provisions, and governance rules. These mechanisms serve as the primary levers through which the system's behavior can be influenced.
3. **Modeling Environmental Uncertainties**: Recognize and model the uncertainties that the system will face. This includes both external factors (such as market volatility and regulatory changes) and internal factors (such as participant behavior and technological failures). Utilizing techniques like stochastic modeling and Monte Carlo simulations can help in understanding how these uncertainties impact the system.
4. **Incorporating Behavioral Strategies**: Integrate models of participant behavior that reflect how users interact with the system under varying conditions. This involves the use of behavioral economics and game theory to predict responses to different system states and changes in controllable mechanisms. Behavioral models help in assessing the robustness of the system against strategic manipulation and emergent phenomena.
5. **Discrete Event Simulations (DES)**: Utilize DES as a tool to simulate the sequence of events that the system might experience. This allows for the examination of the system's performance under a wide range of scenarios, including extreme conditions. DES is particularly useful in capturing the dynamics of digital markets where interactions are discrete and events such as transactions can have significant impacts.
6. **Parameter Selection under Unc

~KMS Timed out Again~

Sean: @KMS Can you summarize this into just a list of potential parameter types/names?

KMS: In a systems engineering context, parameters can be broadly categorized based on their role and impact on the system. The potential types or names of parameters could include:
1. **Performance Parameters**: These define the operational capabilities of the system, such as speed, efficiency, capacity, and accuracy.
2. **Environmental Parameters**: These relate to the conditions under which the system will operate, including temperature, humidity, pressure, and external stress factors.
3. **Physical Parameters**: These include dimensions, weight, volume, and other physical characteristics of system components.
4. **Economic Parameters**: Cost, budget constraints, lifecycle cost, and return on investment considerations that influence system design and implementation.
5. **Quality Parameters**: Reliability, maintainability, availability, and other factors that affect the system's quality and operational lifespan.
6. **Safety Parameters**: Factors that ensure the safety of the system during its operation, including fail-safes, redundancy, and error handling mechanisms.
7. **User Experience Parameters**: Ergonomics, interface design, accessibility, and other factors that affect how users interact with the system.
8. **Regulatory and Compliance Parameters**: Requirements that the system must meet to comply with industry standards, legal regulations, and certification processes.
9. **Technical Parameters**: Specifications that detail the technical aspects of the system, such as software versions, hardware specifications, network protocols, and data formats.
10. **Security Parameters**: Measures and protocols that protect the system from unauthorized access, data breaches, and other security threats.
These parameters are not exhaustive and can overlap depending on the specific system and the context in which it operates. The selection and prioritization of these parameters are critical steps in the systems engineering process, influencing the design, development, and ultimate success of the system.