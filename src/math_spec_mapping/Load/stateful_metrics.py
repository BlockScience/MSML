from typing import Dict
from ..Classes import StatefulMetric, StatefulMetricSet
from .general import check_json_keys


def convert_stateful_metric(ms, data: Dict) -> StatefulMetricSet:
    """Function to convert stateful metric

    Args:
        data (Dict): Data to convert

    Returns:
        StatefulMetricSet: A stateful metric set
    """
    if "metadata" not in data:
        data["metadata"] = {}

    # Check the keys are correct
    check_json_keys(data, "Stateful Metric Set")

    # Copy
    data = data.copy()

    # Convert the variables
    new_variables = []
    for var in data["metrics"]:
        if "metadata" not in var:
            var["metadata"] = {}
        check_json_keys(var, "Stateful Metric")
        for x in var["variables_used"]:
            assert type(x) == tuple, "Variables used is not tuple"
            assert len(x) == 2, "Length of variables used is not 2"
            assert (
                x[0] in ms["State"]
            ), "State '{}' from variables used not in states".format(x[0])
            vm = ms["State"][x[0]].variable_map
            assert (
                x[1] in vm
            ), "Variable '{}' not in variable map for stateful metrics variables used".format(
                x[1]
            )

        assert (
            var["type"] in ms["Types"] or var["type"] in ms["Spaces"]
        ), "{} type/space referenced by {} is not present in math spec".format(
            var["type"], var["name"]
        )

        var["implementations"] = {}
        if "python" in ms["Implementations"]:
            if "stateful_metrics" in ms["Implementations"]["python"]:
                if var["name"] in ms["Implementations"]["python"]["stateful_metrics"]:
                    var["implementations"]["python"] = ms["Implementations"]["python"][
                        "stateful_metrics"
                    ][var["name"]]

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
    check = []
    for sm in json["Stateful Metrics"]:
        ms["Stateful Metrics"][sm["name"]] = convert_stateful_metric(ms, sm)
        for x in ms["Stateful Metrics"][sm["name"]].metrics:
            assert x.name not in check, "{} stateful metric name is repeated"
            check.append(x)
