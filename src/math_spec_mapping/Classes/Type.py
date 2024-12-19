class Type:

    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.type_name = data["type_name"]
        self.notes = data["notes"]
        self.metadata = data["metadata"]
        self.original_type_name = data["original_type_name"]

    def __repr__(self):
        return self.name
