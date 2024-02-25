class Metric:

    def __init__(self, data):
        self.name = data["name"]
        """
        self.type = data["type"]
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
        """
        pass
