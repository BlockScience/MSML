time_advancement_wiring = []

time_advancement_wiring.append(
    {
        "name": "Time Advancement Mechanisms Wiring",
        "components": [
            "Increment Time Mechanism",
            "Update Asset Prices Mechanism",
        ],
        "description": "This wiring takes care of the mechanisms from the time advancement wiring",
        "constraints": [],
        "type": "Parallel",
    }
)

time_advancement_wiring.append(
    {
        "name": "Time Advancement Wiring",
        "components": [
            "Advance Time Control Action",
            "Advance Time Policy",
            "Time Advancement Mechanisms Wiring",
        ],
        "description": "This wiring takes care of time advancement",
        "constraints": [],
        "type": "Stack",
    }
)
