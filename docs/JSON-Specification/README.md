# README

## Top-level Schemas

*   [MSML](./schema.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json`

## Other Schemas

### Objects

*   [Boundary Action](./schema-definitions-boundary-action.md "The definition of different actions that might happen outside of the system such as customers coming into a shop") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction`

*   [ControlAction](./schema-definitions-controlaction.md "The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low or something that could get triggered from a sensor") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction`

*   [Entity](./schema-definitions-entity.md "Entities are any class of user or infrastructure that should have their own state and potentially ability to call boundary actions") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity`

*   [MSMLSpec](./schema-definitions-msmlspec.md "A JSON schema that is used in the mathematical specification mapping library to create the underlying MSML object") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec`

*   [Mechanism](./schema-definitions-mechanism.md "Anything that updates state in the system, usually policies will call these with the outputs of logic") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism`

*   [Metric](./schema-definitions-metric.md "This component takes a variety of potential inputs and creates a metric from it") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric`

*   [Parameter](./schema-definitions-parameter.md "Both local and global parameter sets in the system that could be set") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter`

*   [ParameterElement](./schema-definitions-parameterelement.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement`

*   [Policy](./schema-definitions-policy.md "A definition of the policies that handle all logical things") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy`

*   [PolicyOption](./schema-definitions-policyoption.md "The concrete possible implementations that a given policy block can reference or select") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption`

*   [Schema](./schema-definitions-schema.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Schema`

*   [Space](./schema-definitions-space.md "Spaces are similar to types in that they define a schema for data and are used as the domain/codomain for different blocks") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space`

*   [State](./schema-definitions-state.md "The definition of states in the system") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State`

*   [Stateful Metric](./schema-definitions-stateful-metric.md "Variables that are not held directly in the state but can computed from the state & parameters") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric`

*   [Type](./schema-definitions-type.md "This is for defining what a type might in its most basic form") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type`

*   [Untitled object in MSML](./schema-definitions-policyoption-properties-metadata.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-policy-properties-metadata.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-variable-properties-metadata.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-mechanism-properties-metadata.md "Any metadata that is added onto the mechanism") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-entity-properties-metadata.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-type-properties-metadata.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata`

*   [Untitled object in MSML](./schema-definitions-msmlspec-properties-displays.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Displays`

*   [Untitled object in MSML](./schema-definitions-wiringdisplay.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay`

*   [Untitled object in MSML](./schema-definitions-statefulmetricvar.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar`

*   [Variable](./schema-definitions-variable.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable`

*   [Wiring](./schema-definitions-wiring.md "A wiring is a block composed of other blocks with specific behaviors or orders of execution") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring`

### Arrays

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-policies.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies`

*   [Untitled array in MSML](./schema-definitions-policy-properties-constraints.md "Any constraints which the policy must respect") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints`

*   [Untitled array in MSML](./schema-definitions-policy-properties-policy_options.md "Possible implementations of the policy") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options`

*   [Untitled array in MSML](./schema-definitions-policy-properties-domain.md "The spaces which are passed in as inputs to the policy") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain`

*   [Untitled array in MSML](./schema-definitions-policy-properties-codomain.md "The spaces which are returned as results of the policy") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain`

*   [Untitled array in MSML](./schema-definitions-policy-properties-parameters_used.md "All parameters used in the implementations of policies") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-policy-properties-metrics_used.md "All metrics used in implementation of policies") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metrics_used`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-spaces.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-state.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State`

*   [Untitled array in MSML](./schema-definitions-state-properties-variables.md "All the attatched state variables for the component") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-stateful-metrics.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics`

*   [Untitled array in MSML](./schema-definitions-stateful-metric-properties-metrics.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/metrics`

*   [Untitled array in MSML](./schema-definitions-statefulmetricvar-properties-variables_used.md "The variables used for computation of the form (state, variable)") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/variables_used`

*   [Untitled array in MSML](./schema-definitions-statefulmetricvar-properties-parameters_used.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-parameters.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters`

*   [Untitled array in MSML](./schema-definitions-parameter-properties-parameters.md "All parameters that are a part of this parameter set") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-mechanisms.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms`

*   [Untitled array in MSML](./schema-definitions-mechanism-properties-constraints.md "Any constraints which the mechanism must respect") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints`

*   [Untitled array in MSML](./schema-definitions-mechanism-properties-domain.md "The spaces which are the input into the mechanism") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain`

*   [Untitled array in MSML](./schema-definitions-mechanism-properties-parameters_used.md "The string keys of parameters which have an effect on the mechanism") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-mechanism-properties-updates.md "The states updates that the mechanism causes in the form of (Entity, State Variable)") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-entities.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-boundary-actions.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions`

*   [Untitled array in MSML](./schema-definitions-boundary-action-properties-constraints.md "Any constraints which the boundary action must respect") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/constraints`

*   [Untitled array in MSML](./schema-definitions-boundary-action-properties-boundary_action_options.md "The options for implementation of the boundary action") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/boundary_action_options`

*   [Untitled array in MSML](./schema-definitions-boundary-action-properties-called_by.md "The entities which are allowed to call this boundary action") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/called_by`

*   [Untitled array in MSML](./schema-definitions-boundary-action-properties-codomain.md "List of outputs that come out of this block") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/codomain`

*   [Untitled array in MSML](./schema-definitions-boundary-action-properties-parameters_used.md "The string keys of parameters which have an effect on the boundary action") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-control-actions.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions`

*   [Untitled array in MSML](./schema-definitions-controlaction-properties-constraints.md "Any constraints which the control action must respect") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints`

*   [Untitled array in MSML](./schema-definitions-controlaction-properties-control_action_options.md "Possible implementations of the control action") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options`

*   [Untitled array in MSML](./schema-definitions-controlaction-properties-codomain.md "The output spaces of the control action") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain`

*   [Untitled array in MSML](./schema-definitions-controlaction-properties-parameters_used.md "The parameters which the control action uses in its implenetations") – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-wiring.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring`

*   [Untitled array in MSML](./schema-definitions-wiring-properties-components.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/components`

*   [Untitled array in MSML](./schema-definitions-wiring-properties-constraints.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/constraints`

*   [Untitled array in MSML](./schema-definitions-wiring-properties-optional_indices.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/optional_indices`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-types.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-metrics.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Metrics`

*   [Untitled array in MSML](./schema-definitions-metric-properties-variables_used.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used`

*   [Untitled array in MSML](./schema-definitions-metric-properties-variables_used-items.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used/items`

*   [Untitled array in MSML](./schema-definitions-metric-properties-parameters_used.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/parameters_used`

*   [Untitled array in MSML](./schema-definitions-metric-properties-metrics_used.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/metrics_used`

*   [Untitled array in MSML](./schema-definitions-metric-properties-domain.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/domain`

*   [Untitled array in MSML](./schema-definitions-msmlspec-properties-displays-properties-wiring.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Displays/properties/wiring`

*   [Untitled array in MSML](./schema-definitions-wiringdisplay-properties-components.md) – `https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/components`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-06/schema#`
