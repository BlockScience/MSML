dummy_boundary_action_v1_option = {
    "name": "V1 Dummy Boundary Action Option",
    "description": "Equal weighted probability of choosing A, B or C",
    "logic": "Select A, B, C with equal probabilities",
}

dummy_boundary_action = {
    "name": "Dummy Boundary Action",
    "description": "Randomly returns either A, B, C",
    "constraints": [],
    "boundary_action_options": [dummy_boundary_action_v1_option],
    "called_by": ["Dummy"],
    "codomain": [
        "Dummy Space 1",
    ],
    "parameters_used": [],
}


dummy_boundary_action2_v1_option = {
    "name": "V1 Dummy Boundary Action 2 Option",
    "description": "Equal weighted probability of choosing A, B or C each time",
    "logic": "Select A, B, C with equal probabilities",
}

dummy_boundary_action2_v2_option = {
    "name": "V2 Dummy Boundary Action 2 Option",
    "description": "Equal weighted probability of choosing A, B or C for the first letter, and then equal probability of choose the left over 2 for the next one.",
    "logic": "Select A, B, C with equal probabilities. Then choose from the remaining two with equal probability.",
}

dummy_boundary_action2 = {
    "name": "Dummy Boundary Action 2",
    "description": "Randomly returns any length 2 string of combinations of A, B, C",
    "constraints": [],
    "boundary_action_options": [
        dummy_boundary_action2_v1_option,
        dummy_boundary_action2_v2_option,
    ],
    "called_by": ["Dummy"],
    "codomain": [
        "Dummy Space 1",
    ],
    "parameters_used": [],
}

dummy_boundary_actions = [dummy_boundary_action, dummy_boundary_action2]
