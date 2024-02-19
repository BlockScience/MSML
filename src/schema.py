import pathlib
import json

current_path = pathlib.Path(__file__).parent.resolve()
with open("{}/schema.schema.json".format(current_path), "r") as f:
    f = f.read()
f = f.replace("./schema.schema.json/", "")
schema = json.loads(f)
