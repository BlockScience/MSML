from typing import Dict


class ActionTransmissionChannel:

    def __init__(self, data: Dict):
        self.origin = data["origin"]
        self.target = data["target"]
        self.space = data["space"]
        self.optional = data["optional"]
