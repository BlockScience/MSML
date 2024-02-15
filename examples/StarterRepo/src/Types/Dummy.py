from typing import NewType, TypedDict

DummyType1 = {"name": "Dummy Type 1", "type": str, "notes": ""}

DummyType2 = {"name": "Dummy Type 2", "type": int, "notes": ""}


DummyCompoundType = {
    "name": "Dummy Compound Type",
    "type": TypedDict(
        "Dummy Compound Type", {"A": DummyType1["type"], "B": DummyType2["type"]}
    ),
    "notes": "",
}
