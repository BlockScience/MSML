def load_displays(ms, json) -> None:
    ms["Displays"] = {}
    load_wiring(ms, json)


def load_wiring(ms, json):
    ms["Displays"]["Wiring"] = []
    for display in json["Displays"]["wiring"]:
        for component in display["components"]:
            assert component in ms["Blocks"], "{} is not a valid block".format(
                component
            )
        ms["Displays"]["Wiring"].append(display)
