from .types import DummyType1
from typing import TypedDict

SystemParameters = TypedDict('SystemParameters', {'dummy_parameter2': DummyType1})

BehavioralParameters = TypedDict('BehavioralParameters', {'dummy_parameter': DummyType1})

FunctionalParameters = TypedDict('FunctionalParameters', {'FP Dummy Boundary Action 2': str, 'FP Dummy Control Action': str})

Parameters = TypedDict("Parameters",{**BehavioralParameters.__annotations__,
 **FunctionalParameters.__annotations__,
**SystemParameters.__annotations__})

functional_parameters: FunctionalParameters = {"FP Dummy Boundary Action 2": None,
"FP Dummy Control Action": None,
}

behavioral_parameters: BehavioralParameters = {"dummy_parameter": None,
}

system_parameters: SystemParameters = {"dummy_parameter2": None,
}

parameters: Parameters = {**behavioral_parameters, **functional_parameters, **system_parameters}