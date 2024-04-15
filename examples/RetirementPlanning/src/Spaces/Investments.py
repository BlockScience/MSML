investment_allocation_percentage_space = {
    "name": "Investment Allocation Percentage Space",
    "schema": {
        "percentage_bonds": "Decimal Type",
        "percentage_stocks": "Decimal Type",
    },
}

investment_allocation_space = {
    "name": "Investment Allocation Space",
    "schema": {
        "bond_shares": "Bond Shares Type",
        "stock_shares": "Stock Shares Type",
    },
}


investment_spaces = [
    investment_allocation_percentage_space,
    investment_allocation_space,
]
