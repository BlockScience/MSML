dummy_policy_option = {
    "name": "Dummy Policy V1",
    "description": "V1 Dummy Policy",
    "logic": """
Dummy
Dummy
Dummy
""",
}

dummy_policy = {
    "name": "Dummy Policy",
    "description": "Dummy Policy",
    "constraints": [],
    "policy_options": [dummy_policy_option],
    "domain": ("Dummy Space 1",),
    "codomain": ("Dummy Space 2",),
    "parameters_used": ["dummy_parameter"],
}
