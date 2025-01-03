from typing import Dict
from .Space import TerminatingSpace, EmptySpace


class Block:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.domain = data["domain"]
        self.codomain = data["codomain"]
        self.parameters_used = data["parameters_used"]
        self.metadata = data["metadata"]
        if "metrics_used" in data:
            self.metrics_used = data["metrics_used"]
        else:
            self.metrics_used = []
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        if "called_by" in data:
            self.called_by = data["called_by"]
        else:
            self.called_by = []
        self.calls = []
        self.block_type = "Block"
        self.all_updates = []
        # Will be overwritten in composite blocks to represent individual components
        self.domain_blocks = tuple(
            [
                self
                for _ in range(
                    len(
                        [
                            x
                            for x in self.domain
                            if x not in [TerminatingSpace, EmptySpace]
                        ]
                    )
                )
            ]
        )
        self.domain_blocks2 = self.domain_blocks[:]
        self.codomain_blocks = tuple(
            [
                self
                for _ in range(
                    len(
                        [
                            x
                            for x in self.codomain
                            if x not in [TerminatingSpace, EmptySpace]
                        ]
                    )
                )
            ]
        )
        self.domain_blocks_empty = tuple(
            self for _ in range(len([x for x in self.domain if x == EmptySpace]))
        )
        self.codomain_blocks_empty = tuple(
            self for _ in range(len([x for x in self.codomain if x == EmptySpace]))
        )
        self.codomain_blocks_terminating = tuple(
            self
            for _ in range(len([x for x in self.codomain if x == TerminatingSpace]))
        )

        self.find_all_spaces_used(data)

    def render_mermaid(self, i, go_deep=True):
        i += 1
        out = 'X{}["{}"]'.format(i, self.name)
        if self.block_type == "Mechanism":
            for u in sorted(self.updates, key=lambda x: x[0].name + "-" + x[1].name):
                out += "\n"
                out += 'X{} --"State Update"--> {}'.format(
                    i,
                    (u[0].name + "-" + u[1].name).replace(" ", "-"),
                )
        return out, i

    def render_ending_entities(self):
        if self.block_type == "Mechanism":
            updates = self.updates
        elif self.block_type in ["Parallel Block", "Stack Block", "Split Block"]:
            updates = self.all_updates
        else:
            return "\n", {}, 0
        updates = sorted(updates, key=lambda x: x[0].name + "-" + x[1].name)

        out = "\n"
        out += 'subgraph SVS["State Variables"]\n'

        # Render the entities
        entity_mapping = {}
        entities = set([x[0] for x in updates])
        entities = sorted(entities, key=lambda x: x.name)
        for i, x in enumerate(entities):
            entity_mapping[x.name] = "EE{}".format(i)
            out += '{}[("{}")]'.format(entity_mapping[x.name], x.name)
            out += "\n"

        entity_variable_mapping = {}
        # Render the state variables
        for i, x in enumerate(updates):
            entity_variable_mapping[(x[0].name + "-" + x[1].name).replace(" ", "-")] = (
                "EES{}".format(i)
            )
            out += '{}(["{}"])'.format("EES{}".format(i), x[1].name)
            out += "\n"

            out += "{} --- {}".format("EES{}".format(i), entity_mapping[x[0].name])
            out += "\n"
        out += "end\n"
        out += "\n"
        return out, entity_variable_mapping, len(entities)

    def render_mermaid_root(self, go_deep=True):
        out = """```mermaid\ngraph TB\n"""
        add, entity_variable_mapping, n_entities = self.render_ending_entities()
        out += add
        new, i = self.render_mermaid(0, go_deep=go_deep)
        out += new

        for key in entity_variable_mapping:
            out = out.replace(key, entity_variable_mapping[key])
        out += "\n"
        for x in range(1, i):
            if (
                "X{}[Domain]".format(x) not in out
                and "X{}[Codomain]".format(x) not in out
                and "subgraph X{}".format(x) not in out
            ):
                out += "class X{} internal-link;\n".format(x)

        for x in range(n_entities):
            out += "class EE{} internal-link;\n".format(x)

        out += "\n```"
        return out

    def find_all_spaces_used(self, data):
        self.all_spaces_used = []
        self.all_spaces_used.extend(self.domain)
        self.all_spaces_used.extend(self.codomain)
        if "components" in data:
            for x in data["components"]:
                self.all_spaces_used.extend(x.all_spaces_used)
        self.all_spaces_used = list(set(self.all_spaces_used))

    def find_all_updates(self, data):
        self.all_updates = []
        if "components" in data:
            for x in data["components"]:
                if x.block_type == "Mechanism":
                    self.all_updates.extend(x.updates)
                else:
                    self.all_updates.extend(x.all_updates)
        self.all_updates = list(set(self.all_updates))

    def components_full(self):
        q = [self]
        out = []
        while len(q) > 0:
            cur = q.pop()
            if hasattr(cur, "components"):
                q.extend(cur.components)
            else:
                out.append(cur)
        out = list(set(out))
        return out

    def __repr__(self):
        return "<{}>".format(self.name)


