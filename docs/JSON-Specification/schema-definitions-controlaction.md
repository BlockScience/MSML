# ControlAction Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction
```

The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low or something that could get triggered from a sensor. The key differentiator from boundary actions is that there is no entity calling it and it is not done with randomness.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## ControlAction Type

`object` ([ControlAction](schema-definitions-controlaction.md))

# ControlAction Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                               |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                                       | `string` | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")                                     |
| [description](#description)                         | `string` | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")                       |
| [constraints](#constraints)                         | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")                       |
| [control\_action\_options](#control_action_options) | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options") |
| [codomain](#codomain)                               | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")                             |
| [parameters\_used](#parameters_used)                | `array`  | Required | cannot be null | [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")               |

## name

The name of the control action

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")

### name Type

`string`

## description

The description of the control action

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")

### description Type

`string`

## constraints

Any constraints which the control action must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")

### constraints Type

`string[]`

## control\_action\_options

Possible implementations of the control action

`control_action_options`

*   is required

*   Type: `object[]` ([ControlActionOption](schema-definitions-controlactionoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options")

### control\_action\_options Type

`object[]` ([ControlActionOption](schema-definitions-controlactionoption.md))

## codomain

The output spaces of the control action

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")

### codomain Type

`string[]`

## parameters\_used

The parameters which the control action uses in its implenetations

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")

### parameters\_used Type

`string[]`
