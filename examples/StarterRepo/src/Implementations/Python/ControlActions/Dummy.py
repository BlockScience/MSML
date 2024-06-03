from random import choice


def v1_dummy_control(state, params, spaces):
    return [{"a": choice(["D", "E", "F"])}]


def v2_dummy_control(state, params, spaces):
    return [{"a": choice(["D", "D", "E", "F"])}]
