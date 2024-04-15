## Description

The boundary action for a user looking to rebalance their portfolio.
## Called By
1. [[Person]]

## Followed By

## Constraints
1. CODOMAIN[0].percentage_bonds + CODOMAIN[0].percentage_stocks == 1

## Codomain Spaces
1. [[Investment Allocation Percentage Space]]

## Boundary Action Options:
### 1. 60/40 Portfolio
#### Description
An option where the person always rebalances to a target allocation of 60/40 stocks/bonds.
#### Logic
Return a codomain of {'percentage_bonds': .4, 'percentage_stocks': .6}

