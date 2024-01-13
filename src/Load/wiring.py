from typing import Dict
from ..Classes import Block, StackBlock, ParallelBlock, SplitBlock
from .general import check_json_keys


def load_single_wiring(data, ms):
    block_type = data.pop("type")
    # Check the keys are correct
    check_json_keys(data, "Block")
    assert block_type in [
        "Stack",
        "Parallel",
        "Split",
    ], "{} not a valid block type".format(block_type)

    # Map components
    data["components"] = [ms["Blocks"][x] for x in data["components"]]

    # Map to the correct block
    if block_type == "Stack":
        block = StackBlock(data)
    elif block_type == "Parallel":
        block = ParallelBlock(data)
    elif block_type == "Split":
        block = SplitBlock(data)
    else:
        assert False

    return block


def load_wiring(ms, json):
    ms["Blocks"] = {}
    ms["Blocks"].update(ms["Boundary Actions"])
    ms["Blocks"].update(ms["Control Actions"])
    ms["Blocks"].update(ms["Policies"])
    ms["Blocks"].update(ms["Mechanisms"])

    ms["Wiring"] = {}
    for w in json["Wiring"]:
        w = load_single_wiring(w, ms)
        ms["Wiring"][w.name] = w
        ms["Blocks"][w.name] = w
