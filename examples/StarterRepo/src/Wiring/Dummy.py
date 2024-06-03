dummy_wiring = []

dummy_wiring.append(
    {
        "name": "Dummy Boundary Wiring",
        "components": [
            "Dummy Boundary Action",
            "DUMMY Letter Count Policy",
            "DUMMY Log Results Mechanism",
        ],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)

dummy_wiring.append(
    {
        "name": "Dummy Control Wiring",
        "components": [
            "Dummy Control Action",
            "DUMMY Letter Count Policy",
            "DUMMY Log Results Mechanism",
        ],
        "description": "Dummy Control Block",
        "constraints": [],
        "type": "Stack",
        "optional_indices": [1],
    }
)

dummy_wiring.append(
    {
        "name": "Dummy Boundary Wiring 2",
        "components": [
            "Dummy Boundary Action 2",
            "DUMMY Letter Count Policy",
            "DUMMY Log Results Mechanism",
        ],
        "description": "Dummy Boundary Block",
        "constraints": [],
        "type": "Stack",
    }
)
