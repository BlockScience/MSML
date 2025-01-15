from .general import check_json_keys
from ..Classes import Type
import os
from typing import _UnionGenericAlias, List, _GenericAlias


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
    data["original_type_name"] = type_name

    if "python" in ms["Type Keys"]:

        if type_name in ms["Type Keys"]["python"]:
            data["type"]["python"] = ms["Type Keys"]["python"][type_name]
            if type(data["type"]["python"]) == dict:
                out = {}
                for key in data["type"]["python"]:
                    val = data["type"]["python"][key]
                    if type(val) == str:
                        val = ms["Types"][val].name
                    else:
                        val = val.__name__
                    out[key] = val
                data["type_name"]["python"] = str(out)
            elif type(data["type"]["python"]) == _UnionGenericAlias:
                data["type_name"]["python"] = data["type"]["python"].__repr__()
            elif type(data["type"]["python"]) == _GenericAlias:
                data["type_name"]["python"] = data["type"]["python"].__repr__()
            else:
                data["type_name"]["python"] = data["type"]["python"].__name__
    if "typescript" in ms["Type Keys"]:
        if type_name in ms["Type Keys"]["typescript"]:
            data["type"]["typescript"] = ms["Type Keys"]["typescript"][type_name]
            data["type_name"]["typescript"] = ms["Type Keys"]["typescript"][type_name]
    if "julia" in ms["Type Keys"]:
        if type_name in ms["Type Keys"]["julia"]:
            data["type"]["julia"] = ms["Type Keys"]["julia"][type_name]
            data["type_name"]["julia"] = ms["Type Keys"]["julia"][type_name]

    # Build the type object
    return Type(data)


def load_types(ms, json) -> None:

    ms["Types"] = {}
    for data in json["Types"]:
        ms["Types"][data["name"]] = convert_type(data, ms)


def load_python_type_key():
    from src.TypeMappings.types import mapping

    return mapping


def load_typescript_type_key(path):
    with open(path, "r") as file:
        type_definitions = file.read()
    type_definitions = type_definitions.split("\n")
    type_definitions = [x for x in type_definitions if len(x) > 0]
    hold = type_definitions[:]
    type_definitions = []
    if len(hold) > 0:
        type_definitions.append(hold.pop(0))
    while len(hold) > 0:
        curr = hold.pop(0)
        if "type" in curr or "interface" in curr:
            type_definitions.append(curr)
        else:
            type_definitions[-1] += "\n" + curr

    hold = type_definitions[:]
    type_definitions = {}
    for x in hold:
        name = x
        if x.startswith("type"):
            name = name[5:]
        elif x.startswith("interface"):
            name = name[10:]
        else:
            assert False
        name = name[: name.index("=")].strip()
        type_definitions[name] = x
    return type_definitions


def load_julia_type_key(path):
    with open(path, "r") as file:
        type_definitions = file.read()
    type_definitions = type_definitions.split("end")
    type_definitions = [x.strip() for x in type_definitions]
    type_definitions = [x for x in type_definitions if len(x) > 0]

    hold = type_definitions[:]
    type_definitions = {}
    for x in hold:
        name = x
        if x.startswith("abstract type"):
            name = name[14:]
            name = name[: name.index("<:")].strip()
        elif x.startswith("struct"):
            name = name[7:]
            name = name[: name.index("\n")].strip()
        if x.startswith("const"):
            name = name[6:]
            name = name[: name.index("=")].strip()
        else:
            assert False

        type_definitions[name] = x
    return type_definitions


def load_type_keys(ms):
    type_keys = {}
    python_path = "src/TypeMappings/types.py"
    typescript_path = "src/TypeMappings/types.ts"
    julia_path = "src/TypeMappings/types.jl"
    if os.path.exists(python_path):
        type_keys["python"] = load_python_type_key()
    if os.path.exists(typescript_path):
        type_keys["typescript"] = load_typescript_type_key(typescript_path)
    if os.path.exists(julia_path):
        type_keys["julia"] = load_julia_type_key(julia_path)

    python_path = "../src/TypeMappings/types.py"
    typescript_path = "../src/TypeMappings/types.ts"
    julia_path = "../src/TypeMappings/types.jl"
    if os.path.exists(python_path):
        type_keys["python"] = load_python_type_key()
    if os.path.exists(typescript_path):
        type_keys["typescript"] = load_typescript_type_key(typescript_path)
    if os.path.exists(julia_path):
        type_keys["julia"] = load_julia_type_key(julia_path)

    ms["Type Keys"] = type_keys