class ParallelBlock(Block):
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.components = data["components"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        if "metrics_used" in data:
            self.metrics_used = data["metrics_used"]
        else:
            self.metrics_used = []
        self.mermaid_show_name = data["mermaid_show_name"]
        self.domain = tuple(
            [
                i
                for x in self.components
                for i in x.domain
                if i not in [TerminatingSpace, EmptySpace]
            ]
        )
        if len(self.domain) == 0:
            self.domain = (EmptySpace,)

        self.codomain = tuple(
            [
                i
                for x in self.components
                for i in x.codomain
                if i not in [TerminatingSpace, EmptySpace]
            ]
        )
        if len(self.codomain) == 0:
            self.codomain = (EmptySpace,)
        self.parameters_used = list(
            set([i for x in self.components for i in x.parameters_used])
        )

        self.domain_blocks = tuple(
            [i for x in self.components for i in x.domain_blocks]
        )
        self.domain_blocks2 = tuple(
            [x for x in self.components for i in x.domain_blocks2]
        )
        self.codomain_blocks = tuple(
            [i for x in self.components for i in x.codomain_blocks]
        )

        self.domain_blocks_empty = tuple(
            [i for x in self.components for i in x.domain_blocks_empty]
        )
        self.codomain_blocks_empty = tuple(
            [i for x in self.components for i in x.codomain_blocks_empty]
        )
        self.codomain_blocks_terminating = tuple(
            [i for x in self.components for i in x.codomain_blocks_terminating]
        )

        self.called_by = []
        self.calls = []
        self.block_type = "Parallel Block"
        self.metadata = data["metadata"]
        self.find_all_spaces_used(data)

    def render_mermaid(self, i, go_deep=True):
        if go_deep == "First":
            go_deep = False
        elif go_deep == False:
            i += 1
            out = 'X{}["{}"]'.format(i, self.name)
            for u in sorted(
                self.all_updates, key=lambda x: x[0].name + "-" + x[1].name
            ):
                out += "\n"
                out += 'X{} --"State Update"--> {}'.format(
                    i,
                    (u[0].name + "-" + u[1].name).replace(" ", "-"),
                )
            return out, i
        multi = None
        if type(i) == list:
            multi = i
            i = i[-1]
        start_i = i
        out = ""

        nodes = []

        # Render components
        domain_map = {}
        codomain_map = {}

        for component in self.components:
            domain = component.domain
            codomain = component.codomain
            domain = [
                x.name
                for x in domain
                if x.name not in ["Empty Space", "Terminating Space"]
            ]
            codomain = [
                x.name
                for x in codomain
                if x.name not in ["Empty Space", "Terminating Space"]
            ]

            component, i = component.render_mermaid(i, go_deep=go_deep)
            out += component
            out += "\n"
            domain_map[i] = domain
            codomain_map[i] = codomain
            nodes.append(i)

        # Add domain and codomain
        i += 1
        out += "X{}[Domain]".format(i)
        out += "\n"
        domain_i = i
        i += 1
        out += "X{}[Codomain]".format(i)
        out += "\n"
        codomain_i = i

        out += "direction LR\n"

        # Render invisible connections
        # for ix1, ix2 in zip(nodes[:-1], nodes[1:]):
        #    out += "X{} ~~~~ X{}".format(ix1, ix2)
        #    out += "\n"

        out += "direction TB\n"

        for ix1 in nodes:
            d = domain_map[ix1]
            if len(d) > 0:
                d_length = len(d)
                d = ["<a href='{}' class=internal-link>{}</a>".format(x, x) for x in d]
                d = "\n".join(d)
                d = '"{}"'.format(d)
                out += "X{} --{}{}-> X{}".format(domain_i, d, "-" * d_length, ix1)
            else:
                out += "X{} --> X{}".format(domain_i, ix1)
            out += "\n"

        codomain_connections = 0
        for ix1 in nodes:
            d = codomain_map[ix1]
            if len(d) > 0:
                d = "\n".join(d)
                d = '"{}"'.format(d)
                out += "X{} --{}--> X{}".format(ix1, d, codomain_i)
                codomain_connections += 1
                out += "\n"
            # else:
            #    out += "X{} --> X{}".format(ix1, codomain_i)
        if codomain_connections == 0:
            out = out.replace("X{}[Codomain]".format(codomain_i), "")

        # Subgraph it
        if self.mermaid_show_name:
            name = self.name
        else:
            name = " "
        i += 1
        out = 'subgraph X{}["{}"]\ndirection TB\n'.format(i, name) + out

        out += "end"

        return out, i


class StackBlock(Block):
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.components = data["components"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.mermaid_show_name = data["mermaid_show_name"]
        self.optional_indices = data["optional_indices"]
        self.loop = data["loop"]
        if "metrics_used" in data:
            self.metrics_used = data["metrics_used"]
        else:
            self.metrics_used = []
        self._check_domain_mapping()
        self.domain = self.components[0].domain
        self.codomain = self.components[-1].codomain
        self.parameters_used = list(
            set([i for x in self.components for i in x.parameters_used])
        )

        self.domain_blocks = self.components[0].domain_blocks
        self.domain_blocks2 = self.components[0].domain_blocks2
        self.codomain_blocks = self.components[-1].codomain_blocks
        self.domain_blocks_empty = self.components[0].domain_blocks_empty
        self.codomain_blocks_empty = self.components[-1].codomain_blocks_empty
        self.codomain_blocks_terminating = self.components[
            -1
        ].codomain_blocks_terminating

        self.called_by = []
        self.calls = []

        self.block_type = "Stack Block"
        self.metadata = data["metadata"]
        self.find_all_spaces_used(data)

    def _check_domain_mapping(self):
        x = self.components[:-1]
        y = self.components[1:]
        if self.loop:
            x.append(self.components[-1])
            y.append(self.components[0])
        for a, b in zip(x, y):
            assert [
                x for x in a.codomain if x not in [EmptySpace, TerminatingSpace]
            ] == [
                x for x in b.domain if x not in [EmptySpace, TerminatingSpace]
            ], "{} codomain does not match {} domain, {} != {}".format(
                a.name, b.name, a.codomain, b.domain
            )

    def build_action_transmission_channels(self):
        channels = []
        x = self.components[:-1]
        y = self.components[1:]
        if self.loop:
            x.append(self.components[-1])
            y.append(self.components[0])
        for a, b, c in zip(x, y, range(len(x))):
            assert len(a.codomain_blocks) == len(b.domain_blocks) and len(
                b.domain_blocks
            ) == len([x for x in b.domain if x not in [EmptySpace, TerminatingSpace]])
            global_optional = c in self.optional_indices

            for x, y, z in zip(
                a.codomain_blocks,
                b.domain_blocks,
                [x for x in b.domain if x not in [EmptySpace, TerminatingSpace]],
            ):
                channels.append(
                    {
                        "origin": x.name,
                        "target": y.name,
                        "space": z.name,
                        "optional": global_optional,
                    }
                )
            for x in a.codomain_blocks_empty:
                for y in b.domain_blocks_empty:
                    channels.append(
                        {
                            "origin": x.name,
                            "target": y.name,
                            "space": "Empty Space",
                            "optional": global_optional,
                        }
                    )
        return channels

    def render_mermaid(self, i, go_deep=True):
        if go_deep == "First":
            go_deep = False
        elif go_deep == False:
            i += 1
            out = 'X{}["{}"]'.format(i, self.name)

            for u in sorted(
                self.all_updates, key=lambda x: x[0].name + "-" + x[1].name
            ):
                out += "\n"
                out += 'X{} --"State Update"--> {}'.format(
                    i,
                    (u[0].name + "-" + u[1].name).replace(" ", "-"),
                )
            return out, i
        multi = None
        if type(i) == list:
            multi = i
            i = i[-1]
        start_i = i
        out = ""

        nodes = []

        domain_map = {}
        # Render components
        for component in self.components:
            domain = component.domain
            domain = [
                x.name
                for x in domain
                if x.name not in ["Empty Space", "Terminating Space"]
            ]
            component, i = component.render_mermaid(i, go_deep=go_deep)
            domain_map[i] = domain
            out += component
            out += "\n"
            nodes.append(i)
            if type(i) == list:
                i = i[-1]
        end_i = i

        # Render connections
        x = nodes[:-1]
        y = nodes[1:]
        if self.loop:
            x.append(nodes[-1])
            y.append(nodes[0])
        for ix1, ix2, c in zip(x, y, range(len(x))):
            global_optional = c in self.optional_indices
            if type(ix1) != list:
                ix1 = [ix1]
            if type(ix2) != list:
                ix2 = [ix2]
            for ix3 in ix1:
                for ix4 in ix2:
                    d = domain_map[ix4]
                    optional = global_optional
                    if len(d) > 0:
                        d_length = len(d)
                        d = [
                            "<a href='{}' class=internal-link>{}</a>".format(x, x)
                            for x in d
                        ]
                        d = "\n".join(d)
                        d = '"{}"'.format(d)
                        if optional:
                            out += "X{}-.{}.{}->X{}".format(ix3, d, "." * d_length, ix4)
                        else:
                            out += "X{}--{}-{}->X{}".format(ix3, d, "-" * d_length, ix4)
                    else:
                        if optional:
                            out += "X{}-.->X{}".format(ix3, ix4)
                        else:
                            out += "X{}--->X{}".format(ix3, ix4)
                    out += "\n"

        # Subgraph it
        if self.mermaid_show_name:
            name = self.name
        else:
            name = " "
        i += 1
        out = 'subgraph X{}["{}"]\ndirection TB\n'.format(i, name) + out
        out += "end"

        return out, i


class SplitBlock(Block):
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.components = data["components"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.mermaid_show_name = data["mermaid_show_name"]
        if "metrics_used" in data:
            self.metrics_used = data["metrics_used"]
        else:
            self.metrics_used = []
        self.domain = tuple(
            [
                i
                for x in self.components
                for i in x.domain
                if i not in [TerminatingSpace, EmptySpace]
            ]
        )
        if len(self.domain) == 0:
            self.domain = (EmptySpace,)

        self.codomain = tuple(
            [
                i
                for x in self.components
                for i in x.codomain
                if i not in [TerminatingSpace, EmptySpace]
            ]
        )
        if len(self.codomain) == 0:
            self.codomain = (EmptySpace,)
        self.parameters_used = list(
            set([i for x in self.components for i in x.parameters_used])
        )

        self.domain_blocks = tuple(
            [i for x in self.components for i in x.domain_blocks]
        )
        self.codomain_blocks = tuple(
            [i for x in self.components for i in x.codomain_blocks]
        )

        self.domain_blocks_empty = tuple(
            [i for x in self.components for i in x.domain_blocks_empty]
        )
        self.codomain_blocks_empty = tuple(
            [i for x in self.components for i in x.codomain_blocks_empty]
        )
        self.codomain_blocks_terminating = tuple(
            [i for x in self.components for i in x.codomain_blocks_terminating]
        )

        self.called_by = []
        self.calls = []

        self.block_type = "Split Block"
        self.metadata = data["metadata"]
        self.find_all_spaces_used(data)

    def render_mermaid(self, i, go_deep=True):
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
        # for ix1, ix2 in zip(nodes[:-1], nodes[1:]):
        #    out += "X{} ~~~ X{}".format(ix1, ix2)
        #    out += "\n"
        out = out[:-1]

        return out, nodes
