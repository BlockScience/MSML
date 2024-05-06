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
                contents = contents.replace(
                    "stateful_metrics.extend(dummy_stateful_metrics)", ""
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

    """if "Displays" in directory_folders:
        path2 = path + "/Displays"
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
                f.write(contents)"""

    if "Wiring" in directory_folders:
        path2 = path + "/Wiring"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_wiring\n", "")
                contents = contents.replace("wiring.extend(dummy_wiring)\n", "")
                contents = contents.replace("wiring.extend(dummy_wiring)", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Mechanisms" in directory_folders:
        path2 = path + "/Mechanisms"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_mechanisms\n", "")
                contents = contents.replace("mechanism.extend(dummy_mechanisms)\n", "")
                contents = contents.replace("mechanism.extend(dummy_mechanisms)", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Policies" in directory_folders:
        path2 = path + "/Policies"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_policies\n", "")
                contents = contents.replace("policies.extend(dummy_policies)\n", "")
                contents = contents.replace("policies.extend(dummy_policies)", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "BoundaryActions" in directory_folders:
        path2 = path + "/BoundaryActions"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    "from .Dummy import dummy_boundary_action\n", ""
                )
                contents = contents.replace("dummy_boundary_action,\n", "")
                contents = contents.replace("dummy_boundary_action,", "")
                contents = contents.replace("dummy_boundary_action", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "ControlActions" in directory_folders:
        path2 = path + "/ControlActions"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    "from .Dummy import dummy_control_action\n", ""
                )
                contents = contents.replace("dummy_control_action,\n", "")
                contents = contents.replace("dummy_control_action,", "")
                contents = contents.replace("dummy_control_action", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)
    if "Entities" in directory_folders:
        path2 = path + "/Entities"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_entity\n", "")
                contents = contents.replace("dummy_entity, ", "")
                contents = contents.replace("dummy_entity,", "")
                contents = contents.replace("dummy_entity", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    [
        "Types",
        "Spaces",
        "__init__.py",
        "State",
        "Parameters",
        "TypeMappings",
    ]
