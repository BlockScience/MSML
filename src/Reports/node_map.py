import graphviz


def create_action_chains_graph(ms, action_keys):
    all_nodes = ms.crawl_action_chains(action_keys)

    graph = graphviz.Digraph()

    # Add entities
    for entity in all_nodes["Entities"]:
        graph.node(entity.name, entity.label, shape="cylinder", color="black")

    for ba in all_nodes["Boundary Actions"]:
        graph.node(ba.name, ba.label, shape="diamond",
                   color="orange", style='filled')

    for p in all_nodes["Policies"]:
        graph.node(p.name, p.label, shape="rectangle",
                   color="red", style='filled')

    for m in all_nodes["Mechanisms"]:
        graph.node(m.name, m.label, shape="oval",
                   color="blue", style='filled')

    for ba in all_nodes["Boundary Actions"]:
        for entity in ba.called_by:
            graph.edge(entity.name, ba.name)
        for call in ba.calls:
            graph.edge(ba.name, call.name)

    for p in all_nodes["Policies"]:
        for call in p.calls:
            graph.edge(p.name, call.name)

    return graph
