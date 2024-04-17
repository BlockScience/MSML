from .Dummy import dummy_policies
from .Investments import investment_policies
from .TimeProgression import time_progression_policies

policies = []
policies.extend(dummy_policies)
policies.extend(investment_policies)
policies.extend(time_progression_policies)
