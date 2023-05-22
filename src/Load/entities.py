from typing import Dict
from ..Classes import Entity
from .general import check_json_keys


def convert_entity(data: Dict, ms: Dict) -> Entity:
    """Convert the entity dictionary to an object

    Args:
        data (Dict): The entity data
        ms (Dict): MathSpec dictionary

    Returns:
        Entity: An entity object
    """

    # Check the keys are correct
    check_json_keys(data, "Entity")

    # Copy
    data = data.copy()

    # Assert that the state is in the math spec and assign it here
    if data["state"]:
        name = data["state"]
        assert name in ms["State"], "{} state not in states dictionary".format(
            name)
        data["state"] = ms["State"][name]

    # Build the state object
    return Entity(data)


def load_entities(ms: Dict, json: Dict) -> None:
    """Function to load entities into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Entities"] = {}
    for key in json["Entities"]:
        ms["Entities"][key] = convert_entity(json["Entities"][key], ms)
