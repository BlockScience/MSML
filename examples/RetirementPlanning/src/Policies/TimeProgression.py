advance_time_policy_option1 = {
    "name": "Advance Time Policy V1",
    "description": "Simple policy to convert percentages to shares",
    "logic": """1. Grab the portfolio_value metric at the current time.
2. Define stock_shares as the portfolio_value * DOMAIN[0].percentage_stocks / STATE["Global"].stock_price
3. Define bond_shares as the portfolio_value * DOMAIN[0].percentage_bonds / STATE["Global"].bond_price
4. Return a space of {"bond_shares": bond_shares, "stock_shares": stock_shares}""",
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
    "parameters_used": [],
    "metrics_used": [],
}

time_progression_policies = [advance_time_policy]
