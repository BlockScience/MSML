# Mechanism Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Mechanism Type

`object` ([Mechanism](schema-definitions-mechanism.md))

# Mechanism Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                         |
| :----------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                        | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")                       |
| [description](#description)          | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")         |
| [constraints](#constraints)          | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")         |
| [logic](#logic)                      | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")                     |
| [domain](#domain)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")                   |
| [parameters\_used](#parameters_used) | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used") |
| [updates](#updates)                  | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")                 |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")

### name Type

`string`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")

### description Type

`string`

## constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")

### constraints Type

unknown\[]

## logic



`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")

### logic Type

`string`

## domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")

### domain Type

`string[]`

## parameters\_used



`parameters_used`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used")

### parameters\_used Type

unknown\[]

## updates



`updates`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")

### updates Type

unknown\[]
