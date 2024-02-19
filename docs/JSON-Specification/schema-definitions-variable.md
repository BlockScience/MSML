# Variable Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Variable Type

`object` ([Variable](schema-definitions-variable.md))

# Variable Properties

| Property                    | Type          | Required | Nullable       | Defined by                                                                                                                                                               |
| :-------------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)               | Not specified | Required | cannot be null | [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")               |
| [name](#name)               | `string`      | Required | cannot be null | [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")               |
| [description](#description) | `string`      | Required | cannot be null | [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description") |
| [symbol](#symbol)           | `string`      | Required | can be null    | [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")           |
| [domain](#domain)           | `string`      | Required | can be null    | [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")           |

## type



`type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")

### type Type

unknown

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")

### name Type

`string`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description")

### description Type

`string`

## symbol



`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")

### symbol Type

`string`

## domain



`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")

### domain Type

`string`
