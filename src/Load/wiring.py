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

    # Map to the correct block
    assert False


def load_wiring(ms, json):
    ms["Wiring"] = {}
    for w in json["Wiring"]:
        w = load_single_wiring(w, ms)
        ms["Wiring"][w.name] = w

    # Go through each block's components and map them
    assert False
