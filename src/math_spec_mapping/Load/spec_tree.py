import ast
import os


def index_to_line_and_column(lines, index):
    cumulative_length = 0
    for line_number, line in enumerate(lines):
        line_length = len(line) + 1  # +1 for the newline character
        if cumulative_length + line_length > index:
            column = index - cumulative_length
            return line_number, column
        cumulative_length += line_length

    raise ValueError("Index out of range")


def load_spec_tree(path, ms):
    tree = {}
    for folder in [
        "StatefulMetrics",
        "Metrics",
        "Mechanisms",
        "BoundaryActions",
        "Types",
        "ControlActions",
        "Displays",
        "Spaces",
        "State",
        "Policies",
        "Wiring",
        "Parameters",
        "Entities",
    ]:
        if folder == "StatefulMetrics":
            keys = ms.get_all_stateful_metric_names()
        elif folder == "Metrics":
            keys = ms.metrics.keys()
        elif folder == "Mechanisms":
            keys = ms.mechanisms.keys()
        elif folder == "BoundaryActions":
            keys = ms.boundary_actions.keys()
        elif folder == "Types":
            keys = ms.types.keys()
        elif folder == "ControlActions":
            keys = ms.control_actions.keys()
        elif folder == "Displays":
            keys = [x["name"] for x in ms.displays["Wiring"]]
        elif folder == "Spaces":
            keys = ms.spaces.keys()
        elif folder == "State":
            keys = ms.state.keys()
        elif folder == "Policies":
            keys = ms.policies.keys()
        elif folder == "Wiring":
            keys = ms.wiring.keys()
        elif folder == "Parameters":
            keys = ms.parameters.all_parameters
        elif folder == "Entities":
            keys = ms.entities.keys()
        else:
            assert False
        keys = list(keys)
        tree[folder] = {}

        init_path = path + "/" + folder + "/__init__.py"
        with open(init_path, "r") as file:
            tree2 = ast.parse(file.read(), filename=init_path)
            imports = []
            for node in ast.walk(tree2):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                    assert False, "Not implemented for imports that are not import from"
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        file_path = "{}/{}/{}.py".format(path, folder, node.module)

                        with open(file_path, "r") as file2:
                            contents = file2.read()
                        split = contents.split("\n")
                        for key in keys:
                            if key in contents:
                                line_number = (
                                    index_to_line_and_column(
                                        split, contents.index(key)
                                    )[0]
                                    + 1
                                )
                                tree[folder][key] = os.path.abspath(
                                    file_path
                                ) + "#L{}".format(line_number)
    return tree
