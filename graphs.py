from collections import defaultdict

class Graph():
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(set)

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.vertices.add(vertex)

    def add_edges(self, edges):
        for v1, v2 in edges:
            self.edges[v1].add(v2)

    def transitive_closure(self):
        for vertex in self.vertices:
            vertex_reach = self.reach(vertex)
            new_edges = list(zip([vertex] * len(vertex_reach), vertex_reach))
            self.add_edges(new_edges)

    def reach(self, vertex):
        # TODO fix me
        def dfs(self, vertex, past_vertices):
            if vertex in past_vertices:
                return past_vertices
            else:
                past_vertices.add(vertex)
                if len(self.edges[vertex]) > 0:
                    for next_vertex in self.edges[vertex]:
                        if next_vertex == vertex: continue
                        return past_vertices.union(dfs(self, next_vertex, past_vertices))
                else:
                    return past_vertices

        if len(self.vertices) > 0:
            return dfs(self, vertex, set())

    def is_acyclic(self):
        def dfs(self, vertex, past_vertices):
            if vertex in past_vertices:
                return False
            else:
                past_vertices.append(vertex)
                if len(self.edges[vertex]) > 0:
                    for next_vertex in self.edges[vertex]:
                        return True and dfs(self, next_vertex, past_vertices)
                else:
                    return True


        if len(self.vertices) > 0:
            start = next(iter(self.vertices))
            return dfs(self, start, [])
        else:
            return True


class Poset(Graph):
    def add_edges(self, edges):
        Graph.add_edges(self, edges)
        Graph.transitive_closure(self)


if __name__ == "__main__":
    g = Graph()
    g.add_vertices(list(range(5)))
    g.add_edges([(i, i+1) for i in range(4)])
    g.transitive_closure()
    print(g.vertices)
    print(g.edges)
    print(g.is_acyclic())
    print(g.reach(2))

