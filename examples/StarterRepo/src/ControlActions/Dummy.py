dummy_control_action_v1_option = {
    "name": "V1 Dummy Control",
    "description": "Equal weighted probability of choosing D, E or F each time",
    "logic": "Select D, E, F with equal probabilities",
}


dummy_control_action = {
    "name": "Dummy Control Action",
    "description": "Randomly returns any length 1 string of combinations of D, E, F",
    "constraints": [],
    "control_action_options": [dummy_control_action_v1_option],
    "codomain": [
        "Dummy Space 1",
    ],
    "parameters_used": [],
}
