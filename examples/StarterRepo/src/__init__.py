from .StatefulMetrics import stateful_metrics
from .State import states
from .Spaces import spaces
from .Policies import policies
from .Parameters import parameters
from .Mechanisms import mechanisms
from .Entities import entities
from .BoundaryActions import boundary_actions
from .ControlActions import control_actions
from .Wiring import wiring
from .Types import types
from .Metrics import metrics
from .Displays import displays

math_spec_json = {
    "Policies": policies,
    "Spaces": spaces,
    "State": states,
    "Stateful Metrics": stateful_metrics,
    "Parameters": parameters,
    "Mechanisms": mechanisms,
    "Entities": entities,
    "Boundary Actions": boundary_actions,
    "Control Actions": control_actions,
    "Wiring": wiring,
    "Types": types,
    "Metrics": metrics,
    "Displays": displays,
}
