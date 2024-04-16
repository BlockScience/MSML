## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Person")]
EES0(["Stock Shares"])
EES0 --- EE0
EES1(["Bond Shares"])
EES1 --- EE0
end

subgraph X4["Portfolio Allocation Wiring"]
direction TB
X1["Portfolio Allocation Boundary Action"]
X2["Portfolio Allocation Policy"]
X3["Update Shares Mechanism"]
X3 --> EES0
X3 --> EES1
X1--"Investment Allocation Percentage Space"--->X2
X2--"Investment Allocation Space"--->X3
end
```

## Description

Block Type: Stack Block
This wiring takes care of all logic around a person updating their portfolio allocation
## Components
1. [[Portfolio Allocation Boundary Action]]
2. [[Portfolio Allocation Policy]]
3. [[Update Shares Mechanism]]

## All Blocks
1. [[Portfolio Allocation Boundary Action]]
2. [[Update Shares Mechanism]]
3. [[Portfolio Allocation Policy]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Investment Allocation Percentage Space]]
2. [[Terminating Space]]
3. [[Investment Allocation Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Person]].Stock Shares
2. [[Person]].Bond Shares

