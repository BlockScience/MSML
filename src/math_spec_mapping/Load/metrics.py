from typing import Dict
from ..Classes import Metric
from .general import check_json_keys


def convert_metric(ms, data: Dict, stateful_metrics_map) -> Metric:
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

    assert data["type"] in ms["Types"], "Type {} not in ms".format(data["type"])
    data["type"] = data["type"]

    for x in data["variables_used"]:
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
    for x in data["parameters_used"]:
        assert x in ms["Parameters"].all_parameters, "{} not in parameters".format(x)

    data["domain"] = tuple(data["domain"])
    for x in data["domain"]:
        assert x in ms["Spaces"], "{} not a valid space".format(x)
    data["domain"] = tuple(ms["Spaces"][x] for x in data["domain"])

    for x in data["metrics_used"]:
        assert (
            x in ms["Metrics"] or x in stateful_metrics_map
        ), "{} not a valid metric".format(x)

    data["metrics_used"] = tuple(
        ms["Metrics"][x] if x in ms["Metrics"] else stateful_metrics_map[x]
        for x in data["metrics_used"]
    )

    data["implementations"] = {}
    if "python" in ms["Implementations"]:
        if "metrics" in ms["Implementations"]["python"]:
            if data["name"] in ms["Implementations"]["python"]["metrics"]:
                data["implementations"]["python"] = ms["Implementations"]["python"][
                    "metrics"
                ][data["name"]]

    # Build the metric object
    return Metric(data)


def load_metrics(ms: Dict, json: Dict, stateful_metrics_map) -> None:
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
            if all(
                [
                    x in ms["Metrics"] or x in stateful_metrics_map
                    for x in metric["metrics_used"]
                ]
            ):
                i += 1
                metric = convert_metric(ms, metric, stateful_metrics_map)
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
                    z in ms["Metrics"] or z in names or z in stateful_metrics_map
                ), "{} is not defined in the spec, but it is referenced in {}".format(
                    z, y["name"]
                )
        assert len(metrics) == 0, "There are circular references"

    # Load the metrics into the policies
    for key in ms["Blocks"]:
        block = ms["Blocks"][key]
        hold = block.metrics_used[:]
        block.metrics_used = []
        for x in hold:
            assert (
                x in ms["Metrics"] or x in stateful_metrics_map
            ), "{} not a valid metric or stateful metric".format(x)
            block.metrics_used.append(
                ms["Metrics"][x] if x in ms["Metrics"] else stateful_metrics_map[x]
            )
        block.metrics_used = sorted(block.metrics_used, key=lambda x: x.name)
