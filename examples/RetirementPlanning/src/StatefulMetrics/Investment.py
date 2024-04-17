investment_stateful_metric = {
    "name": "Investment Stateful Metrics",
    "notes": "Stateful metrics related to investments",
    "metrics": [
        {
            "type": "USD Type",
            "name": "portfolio_value",
            "description": "The total portfolio value as measured by the shares a person has times their prices, and then summed.",
            "variables_used": [
                ("Global State", "Stock Price"),
                ("Global State", "Bond Price"),
                ("Person State", "Stock Shares"),
                ("Person State", "Bond Shares"),
            ],
            "parameters_used": [],
            "symbol": "$V$",
            "domain": "$\mathbb{R}_{>=0}$",
        }
    ],
}

investment_stateful_metric_sets = [investment_stateful_metric]
