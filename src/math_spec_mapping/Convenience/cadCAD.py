from copy import deepcopy
from typing import _TypedDictMeta, _GenericAlias


def get_underlying_type(data):
    if type(data) == _GenericAlias:
        data = [get_underlying_type(x) for x in data.__args__]
    elif type(data) == _TypedDictMeta:
        data = get_nested_types(data.__annotations__)
    return data


def get_nested_types(data):
    data = deepcopy(data)
    for key in data:
        if type(data[key]) == _TypedDictMeta:
            data[key] = get_nested_types(data[key].__annotations__)
        elif type(data[key]) == _GenericAlias:
            data[key] = get_underlying_type(data[key])

    return data
