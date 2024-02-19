# Entity Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Entity Type

`object` ([Entity](schema-definitions-entity.md))

# Entity Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")         |
| [notes](#notes)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")       |
| [state](#state)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")       |
| [metadata](#metadata) | `object` | Optional | cannot be null | [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")

### name Type

`string`

## notes



`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")

### notes Type

`string`

## state



`state`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")

### state Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-entity-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-entity-properties-metadata.md))
