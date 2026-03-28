class Graph:
    # Initialize empty graph
    def __init__(self):
        self.adjacency_list = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    # Add a directed edge with weight
    def add_edge(self, from_v, to_v, weight):
        # Make sure both vertices exist
        if from_v not in self.adjacency_list:
            self.add_vertex(from_v)
        if to_v not in self.adjacency_list:
            self.add_vertex(to_v)

        # Add the directed edge
        self.adjacency_list[from_v][to_v] = weight

    # Get all vertices
    def get_vertices(self):
        return list(self.adjacency_list.keys())

    # Get neighbors of a vertex
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, {})


def dijkstra(graph, start):
    inf = float('inf')
    vertices = graph.get_vertices()

    dist = {v: inf for v in vertices}
    dist[start] = 0
    visited = set()

    # until all point can be reached
    while len(visited) < len(vertices):
        min_dist = inf
        now = None

        # find min distance point
        for v in vertices:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                now = v

        # we do not find point
        if now is None:
            break

        visited.add(now)
        neighbors = graph.get_neighbors(now)

        
        for neighbor, weight in neighbors.items():
            if neighbor not in visited:
                new_dist = dist[now] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
    return dist



if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "D", 3)
    g.add_edge("D", "E", 1)

    # calculate min distance
    result = dijkstra(g, "A")
    print("find min distance")
    for vertex, distance in result.items():
        print(f"{vertex}: {distance}")




