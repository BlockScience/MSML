## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Stock Price"])
EES0 --- EE0
EES1(["Time"])
EES1 --- EE0
EES2(["Bond Price"])
EES2 --- EE0
end

subgraph X8["Time Advancement Wiring"]
direction TB
X1["Advance Time Control Action"]
X2["Advance Time Policy"]
subgraph X7["Time Advancement Mechanisms Wiring"]
direction TB
X3["Increment Time Mechanism"]
X3 --> EES1
X4["Update Asset Prices Mechanism"]
X4 --> EES0
X4 --> EES2
X5[Domain]

direction LR
direction TB
X5 --"Advance Time Space"--> X3
X5 --"Asset Prices Space"--> X4
end
X1--"Advance Time Space"--->X2
X2--"Advance Time Space
Asset Prices Space"---->X7
end
```

## Description

Block Type: Stack Block
This wiring takes care of time advancement
## Components
1. [[Advance Time Control Action]]
2. [[Advance Time Policy]]
3. [[Time Advancement Mechanisms Wiring]]

## All Blocks
1. [[Increment Time Mechanism]]
2. [[Update Asset Prices Mechanism]]
3. [[Advance Time Policy]]
4. [[Advance Time Control Action]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Asset Prices Space]]
2. [[Empty Space]]
3. [[Terminating Space]]
4. [[Advance Time Space]]

## Parameters Used
1. [[bond_return_std]]
2. [[stock_return_mu]]
3. [[bond_return_mu]]
4. [[stock_return_std]]

## Called By

## Calls

## All State Updates
1. [[Global]].Stock Price
2. [[Global]].Time
3. [[Global]].Bond Price

