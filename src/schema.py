import pathlib
import json

current_path = pathlib.Path(__file__).parent.resolve()
with open("{}/schema.json".format(current_path), "r") as f:
    schema = json.loads(f.read())
