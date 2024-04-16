## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Stock Price"])
EES0 --- EE0
EES1(["Bond Price"])
EES1 --- EE0
EES2(["Time"])
EES2 --- EE0
end

subgraph X5["Time Advancement Mechanisms Wiring"]
direction TB
X1["Update Asset Prices Mechanism"]
X1 --> EES0
X1 --> EES1
X2["Increment Time Mechanism"]
X2 --> EES2
X3[Domain]

direction LR
direction TB
X3 --"Asset Prices Space"--> X1
X3 --"Advance Time Space"--> X2
end
```

## Description

Block Type: Parallel Block
This wiring takes care of the mechanisms from the time advancement wiring
## Components
1. [[Update Asset Prices Mechanism]]
2. [[Increment Time Mechanism]]

## All Blocks
1. [[Increment Time Mechanism]]
2. [[Update Asset Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Asset Prices Space]]
2. [[Advance Time Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Asset Prices Space]]
3. [[Advance Time Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].Stock Price
2. [[Global]].Bond Price
3. [[Global]].Time

