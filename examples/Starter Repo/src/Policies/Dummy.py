from ..Spaces import dummy_space1, dummy_space2

dummy_policy_option = {"name": "Dummy Policy V1",
                                 "description": "V1 Dummy Policy",
                                 "logic": """
Dummy
Dummy
Dummy
"""
                                 }

dummy_policy = {"name": "Dummy Policy",
                        "description": "Dummy Policy",
                        "constraints": [],
                        "policy_options": [dummy_policy_option],
                        "domain": [dummy_space1],
                        "codomain": [dummy_space2],
                        "parameters_used": ["dummy_parameter"]}
