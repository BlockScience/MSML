from .general import check_json_keys
from ..Classes import Type
import os


def convert_type(data, ms):

    if "metadata" not in data:
        data["metadata"] = {}

    # Check the keys are correct
    check_json_keys(data, "Type")

    # Copy
    data = data.copy()

    type_name = data["type"]
    data["type"] = {}
    data["type_name"] = {}

    if "python" in ms["Type Keys"]:

        if type_name in ms["Type Keys"]["python"]:
            data["type"]["python"] = ms["Type Keys"]["python"][type_name]
            data["type_name"]["python"] = str(data["type"]["python"])

    # Build the type object
    return Type(data)


def load_types(ms, json) -> None:

    ms["Types"] = {}
    for data in json["Types"]:
        ms["Types"][data["name"]] = convert_type(data, ms)


def load_python_type_key():
    from src.TypeMappings.types import mapping

    return mapping


def load_type_keys(ms) -> dict:
    type_keys = {}
    python_path = "src/TypeMappings/types.py"
    if os.path.exists(python_path):
        type_keys["python"] = load_python_type_key()

    ms["Type Keys"] = type_keys
