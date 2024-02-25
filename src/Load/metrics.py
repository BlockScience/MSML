from typing import Dict
from ..Classes import Metric
from .general import check_json_keys


def convert_metric(ms, data: Dict) -> Metric:
    """Function to convert metric

    Args:
        data (Dict): Data to convert

    Returns:
        Metric: A metric
    """
    if "metadata" not in data:
        data["metadata"] = {}

    # Copy
    data = data.copy()

    """
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
        new_variables.append(StatefulMetric(var))
    data["metrics"] = new_variables
    """

    # Build the metric object
    return Metric(data)


def load_metrics(ms: Dict, json: Dict) -> None:
    """Function to load metrics into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Metrics"] = {}
    metrics = json["Metrics"]

    i = 1
    while i > 0:
        i = 0
        hold = []
        for metric in metrics:
            if all([x in ms["Metrics"] for x in metric["metrics_used"]]):
                i += 1
                metric = convert_metric(ms, metric)
                assert (
                    metric.name not in ms["Metrics"]
                ), "{} was a repeated metric".format(metric.name)
                ms["Metrics"][metric.name] = metric
            else:
                hold.append(metric)
        metrics = hold
    if len(metrics) > 0:
        names = [x["name"] for x in metrics]
        for y in metrics:
            for z in y["metrics_used"]:
                assert (
                    z in ms["Metrics"] or z in names
                ), "{} is not defined in the spec".format(z)
        assert len(metrics) == 0, "There are circular references"
