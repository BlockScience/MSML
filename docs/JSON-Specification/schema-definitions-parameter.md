# Parameter Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Parameter Type

`object` ([Parameter](schema-definitions-parameter.md))

# Parameter Properties

| Property                  | Type     | Required | Nullable       | Defined by                                                                                                                                                               |
| :------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)             | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")             |
| [notes](#notes)           | `string` | Required | cannot be null | [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")           |
| [parameters](#parameters) | `array`  | Required | cannot be null | [MSML](schema-definitions-parameter-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/name")

### name Type

`string`

## notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/notes")

### notes Type

`string`

## parameters



`parameters`

*   is required

*   Type: `object[]` ([ParameterElement](schema-definitions-parameterelement.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-parameter-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Parameter/properties/parameters")

### parameters Type

`object[]` ([ParameterElement](schema-definitions-parameterelement.md))
