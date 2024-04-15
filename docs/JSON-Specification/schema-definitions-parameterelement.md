# ParameterElement Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## ParameterElement Type

`object` ([ParameterElement](schema-definitions-parameterelement.md))

# ParameterElement Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :----------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [variable\_type](#variable_type)     | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-variable_type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/variable_type")     |
| [name](#name)                        | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")                       |
| [description](#description)          | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")         |
| [symbol](#symbol)                    | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")                   |
| [domain](#domain)                    | `string` | Required | can be null    | [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")                   |
| [parameter\_class](#parameter_class) | `string` | Required | cannot be null | [MSML](schema-definitions-parameterelement-properties-parameter_class.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/parameter_class") |

## variable\_type

The type of that the parameter takes.

`variable_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-variable_type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/variable_type")

### variable\_type Type

`string`

## name

The unique name of the parameter

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/name")

### name Type

`string`

## description

The description of the parameter

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/description")

### description Type

`string`

## symbol

The symbol associated with the parameter (optional)

`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/symbol")

### symbol Type

`string`

## domain

The mathematical domain of the parameter (optional)

`domain`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/domain")

### domain Type

`string`

## parameter\_class

The type of paramter this is, of which the options are system (what you would find in production code of a system), behavioral (for what kinds of behavioral assumptions and distributions there are), and functional (for defining out different functional forms such as swapping in and out policies)

`parameter_class`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-parameterelement-properties-parameter_class.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/ParameterElement/properties/parameter_class")

### parameter\_class Type

`string`
