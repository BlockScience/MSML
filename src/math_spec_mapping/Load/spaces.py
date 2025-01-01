from typing import Dict
from ..Classes import Space, TerminatingSpace, EmptySpace
from .general import check_json_keys


def convert_space(ms, data: Dict) -> Space:
    if "metadata" not in data:
        data["metadata"] = {}
    # Check the keys are correct
    check_json_keys(data, "Space")

    # Copy
    data = data.copy()

    for x in data["schema"]:
        assert (
            data["schema"][x] in ms["Types"]
        ), "Type {} not in ms for space {} at attribute {}".format(
            data["schema"][x], data["name"], x
        )
        data["schema"][x] = ms["Types"][data["schema"][x]]

    if "description" not in data:
        data["description"] = None

    # Build the space object
    return Space(data)


def load_spaces(ms: Dict, json: Dict) -> None:
    """Function to load spaces into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    # Placeholder for now
    ms["Spaces"] = {}
    ms["Spaces"]["Terminating Space"] = TerminatingSpace
    ms["Spaces"]["Empty Space"] = EmptySpace

    for space in json["Spaces"]:
        assert space["name"] not in ms["Spaces"], "{} repeated"
        ms["Spaces"][space["name"]] = convert_space(ms, space)
