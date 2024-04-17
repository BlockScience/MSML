# Policy Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy
```

A definition of the policies that handle all logical things. This could be, for example, a policy which determines what price is paid given a boundary action of someone putting in a market buy order for a stock.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

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
| [metrics\_used](#metrics_used)       | `array`  | Required | cannot be null | [MSML](schema-definitions-policy-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metrics_used")       |
| [metadata](#metadata)                | `object` | Optional | cannot be null | [MSML](schema-definitions-policy-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metadata")               |

## name

The name of the policy

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/name")

### name Type

`string`

## description

Description of the policy

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/description")

### description Type

`string`

## constraints

Any constraints which the policy must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/constraints")

### constraints Type

`string[]`

## policy\_options

Possible implementations of the policy

`policy_options`

*   is required

*   Type: `object[]` ([PolicyOption](schema-definitions-policyoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-policy_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/policy_options")

### policy\_options Type

`object[]` ([PolicyOption](schema-definitions-policyoption.md))

## domain

The spaces which are passed in as inputs to the policy

`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/domain")

### domain Type

`string[]`

## codomain

The spaces which are returned as results of the policy

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/codomain")

### codomain Type

`string[]`

## parameters\_used

All parameters used in the implementations of policies

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/parameters_used")

### parameters\_used Type

`string[]`

## metrics\_used

All metrics used in implementation of policies

`metrics_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metrics_used")

### metrics\_used Type

`string[]`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-policy-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policy-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Policy/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-policy-properties-metadata.md))
