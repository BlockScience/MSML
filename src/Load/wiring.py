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


def check_repeat(d, blocks):
    for x in blocks:
        assert x not in d, "{} was a repeated block".format(x)


def load_wiring(ms, json):
    ms["Blocks"] = {}
    check_repeat(ms["Blocks"], ms["Boundary Actions"])
    ms["Blocks"].update(ms["Boundary Actions"])
    check_repeat(ms["Blocks"], ms["Control Actions"])
    ms["Blocks"].update(ms["Control Actions"])
    check_repeat(ms["Blocks"], ms["Policies"])
    ms["Blocks"].update(ms["Policies"])
    check_repeat(ms["Blocks"], ms["Mechanisms"])
    ms["Blocks"].update(ms["Mechanisms"])

    ms["Wiring"] = {}
    for w in json["Wiring"]:
        w = load_single_wiring(w, ms)
        assert w.name not in ms["Blocks"], "{} was a repeated block".format(w.name)
        ms["Wiring"][w.name] = w
        ms["Blocks"][w.name] = w
        if w.block_type == "Stack Block":
            print(w.build_action_transmission_channels())
