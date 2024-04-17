from .Dummy import dummy_wiring
from .Investments import investments_wiring
from .TimeAdvancement import time_advancement_wiring

wiring = []
wiring.extend(dummy_wiring)
wiring.extend(investments_wiring)
wiring.extend(time_advancement_wiring)
