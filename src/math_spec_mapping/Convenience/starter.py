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

    if "Displays" in directory_folders:
        path2 = path + "/Displays"
        contents = os.listdir(path2)
        if "wiring.py" in contents:
            with open(path2 + "/wiring.py", "r") as f:
                contents = f.read()

                contents = contents.replace('"Dummy Boundary Wiring 2",\n', "")
                contents = contents.replace('"Dummy Boundary Wiring 2",', "")
                contents = contents.replace('"Dummy Boundary Wiring 2"', "")

                contents = contents.replace('"Dummy Boundary Wiring",\n', "")
                contents = contents.replace('"Dummy Boundary Wiring",', "")
                contents = contents.replace('"Dummy Boundary Wiring"', "")

                contents = contents.replace('"Dummy Control Wiring",\n', "")
                contents = contents.replace('"Dummy Control Wiring",', "")
                contents = contents.replace('"Dummy Control Wiring"', "")

            with open(path2 + "/wiring.py", "w") as f:
                f.write(contents)

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
                contents = contents.replace("mechanisms.extend(dummy_mechanisms)\n", "")
                contents = contents.replace("mechanisms.extend(dummy_mechanisms)", "")
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
                    "from .Dummy import dummy_boundary_action, dummy_boundary_action2\n",
                    "",
                )
                contents = contents.replace(
                    "from .Dummy import dummy_boundary_actions\n",
                    "",
                )

                contents = contents.replace(
                    "boundary_actions.extend(dummy_boundary_actions)",
                    "",
                )

                contents = contents.replace("dummy_boundary_action2,\n", "")
                contents = contents.replace("dummy_boundary_action2,", "")
                contents = contents.replace("dummy_boundary_action2", "")

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
                contents = contents.replace(
                    "from .Dummy import dummy_control_actions\n", ""
                )
                contents = contents.replace(
                    "control_actions.extend(dummy_control_actions)", ""
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
    if "State" in directory_folders:
        path2 = path + "/State"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_state\n", "")
                contents = contents.replace("dummy_state, ", "")
                contents = contents.replace("dummy_state,", "")
                contents = contents.replace("dummy_state", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Parameters" in directory_folders:
        path2 = path + "/Parameters"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    "from .Dummy import dummy_parameter_sets", ""
                )
                contents = contents.replace(
                    "parameters.extend(dummy_parameter_sets)", ""
                )

            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Spaces" in directory_folders:
        path2 = path + "/Spaces"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace("from .Dummy import dummy_spaces\n", "")
                contents = contents.replace("spaces.extend(dummy_spaces)", "")

            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Types" in directory_folders:
        path2 = path + "/Types"
        contents = os.listdir(path2)
        if "Dummy.py" in contents:
            os.remove(path2 + "/Dummy.py")
        if "__init__.py" in contents:
            with open(path2 + "/__init__.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    "from .Dummy import DummyCompoundType, DummyType1, DummyType2\n", ""
                )
                contents = contents.replace("from .Dummy import dummy_types\n", "")
                contents = contents.replace("types.extend(dummy_types)", "")
                contents = contents.replace(
                    """    DummyType1,
    DummyType2,
    DummyCompoundType,""",
                    "",
                )
                contents = contents.replace(
                    """    DummyType1,
    DummyType2,
    DummyCompoundType""",
                    "",
                )

            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "TypeMappings" in directory_folders:
        path2 = path + "/TypeMappings"
        contents = os.listdir(path2)

        if "types.py" in contents:
            with open(path2 + "/types.py", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    """    "DummyType1": str,
    "DummyType2": int,
    "DummyCompoundType": {"A": "Dummy Type 1", "B": "Dummy Type 2"},""",
                    "",
                )

            with open(path2 + "/types.py", "w") as f:
                f.write(contents)

    if "TypeMappings" in directory_folders:
        path2 = path + "/TypeMappings"
        contents = os.listdir(path2)

        if "types.py" in contents:
            with open(path2 + "/types.jl", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    """const DummyType1 = String
const DummyType2 = Integer
struct DummyCompoundType
    A::DummyType1
    B::DummyType2
end""",
                    "",
                )

            with open(path2 + "/types.jl", "w") as f:
                f.write(contents)

    if "TypeMappings" in directory_folders:
        path2 = path + "/TypeMappings"
        contents = os.listdir(path2)

        if "types.py" in contents:
            with open(path2 + "/types.ts", "r") as f:
                contents = f.read()
                contents = contents.replace(
                    """type DummyType1 = string
type DummyType2 = number
type DummyCompoundType = {"A": DummyType1, "B": DummyType2}""",
                    "",
                )

            with open(path2 + "/types.ts", "w") as f:
                f.write(contents)
