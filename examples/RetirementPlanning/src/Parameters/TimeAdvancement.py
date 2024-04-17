time_advancement_parameter_set = {
    "name": "Time Advancement Parameter Set",
    "notes": "",
    "parameters": [
        {
            "variable_type": "Decimal Type",
            "name": "stock_return_mu",
            "description": "The average yearly return of stocks",
            "symbol": "$r_s$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "stock_return_std",
            "description": "The average yearly standard deviation of stock returns",
            "symbol": "$\sigma_s$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "bond_return_mu",
            "description": "The average yearly return of bonds",
            "symbol": "$r_b$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "bond_return_std",
            "description": "The average yearly standard deviation of bond returns",
            "symbol": "$\sigma_b$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
    ],
}


time_advancement_parameter_set = [time_advancement_parameter_set]
