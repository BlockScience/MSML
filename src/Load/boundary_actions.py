from typing import Dict
from ..Classes import BoundaryAction, BoundaryActionOption
from .general import check_json_keys


def convert_boundary_action(data: Dict, ms: Dict) -> BoundaryAction:
    """Function to convert boundary action

    Args:
        data (Dict): JSON data
        ms (Dict): MathSpec dictionary

    Returns:
        BoundaryAction: Boundary action object
    """

    # Check the keys are correct
    check_json_keys(data, "Boundary Action")

    # Copy
    data = data.copy()

    # Convert the boundary action options
    new_bao = []
    for ba in data["boundary_action_options"]:
        check_json_keys(ba, "Boundary Action Option")
        new_bao.append(BoundaryActionOption(ba))
    data["boundary_action_options"] = new_bao

    # Assert that the entities in called_by are in math spec
    if data["called_by"]:
        for name in data["called_by"]:
            assert name in ms["Entities"], "{} entity not in entities dictionary".format(
                name)
        data["called_by"] = [ms["Entities"][x] for x in data["called_by"]]

    # Build the boundary action object
    return BoundaryAction(data)


def load_boundary_actions(ms: Dict, json: Dict) -> None:
    """Function to load boundary actions into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Boundary Actions"] = {}
    for key in json["Boundary Actions"]:
        ms["Boundary Actions"][key] = convert_boundary_action(
            json["Boundary Actions"][key], ms)
        for entity in ms["Boundary Actions"][key].called_by:
            entity.add_boundary_action(ms["Boundary Actions"][key])
