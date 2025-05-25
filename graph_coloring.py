import networkx as nx
import matplotlib.pyplot as plt

def welsh_powell_coloring(G):
    # Sort vertices by degree in descending order
    nodes = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    color_map = {}  # Vertex -> color
    color = 0  # Start with color 0

    for node in nodes:
        # Get colors of adjacent nodes
        used_colors = {color_map.get(neighbor) for neighbor in G.neighbors(node)}
        # Find the first available color
        while color in used_colors:
            color += 1
        color_map[node] = color
        color = 0  # Reset color for next node

    return color_map

# Visualization function
def plot_graph(G, color_map, title="Graph with Vertex Coloring"):
    pos = nx.spring_layout(G)
    # Convert color numbers to colors for visualization
    colors = [color_map[node] for node in G.nodes()]
    cmap = plt.colormaps.get_cmap('tab20')  # Use a colormap with distinct colors
    nx.draw(G, pos, with_labels=True, node_color=colors, cmap=cmap, node_size=500, font_color='white')
    plt.title(title)
    plt.show()

# Verification function
def verify_vertex_coloring(G, color_map):
    for u, v in G.edges():
        if color_map[u] == color_map[v]:
            return False, f"Adjacent vertices {u} and {v} have the same color {color_map[u]}"
    return True, f"Vertex coloring is valid. Used {len(set(color_map.values()))} colors."

# Graph 1: Small Manual Graph (6 vertices)
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6)])

color_map1 = welsh_powell_coloring(G1)
plot_graph(G1, color_map1, "Small Graph - Vertex Coloring")
valid, msg = verify_vertex_coloring(G1, color_map1)
print(f"Graph 1 Vertex Coloring: {msg}")

# Graph 2: Larger Graph with Cycle
G2 = nx.cycle_graph(10)  # 10 vertices in a cycle
G2.add_edges_from([(0, 5), (2, 7)])  # Add some chords

color_map2 = welsh_powell_coloring(G2)
plot_graph(G2, color_map2, "Cycle Graph - Vertex Coloring")
valid, msg = verify_vertex_coloring(G2, color_map2)
print(f"Graph 2 Vertex Coloring: {msg}")

# Graph 3: Graph with High-Degree Vertices
G3 = nx.star_graph(9)  # Star graph: 1 central vertex, 9 leaves
G3.add_edges_from([(1, 2), (2, 3), (3, 4)])  # Add a small cycle among leaves

color_map3 = welsh_powell_coloring(G3)
plot_graph(G3, color_map3, "Star Graph - Vertex Coloring")
valid, msg = verify_vertex_coloring(G3, color_map3)
print(f"Graph 3 Vertex Coloring: {msg}")

# Graph 4: Graph with Varied Degrees
G4 = nx.Graph()
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 6), (4, 7), (5, 8), (6, 8), (7, 8)]
G4.add_edges_from(edges)  # Graph with 8 vertices, mixed degrees

color_map4 = welsh_powell_coloring(G4)
plot_graph(G4, color_map4, "Mixed Degree Graph - Vertex Coloring")
valid, msg = verify_vertex_coloring(G4, color_map4)
print(f"Graph 4 Vertex Coloring: {msg}")

# Graph 5: Random Auto-Generated Graph
G5 = nx.erdos_renyi_graph(12, 0.3, seed=42)  # Random graph with 12 vertices, edge prob 0.3

color_map5 = welsh_powell_coloring(G5)
plot_graph(G5, color_map5, "Random Graph - Vertex Coloring")
valid, msg = verify_vertex_coloring(G5, color_map5)
print(f"Graph 5 Vertex Coloring: {msg}")