from random import choice, choices


def v1_dummy_control(state, params, spaces):
    return [{"a": choice(["D", "E", "F"])}]


def v2_dummy_control(state, params, spaces):
    p1 = params["DUMMY D Probability"]
    p2 = (1 - p1) / 2
    return [{"a": choices(["D", "E", "F"], weights=[p1, p2, p2])[0]}]
