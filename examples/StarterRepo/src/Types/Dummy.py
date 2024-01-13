from typing import NewType, TypedDict

DummyType1 = NewType("Dummy Type 1", str)
DummyType2 = NewType("Dummy Type 2", int)

DummyCompoundType =  NewType("Dummy Compound Type", TypedDict("Dummy Compound Type", {"A": DummyType1,
                                                                                      "B": DummyType2}))
