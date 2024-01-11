# JSON Schema

The specification presented here is the schema that MSML uses for standardized specs.

## Component Descriptions

### Types, States, Parameters & Entities
- **Types** - This is for defining what a type might in its most basic form. These could be single typings or compound typings. The point here is to allow for changing typing in one single place and having it flow through anywhere else. I.e. if one were to define the currency type as USD, but then the project switched to using EUR, it would just require changing currency to be EUR.
- **States** - All states that are present in the system, this can be local states for entities or the global system state
- **Stateful Metrics** - Variables that are not held directly in the state but can computed from the state & parameters
- **Parameters** - Both local and global parameters in the system that could be set
- **Entities** - an entity in the system such as a class of users that need to have certain states recorded, an entity for some sort of infrastructure such as a smart contract or treasury, etc.

### Blocks & Spaces
- **Spaces** - This defines input/ouput from functions. Similar to how typescript uses interfaces, this would ensure that if we have a policy call a mechanism, we could check that their messages/interfaces passed between matched up.
- **Boundary Actions** - The definition of different actions that might happen outside of the system such as customers coming into a shop. 
- **Control Actions** - The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low.
- **Policies** - A definition of the policies that handle all logical things. This could be, for example, a policy which determines what price is paid given an exogenous of someone putting in a market buy order for a stock
- **State Update Mechanisms** - Anything that updates state in the system, usually policies will call these with the outputs of logic. The reasoning to split them out is so that if at some point you want to add a recording variable every time an account is changed or do something like have a variable listener, you can just change the mechanism responsible for it in only one place.

### Transmission Channels
- **Action Transmission Channels** - The definitions of all the topology of the actions that are spurring on other actions, such as a policy calling another policy or state update mechanism.
- **State Update Transmission Channels** - The definitions of topology of mechanisms updating state, the start of the directed edge is from a mechanism and the end of the edge is the state attribute that is being updated.


### Metrics and KPIs

- **Metrics** - Any measurements to find things like averages of a variable over a period, defined in a way that we are trying to measure some sort of success, usually done after simulations are complete
- **KPIs** - A conversion of metrics to boolean values to decide if a metric is good enough or not. Possibly could also just be a value bounded between [0, 1].

## Types

- This will follow the typing convention of python
- You can organize the types in whatever folders are preferred
- Some suggestions are to use distinctions similar to this:
    - Primitive Types (mapping to python primitives)
        - Examples: USD = float, t = Timestamp
    - Derived Types (types that are derived from primitives but might change such as the currency used in the system)
        - Examples: CurrencyUsed = USD
    - Compound Types (Types that combine multiple types)
        - Examples: PaymentSchedule = Dict[t, CurrencyUsed]

## States

All states that are present in the system, this can be local states for entities or the global system state. Below are the JSON components for each state that is defined. For each state

**State Variable JSON Components**
- type: type, the type of the variable
- name: str, the name of the state for use in the mapping
- description: str (optional), the description of the state
- symbol: str (optional), the symbol for the state
- domain: str (optional), the domain of the state

**State Vector JSON Components**
- name: str, the name of the state
- notes: str, any notes about the state or its implementation
- variables: List[StateVariable], all the attatched state variables for the component


## Stateful Metrics

**Stateful Metric**
- type: type, the type of the variable
- name: str, the name of the state for use in the mapping
- variables_used: List[str] (optional), the string keys of variables that would be used in the computation of this metric
- parameters_used: List[str] (optional), the string keys of parameters which are used in the metric calculation
- description: str (optional), the description of the computation
- symbol: str (optional), the symbol for the state
- domain: str (optional), the domain of the state

**Stateful Metric Set**
- name: str, the name of the stateful metric set
- notes: str, any notes about the stateful metrics
- metrics: List[StatefulMetric], all the attatched stateful metrics for the state

## Parameters

**Parameter Variable JSON Components**

- variable_type, the type of the variable
- name: str, the name of the state for use in the mapping
- description: str (optional), the description of the computation
- symbol: str (optional), the symbol for the state
- domain: str (optional), the domain of the state

Attributes Imputed
- blocks_affected: block, the blocks that the parameter affects which are filled in by traversing the blocks

**Parameter Set JSON Components**

This is for organizing the parameters together into distinct groups, but in the model these can all be combined.

- name: str, the name of the parameter set
- notes: str, any notes about these parameters (are they all related to some signal or actor)
- parameters: List[ParameterVariable], all the attatched parameters for the parameter set

## Entities

- name: str, the name of the entity
- notes: str, any notes about this entity (can there be multiple or only one for example)
- state: State, the state within the entity

## Spaces

Spaces are similar to types in that they define a schema for data and are used as the domain/codomain for different actions. They can be thought of as typed dictionaries.

## Boundary Actions

