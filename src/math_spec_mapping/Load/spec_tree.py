import ast


def load_spec_tree(path):
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
                        for name in node.names:
                            file_path = "{}/{}/{}.py".format(path, folder, node.module)
                            print(file_path)
                            print(name.name)
