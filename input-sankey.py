import plotly.graph_objects as go

# Get number of nodes
num_nodes = int(input("How many nodes? "))

# Get node labels
nodes = []
for i in range(num_nodes):
    label = input(f"Enter label for node {i}: ")
    nodes.append(label)

# Get number of links
num_links = int(input("How many links? "))

sources = []
targets = []
values = []

for i in range(num_links):
    print(f"\nLink {i+1}")
    s = int(input("  Enter source index: "))
    t = int(input("  Enter target index: "))
    v = float(input("  Enter value: "))

    sources.append(s)
    targets.append(t)
    values.append(v)

print("\nNodes:", nodes)
print("Sources:", sources)
print("Targets:", targets)
print("Values:", values)

# Compute outgoing total for each node
node_totals = [0] * num_nodes
for s, v in zip(sources, values):
    node_totals[s] += v

# Add totals to labels
nodes_with_values = [
    f"{label} ({node_totals[i]})" for i, label in enumerate(nodes)
]

fig = go.Figure(data=[go.Sankey(
    node=dict(label=nodes_with_values),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

fig.update_layout(title_text="Test Sankey")
fig.show()

