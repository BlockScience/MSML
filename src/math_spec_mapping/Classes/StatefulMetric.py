from typing import Dict


class StatefulMetric:

    def __init__(self, data: Dict):
        self.type = data["type"]
        self.name = data["name"]
        self.description = data["description"]
        self.variables_used = data["variables_used"]
        self.parameters_used = data["parameters_used"]
        self.symbol = data["symbol"]
        self.domain = data["domain"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.metadata = data["metadata"]
        self.implementations = data["implementations"]


class StatefulMetricSet:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.metrics = data["metrics"]
        self.metadata = data["metadata"]
