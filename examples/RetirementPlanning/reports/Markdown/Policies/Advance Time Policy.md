## Description

The policy which pushes forward time and determines any changes in asset prices.
## Called By
## Domain Spaces
1. [[Advance Time Space]]
## Followed By
## Codomain Spaces
1. [[Advance Time Space]]
2. [[Asset Prices Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Advance Time Policy V1
#### Description
Simple policy to convert percentages to shares
#### Logic
1. Grab the portfolio_value metric at the current time.
2. Define stock_shares as the portfolio_value * DOMAIN[0].percentage_stocks / STATE["Global"].stock_price
3. Define bond_shares as the portfolio_value * DOMAIN[0].percentage_bonds / STATE["Global"].bond_price
4. Return a space of {"bond_shares": bond_shares, "stock_shares": stock_shares}

