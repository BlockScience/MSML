from graphviz import Digraph
import os


def load_svg_graphviz(graph: Digraph, overwrite: bool = False) -> str:
    """Function to load the svg version source, first writes
    an svg to the current directory, then reads it in, and finally
    deletes it after reading.

    Args:
        graph (Digraph): The graph to write
        overwrite (bool, optional): Whether to overwrite a file with the same name
        in the current directory. Defaults to False.

    Returns:
        str: The string representation of the svg
    """
    assert graph.name, "No graph name"

    # Check to avoid overwrites
    if not overwrite:
        assert "{}.gv.svg".format(graph.name) not in os.listdir(".")
        assert "{}.gv".format(graph.name) not in os.listdir(".")

    # Render the graph
    graph.render(directory=".", format='svg')

    # Read the svg
    with open("./{}.gv.svg".format(graph.name), "r") as f:
        svg = "\n".join(f.readlines())

    # Delete the files
    os.remove("./{}.gv.svg".format(graph.name))
    os.remove("./{}.gv".format(graph.name))

    return svg

def write_header() -> str:
    out = '<p>For explanations of generalized dynamical systems as well as how the mathematical specification library works in detail, please consult the documentation <a href="https://github.com/BlockScience/MSML/tree/main/docs">here</a></p>'
    out += "Graph Legend:<br/>"
    out += "Cylinder: Entity<br/>"
    out += "Orange Diamond: Boundary Action<br/>"
    out += "Red Square: Policy<br/>"
    out += "Blue Circle: Mechanism<br/>"
    out += "Transparent Circle: State Variable"
    return out