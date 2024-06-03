from .types import DummyType1, DummyType2
from typing import TypedDict

DummyState = TypedDict('Dummy State', {'Words': DummyType1, 'Total Length': DummyType2, 'Variable C': DummyType2})
GlobalState = TypedDict('Global State', {})

state: GlobalState = {}