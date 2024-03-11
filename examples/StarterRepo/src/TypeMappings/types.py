from typing import TypedDict

mapping = {
    "DummyType1": str,
    "DummyType2": int,
    "DummyCompoundType": TypedDict(
        "DummyCompoundType", {"A": "DummyType1", "B": "DummyType2"}
    ),
}
