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
                contents = contents.replace("from .Dummy import dummy_metrics\n", "")
                contents = contents.replace("metrics.extend(dummy_metrics)\n", "")
                contents = contents.replace("metrics.extend(dummy_metrics)", "")
            with open(path2 + "/__init__.py", "w") as f:
                f.write(contents)

    if "Displays" in directory_folders:
        path2 = path + "/Displays"
        contents = os.listdir(path2)
        if "wiring.py" in contents:
            with open(path2 + "/wiring.py", "r") as f:
                contents = f.read()

                contents = contents.replace('"DUMMY Length-1 Boundary Wiring",\n', "")
                contents = contents.replace('"DUMMY Length-1 Boundary Wiring",', "")
                contents = contents.replace('"DUMMY Length-1 Boundary Wiring"', "")

                contents = contents.replace('"DUMMY Length-2 Boundary Wiring",\n', "")
                contents = contents.replace('"DUMMY Length-2 Boundary Wiring",', "")
                contents = contents.replace('"DUMMY Length-2 Boundary Wiring"', "")

                contents = contents.replace('"DUMMY Control Wiring",\n', "")
                contents = contents.replace('"DUMMY Control Wiring",', "")
                contents = contents.replace('"DUMMY Control Wiring"', "")

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
        contents = os.listdir(path2)
        if "Global.py" in contents:
            with open(path2 + "/Global.py", "r") as f:
                contents = f.read()
            for x in [
                """        {
            "type": "DUMMY Integer Type",
            "name": "Time",
            "description": "The clock time",
            "symbol": None,
            "domain": None,
        }""",
                """        {
            "type": "Entity Type",
            "name": "Dummy",
            "description": "The dummy entity",
            "symbol": None,
            "domain": None,
        }""",
            ]:
                contents = contents.replace("{},\n".format(x), "")
                contents = contents.replace("{}\n".format(x), "")
                contents = contents.replace("{},".format(x), "")
                contents = contents.replace("{}".format(x), "")
            with open(path2 + "/Global.py", "w") as f:
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
                for x in [
                    '"DummyABCDEFType": str',
                    '"DummyIntegerType": int',
                    '"DummyDecimalType": float',
                ]:
                    contents = contents.replace("{},\n".format(x), "")
                    contents = contents.replace("{}\n".format(x), "")
                    contents = contents.replace("{},".format(x), "")
                    contents = contents.replace("{}".format(x), "")

            with open(path2 + "/types.py", "w") as f:
                f.write(contents)

    if "TypeMappings" in directory_folders:
        path2 = path + "/TypeMappings"
        contents = os.listdir(path2)

        if "types.jl" in contents:
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
                    """type DummyABCDEFType = string""",
                    "",
                )
                contents = contents.replace(
                    """type DummyIntegerType = number""",
                    "",
                )
                contents = contents.replace(
                    """type DummyDecimalType = number""",
                    "",
                )

            with open(path2 + "/types.ts", "w") as f:
                f.write(contents)

    remove_dummy_repo_implementations(path)


def remove_implementation_folder(path, folder, component_names, import_statement):
    path = path + "/" + folder
    contents = os.listdir(path)
    if "Dummy.py" in contents:
        os.remove(path + "/Dummy.py")
    if "__init__.py" in contents:
        with open(path + "/__init__.py", "r") as f:
            contents = f.read()
            contents = contents.replace(import_statement + "\n", "")
            contents = contents.replace(import_statement, "")
            for x in component_names:
                contents = contents.replace("{},\n".format(x), "")
                contents = contents.replace("{}\n".format(x), "")
                contents = contents.replace("{},".format(x), "")
                contents = contents.replace("{}".format(x), "")
        with open(path + "/__init__.py", "w") as f:
            f.write(contents)


def remove_dummy_repo_implementations(path):
    path = path + "/Implementations/Python"
    directory_folders = os.listdir(path)

    if "BoundaryActions" in directory_folders:
        remove_implementation_folder(
            path,
            "BoundaryActions",
            [
                '"Length-1 ABC Equal Weight Option": v1_dummy_boundary',
                '"DUMMY Length-2 ABC Equal Weight Option": v1_dummy_boundary2',
                '"DUMMY Length-2 ABC Equal Weight 2 Option": v2_dummy_boundary2',
            ],
            "from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2",
        )
    if "ControlActions" in directory_folders:
        remove_implementation_folder(
            path,
            "ControlActions",
            [
                '"DUMMY Length-1 DEF Equal Weight Option": v1_dummy_control',
                '"DUMMY Length-1 DEF D Probability Option": v2_dummy_control',
            ],
            "from .Dummy import v1_dummy_control, v2_dummy_control",
        )
    if "Policies" in directory_folders:
        remove_implementation_folder(
            path,
            "Policies",
            ['"DUMMY Letter Count Policy V1": dummy_letter_count_policy'],
            "from .Dummy import dummy_letter_count_policy",
        )
    if "Mechanisms" in directory_folders:
        remove_implementation_folder(
            path,
            "Mechanisms",
            [
                '"DUMMY Update Dummy Entity Mechanism": dummy_update_dummy_entity_mechanism',
                '"DUMMY Increment Time Mechanism": dummy_increment_time_mechanism',
                '"DUMMY Log Simulation Data Mechanism": dummy_log_simulation_data_mechanism',
            ],
            """from .Dummy import (
    dummy_update_dummy_entity_mechanism,
    dummy_increment_time_mechanism,
    dummy_log_simulation_data_mechanism,
)""",
        )

    if "StatefulMetrics" in directory_folders:
        remove_implementation_folder(
            path,
            "StatefulMetrics",
            ['"DUMMY Nominal Length Stateful Metric": dummy_metric'],
            """from .Dummy import dummy_metric""",
        )
    if "Metrics" in directory_folders:
        remove_implementation_folder(
            path,
            "Metrics",
            ['"DUMMY Multiplied Length Metric": dummy_multiplied_length_metric'],
            """from .Dummy import dummy_multiplied_length_metric""",
        )
