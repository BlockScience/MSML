class Metric:

    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.description = data["description"]
        self.variables_used = data["variables_used"]
        self.parameters_used = data["parameters_used"]
        self.domain = data["domain"]
        self.symbol = data["symbol"]
        self.metrics_used = data["metrics_used"]
        self.logic = data["logic"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.metadata = data["metadata"]
        self.implementations = data["implementations"]
