# Space Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space
```

Spaces are similar to types in that they define a schema for data and are used as the domain/codomain for different blocks. They can be thought of as typed dictionaries.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## Space Type

`object` ([Space](schema-definitions-space.md))

# Space Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                           |
| :---------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)     | `string` | Required | cannot be null | [MSML](schema-definitions-space-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/name") |
| [schema](#schema) | `object` | Required | cannot be null | [MSML](schema-definitions-schema.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/schema")              |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-space-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/name")

### name Type

`string`

## schema



`schema`

*   is required

*   Type: `object` ([Schema](schema-definitions-schema.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-schema.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Space/properties/schema")

### schema Type

`object` ([Schema](schema-definitions-schema.md))
