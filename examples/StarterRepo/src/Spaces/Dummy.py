from ..Types import DummyType1, DummyType2

dummy_space1 = {
    "name": "Dummy Space 1",
    "schema": {
        "a": DummyType1,
    },
}

dummy_space2 = {
    "name": "Dummy Space 2",
    "schema": {"a": DummyType1, "b": DummyType1, "c": DummyType2},
}

dummy_spaces = [dummy_space1, dummy_space2]
