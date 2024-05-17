# MSML Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json
```



| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [schema.schema.json](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## MSML Type

unknown ([MSML](schema.md))

# MSML Definitions

## Definitions group MSMLSpec

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec"}
```

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                         |
| :------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Policies](#policies)                 | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-policies.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies")                 |
| [Spaces](#spaces)                     | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-spaces.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces")                     |
| [State](#state)                       | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State")                       |
| [Stateful Metrics](#stateful-metrics) | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics") |
| [Parameters](#parameters)             | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters")             |
| [Mechanisms](#mechanisms)             | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-mechanisms.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms")             |
| [Entities](#entities)                 | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-entities.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities")                 |
| [Boundary Actions](#boundary-actions) | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions") |
| [Control Actions](#control-actions)   | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-control-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions")   |
| [Wiring](#wiring)                     | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-wiring.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring")                     |
| [Types](#types)                       | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-types.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types")                       |
| [Metrics](#metrics)                   | `array`  | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Metrics")                   |
| [Displays](#displays)                 | `object` | Optional | cannot be null | [MSML](schema-definitions-msmlspec-properties-displays.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Displays")                 |

### Policies



`Policies`

*   is required

*   Type: `object[]` ([Policy](schema-definitions-policy.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-policies.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies")

#### Policies Type

`object[]` ([Policy](schema-definitions-policy.md))

### Spaces



`Spaces`

*   is required

*   Type: `object[]` ([Space](schema-definitions-space.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-spaces.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces")

#### Spaces Type

`object[]` ([Space](schema-definitions-space.md))

### State



`State`

*   is required

*   Type: `object[]` ([State](schema-definitions-state.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State")

#### State Type

`object[]` ([State](schema-definitions-state.md))

### Stateful Metrics



`Stateful Metrics`

*   is required

*   Type: `object[]` ([Stateful Metric](schema-definitions-stateful-metric.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics")

#### Stateful Metrics Type

`object[]` ([Stateful Metric](schema-definitions-stateful-metric.md))

### Parameters



`Parameters`

*   is required

*   Type: `object[]` ([Parameter](schema-definitions-parameter.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters")

#### Parameters Type

`object[]` ([Parameter](schema-definitions-parameter.md))

### Mechanisms



`Mechanisms`

*   is required

*   Type: `object[]` ([Mechanism](schema-definitions-mechanism.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-mechanisms.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms")

#### Mechanisms Type

`object[]` ([Mechanism](schema-definitions-mechanism.md))

### Entities



`Entities`

*   is required

*   Type: `object[]` ([Entity](schema-definitions-entity.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-entities.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities")

#### Entities Type

`object[]` ([Entity](schema-definitions-entity.md))

### Boundary Actions



`Boundary Actions`

*   is required

*   Type: `object[]` ([Boundary Action](schema-definitions-boundary-action.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions")

#### Boundary Actions Type

`object[]` ([Boundary Action](schema-definitions-boundary-action.md))

### Control Actions



`Control Actions`

*   is required

*   Type: `object[]` ([ControlAction](schema-definitions-controlaction.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-control-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions")

#### Control Actions Type

`object[]` ([ControlAction](schema-definitions-controlaction.md))

### Wiring



`Wiring`

*   is required

*   Type: `object[]` ([Wiring](schema-definitions-wiring.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-wiring.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring")

#### Wiring Type

`object[]` ([Wiring](schema-definitions-wiring.md))

### Types



`Types`

*   is required

*   Type: `object[]` ([Type](schema-definitions-type.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-types.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types")

#### Types Type

`object[]` ([Type](schema-definitions-type.md))

### Metrics



`Metrics`

*   is required

*   Type: `object[]` ([Metric](schema-definitions-metric.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Metrics")

#### Metrics Type

`object[]` ([Metric](schema-definitions-metric.md))

### Displays



`Displays`

*   is optional

*   Type: `object` ([Details](schema-definitions-msmlspec-properties-displays.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-displays.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Displays")

#### Displays Type

`object` ([Details](schema-definitions-msmlspec-properties-displays.md))

## Definitions group ControlAction

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction"}
```

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                               |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                                       | `string` | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")                                     |
| [description](#description)                         | `string` | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")                       |
| [constraints](#constraints)                         | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")                       |
| [control\_action\_options](#control_action_options) | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options") |
| [codomain](#codomain)                               | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")                             |
| [parameters\_used](#parameters_used)                | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")               |

### name

The name of the control action

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")

#### name Type

`string`

### description

The description of the control action

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")

#### description Type

`string`

### constraints

Any constraints which the control action must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")

#### constraints Type

`string[]`

### control\_action\_options

Possible implementations of the control action

`control_action_options`

*   is required

*   Type: `object[]` ([ControlActionOption](schema-definitions-controlactionoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options")

#### control\_action\_options Type

`object[]` ([ControlActionOption](schema-definitions-controlactionoption.md))

### codomain

The output spaces of the control action

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")

#### codomain Type

`string[]`

### parameters\_used

The parameters which the control action uses in its implenetations

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")

#### parameters\_used Type

`string[]`

## Definitions group BoundaryActionOption

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :---------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-1)               | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/name")               |
| [description](#description-1) | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/description") |
| [logic](#logic)               | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/logic")             |
| [metadata](#metadata)         | `object` | Optional | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/metadata")       |

### name

The name of the boundary action option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/name")

#### name Type

`string`

### description

A description of what this implementation does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/description")

#### description Type

`string`

### logic

The logic related to the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/logic")

#### logic Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-boundaryactionoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-boundaryactionoption-properties-metadata.md))

## Definitions group ControlActionOption

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                     |
| :---------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-2)               | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/name")               |
| [description](#description-2) | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/description") |
| [logic](#logic-1)             | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/logic")             |
| [metadata](#metadata-1)       | `object` | Optional | cannot be null | [MSML](schema-definitions-controlactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/metadata")       |

### name

The name of the control action option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/name")

#### name Type

`string`

### description

A description of what this implementation does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/description")

#### description Type

`string`

### logic

The logic related to the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/logic")

#### logic Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-controlactionoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-controlactionoption-properties-metadata.md))

## Definitions group Entity

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-3)         | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")         |
| [notes](#notes)         | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")       |
| [state](#state-1)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")       |
| [metadata](#metadata-2) | `object` | Optional | cannot be null | [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata") |

### name

The name of the entity

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")

#### name Type

`string`

### notes

Any notes on the entity

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")

#### notes Type

`string`

### state

The string key for the state associated with the entity

`state`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")

#### state Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-entity-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-entity-properties-metadata.md))

## Definitions group Mechanism

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism"}
```

| Property                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                         |
| :------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-4)                        | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")                       |
| [description](#description-3)          | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")         |
| [constraints](#constraints-1)          | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")         |
| [logic](#logic-2)                      | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")                     |
| [domain](#domain)                      | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")                   |
| [parameters\_used](#parameters_used-1) | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used") |
| [updates](#updates)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")                 |
| [metadata](#metadata-3)                | `object` | Optional | cannot be null | [MSML](schema-definitions-mechanism-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata")               |

### name

The name of the mechanism

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")

#### name Type

`string`

### description

The description of what the mechanism does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")

#### description Type

`string`

### constraints

Any constraints which the mechanism must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")

#### constraints Type

`string[]`

### logic

The logic of how the mechanism should work

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")

#### logic Type

`string`

### domain

The spaces which are the input into the mechanism

`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")

#### domain Type

`string[]`

### parameters\_used

The string keys of parameters which have an effect on the mechanism

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used")

#### parameters\_used Type

`string[]`

### updates

The states updates that the mechanism causes in the form of (Entity, State Variable)

`updates`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")

#### updates Type

unknown\[]

### metadata

Any metadata that is added onto the mechanism

`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-mechanism-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-mechanism-properties-metadata.md))

## Definitions group Parameter

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                               |
| :-------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-5)             | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")             |
| [notes](#notes-1)           | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")           |
| [parameters](#parameters-1) | `array`  | Required | cannot be null | [MSML](schema-definitions-parameter-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters") |

### name

The name of the parameter set

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")

#### name Type

`string`

### notes

Any notes about the parameter set

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")

#### notes Type

`string`

### parameters

All parameters that are a part of this parameter set

`parameters`

*   is required

*   Type: `object[]` ([ParameterElement](schema-definitions-parameterelement.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters")

#### parameters Type

`object[]` ([ParameterElement](schema-definitions-parameterelement.md))

## Definitions group ParameterElement

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement"}
```

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :----------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [variable\_type](#variable_type)     | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-variable_type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/variable_type")     |
| [name](#name-6)                      | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")                       |
| [description](#description-4)        | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")         |
| [symbol](#symbol)                    | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")                   |
| [domain](#domain-1)                  | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")                   |
| [parameter\_class](#parameter_class) | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-parameter_class.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/parameter_class") |

### variable\_type

The type of that the parameter takes.

`variable_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-variable_type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/variable_type")

#### variable\_type Type

`string`

### name

The unique name of the parameter

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")

#### name Type

`string`

### description

The description of the parameter

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")

#### description Type

`string`

### symbol

The symbol associated with the parameter (optional)

`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")

#### symbol Type

`string`

### domain

The mathematical domain of the parameter (optional)

`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")

#### domain Type

`string`

### parameter\_class

The type of paramter this is, of which the options are system (what you would find in production code of a system), behavioral (for what kinds of behavioral assumptions and distributions there are), and functional (for defining out different functional forms such as swapping in and out policies)

`parameter_class`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-parameter_class.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/parameter_class")

#### parameter\_class Type

`string`

## Definitions group Policy

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy"}
```

| Property                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                   |
| :------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-7)                        | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")                       |
| [description](#description-5)          | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")         |
| [constraints](#constraints-2)          | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")         |
| [policy\_options](#policy_options)     | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")   |
| [domain](#domain-2)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")                   |
| [codomain](#codomain-1)                | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")               |
| [parameters\_used](#parameters_used-2) | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used") |
| [metrics\_used](#metrics_used)         | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metrics_used")       |
| [metadata](#metadata-4)                | `object` | Optional | cannot be null | [MSML](schema-definitions-policy-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metadata")               |

### name

The name of the policy

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")

#### name Type

`string`

### description

Description of the policy

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")

#### description Type

`string`

### constraints

Any constraints which the policy must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")

#### constraints Type

`string[]`

### policy\_options

Possible implementations of the policy

`policy_options`

*   is required

*   Type: `object[]` ([PolicyOption](schema-definitions-policyoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")

#### policy\_options Type

`object[]` ([PolicyOption](schema-definitions-policyoption.md))

### domain

The spaces which are passed in as inputs to the policy

`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")

#### domain Type

`string[]`

### codomain

The spaces which are returned as results of the policy

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")

#### codomain Type

`string[]`

### parameters\_used

All parameters used in the implementations of policies

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used")

#### parameters\_used Type

`string[]`

### metrics\_used

All metrics used in implementation of policies

`metrics_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metrics_used")

#### metrics\_used Type

`string[]`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-policy-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-policy-properties-metadata.md))

## Definitions group PolicyOption

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                       |
| :---------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-8)               | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")               |
| [description](#description-6) | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description") |
| [logic](#logic-3)             | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")             |
| [metadata](#metadata-5)       | `object` | Optional | cannot be null | [MSML](schema-definitions-policyoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/metadata")       |

### name

The name of the policy option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")

#### name Type

`string`

### description

A description of the implementation

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description")

#### description Type

`string`

### logic

Any logic associated with the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")

#### logic Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-policyoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-policyoption-properties-metadata.md))

## Definitions group Space

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space"}
```

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                           |
| :---------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-9)   | `string` | Required | cannot be null | [MSML](schema-definitions-space-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/name") |
| [schema](#schema) | `object` | Required | cannot be null | [MSML](schema-definitions-schema.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/schema")              |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-space-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/name")

#### name Type

`string`

### schema



`schema`

*   is required

*   Type: `object` ([Schema](schema-definitions-schema.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-schema.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/schema")

#### schema Type

`object` ([Schema](schema-definitions-schema.md))

## Definitions group StatefulMetric

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric"}
```

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                    |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-10)      | `string` | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/name")       |
| [notes](#notes-2)     | `string` | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/notes")     |
| [metrics](#metrics-1) | `array`  | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/metrics") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                               |

### name

The name of the stateful metric set

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/name")

#### name Type

`string`

### notes

Any notes about the stateful metric set

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/notes")

#### notes Type

`string`

### metrics



`metrics`

*   is required

*   Type: `object[]` ([Details](schema-definitions-statefulmetricvar.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/metrics")

#### metrics Type

`object[]` ([Details](schema-definitions-statefulmetricvar.md))

### Additional Properties

Additional properties are allowed and do not have to follow a specific schema

## Definitions group BoundaryAction

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction"}
```

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                    |
| :---------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name-11)                                      | `string` | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/name")                                       |
| [description](#description-7)                         | `string` | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/description")                         |
| [constraints](#constraints-3)                         | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/constraints")                         |
| [boundary\_action\_options](#boundary_action_options) | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-boundary_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/boundary_action_options") |
| [called\_by](#called_by)                              | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-called_by.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/called_by")                             |
| [codomain](#codomain-2)                               | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/codomain")                               |
| [parameters\_used](#parameters_used-3)                | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/parameters_used")                 |
| Additional Properties                                 | Any      | Optional | can be null    |                                                                                                                                                                                                               |

### name

Name of the boundary action

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/name")

#### name Type

`string`

### description

Quick description of the boundary action

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/description")

#### description Type

`string`

### constraints

Any constraints which the boundary action must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/constraints")

#### constraints Type

`string[]`

### boundary\_action\_options

The options for implementation of the boundary action

`boundary_action_options`

*   is required

*   Type: `object[]` ([BoundaryActionOption](schema-definitions-boundaryactionoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-boundary_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/boundary_action_options")

#### boundary\_action\_options Type

`object[]` ([BoundaryActionOption](schema-definitions-boundaryactionoption.md))

### called\_by

The entities which are allowed to call this boundary action

`called_by`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-called_by.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/called_by")

#### called\_by Type

`string[]`

### codomain

List of outputs that come out of this block

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/codomain")

#### codomain Type

`string[]`

### parameters\_used

The string keys of parameters which have an effect on the boundary action

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/parameters_used")

#### parameters\_used Type

`string[]`

### Additional Properties

Additional properties are allowed and do not have to follow a specific schema

## Definitions group Schema

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Schema"}
```

| Property              | Type | Required | Nullable    | Defined by |
| :-------------------- | :--- | :------- | :---------- | :--------- |
| Additional Properties | Any  | Optional | can be null |            |

### Additional Properties

Additional properties are allowed and do not have to follow a specific schema

## Definitions group State

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-12)        | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")           |
| [notes](#notes-3)       | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")         |
| [variables](#variables) | `array`  | Required | cannot be null | [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables") |

### name

Any notes about the state or its implementation

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")

#### name Type

`string`

### notes

The name of the state

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")

#### notes Type

`string`

### variables

All the attatched state variables for the component

`variables`

*   is required

*   Type: `object[]` ([Variable](schema-definitions-variable.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables")

#### variables Type

`object[]` ([Variable](schema-definitions-variable.md))

## Definitions group Variable

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                               |
| :---------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                 | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")               |
| [name](#name-13)              | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")               |
| [description](#description-8) | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description") |
| [symbol](#symbol-1)           | `string` | Required | can be null    | [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")           |
| [domain](#domain-3)           | `string` | Required | can be null    | [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")           |
| [metadata](#metadata-6)       | `object` | Optional | cannot be null | [MSML](schema-definitions-variable-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/metadata")       |

### type

The type of the variable

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")

#### type Type

`string`

### name

Variable name

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")

#### name Type

`string`

### description

Description of what the variable is

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description")

#### description Type

`string`

### symbol

The symbol associated with the parameter (optional)

`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")

#### symbol Type

`string`

### domain

The mathematical domain of the parameter (optional)

`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")

#### domain Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-variable-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-variable-properties-metadata.md))

## Definitions group Type

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                 |
| :---------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-14)        | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/name")         |
| [type](#type-1)         | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")         |
| [notes](#notes-4)       | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/notes")       |
| [metadata](#metadata-7) | `object` | Optional | cannot be null | [MSML](schema-definitions-type-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata") |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/name")

#### name Type

`string`

### type



`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")

#### type Type

`string`

### notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/notes")

#### notes Type

`string`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-type-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-type-properties-metadata.md))

## Definitions group Metric

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric"}
```

| Property                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                   |
| :------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type-2)                        | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/type")                       |
| [name](#name-15)                       | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/name")                       |
| [description](#description-9)          | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/description")         |
| [variables\_used](#variables_used)     | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used")   |
| [parameters\_used](#parameters_used-4) | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/parameters_used") |
| [metrics\_used](#metrics_used-1)       | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/metrics_used")       |
| [domain](#domain-4)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/domain")                   |
| [logic](#logic-4)                      | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/logic")                     |
| [symbol](#symbol-2)                    | `string` | Required | can be null    | [MSML](schema-definitions-metric-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/symbol")                   |

### type



`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/type")

#### type Type

`string`

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/description")

#### description Type

`string`

### variables\_used



`variables_used`

*   is required

*   Type: `string[][]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used")

#### variables\_used Type

`string[][]`

### parameters\_used



`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/parameters_used")

#### parameters\_used Type

`string[]`

### metrics\_used



`metrics_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/metrics_used")

#### metrics\_used Type

`string[]`

### domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/domain")

#### domain Type

`string[]`

### logic



`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/logic")

#### logic Type

`string`

### symbol



`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-metric-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/symbol")

#### symbol Type

`string`

## Definitions group Wiring

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring"}
```

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                       |
| :---------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-16)                          | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/name")                           |
| [components](#components)                 | `array`   | Required | cannot be null | [MSML](schema-definitions-wiring-properties-components.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/components")               |
| [description](#description-10)            | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/description")             |
| [constraints](#constraints-4)             | `array`   | Required | cannot be null | [MSML](schema-definitions-wiring-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/constraints")             |
| [type](#type-3)                           | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-typeenum.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/type")                       |
| [mermaid\_show\_name](#mermaid_show_name) | `boolean` | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-mermaid_show_name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/mermaid_show_name") |
| [loop](#loop)                             | `boolean` | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-loop.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/loop")                           |
| [optional\_indices](#optional_indices)    | `array`   | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-optional_indices.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/optional_indices")   |
| [metadata](#metadata-8)                   | `object`  | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/metadata")                   |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/name")

#### name Type

`string`

### components



`components`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-components.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/components")

#### components Type

`string[]`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/description")

#### description Type

`string`

### constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/constraints")

#### constraints Type

unknown\[]

### type



`type`

*   is required

*   Type: `string` ([TypeEnum](schema-definitions-wiring-properties-typeenum.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-typeenum.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/type")

#### type Type

`string` ([TypeEnum](schema-definitions-wiring-properties-typeenum.md))

#### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"Parallel"` |             |
| `"Stack"`    |             |

### mermaid\_show\_name



`mermaid_show_name`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-mermaid_show_name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/mermaid_show_name")

#### mermaid\_show\_name Type

`boolean`

### loop



`loop`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-loop.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/loop")

#### loop Type

`boolean`

### optional\_indices



`optional_indices`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-optional_indices.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/optional_indices")

#### optional\_indices Type

`integer[]`

### metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-wiring-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-wiring-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/metadata")

#### metadata Type

`object` ([Details](schema-definitions-wiring-properties-metadata.md))

## Definitions group Update

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Update"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group TypeEnum

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/TypeEnum"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group WiringDisplay

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay"}
```

| Property                       | Type     | Required | Nullable       | Defined by                                                                                                                                                                         |
| :----------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-17)               | `string` | Required | cannot be null | [MSML](schema-definitions-wiringdisplay-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/name")               |
| [description](#description-11) | `string` | Required | cannot be null | [MSML](schema-definitions-wiringdisplay-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/description") |
| [components](#components-1)    | `array`  | Required | cannot be null | [MSML](schema-definitions-wiringdisplay-properties-components.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/components")   |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiringdisplay-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiringdisplay-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/description")

#### description Type

`string`

### components



`components`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-wiringdisplay-properties-components.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/WiringDisplay/properties/components")

#### components Type

`string[]`

## Definitions group StatefulMetricVar

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar"}
```

| Property                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                                         |
| :------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type-4)                        | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/type")                       |
| [name](#name-18)                       | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/name")                       |
| [description](#description-12)         | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/description")         |
| [variables\_used](#variables_used-1)   | `array`  | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/variables_used")   |
| [parameters\_used](#parameters_used-5) | `array`  | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/parameters_used") |
| [symbol](#symbol-3)                    | `string` | Optional | can be null    | [MSML](schema-definitions-statefulmetricvar-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/symbol")                   |
| [domain](#domain-5)                    | `string` | Optional | can be null    | [MSML](schema-definitions-statefulmetricvar-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/domain")                   |

### type

The type of the metric variable

`type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/type")

#### type Type

`string`

### name

The name of the stateful metric variable

`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/name")

#### name Type

`string`

### description

The description of the computation

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/description")

#### description Type

`string`

### variables\_used

The variables used for computation of the form (state, variable)

`variables_used`

*   is optional

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/variables_used")

#### variables\_used Type

unknown\[]

### parameters\_used



`parameters_used`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/parameters_used")

#### parameters\_used Type

`string[]`

### symbol

The symbol associated with the stateful metric (optional)

`symbol`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/symbol")

#### symbol Type

`string`

### domain

The mathematical domain of the stateful metric (optional)

`domain`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/domain")

#### domain Type

`string`
