from src.math_spec_mapping import schema


def write_json_description(schema, key, name):
    out = "- **{}**: ".format(name)

    out += schema["definitions"][key]["description"]
    out += "\n"
    return out


def write_top_level_json_description(indent_level):

    out = "#{} MSML Components".format("#" * indent_level)
    out += "\n\n"
    out += "MSML extends GDS with multiple types of blocks and other enhancements. Below are the definitions of top level components."
    out += "\n\n"

    out += "##{} Types & Spaces".format("#" * indent_level)
    out += "\n\n"

    out += write_json_description(schema, "Type", "Type")
    out += write_json_description(schema, "Space", "Space")

    out += "\n"

    out += "##{} Entities, States, Parameters & Metrics".format("#" * indent_level)
    out += "\n\n"

    out += write_json_description(schema, "Entity", "Entity")
    out += write_json_description(schema, "State", "State")
    out += write_json_description(schema, "StatefulMetric", "Stateful Metric")
    out += write_json_description(schema, "Parameter", "Parameter")
    out += write_json_description(schema, "Metric", "Metric")

    out += "\n"

    out += "##{} Blocks & Wiring".format("#" * indent_level)
    out += "\n\n"

    out += write_json_description(schema, "BoundaryAction", "Boundary Action")
    out += write_json_description(schema, "ControlAction", "Control Action")
    out += write_json_description(schema, "Policy", "Policy")
    out += write_json_description(schema, "Mechanism", "Mechanism")
    out += write_json_description(schema, "Wiring", "Wiring")

    out += "\n"

    return out
