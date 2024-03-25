class Type:

    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.type_name = data["type_name"]
        self.notes = data["notes"]
        self.metadata = data["metadata"]
