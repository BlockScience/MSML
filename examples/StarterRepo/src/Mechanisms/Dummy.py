dummy_mechanism = {
    "name": "DUMMY Log Results Mechanism",
    "description": "A mechanism which appends the word just added and also increments the total length",
    "constraints": [],
    "logic": "",
    "domain": [
        "Dummy Space 2",
    ],
    "parameters_used": [],
    "updates": [("Dummy", "Words", False), ("Dummy", "Total Length", False)],
}

dummy_mechanisms = [dummy_mechanism]
