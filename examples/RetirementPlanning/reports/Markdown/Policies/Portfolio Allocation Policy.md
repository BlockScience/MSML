## Description

The policy which maps a percentage allocation to a shares allocation.
## Called By
1. [[Portfolio Allocation Boundary Action]]
## Domain Spaces
1. [[Investment Allocation Percentage Space]]
## Followed By
1. [[Update Shares Mechanism]]
## Codomain Spaces
1. [[Investment Allocation Space]]
## Constraints
1. DOMAIN[0].percentage_bonds + DOMAIN[0].percentage_stocks == 1
## Parameters Used
## Metrics Used
1. [[portfolio_value]]
## Policy Options
### 1. Portfolio Allocation Policy V1
#### Description
Simple policy to convert percentages to shares
#### Logic
1. Grab the portfolio_value metric at the current time.
2. Define stock_shares as the portfolio_value * DOMAIN[0].percentage_stocks / STATE["Global"].stock_price
3. Define bond_shares as the portfolio_value * DOMAIN[0].percentage_bonds / STATE["Global"].bond_price
4. Return a space of {"bond_shares": bond_shares, "stock_shares": stock_shares}

