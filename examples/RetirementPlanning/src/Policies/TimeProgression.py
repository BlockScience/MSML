advance_time_policy_option1 = {
    "name": "Advance Time Policy V1",
    "description": "Simple policy to advance time and use the normal distribution for price movements.",
    "logic": """1. Take the current stock price and multiply it by (1+NORMAL_RANDOM(PARAMS["stock_return_mu"], PARAMS["stock_return_std"])) ** (DOMAIN["delta_time"]), define it as new_stock_price
2. Take the current bond price and multiply it by (1+NORMAL_RANDOM(PARAMS["bond_return_mu"], PARAMS["bond_return_std"])) ** (DOMAIN["delta_time"]), define it as new_bond_price
3. Return (DOMAIN[0], {
        "stock_price": new_stock_price,
        "bond_price": new_bond_price,
    })""",
}

advance_time_policy = {
    "name": "Advance Time Policy",
    "description": "The policy which pushes forward time and determines any changes in asset prices.",
    "constraints": [],
    "policy_options": [advance_time_policy_option1],
    "domain": [
        "Advance Time Space",
    ],
    "codomain": ["Advance Time Space", "Asset Prices Space"],
    "parameters_used": [
        "stock_return_mu",
        "stock_return_std",
        "bond_return_mu",
        "bond_return_std",
    ],
    "metrics_used": [],
}

time_progression_policies = [advance_time_policy]
