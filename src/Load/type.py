from .general import check_json_keys
from ..Classes import Type


def convert_type(data, ms):

    if "metadata" not in data:
        data["metadata"] = {}

    # Check the keys are correct
    check_json_keys(data, "Policy")

    # Copy
    data = data.copy()

    # Build the policy object
    return Type(data)


def load_types(ms, json) -> None:

    ms["Types"] = {}
    for data in json["Types"]:
        ms["Types"][data["name"]] = convert_type(data, ms)
