from typing import Dict
from ..Classes import BoundaryAction, BoundaryActionOption
from .general import check_json_keys, check_domain_codomain_spaces


def convert_boundary_action(data: Dict, ms: Dict) -> BoundaryAction:
    """Function to convert boundary action

    Args:
        data (Dict): JSON data
        ms (Dict): MathSpec dictionary

    Returns:
        BoundaryAction: Boundary action object
    """
    if "metadata" not in data:
        data["metadata"] = {}

    data["codomain"] = tuple(data["codomain"])

    # Check the keys are correct
    check_json_keys(data, "Boundary Action")
    assert type(data["codomain"]) == tuple, "{} codomain is not a tuple".format(
        data["name"]
    )

    check_domain_codomain_spaces(data, ms)

    if len(data["codomain"]) == 0:
        data["codomain"] = ("Empty Space",)

    # Copy
    data = data.copy()

    # Convert the boundary action options
    new_bao = []
    for ba in data["boundary_action_options"]:
        check_json_keys(ba, "Boundary Action Option")

        ba["implementations"] = {}
        if "python" in ms["Implementations"]:
            if "boundary_action_options" in ms["Implementations"]["python"]:
                if (
                    ba["name"]
                    in ms["Implementations"]["python"]["boundary_action_options"]
                ):
                    ba["implementations"]["python"] = ms["Implementations"]["python"][
                        "boundary_action_options"
                    ][ba["name"]]
        new_bao.append(BoundaryActionOption(ba))
    data["boundary_action_options"] = new_bao

    # Assert that the entities in called_by are in math spec
    if data["called_by"]:
        for name in data["called_by"]:
            assert (
                name in ms["Entities"]
            ), "{} entity not in entities dictionary which is referenced in called_by for {}".format(
                name, data["name"]
            )
        data["called_by"] = [ms["Entities"][x] for x in data["called_by"]]

    data["codomain"] = tuple(ms["Spaces"][x] for x in data["codomain"])
    data["domain"] = (ms["Spaces"]["Empty Space"],)

    # Build the boundary action object
    return BoundaryAction(data)


def load_boundary_actions(ms: Dict, json: Dict) -> None:
    """Function to load boundary actions into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Boundary Actions"] = {}
    for ba in json["Boundary Actions"]:
        key = ba["name"]
        ms["Boundary Actions"][key] = convert_boundary_action(ba, ms)
        for entity in ms["Boundary Actions"][key].called_by:
            entity.add_boundary_action(ms["Boundary Actions"][key])

        for space in ms["Boundary Actions"][key].domain:
            space.domain_blocks.append(ms["Boundary Actions"][key])

        for space in ms["Boundary Actions"][key].codomain:
            space.codomain_blocks.append(ms["Boundary Actions"][key])
