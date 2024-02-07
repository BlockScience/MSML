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
            var.type.__name__,
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


def write_state_section(state):
    out = ""
    out += "### Notes"
    out += "\n"
    out += state.notes
    out += "\n"
    out += "### Variable Table"
    out += "\n"
    out += write_state_variable_table(state, links=True)
    return out
