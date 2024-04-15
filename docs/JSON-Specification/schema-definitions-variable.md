# Variable Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## Variable Type

`object` ([Variable](schema-definitions-variable.md))

# Variable Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                               |
| :-------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)               | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")               |
| [name](#name)               | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")               |
| [description](#description) | `string` | Required | cannot be null | [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description") |
| [symbol](#symbol)           | `string` | Required | can be null    | [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")           |
| [domain](#domain)           | `string` | Required | can be null    | [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")           |
| [metadata](#metadata)       | `object` | Optional | cannot be null | [MSML](schema-definitions-variable-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/metadata")       |

## type

The type of the variable

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/type")

### type Type

`string`

## name

Variable name

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/name")

### name Type

`string`

## description

Description of what the variable is

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/description")

### description Type

`string`

## symbol

The symbol associated with the parameter (optional)

`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/symbol")

### symbol Type

`string`

## domain

The mathematical domain of the parameter (optional)

`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-variable-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/domain")

### domain Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-variable-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-variable-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Variable/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-variable-properties-metadata.md))
