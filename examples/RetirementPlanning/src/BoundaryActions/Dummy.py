dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary",
    "description": "Description",
    "logic": "A+B=C",
}

dummy_boundary_action = {
    "name": "Dummy Boundary Action",
    "description": "Dummy",
    "constraints": [],
    "boundary_action_options": [dummy_boundary_action_v1_option],
    "called_by": ["Dummy"],
    "codomain": [
        "Dummy Space 1",
    ],
    "parameters_used": [],
}