The definition of different actions that might happen outside of the system such as customers coming into a shop.

**Boundary Action Option JSON Components**

Specific assumptions of how the boundary action might be represented such as different distributions or behavioral models

- name: str, the name of the boundary action option
- description: str, the description of the boundary action option
- logic: str, the logic defining out how the implementation of the boundary action would work

**Boundary Action JSON Components**

- name: str, the name of the boundary action
- description: str, the description of the boundary action
- constraints: List[str], any constraints on the boundary action
- boundary_action_options: List[BoundaryActionOption], possible implementations of the boundary action
- called_by: List[Entity], the entities which are allowed to call this action
- codomain: Tuple[Space] (optional), list of outputs that come out of this block
- parameters_used: List[str] (optional), the string keys of parameters which have an effect on the boundary action

## Control Actions

The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low.

**Control Action Option JSON Components**

Specific assumptions of how the control action might be represented such as a function that takes a threshold for when to call an action, or a random process.

- name: str, the name of the control action option
- description: str, the description of the control action option
- logic: str, the logic defining out how the implementation of the control action would work

**Control Action JSON Components**

- name: str, the name of the control action
- description: str, the description of the control action
- constraints: List[str], any constraints on the control action
- control_action_options: List[ControlActionOption], possible implementations of the control action
- codomain: Tuple[Space], list of outputs that come out of this block
- parameters_used: List[str] (optional), the string keys of parameters which have an effect on the control action


## Policies

**Policy Option JSON Components**

The concrete possible implementations that a given policy block can reference or select

- name: str, the name of the policy option
- description: str, the description of the policy option
- logic: str, the logic defining out how the implementation of the policy would work

**Policy JSON Components**

A definition of the policies that handle all logical things. This could be, for example, a policy which determines what price is paid given an exogenous of someone putting in a market buy order for a stock, this defines out the overall form and has policy options for potential implementations

- name: str, the name of the policy
- description: str, the description of the policy
- constraints: List[str], any constraints on the policy
- policy_options: List[PolicyOption], possible implementations of the policy
- domain: Tuple[Space], list of inputs that are passed in
- codomain: Tuple[Space], list of outputs that come out of the policy
- parameters_used: List[str] (optional), the string keys of parameters which have an effect on the policy

The domain and codomain can be populated from the transmission channels if none are passed, but it will be best practice to define it here as well to check that the transmission channels align with the domain/codomain.


## State Update Mechanisms

Anything that updates state in the system, usually policies will call these with the outputs of logic. The reasoning to split them out is so that if at some point you want to add a recording variable every time an account is changed or do something like have a variable listener, you can just change the mechanism responsible for it in only one place.

- name: str, the name of the mechanism
- description: str, the description of the mechanism
- constraints: List[str], any constraints on the mechanism
- logic: str, the logic of how the mechanism should work
- domain: Tuple[Space] (optional), list of inputs that are passed in
- parameters_used: List[str] (optional), the string keys of parameters which have an effect on the mechanism

Attributes imputed
- states_effected: List[Tuple(Entity, AttributeName)], all the entity attributes which are effected by this mechanism, imputed from transmission channels

## Action Transmission Channels

The definitions of all the topology of the actions that are spurring on other actions, such as a policy calling another policy or state update mechanism.

- origin: Union[BoundaryAction, ControlAction, Policy], the origin action that outputs the space
- target: Union[Policy, Mechanism], the action which is called from the origin, receiving the space as input
- space: Space, the space which is passed
- optional: bool, a boolean which indicates whether this transmission channel happens every time the origin action happens, or is only sometimes called by the origin action (such as a case where the transmission only happens a percentage of the time)


## State Update Transmission Channels
The definitions of topology of mechanisms updating state, the start of the directed edge is from a mechanism and the end of the edge is the state attribute that is being updated.

- origin: Mechanism, the mechanism which is updating the state
- entity: Entity, the entity that is having a state variable updated
- variable: str, the name of the variable in the entity which is being updated
- optional: bool, a boolean which indicates whether this transmission channel happens every time the origin action occurs, or is only sometimes called by the origin action


## Metrics

Any measurements to find things like averages of a variable over a period, defined in a way that we are trying to measure some sort of success, usually done after simulations are complete

- name: str, the name of the metric being measured
- inputs: List[StateVariable], the state variables which are used in metric computation
- logic: str, the logic defining how the metric should work


## KPIs

A conversion of metrics to boolean values to decide if a metric is good enough or not. Possibly could also just be a value bounded between [0, 1]. 

- name: str, The name of the KPI
- inputs: List[Union(Metric, KPI)], The inputs used to calculate the KPI. It could involve metrics or even other KPIs (such as defining a KPI that aggregates the maximum of two other KPIs)
- logic: str, The logic of how the computation of the KPI should work