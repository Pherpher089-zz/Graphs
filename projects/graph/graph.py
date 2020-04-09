"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        v1_edges_set = self.vertices[v1]
        v1_edges_set.add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print("DFS")
        search_queue = Queue()
        visited = set()
        search_queue.enqueue(starting_vertex)
        while search_queue.size() > 0:
            current_node = search_queue.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for n in neighbors:
                    search_queue.enqueue(n)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print("DFT - ITERATIVE")
        search_stack = Stack()
        search_stack.push(starting_vertex)
        visited = set()
        while search_stack.size() > 0:
            current_node = search_stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                print(current_node)
                for n in neighbors:
                    search_stack.push(n)
        return visited

    def dft_helper(self, vertex, visited):
        if vertex in visited:
            return

        neighbors = self.get_neighbors(vertex)
        print(vertex)
        visited.append(vertex)

        if len(neighbors) == 0:
            return
        else:
            for i in neighbors:
                self.dft_helper(i, visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print("DFT - RECURSIVE")
        visited = []
        self.dft_helper(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = []
        paths = {}
        queue.enqueue(starting_vertex)
        paths[starting_vertex] = [starting_vertex]
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            visited.append(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for n in neighbors:
                if n not in visited:
                    new_path = [i for i in paths[current_vertex]]
                    new_path.append(n)
                    paths[n] = new_path
                    if n == destination_vertex:
                        return paths[n]
                    queue.enqueue(n)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = []
        paths = {}
        stack.push(starting_vertex)
        paths[starting_vertex] = [starting_vertex]
        while stack.size() > 0:
            current_vertex = stack.pop()
            visited.append(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for n in neighbors:
                if n not in visited:
                    new_path = [i for i in paths[current_vertex]]
                    new_path.append(n)
                    paths[n] = new_path
                    if n == destination_vertex:
                        return paths[n]
                    stack.push(n)

    def dfs_helper(self, vertex, target, visited, paths):
        if vertex in visited:
            return paths

        neighbors = self.get_neighbors(vertex)
        visited.append(vertex)

        if len(neighbors) == 0:
            return paths
        else:
            for n in neighbors:
                new_path = [i for i in paths[vertex]]
                new_path.append(n)
                paths[n] = new_path
                if n == target:
                    return new_path
                new_paths = self.dfs_helper(n, target, visited, new_path)
                if new_paths != None:
                    return new_paths
                else:
                    return paths

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("DFS - RECURSIVE")
        visited = []
        paths = {}
        paths[starting_vertex] = [starting_vertex]
        print(self.dfs_helper(starting_vertex, destination_vertex, visited, paths))


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
