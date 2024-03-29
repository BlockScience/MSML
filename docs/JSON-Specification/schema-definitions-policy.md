# Policy Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Policy Type

`object` ([Policy](schema-definitions-policy.md))

# Policy Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                   |
| :----------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                        | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")                       |
| [description](#description)          | `string` | Required | cannot be null | [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")         |
| [constraints](#constraints)          | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")         |
| [policy\_options](#policy_options)   | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")   |
| [domain](#domain)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")                   |
| [codomain](#codomain)                | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")               |
| [parameters\_used](#parameters_used) | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used") |

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")

### name Type

`string`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")

### description Type

`string`

## constraints



`constraints`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")

### constraints Type

unknown\[]

## policy\_options



`policy_options`

*   is required

*   Type: `object[]` ([PolicyOption](schema-definitions-policyoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")

### policy\_options Type

`object[]` ([PolicyOption](schema-definitions-policyoption.md))

## domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")

### domain Type

`string[]`

## codomain



`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")

### codomain Type

`string[]`

## parameters\_used



`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used")

### parameters\_used Type

`string[]`
