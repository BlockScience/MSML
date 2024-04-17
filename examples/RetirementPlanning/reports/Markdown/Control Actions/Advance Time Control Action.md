## Description

The control action which pushes forward the simulation time
## Followed By
1. [[Advance Time Policy]]

## Constraints
## Codomain Spaces
1. [[Advance Time Space]]

## Control Action Options:
### 1. Quarter Time Progression
#### Description
Control action option which simply pushes time forward by a quarter.
#### Logic
Return a codomain space of {'time_delta': .25}

