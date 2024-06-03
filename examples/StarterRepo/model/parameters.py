from .types import DummyType2
from typing import TypedDict

SystemParameters = TypedDict('SystemParameters', {'DUMMY Length Multiplier': DummyType2})

BehavioralParameters = TypedDict('BehavioralParameters', {'DUMMY D Probability': DummyType2})

FunctionalParameters = TypedDict('FunctionalParameters', {'FP Dummy Boundary Action 2': str, 'FP Dummy Control Action': str})

Parameters = TypedDict("Parameters",{**BehavioralParameters.__annotations__,
 **FunctionalParameters.__annotations__,
**SystemParameters.__annotations__})

functional_parameters: FunctionalParameters = {"FP Dummy Boundary Action 2": None,
"FP Dummy Control Action": None,
}

behavioral_parameters: BehavioralParameters = {"DUMMY D Probability": None,
}

system_parameters: SystemParameters = {"DUMMY Length Multiplier": None,
}

parameters: Parameters = {**behavioral_parameters, **functional_parameters, **system_parameters}