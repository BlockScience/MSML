from typing import TypedDict
from ..Types import DummyType1, DummyType2


dummy_space1 = TypedDict("Dummy Space 1", {"a": DummyType1,})
dummy_space2 = TypedDict("Dummy Space 2", {"a": DummyType1,
                                           "b": DummyType1,
                                           "c": DummyType2})