from random import choice


def v1_dummy_control(state, params, spaces):
    return [{"a": choice(["D", "E", "F"])}]
