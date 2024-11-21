from typing import Dict
from ..Classes import Block, StackBlock, ParallelBlock, SplitBlock
from .general import check_json_keys


def load_single_wiring(data, ms):
    block_type = data.pop("type")
    if "mermaid_show_name" not in data:
        data["mermaid_show_name"] = True
    if "loop" not in data:
        data["loop"] = False
    if "optional_indices" not in data:
        data["optional_indices"] = []
    if "metadata" not in data:
        data["metadata"] = {}
    # Check the keys are correct
    check_json_keys(data, "Block")
    assert block_type in [
        "Stack",
        "Parallel",
        "Split",
    ], "{} not a valid block type".format(block_type)

    # Map components
    data["components"] = [ms["Blocks"][x] for x in data["components"]]

    data["metrics_used"] = []
    for x in data["components"]:
        data["metrics_used"].extend(x.metrics_used)
    data["metrics_used"] = list(set(data["metrics_used"]))

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


def filter_atc(action_transmission_channels):
    seen = []
    out = []
    for x in action_transmission_channels:
        key = frozenset(x.items())
        if key not in seen:
            seen.append(key)
            out.append(x)
    return out


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
    action_transmission_channels = []
    wiring = json["Wiring"]

    i = 1
    while i > 0:
        i = 0
        hold = []
        for w in wiring:
            if all([x in ms["Blocks"] for x in w["components"]]):
                i += 1
                w = load_single_wiring(w, ms)
                assert w.name not in ms["Blocks"], "{} was a repeated block".format(
                    w.name
                )
                ms["Wiring"][w.name] = w
                ms["Blocks"][w.name] = w
                if w.block_type == "Stack Block":
                    action_transmission_channels.extend(
                        w.build_action_transmission_channels()
                    )
            else:
                hold.append(w)
        wiring = hold
    if len(wiring) > 0:
        names = [x["name"] for x in wiring]
        for y in wiring:
            for z in y["components"]:
                assert (
                    z in ms["Blocks"] or z in names
                ), "{} is not defined in the spec".format(z)
        assert len(wiring) == 0, "There are circular references"
    action_transmission_channels = filter_atc(action_transmission_channels)

    return action_transmission_channels
