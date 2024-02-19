# MSML Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json
```



| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [schema.schema.json](../../out/schema.schema.json "open original schema") |

## MSML Type

unknown ([MSML](schema.md))

# MSML Definitions

## Definitions group MSMLSpec

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec"}
```

| Property                              | Type    | Required | Nullable       | Defined by                                                                                                                                                                         |
| :------------------------------------ | :------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Policies](#policies)                 | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-policies.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies")                 |
| [Spaces](#spaces)                     | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-spaces.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces")                     |
| [State](#state)                       | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State")                       |
| [Stateful Metrics](#stateful-metrics) | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics") |
| [Parameters](#parameters)             | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters")             |
| [Mechanisms](#mechanisms)             | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-mechanisms.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms")             |
| [Entities](#entities)                 | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-entities.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities")                 |
| [Boundary Actions](#boundary-actions) | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions") |
| [Control Actions](#control-actions)   | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-control-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions")   |
| [Wiring](#wiring)                     | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-wiring.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring")                     |
| [Types](#types)                       | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-types.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types")                       |

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

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics")

#### Stateful Metrics Type

unknown\[]

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

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions")

#### Boundary Actions Type

unknown\[]

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



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")

#### description Type

`string`

### constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")

#### constraints Type

unknown\[]

### control\_action\_options



`control_action_options`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options")

#### control\_action\_options Type

unknown\[]

### codomain



`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")

#### codomain Type

`string[]`

### parameters\_used



`parameters_used`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")

#### parameters\_used Type

unknown\[]

## Definitions group Entity

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity"}
```

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-1)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")         |
| [notes](#notes)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")       |
| [state](#state-1)     | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")       |
| [metadata](#metadata) | `object` | Optional | cannot be null | [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata") |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")

#### name Type

`string`

### notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")

#### notes Type

`string`

### state



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
| [name](#name-2)                        | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")                       |
| [description](#description-1)          | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")         |
| [constraints](#constraints-1)          | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")         |
| [logic](#logic)                        | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")                     |
| [domain](#domain)                      | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")                   |
| [parameters\_used](#parameters_used-1) | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used") |
| [updates](#updates)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")                 |
| [metadata](#metadata-1)                | `object` | Optional | cannot be null | [MSML](schema-definitions-mechanism-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata")               |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")

#### description Type

`string`

### constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")

#### constraints Type

unknown\[]

### logic



`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")

#### logic Type

`string`

### domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")

#### domain Type

`string[]`

### parameters\_used



`parameters_used`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used")

#### parameters\_used Type

unknown\[]

### updates



`updates`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")

#### updates Type

unknown\[]

### metadata



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
| [name](#name-3)             | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")             |
| [notes](#notes-1)           | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")           |
| [parameters](#parameters-1) | `array`  | Required | cannot be null | [MSML](schema-definitions-parameter-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters") |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")

#### name Type

`string`

### notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")

#### notes Type

`string`

### parameters



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
| [name](#name-4)                      | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")                       |
| [description](#description-2)        | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")         |
| [symbol](#symbol)                    | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")                   |
| [domain](#domain-1)                  | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")                   |
| [parameter\_class](#parameter_class) | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-parameter_class.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/parameter_class") |

### variable\_type



`variable_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-variable_type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/variable_type")

#### variable\_type Type

`string`

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")

#### description Type

`string`

### symbol



`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")

#### symbol Type

`string`

### domain



`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")

#### domain Type

`string`

### parameter\_class



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
| [name](#name-5)                        | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")                       |
| [description](#description-3)          | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")         |
| [constraints](#constraints-2)          | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")         |
| [policy\_options](#policy_options)     | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")   |
| [domain](#domain-2)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")                   |
| [codomain](#codomain-1)                | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")               |
| [parameters\_used](#parameters_used-2) | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used") |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")

#### description Type

`string`

### constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")

#### constraints Type

unknown\[]

### policy\_options



`policy_options`

*   is required

*   Type: `object[]` ([PolicyOption](schema-definitions-policyoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")

#### policy\_options Type

`object[]` ([PolicyOption](schema-definitions-policyoption.md))

### domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")

#### domain Type

`string[]`

### codomain



`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")

#### codomain Type

`string[]`

### parameters\_used



`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used")

#### parameters\_used Type

`string[]`

## Definitions group PolicyOption

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption"}
```

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                       |
| :---------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-6)               | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")               |
| [description](#description-4) | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description") |
| [logic](#logic-1)             | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")             |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description")

#### description Type

`string`

### logic



`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")

#### logic Type

`string`

## Definitions group Space

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space"}
```

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                           |
| :---------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-7)   | `string` | Required | cannot be null | [MSML](schema-definitions-space-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/name") |
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
| [name](#name-8)         | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")           |
| [notes](#notes-2)       | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")         |
| [variables](#variables) | `array`  | Required | cannot be null | [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables") |

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")

#### name Type

`string`

### notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")

#### notes Type

`string`

### variables



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

| Property                      | Type          | Required | Nullable       | Defined by                                                                                                                                                               |
| :---------------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                 | Not specified | Required | cannot be null | [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")               |
| [name](#name-9)               | `string`      | Required | cannot be null | [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")               |
| [description](#description-5) | `string`      | Required | cannot be null | [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description") |
| [symbol](#symbol-1)           | `string`      | Required | can be null    | [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")           |
| [domain](#domain-3)           | `string`      | Required | can be null    | [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")           |

### type



`type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")

#### type Type

unknown

### name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")

#### name Type

`string`

### description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description")

#### description Type

`string`

### symbol



`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")

#### symbol Type

`string`

### domain



`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")

#### domain Type

`string`

## Definitions group Type

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type"}
```

| Property                | Type          | Required | Nullable       | Defined by                                                                                                                                                 |
| :---------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-10)        | `string`      | Required | cannot be null | [MSML](schema-definitions-type-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/name")         |
| [type](#type-1)         | Not specified | Required | cannot be null | [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")         |
| [notes](#notes-3)       | `string`      | Required | cannot be null | [MSML](schema-definitions-type-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/notes")       |
| [metadata](#metadata-2) | `object`      | Optional | cannot be null | [MSML](schema-definitions-type-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata") |

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

*   Type: unknown

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")

#### type Type

unknown

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

## Definitions group Wiring

Reference this group by using

```json
{"$ref":"https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring"}
```

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                       |
| :---------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name-11)                          | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/name")                           |
| [components](#components)                 | `array`   | Required | cannot be null | [MSML](schema-definitions-wiring-properties-components.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/components")               |
| [description](#description-6)             | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/description")             |
| [constraints](#constraints-3)             | `array`   | Required | cannot be null | [MSML](schema-definitions-wiring-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/constraints")             |
| [type](#type-2)                           | `string`  | Required | cannot be null | [MSML](schema-definitions-wiring-properties-typeenum.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/type")                       |
| [mermaid\_show\_name](#mermaid_show_name) | `boolean` | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-mermaid_show_name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/mermaid_show_name") |
| [loop](#loop)                             | `boolean` | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-loop.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/loop")                           |
| [optional\_indices](#optional_indices)    | `array`   | Optional | cannot be null | [MSML](schema-definitions-wiring-properties-optional_indices.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Wiring/properties/optional_indices")   |

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
