from .StateUpdateTransmissionChannels import state_update_transmission_channels
from .StatefulMetrics import stateful_metrics
from .State import state
from .Spaces import spaces
from .Policies import policies
from .Parameters import parameters
from .Mechanisms import mechanism
from .Entities import entities
from .BoundaryActions import boundary_actions
from .ControlActions import control_actions
from .Wiring import wiring

math_spec_json = {
    "Policies": policies,
    "Spaces": spaces,
    "State": state,
    "Stateful Metrics": stateful_metrics,
    "State Update Transmission Channels": state_update_transmission_channels,
    "Parameters": parameters,
    "Mechanisms": mechanism,
    "Entities": entities,
    "Boundary Actions": boundary_actions,
    "Control Actions": control_actions,
    "Wiring": wiring,
}
