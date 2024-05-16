# ControlActionOption Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption
```

Specific implementations of a control action which are in the same form of the underlying control action definition.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## ControlActionOption Type

`object` ([ControlActionOption](schema-definitions-controlactionoption.md))

# ControlActionOption Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                     |
| :-------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/name")               |
| [description](#description) | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/description") |
| [logic](#logic)             | `string` | Required | cannot be null | [MSML](schema-definitions-controlactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/logic")             |
| [metadata](#metadata)       | `object` | Optional | cannot be null | [MSML](schema-definitions-controlactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/metadata")       |

## name

The name of the control action option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/name")

### name Type

`string`

## description

A description of what this implementation does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/description")

### description Type

`string`

## logic

The logic related to the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/logic")

### logic Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-controlactionoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-controlactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ControlActionOption/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-controlactionoption-properties-metadata.md))
