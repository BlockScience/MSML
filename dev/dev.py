class Block:
    def __init__(self, name):
        self.name = name

    def render(self, i):
        i += 1
        return "X{}[{}]".format(i, self.name), i


class ParallelBlock:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def render(self, i):
        start_i = i
        out = ""

        nodes = []

        # Render components
        for component in self.components:
            component, i = component.render(i)
            out += component
            out += "\n"
            nodes.append(i)
        end_i = i

        # Render invisible connections
        for ix1, ix2 in zip(nodes[:-1], nodes[1:]):
            out += "X{} ~~~ X{}".format(ix1, ix2)
            out += "\n"

        # Subgraph it
        i += 1
        out = "subgraph X{}[{}]\ndirection LR\n".format(i, self.name) + out

        out += "end"

        return out, i


class StackBlock:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def render(self, i):
        start_i = i
        out = ""

        nodes = []

        # Render components
        for component in self.components:
            component, i = component.render(i)
            out += component
            out += "\n"
            nodes.append(i)
        end_i = i

        # Render connections
        for ix1, ix2 in zip(nodes[:-1], nodes[1:]):
            out += "X{}-->X{}".format(ix1, ix2)
            out += "\n"

        # Subgraph it
        i += 1
        out = "subgraph X{}[{}]\ndirection TB\n".format(i, self.name) + out
        out += "end"

        return out, i


def write_simulation_block(sim_block):
    out = """```mermaid\ngraph TB\n"""
    out += sim_block.render(0)[0]
    out += "\n```"
    return out
