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
1. [[stock_return_mu]]
2. [[stock_return_std]]
3. [[bond_return_mu]]
4. [[bond_return_std]]
## Metrics Used
## Policy Options
### 1. Advance Time Policy V1
#### Description
Simple policy to advance time and use the normal distribution for price movements.
#### Logic
1. Take the current stock price and multiply it by (1+NORMAL_RANDOM(PARAMS["stock_return_mu"], PARAMS["stock_return_std"])) ** (DOMAIN["delta_time"]), define it as new_stock_price
2. Take the current bond price and multiply it by (1+NORMAL_RANDOM(PARAMS["bond_return_mu"], PARAMS["bond_return_std"])) ** (DOMAIN["delta_time"]), define it as new_bond_price
3. Return (DOMAIN[0], {
        "stock_price": new_stock_price,
        "bond_price": new_bond_price,
    })

