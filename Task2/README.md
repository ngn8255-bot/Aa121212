1. Project Introduction This project implements an undirected graph using an adjacency list and solves the single-source shortest path problem with the Dijkstra's algorithm in Python. The code is concise and clear, suitable for graph theory learning, course assignments, or practical applications in projects. 2. Core Features • Graph Construction: Supports adding vertices and undirected edges (with weights). • Shortest Path Calculation: Computes the shortest path from a specified starting vertex to all other vertices (applicable for non-negative weights).Class/Method Description  Graph() Initializes the graph, using an adjacency list adj_list to store vertices and edges.  add_vertex(v) Adds vertex v to the graph (if it does not exist).  add_edge(v1, v2, weight) Adds an undirected edge v1-v2 with weight weight (stored bidirectionally).  dijkstra(start) Calculates the shortest path from start to all vertices, returns a distance dictionary (format: {vertex: shortest_distance}).








