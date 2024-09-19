def write_state_variable_table(target_state, links=False):
    table = """<table>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
        <th>Symbol</th>
        <th>Domain</th>
      </tr>"""

    for var in target_state.variables:
        table_vars = [
            var.name,
            var.description,
            var.type.name,
            var.symbol,
            var.domain,
        ]
        table += "<tr>"
        for i, tv in enumerate(table_vars):
            table += "<td>"
            if tv:
                if links and i == 2:
                    table += "[[{}]]".format(tv).replace("<", "&lt").replace(">", "&gt")
                else:
                    table += "{}".format(tv).replace("<", "&lt").replace(">", "&gt")

            table += "</td>"

        table += "</tr>"

    table += "</table>"
    return table


def write_state_variable_table_markdown(
    target_state, initial_values=None, links=False, compress_arrays=False
):
    if initial_values:
        table = """| Name | Description | Type | Symbol | Domain | Initial Value |
| --- | --- | --- | --- | --- | --- |
"""
    else:
        table = """| Name | Description | Type | Symbol | Domain |
| --- | --- | --- | --- | --- |
"""

    for var in target_state.variables:
        table_vars = [
            var.name,
            var.description,
            var.type.name,
            var.symbol,
            var.domain,
        ]
        table += "|"
        for i, tv in enumerate(table_vars):
            if tv:
                if links and i == 2:
                    table += "[[{}]]".format(tv)
                elif links and i == 0:
                    table += "[[{}-{}\|{}]]".format(target_state.name, tv, tv)
                else:
                    table += "{}".format(tv)
            table += "|"
        if initial_values:
            if compress_arrays:
                iv = initial_values[var.name]
                if type(iv) == list:
                    if len(iv) > 4:
                        iv = "[{}, {}, ... , {}, {}]".format(
                            iv[0], iv[1], iv[-2], iv[-1]
                        )
                table += " {} |".format(iv)
            else:
                table += " {} |".format(initial_values[var.name])

        table += "\n"

    return table


def write_initial_state_variables_tables(
    ms, initial_values, links=False, compress_arrays=False
):
    out = "### Global State"
    out += "\n\n"
    out += write_state_variable_table_markdown(
        ms.state["Global State"],
        initial_values=initial_values,
        links=links,
        compress_arrays=compress_arrays,
    )
    out += "\n"
    for x in ms.state:
        if x == "Global State":
            continue

        out += "### {}".format(x)
        out += "\n\n"
        out += write_state_variable_table_markdown(
            ms.state[x], links=links, compress_arrays=compress_arrays
        )
        out += "\n"

    return out


def write_global_state_variable_table(state):
    out = ""
    out += "<h3>Global State</h3>"
    out += write_state_variable_table(state)
    return out


def write_local_state_variable_tables(states):
    out = ""
    out += "<h3>Local States</h3>"
    for state in states:
        out += "<h4>{}</h4>".format(state.name)
        out += write_state_variable_table(state)
    return out


def write_state_section(state, links=False):
    out = ""
    out += "### Notes"
    out += "\n"
    out += state.notes
    out += "\n"
    out += "### Variable Table"
    out += "\n"
    out += write_state_variable_table_markdown(state, links=links)
    return out
