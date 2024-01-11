from ..Types import DummyType1, DummyType2

dummy_space1 = {
    "Name": "Dummy Space 1",
    "Schema": {
        "a": DummyType1,
    },
}

dummy_space2 = {
    "Name": "Dummy Space 2",
    "Schema": {"a": DummyType1, "b": DummyType1, "c": DummyType2},
}

dummy_spaces = [dummy_space1, dummy_space2]
