from typing import Dict


class StateUpdateTransmissionChannel:

    def __init__(self, data: Dict):
        self.origin = data["origin"]
        self.entity = data["entity"]
        self.variable = data["variable"]
        self.optional = data["optional"]
