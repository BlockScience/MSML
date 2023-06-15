import graphviz


def create_action_chains_graph(ms, action_keys):
    all_nodes = ms.crawl_action_chains(action_keys)

    graph = graphviz.Digraph()

    for entity in all_nodes["Entities"]:
        graph.node(entity.name, entity.name, shape="cylinder", color="black")

    return graph
