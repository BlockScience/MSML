update_asset_prices_mechanism = {
    "name": "Update Asset Prices Mechanism",
    "description": "The mechanism which updates the amount of shares that a person has",
    "constraints": [],
    "logic": "The values from the domain space are mapped into the global state variables of stock_price and bond_price",
    "domain": [
        "Advance Time Space",
    ],
    "parameters_used": [],
    "updates": [("Person", "Stock Shares", False), ("Person", "Bond Shares", False)],
}

increment_time_mechanism = {
    "name": "Increment Time Mechanism",
    "description": "The mechanism which increments the time passed",
    "constraints": [],
    "logic": "The time attribute of the global state is incremented by DOMAIN[0].delta_time",
    "domain": [
        "Asset Prices Space",
    ],
    "parameters_used": [],
    "updates": [("Person", "Stock Shares", False), ("Person", "Bond Shares", False)],
}

time_advancement_mechanisms = [update_asset_prices_mechanism, increment_time_mechanism]
