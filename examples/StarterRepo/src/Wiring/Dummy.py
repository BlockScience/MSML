dummy_wiring = []

dummy_wiring.append(
    {
        "name": "Dummy Boundary Wiring",
        "components": ["Dummy Boundary Action", "Dummy Policy", "Dummy Mechanism"],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)

dummy_wiring.append(
    {
        "name": "Dummy Control Wiring",
        "components": ["Dummy Control Action", "Dummy Policy", "Dummy Mechanism"],
        "description": "Dummy Control Block",
        "constraints": [],
        "type": "Stack",
        "optional_indices": [1],
    }
)

dummy_wiring.append(
    {
        "name": "Dummy Boundary Wiring 2",
        "components": ["Dummy Boundary Action 2", "Dummy Policy", "Dummy Mechanism"],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)
