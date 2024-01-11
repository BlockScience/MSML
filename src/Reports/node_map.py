import graphviz
from textwrap import wrap


def create_action_chains_graph(ms, action_keys, name):
    all_nodes = ms.crawl_action_chains(action_keys)

    graph = graphviz.Digraph(name)

    # Add nodes
    for entity in all_nodes["Entities"]:
        graph.node(entity.name, entity.label, shape="cylinder", color="black")

    for ba in all_nodes["Boundary Actions"]:
        graph.node(ba.name, ba.label, shape="diamond", color="orange", style="filled")

    for ca in all_nodes["Control Actions"]:
        graph.node(ca.name, ca.label, shape="diamond", color="yellow", style="filled")

    for p in all_nodes["Policies"]:
        graph.node(p.name, p.label, shape="rectangle", color="red", style="filled")

    for m in all_nodes["Mechanisms"]:
        graph.node(m.name, m.label, shape="oval", color="azure2", style="filled")

    for entity in all_nodes["Entities2"]:
        graph.node(entity.name + "_2", entity.label, shape="cylinder", color="black")

    for su in all_nodes["State Updates"]:
        label = "{}.{}".format(su[0].name, su[1].name)
        graph.node(label, label)

    # Add edges
    for ba in all_nodes["Boundary Actions"]:
        for entity in ba.called_by:
            graph.edge(entity.name, ba.name)
        for call in ba.calls:
            optional_flag = call[1]
            space = call[2].name
            space = wrap(space, 12)
            space = "\n".join(space)
            call = call[0]
            graph.edge(ba.name, call.name, label=space)

    for ca in all_nodes["Control Actions"]:
        for call in ca.calls:
            optional_flag = call[1]
            space = call[2].name
            space = wrap(space, 12)
            space = "\n".join(space)
            call = call[0]
            graph.edge(ca.name, call.name, label=space)

    for p in all_nodes["Policies"]:
        for call in p.calls:
            space = call[2].name
            space = wrap(space, 12)
            space = "\n".join(space)
            # space = "\n".join(space.split(" "))
            optional_flag = call[1]
            call = call[0]
            if optional_flag:
                graph.edge(p.name, call.name, style="dashed", label=space)
            else:
                graph.edge(p.name, call.name, label=space)

    for m in all_nodes["Mechanisms"]:
        for u in m.updates:
            label1 = m.name
            label2 = "{}.{}".format(u[0].name, u[1].name)
            graph.edge(label1, label2)

    for su in all_nodes["State Updates"]:
        label1 = "{}.{}".format(su[0].name, su[1].name)
        label2 = su[0].name + "_2"
        graph.edge(label1, label2)

    return graph


"""
for sm in sm_actions:
    entity_name2 = sm.entity.label + "_2"
    if entity_name2 not in seen:
        graph.node(entity_name2, sm.entity.label,
                   shape="cylinder", color="black")
        seen.append(entity_name2)
    var_label = "{}.{}".format(sm.entity.label, sm.variable)
    if var_label not in seen:
        graph.node(var_label, var_label)
        graph.edge(var_label, entity_name2)
        seen.append(var_label)

    graph.edge(sm.origin.label, var_label)
"""
