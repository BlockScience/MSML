from .Dummy import dummy_mechanisms
from .Investment import investment_mechanisms
from .TimeAdvancement import time_advancement_mechanisms

mechanism = []
mechanism.extend(dummy_mechanisms)
mechanism.extend(investment_mechanisms)
mechanism.extend(time_advancement_mechanisms)
