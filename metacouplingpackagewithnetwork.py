from telecouplingpackagewithnetwork import TelecouplingComponent, TelecouplingHypothesis, TelecouplingFramework
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class MetacouplingFramework(TelecouplingFramework):
    def visualize_metacoupling_network(self, hypothesis):
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
        fig, ax = plt.subplots(figsize=(12, 8))

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

        # Encircle coupled system pairs
        coupled_systems = [
            ("Ecuador's stock market", "Global oil market"),
            ("Rural sales system", "Urban sales system"),
            ("Local markets", "Communities affected by the earthquake"),
            ("Agricultural sector", "Weather system")
        ]

        for system1, system2 in coupled_systems:
            nodes = [node for node in G.nodes if G.nodes[node]['description'] in (system1, system2)]
            if len(nodes) == 2:
                xy = np.array([pos[node] for node in nodes])
                x_center = xy[:, 0].mean()
                y_center = xy[:, 1].mean()
                diameter = np.sqrt(np.sum((xy[0] - xy[1])**2)) * 1.5
                circle = plt.Circle((x_center, y_center), diameter/2, color='red', alpha=0.2)
                ax.add_patch(circle)

        ax.axis('off')
        plt.tight_layout()
        plt.show()


# Create Telecoupling Components
systems = [
    TelecouplingComponent("Ecuador's stock market"),
    TelecouplingComponent("Global oil market"),
    TelecouplingComponent("Rural sales system"),
    TelecouplingComponent("Urban sales system"),
    TelecouplingComponent("Local markets"),
    TelecouplingComponent("Communities affected by the earthquake"),
    TelecouplingComponent("Agricultural sector"),
    TelecouplingComponent("Weather system")
]

flows = [
    TelecouplingComponent("Financial capital"),
    TelecouplingComponent("Financial capital"),
    TelecouplingComponent("Money, goods, and services"),
    TelecouplingComponent("Sales transactions"),
    TelecouplingComponent("Changes in demand for goods and services"),
    TelecouplingComponent("Agricultural products")
]

agents = [
    TelecouplingComponent("Stock market investors"),
    TelecouplingComponent("Oil industry players"),
    TelecouplingComponent("Retailers"),
    TelecouplingComponent("Customers"),
    TelecouplingComponent("Farmers"),
    TelecouplingComponent("Consumers")
]

# Create the Metacoupled System Hypothesis
metacoupled_hypothesis = TelecouplingHypothesis(
    "The metacoupled system of Ecuador's economy exhibits complex interactions and feedbacks between various subsystems, flows, agents, causes, and effects, resulting in dynamic responses to natural disasters and global market forces.",
    systems, flows, agents, [], []
)

# Create Metacoupling Framework and Add Hypothesis
framework = MetacouplingFramework()
framework.add_hypothesis(metacoupled_hypothesis)

# Visualize the Metacoupling Network Diagram
framework.visualize_metacoupling_network(metacoupled_hypothesis)