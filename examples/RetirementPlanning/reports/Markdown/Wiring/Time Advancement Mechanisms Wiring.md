## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Bond Price"])
EES0 --- EE0
EES1(["Time"])
EES1 --- EE0
EES2(["Stock Price"])
EES2 --- EE0
end

subgraph X5["Time Advancement Mechanisms Wiring"]
direction TB
X1["Increment Time Mechanism"]
X1 --> EES1
X2["Update Asset Prices Mechanism"]
X2 --> EES2
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"Advance Time Space"--> X1
X3 --"Asset Prices Space"--> X2
end
```

## Description

Block Type: Parallel Block
This wiring takes care of the mechanisms from the time advancement wiring
## Components
1. [[Increment Time Mechanism]]
2. [[Update Asset Prices Mechanism]]

## All Blocks
1. [[Increment Time Mechanism]]
2. [[Update Asset Prices Mechanism]]

## Constraints

## Domain Spaces
1. [[Advance Time Space]]
2. [[Asset Prices Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Terminating Space]]
2. [[Asset Prices Space]]
3. [[Empty Space]]
4. [[Advance Time Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Bond Price|Bond Price]]
2. [[Global]].[[Global State-Time|Time]]
3. [[Global]].[[Global State-Stock Price|Stock Price]]

