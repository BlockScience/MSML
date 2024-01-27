from ..Types import DummyCompoundType, DummyType1, DummyType2

dummy_state = {
    "name": "Dummy",
    "notes": "A dummy state",
    "variables": [
        {
            "type": DummyCompoundType,
            "name": "Variable A",
            "description": "Variable A",
            "symbol": None,
            "domain": None,
        },
        {
            "type": DummyType1,
            "name": "Variable B",
            "description": "Variable B",
            "symbol": None,
            "domain": None,
        },
        {
            "type": DummyType2,
            "name": "Variable C",
            "description": "Variable C",
            "symbol": None,
            "domain": None,
        },
    ],
}
