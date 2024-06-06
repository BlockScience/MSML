dummy_stateful_metric = {
    "name": "Dummy Stateful Metrics",
    "notes": "",
    "metrics": [
        {
            "type": "Dummy Type 2",
            "name": "dummy_metric",
            "description": "The number of letters after the multiplier is taken off",
            "variables_used": [("Dummy State", "Total Length")],
            "parameters_used": ["DUMMY Length Multiplier"],
            "symbol": None,
            "domain": None,
        }
    ],
}

dummy_stateful_metrics = [dummy_stateful_metric]
