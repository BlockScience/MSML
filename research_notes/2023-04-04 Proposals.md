# 4/4/2023 Proposals

## Boundary/Control/Exogenous Actions

- There should be a set way to define actions that are beginning chains of policies/mechanisms
- **Proposal 1**: We have control actions (also might be referred to as system actions) which describe the actions the system may do (rebalance a portfolio, decide to restock the store).
    - THIS JUST STARTS THE CHAIN, i.e. if it is restock the store it is the system sending the signal to restock with information to a policy that takes care of it and does any checking of things like enough money is there
- **Proposal 2**: Call actions that are from exogenous signals or user behaviors boundary actions
    - We possibly could distinguish further into signals vs. behavioral stuff but boundary actions may be the easier approach


## Blocks & Spaces

- **Proposal 3**: Refer to boundary, control, policy, and state update actions as blocks
    - For the boundary/control there will be no domain, however
    - It probably does make sense because they have domain port, codomain port, and do all the functionalities within
- **Proposal 4**: Refer to what was previously messages (the payloads being sent between what is now going to be called blocks) as spaces
    - Seems to be the same thing, only caveat is that we are going to be using the nested schema


## Entities and Global States

- **Proposal 5**: Use a loose definition that we entities can be any single or multiple object that we want to define with its own state
    - An example with the coffee example is that we could either have no entity for consumers if we are just counting them in the queue, or we create an entity for consumer if we want them to have richer behavior and tracking of specific attributes
- **Proposal 6**: Keep global state
    - While global state can be technically recovered by just grabbing most of the local states, there may also be specific global attributes such as the system time
    - We would have the metrics as well for it
    - We might be able to get rid of global state, but I have a personally feeling that it is just safer to leave in 

