from copy import deepcopy
from typing import _TypedDictMeta


def get_nested_types(data):
    data = deepcopy(data)
    for key in data:
        print(type(data[key]))
        if type(data[key]) == _TypedDictMeta:
            data[key] = get_nested_types(data[key].__annotations__)

    return data
