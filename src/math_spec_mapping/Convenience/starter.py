import os


def remove_dummy_repo_components(path):

    directory_folders = os.listdir(path)

    if "StatefulMetrics" in directory_folders:
        path2 = path + "/StatefulMetrics"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    "from .Dummy import dummy_stateful_metrics\n", ""
                )
                contents = contents.replace(
                    "stateful_metrics.extend(dummy_stateful_metrics)\n", ""
                )
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Metrics" in directory_folders:
        path2 = path + "/Metrics"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import metrics_x\n", "")
                contents = contents.replace("metrics.extend(metrics_x)\n", "")
                contents = contents.replace("metrics.extend(metrics_x)", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    [
        "Mechanisms",
        "BoundaryActions",
        "Types",
        ".DS_Store",
        "ControlActions",
        "Displays",
        "Spaces",
        "__init__.py",
        "__pycache__",
        "State",
        "Policies",
        "Wiring",
        "Parameters",
        "TypeMappings",
        "Entities",
    ]
