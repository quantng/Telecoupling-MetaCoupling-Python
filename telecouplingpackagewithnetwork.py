import statsmodels.api as sm
import networkx as nx
import matplotlib.pyplot as plt

class TelecouplingComponent:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


class TelecouplingHypothesis:
    def __init__(self, description, systems, flows, agents, causes, effects):
        self.description = description
        self.systems = systems
        self.flows = flows
        self.agents = agents
        self.causes = causes
        self.effects = effects

    def test_hypothesis(self, data):
        X = data[['post_disaster', 'oilprice']]
        X = sm.add_constant(X)
        y = data['Last Price']
        model = sm.OLS(y, X).fit()
        return model.summary()

    def __str__(self):
        output = f"Hypothesis: {self.description}\n"
        output += f"Systems: {', '.join(str(system) for system in self.systems)}\n"
        output += f"Flows: {', '.join(str(flow) for flow in self.flows)}\n"
        output += f"Agents: {', '.join(str(agent) for agent in self.agents)}\n"
        output += f"Causes: {', '.join(str(cause) for cause in self.causes)}\n"
        output += f"Effects: {', '.join(str(effect) for effect in self.effects)}\n"
        return output


class TelecouplingFramework:
    def __init__(self):
        self.hypotheses = []

    def add_hypothesis(self, hypothesis):
        self.hypotheses.append(hypothesis)

    def remove_hypothesis(self, index):
        if 0 <= index < len(self.hypotheses):
            del self.hypotheses[index]
        else:
            print("Invalid hypothesis index.")

    def test_hypotheses(self, data):
        for hypothesis in self.hypotheses:
            print(f"Testing hypothesis: {hypothesis.description}")
            print(hypothesis.test_hypothesis(data))

    def display_hypotheses(self):
        for i, hypothesis in enumerate(self.hypotheses, start=1):
            print(f"Hypothesis {i}:")
            print(hypothesis)

    def visualize_network(self, hypothesis):
        G = nx.DiGraph()

        # Add systems as nodes
        for i, system in enumerate(hypothesis.systems, start=1):
            G.add_node(f"System {i}", description=system.description, type='system')

        # Add agents as nodes
        for i, agent in enumerate(hypothesis.agents, start=1):
            G.add_node(f"Agent {i}", description=agent.description, type='agent')

        # Add flows as edges with arrows
        for flow in hypothesis.flows:
            for i, agent in enumerate(hypothesis.agents, start=1):
                for j, system in enumerate(hypothesis.systems, start=1):
                    G.add_edge(f"Agent {i}", f"System {j}", label=flow.description)

        # Set node positions
        pos = nx.spring_layout(G)

        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))

        # Draw systems
        systems = [node for node in G.nodes if G.nodes[node]['type'] == 'system']
        nx.draw_networkx_nodes(G, pos, nodelist=systems, node_size=1000, node_color='lightblue', node_shape='s', ax=ax)

        # Draw agents
        agents = [node for node in G.nodes if G.nodes[node]['type'] == 'agent']
        nx.draw_networkx_nodes(G, pos, nodelist=agents, node_size=800, node_color='lightgreen', node_shape='o', ax=ax)

        # Draw edges with arrows
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowstyle='->', arrowsize=20, ax=ax)

        # Draw node labels
        node_labels = {node: G.nodes[node]['description'] for node in G.nodes}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, ax=ax)

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

        ax.axis('off')
        plt.tight_layout()
        plt.show()