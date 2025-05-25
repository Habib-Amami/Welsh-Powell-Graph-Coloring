# Welsh-Powell Graph Coloring

This project implements the **Welsh-Powell graph coloring algorithm** to assign colors to vertices of a graph such that no adjacent vertices share the same color. The implementation uses Python with the `networkx` and `matplotlib` libraries for graph creation, coloring, and visualization. The script includes a verification function to ensure the coloring is valid and demonstrates the algorithm on five different graphs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Graph Examples](#graph-examples)
- [Dependencies](#dependencies)

## Overview

The Welsh-Powell algorithm is a greedy approach to graph vertex coloring. It sorts vertices by their degree in descending order and assigns the smallest possible color to each vertex that does not conflict with its neighbors. This project applies the algorithm to various graph structures, visualizes the results, and verifies the correctness of the coloring.

## Features

- **Welsh-Powell Algorithm**: Colors graph vertices efficiently using a greedy strategy.
- **Graph Visualization**: Displays colored graphs using Matplotlib with distinct colors for each vertex.
- **Coloring Verification**: Checks if the coloring is valid (no adjacent vertices share the same color).
- **Multiple Graph Examples**: Demonstrates the algorithm on five different graphs:
  - Small manual graph (6 vertices).
  - Cycle graph with chords (10 vertices).
  - Star graph with a small cycle (10 vertices).
  - Graph with varied degrees (8 vertices).
  - Random Erdos-Renyi graph (12 vertices).

## Installation

To run the script, you need Python 3.x and the required libraries. Follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Habib-Amami/Welsh-Powell-Graph-Coloring.git
   cd Welsh-Powell-Graph-Coloring
   ```

2. **Install Dependencies**: Install the required Python libraries using pip:

   ```bash
   pip install networkx matplotlib
   ```

3. **Run the Script**: Execute the script using Python:

   ```bash
   python graph_coloring.py
   ```

## Usage

The script `graph_coloring.py` defines the Welsh-Powell algorithm, a visualization function, and a verification function. It creates and processes five different graphs, applying the coloring algorithm, visualizing each graph, and verifying the results.

To run the script:

1. Ensure the dependencies are installed.
2. Run the script:

    ```bash
   python graph_coloring.py
   ```

The script will:
    - Generate and color five different graphs.
    - Display each graph with colored vertices using Matplotlib.
    - Print verification messages indicating whether the coloring is valid and the number of colors used.

## Graph Examples

The script includes five graphs to demonstrate the algorithm:

- **Small Manual Graph**: A 6-vertex graph with a simple structure.
- **Cycle Graph with Chords**: A 10-vertex cycle graph with additional edges.
- **Star Graph with Cycle**: A star graph with 9 leaves and a small cycle among leaves.
- **Mixed Degree Graph**: An 8-vertex graph with varied vertex degrees.
- **Random Graph**: A 12-vertex Erdos-Renyi random graph with edge probability 0.3.

Each graph is visualized with colored vertices, and the coloring is verified to ensure no adjacent vertices share the same color.

## Dependencies

- **Python 3.x**: Required to run the script.
- **NetworkX**: For graph creation and manipulation.
  - Install: `pip install networkx`
- **Matplotlib**: For graph visualization.
  - Install: `pip install matplotlib`
