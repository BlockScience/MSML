from .types import DummyType2, DummyType1
from typing import TypedDict

TerminatingSpace = TypedDict('Terminating Space', {})
EmptySpace = TypedDict('Empty Space', {})
DummySpace1 = TypedDict('Dummy Space 1', {'a': DummyType1})
DummySpace2 = TypedDict('Dummy Space 2', {'a': DummyType1, 'b': DummyType1, 'c': DummyType2})
