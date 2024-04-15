portfolio_allocation_boundary_action_option1 = {
    "name": "60/40 Portfolio",
    "description": "An option where the person always rebalances to a target allocation of 60/40 stocks/bonds.",
    "logic": "Return a codomain of {'percentage_bonds': .4, 'percentage_stocks': .6}",
}

portfolio_allocation_boundary_action = {
    "name": "Portfolio Allocation Boundary Action",
    "description": "The boundary action for a user looking to rebalance their portfolio.",
    "constraints": [
        "CODOMAIN[0].percentage_bonds + CODOMAIN[0].percentage_stocks == 1"
    ],
    "boundary_action_options": [portfolio_allocation_boundary_action_option1],
    "called_by": ["Person"],
    "codomain": [
        "Investment Allocation Percentage Space",
    ],
    "parameters_used": [],
}
