dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary",
    "description": "Description",
    "logic": "A+B=C",
}

portfolio_allocation_boundary_action = {
    "name": "Portfolio Allocation Boundary Action",
    "description": "The boundary action for a user looking to rebalance their portfolio.",
    "constraints": [""],
    "boundary_action_options": [dummy_boundary_action_v1_option],
    "called_by": ["Dummy"],
    "codomain": [
        "Allocation Percentage Space",
    ],
    "parameters_used": [],
}
