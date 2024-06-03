## Description

Randomly returns any length 1 string of combinations of D, E, F
## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints
## Codomain Spaces
1. [[Dummy Space 1]]

## Control Action Options:
### 1. V1 Dummy Control
#### Description
Equal weighted probability of choosing D, E or F each time
#### Logic
Select D, E, F with equal probabilities

### 2. V2 Dummy Control
#### Description
Randomly picks between D, E, F based on the 'DUMMY D Probability' Parameter
#### Logic
PARAM['DUMMY D Probability'] chance of picking D, (1-['D Probability']) / 2 chance for the other two

