from typing import Dict


class Block:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.domain = data["domain"]
        self.codomain = data["codomain"]
        self.parameters_used = data["parameters_used"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.called_by = []
        self.calls = []

    def render_mermaid(self, i):
        i += 1
        return "X{}[{}]".format(i, self.name), i

    def render_mermaid_root(self):
        out = """```mermaid\ngraph TB\n"""
        out += self.render_mermaid(0)[0]
        out += "\n```"
        return out


class ParallelBlock(Block):
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.components = data["components"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.domain = tuple([i for x in self.components for i in x.domain])

        self.codomain = tuple([i for x in self.components for i in x.codomain])
        self.parameters_used = list(
            set([i for x in self.components for i in x.parameters_used])
        )

        self.called_by = []
        self.calls = []

    def render_mermaid(self, i):
        start_i = i
        out = ""

        nodes = []

        # Render components
        for component in self.components:
            component, i = component.render_mermaid(i)
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
