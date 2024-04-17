portfolio_allocation_policy_option1 = {
    "name": "Portfolio Allocation Policy V1",
    "description": "Simple policy to convert percentages to shares",
    "logic": """1. Grab the portfolio_value metric at the current time.
2. Define stock_shares as the portfolio_value * DOMAIN[0].percentage_stocks / STATE["Global"].stock_price
3. Define bond_shares as the portfolio_value * DOMAIN[0].percentage_bonds / STATE["Global"].bond_price
4. Return a space of {"bond_shares": bond_shares, "stock_shares": stock_shares}""",
}

portfolio_allocation_policy = {
    "name": "Portfolio Allocation Policy",
    "description": "The policy which maps a percentage allocation to a shares allocation.",
    "constraints": ["DOMAIN[0].percentage_bonds + DOMAIN[0].percentage_stocks == 1"],
    "policy_options": [portfolio_allocation_policy_option1],
    "domain": [
        "Investment Allocation Percentage Space",
    ],
    "codomain": [
        "Investment Allocation Space",
    ],
    "parameters_used": [],
    "metrics_used": ["portfolio_value"],
}

investment_policies = [portfolio_allocation_policy]
