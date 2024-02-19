# Wiring Schema

```txt
undefined#/definitions/Wiring
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Wiring Type

`object` ([Wiring](schema-definitions-wiring.md))

# Wiring Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                |
| :---------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                             | `string`  | Required | cannot be null | [Untitled schema](schema-definitions-wiring-properties-name.md "undefined#/definitions/Wiring/properties/name")                           |
| [components](#components)                 | `array`   | Required | cannot be null | [Untitled schema](schema-definitions-wiring-properties-components.md "undefined#/definitions/Wiring/properties/components")               |
| [description](#description)               | `string`  | Required | cannot be null | [Untitled schema](schema-definitions-wiring-properties-description.md "undefined#/definitions/Wiring/properties/description")             |
| [constraints](#constraints)               | `array`   | Required | cannot be null | [Untitled schema](schema-definitions-wiring-properties-constraints.md "undefined#/definitions/Wiring/properties/constraints")             |
| [type](#type)                             | `string`  | Required | cannot be null | [Untitled schema](schema-definitions-wiring-properties-typeenum.md "undefined#/definitions/Wiring/properties/type")                       |
| [mermaid\_show\_name](#mermaid_show_name) | `boolean` | Optional | cannot be null | [Untitled schema](schema-definitions-wiring-properties-mermaid_show_name.md "undefined#/definitions/Wiring/properties/mermaid_show_name") |
| [loop](#loop)                             | `boolean` | Optional | cannot be null | [Untitled schema](schema-definitions-wiring-properties-loop.md "undefined#/definitions/Wiring/properties/loop")                           |
| [optional\_indices](#optional_indices)    | `array`   | Optional | cannot be null | [Untitled schema](schema-definitions-wiring-properties-optional_indices.md "undefined#/definitions/Wiring/properties/optional_indices")   |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-name.md "undefined#/definitions/Wiring/properties/name")

### name Type

`string`

## components



`components`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-components.md "undefined#/definitions/Wiring/properties/components")

### components Type

`string[]`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-description.md "undefined#/definitions/Wiring/properties/description")

### description Type

`string`

## constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-constraints.md "undefined#/definitions/Wiring/properties/constraints")

### constraints Type

unknown\[]

## type



`type`

*   is required

*   Type: `string` ([TypeEnum](schema-definitions-wiring-properties-typeenum.md))

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-typeenum.md "undefined#/definitions/Wiring/properties/type")

### type Type

`string` ([TypeEnum](schema-definitions-wiring-properties-typeenum.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"Parallel"` |             |
| `"Stack"`    |             |

## mermaid\_show\_name



`mermaid_show_name`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-mermaid_show_name.md "undefined#/definitions/Wiring/properties/mermaid_show_name")

### mermaid\_show\_name Type

`boolean`

## loop



`loop`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-loop.md "undefined#/definitions/Wiring/properties/loop")

### loop Type

`boolean`

## optional\_indices



`optional_indices`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [Untitled schema](schema-definitions-wiring-properties-optional_indices.md "undefined#/definitions/Wiring/properties/optional_indices")

### optional\_indices Type

`integer[]`
