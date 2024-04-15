# Type Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type
```

This is for defining what a type might in its most basic form. These could be single typings or compound typings. The point here is to allow for changing typing in one single place and having it flow through anywhere else. I.e. if one were to define the currency type as USD, but then the project switched to using EUR, it would just require changing currency to be EUR.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## Type Type

`object` ([Type](schema-definitions-type.md))

# Type Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                 |
| :-------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/name")         |
| [type](#type)         | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")         |
| [notes](#notes)       | `string` | Required | cannot be null | [MSML](schema-definitions-type-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/notes")       |
| [metadata](#metadata) | `object` | Optional | cannot be null | [MSML](schema-definitions-type-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/name")

### name Type

`string`

## type



`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/type")

### type Type

`string`

## notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/notes")

### notes Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-type-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-type-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Type/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-type-properties-metadata.md))
