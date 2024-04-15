dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary",
    "description": "Description",
    "logic": "A+B=C",
}

portfolio_allocation_boundary_action = {
    "name": "Portfolio Allocation Boundary Action",
    "description": "The boundary action for a user looking to rebalance their portfolio.",
    "constraints": [
        "CODOMAIN[0].percentage_bonds + CODOMAIN[0].percentage_stocks == 1"
    ],
    "boundary_action_options": [],
    "called_by": ["Person"],
    "codomain": [
        "Investment Allocation Percentage Space",
    ],
    "parameters_used": [],
}
