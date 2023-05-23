from typing import Dict
from ..Classes import StatefulMetric, StatefulMetricSet
from .general import check_json_keys


def convert_stateful_metric(data: Dict) -> StatefulMetricSet:
    """Function to convert stateful metric

    Args:
        data (Dict): Data to convert

    Returns:
        StatefulMetricSet: A stateful metric set
    """

    # Check the keys are correct
    check_json_keys(data, "Stateful Metric Set")

    # Copy
    data = data.copy()

    # Convert the variables
    new_variables = []
    for var in data["metrics"]:
        check_json_keys(var, "Stateful Metric")
        new_variables.append(StatefulMetric(var))
    data["metrics"] = new_variables

    # Build the state object
    return StatefulMetricSet(data)


def load_stateful_metrics(ms: Dict, json: Dict) -> None:
    """Function to load stateful metrics into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Stateful Metrics"] = {}
    for key in json["Stateful Metrics"]:
        ms["Stateful Metrics"][key] = convert_stateful_metric(
            json["Stateful Metrics"][key])
