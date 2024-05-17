from .types import DummyType2, DummyCompoundType, DummyType1
from typing import TypedDict

DummyState = TypedDict('Dummy State', {'Variable A': DummyCompoundType, 'Variable B': DummyType1, 'Variable C': DummyType2})
GlobalState = TypedDict('Global State', {})

state: GlobalState = {}