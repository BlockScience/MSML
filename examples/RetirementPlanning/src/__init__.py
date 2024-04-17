from .StatefulMetrics import stateful_metrics
from .State import states
from .Spaces import spaces
from .Policies import policies
from .Parameters import parameters
from .Mechanisms import mechanism
from .Entities import entities
from .BoundaryActions import boundary_actions
from .ControlActions import control_actions
from .Wiring import wiring
from .Types import types
from .Metrics import metrics

math_spec_json = {
    "Policies": policies,
    "Spaces": spaces,
    "State": states,
    "Stateful Metrics": stateful_metrics,
    "Parameters": parameters,
    "Mechanisms": mechanism,
    "Entities": entities,
    "Boundary Actions": boundary_actions,
    "Control Actions": control_actions,
    "Wiring": wiring,
    "Types": types,
    "Metrics": metrics,
}
