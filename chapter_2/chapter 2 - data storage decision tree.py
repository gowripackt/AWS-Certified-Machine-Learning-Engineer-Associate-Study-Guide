import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for the decision tree
G = nx.DiGraph()

# Add nodes and edges for the decision tree
G.add_edges_from([
    ("Start", "Is data size small (<100 GB)?"),
    ("Is data size small (<100 GB)?", "Amazon EBS (Small Datasets)"),
    ("Is data size small (<100 GB)?", "Is data used for real-time processing?"),

    ("Is data used for real-time processing?", "Amazon EFS (Real-Time Access)"),
    ("Is data used for real-time processing?", "Centralized data lake for analytics?"),

    ("Centralized data lake for analytics?", "Amazon S3 (Data Lake)"),
    ("Centralized data lake for analytics?", "Highly scalable HPC storage?"),

    ("Highly scalable HPC storage?", "Amazon FSx (High-Performance)"),
    ("Highly scalable HPC storage?", "Evaluate other solutions")
])

# Define positions for nodes
pos = nx.spring_layout(G, seed=42)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color='black')
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', node_shape="o")
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

# Title and display
plt.title("Decision Tree for Selecting AWS Storage Solutions", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()