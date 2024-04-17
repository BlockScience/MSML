advance_time_control_action_option1 = {
    "name": "Quarter Time Progression",
    "description": "Control action option which simply pushes time forward by a quarter.",
    "logic": "Return a codomain space of {'time_delta': .25}",
}

advance_time_control_action = {
    "name": "Advance Time Control Action",
    "description": "The control action which pushes forward the simulation time",
    "constraints": [],
    "control_action_options": [advance_time_control_action_option1],
    "codomain": [
        "Advance Time Space",
    ],
    "parameters_used": [],
}
