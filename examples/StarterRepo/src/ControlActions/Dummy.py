dummy_control_action_v1_option = {
    "name": "V1 Dummy Control",
    "description": "Equal weighted probability of choosing D, E or F each time",
    "logic": "Select D, E, F with equal probabilities",
}

dummy_control_action_v2_option = {
    "name": "V2 Dummy Control",
    "description": "Randomly picks between D, E, F based on the 'DUMMY D Probability' Parameter",
    "logic": "PARAM['DUMMY D Probability'] chance of picking D, (1-['D Probability']) / 2 chance for the other two",
}


dummy_control_action = {
    "name": "Dummy Control Action",
    "description": "Randomly returns any length 1 string of combinations of D, E, F",
    "constraints": [],
    "control_action_options": [
        dummy_control_action_v1_option,
        dummy_control_action_v2_option,
    ],
    "codomain": [
        "Dummy Space 1",
    ],
    "parameters_used": ["DUMMY D Probability"],
}

dummy_control_actions = [dummy_control_action]
