## Description

Randomly returns any length 2 string of combinations of A, B, C
## Called By
1. [[Dummy]]

## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints

## Codomain Spaces
1. [[Dummy Space 1]]

## Boundary Action Options:
### 1. V1 Dummy Boundary Action 2 Option
#### Description
Equal weighted probability of choosing A, B or C each time
#### Logic
Select A, B, C with equal probabilities

### 2. V2 Dummy Boundary Action 2 Option
#### Description
Equal weighted probability of choosing A, B or C for the first letter, and then equal probability of choose the left over 2 for the next one.
#### Logic
Select A, B, C with equal probabilities. Then choose from the remaining two with equal probability.

