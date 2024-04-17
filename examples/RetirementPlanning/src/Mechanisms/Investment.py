update_shares_mechanism = {
    "name": "Update Shares Mechanism",
    "description": "The mechanism which updates the amount of shares that a person has",
    "constraints": [],
    "logic": "The values from the domain space are mapped into the person's state",
    "domain": [
        "Investment Allocation Space",
    ],
    "parameters_used": [],
    "updates": [("Person", "Stock Shares", False), ("Person", "Bond Shares", False)],
}

investment_mechanisms = [update_shares_mechanism]
