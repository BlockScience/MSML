from .Dummy import dummy_spaces
from .Investments import investment_spaces
from .TimeProgression import time_progression_spaces

spaces = []
spaces.extend(dummy_spaces)
spaces.extend(investment_spaces)
spaces.extend(time_progression_spaces)
