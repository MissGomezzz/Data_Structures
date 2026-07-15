# This is an implementation an undirected graph data structure, which uses adjacency lists to store and relate data.

class Graph:
    def __init__(self):
        # Each key will be a vertex, each value will be a list of neighbors
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self,vertex1,vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self,vertex1,vertex2):
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self,vertex):
        for element in self.adjacency_list:
            if vertex in self.adjacency_list[element]:
                self.adjacency_list[element].remove(vertex)
        del self.adjacency_list[vertex]

    def print_graph(self):
        if self.adjacency_list == {}:
            print ("Nothing to print here: the graph is empty. ")
        for vertex in self.adjacency_list:
                print (f"Vertex: {vertex}, edges: {self.adjacency_list[vertex]}")

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.print_graph()
graph.remove_vertex("A")
graph.remove_vertex("B")
graph.remove_vertex("C")
graph.print_graph()