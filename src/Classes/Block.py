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
        self.block_type = "Block"

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
        self.block_type = "Paralell Block"

    def render_mermaid(self, i):
        multi = None
        if type(i) == list:
            multi = i
            i = i[-1]
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


class StackBlock(Block):
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.components = data["components"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self._check_domain_mapping()
        self.domain = self.components[0].domain
        self.codomain = self.components[-1].codomain
        self.parameters_used = list(
            set([i for x in self.components for i in x.parameters_used])
        )

        self.called_by = []
        self.calls = []

        self.block_type = "Stack Block"

    def _check_domain_mapping(self):
        for a, b in zip(self.components[:-1], self.components[1:]):
            assert (
                a.codomain == b.domain
            ), "{} codomain does not match {} domain".format(a.name, b.name)

    def render_mermaid(self, i):
        multi = None
        if type(i) == list:
            multi = i
            i = i[-1]
        start_i = i
        out = ""

        nodes = []

        # Render components
        for component in self.components:
            component, i = component.render_mermaid(i)
            out += component
            out += "\n"
            nodes.append(i)
            if type(i) == list:
                i = i[-1]
        end_i = i

        # Render connections
        for ix1, ix2 in zip(nodes[:-1], nodes[1:]):
            if type(ix1) != list:
                ix1 = [ix1]
            if type(ix2) != list:
                ix2 = [ix2]
            for ix3 in ix1:
                for ix4 in ix2:
                    out += "X{}-->X{}".format(ix3, ix4)
                    out += "\n"

        # Subgraph it
        i += 1
        out = "subgraph X{}[{}]\ndirection TB\n".format(i, self.name) + out
        out += "end"

        return out, i


class SplitBlock(Block):
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

        self.block_type = "Split Block"

    def render_mermaid(self, i):
        multi = None
        if type(i) == list:
            multi = i
            i = i[-1]
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
        out = out[:-1]

        return out, nodes
