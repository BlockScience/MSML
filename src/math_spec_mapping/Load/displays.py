def load_displays(ms, json) -> None:
    ms["Displays"] = {}
    load_wiring(ms, json)


def load_wiring(ms, json):
    ms["Displays"]["Wiring"] = []
    for display in json["Displays"]["wiring"]:
        for component in display["components"]:
            assert (
                component in ms["Blocks"]
            ), "{} referenced in {} is not a valid block".format(
                component, display["name"]
            )
        ms["Displays"]["Wiring"].append(display)
