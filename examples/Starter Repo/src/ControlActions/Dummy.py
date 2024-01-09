from ..Spaces import dummy_space2

dummy_control_action_v1_option = {
    "name": "V1 Dummy Control",
    "description": "Description",
    "logic": "A+B=C",
}

dummy_control_action = {
    "name": "Dummy Control Action",
    "description": "Dummy",
    "constraints": [],
    "control_action_options": [dummy_control_action_v1_option],
    "codomain": [dummy_space2],
    "parameters_used": [],
}
