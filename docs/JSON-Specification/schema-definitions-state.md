# State Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## State Type

`object` ([State](schema-definitions-state.md))

# State Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)           | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")           |
| [notes](#notes)         | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")         |
| [variables](#variables) | `array`  | Required | cannot be null | [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")

### name Type

`string`

## notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")

### notes Type

`string`

## variables



`variables`

*   is required

*   Type: `object[]` ([Variable](schema-definitions-variable.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables")

### variables Type

`object[]` ([Variable](schema-definitions-variable.md))
