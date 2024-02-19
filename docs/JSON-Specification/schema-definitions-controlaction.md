# ControlAction Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

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



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/name")

### name Type

`string`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/description")

### description Type

`string`

## constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/constraints")

### constraints Type

unknown\[]

## control\_action\_options



`control_action_options`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-control_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/control_action_options")

### control\_action\_options Type

unknown\[]

## codomain



`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/codomain")

### codomain Type

`string[]`

## parameters\_used



`parameters_used`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-controlaction-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlAction/properties/parameters_used")

### parameters\_used Type

unknown\[]
