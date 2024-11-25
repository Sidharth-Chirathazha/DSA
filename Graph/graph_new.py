class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def show_graph(self):

        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")

    def bfs(self,start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            cur_vertex = queue.pop(0)
            if cur_vertex not in visited:
                print(cur_vertex,end=" ")
                visited.add(cur_vertex)
                for neighbour in self.graph[cur_vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        print()

    def dfs(self,start_vertex):
        visited = set()
        stack = [start_vertex]
        while stack:
            cur_vertex = stack.pop()
            if cur_vertex not in visited:
                print(cur_vertex,end=" ")
                visited.add(cur_vertex)
                for neighbour in reversed(self.graph[cur_vertex]):
                    if neighbour not in visited:
                        stack.append(neighbour)
        print()

    def shortest_path(self,start,end):
        visited = set()
        if start == end:
            return [start]
        
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph.get(node,[])
                for neigh in neighbours:
                    new_path = list(path)
                    new_path.append(neigh)
                    queue.append(new_path)
                    if neigh == end:
                        return new_path
                visited.add(node)
        return None

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(1, 5)
g.add_edge(2, 4)
g.add_edge(2, 6)

g.show_graph()
g.bfs(0)
g.dfs(0)
print(g.shortest_path(0,4))