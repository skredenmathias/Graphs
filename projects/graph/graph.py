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
        self.vertices[vertex_id] = set() # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex_id)

        # make a set to track if we've been here before
        visited = set()

        # while our queue isn't empty
        while q.size() > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            v = q.dequeue()
        ## if we haven't visited this node yet,
            if v not in visited:
                print(v)
        ### mark as visited
                visited.add(v)
        ### get its neighbors
        ### for each of the neighbors,
                for neighbor in self.get_neighbors(v):
        #### add to queue
                    q.enqueue(neighbor)


    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        # add our starting node to stack
        s.push(starting_vertex_id)

        # make a set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while s.size() > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            v = s.pop()
            
        ## if we haven't visited this node yet,
            if v not in visited:
                print(v)
        ### mark as visited
                visited.add(v)
        ### get its neighbors
        ### for each of the neighbors,
                for neighbor in self.get_neighbors(v):
        #### add to queue
                    s.push(neighbor)
        
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited:
            visited(starting_vertex)
        else:
            visited = set()

        v = starting_vertex

        if v in visited:
            return
        
        print(v)
        visited.add(v)

        for neighbor in self.get_neighbors(v):
            self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # difference in what you store in Q / S

        # store the entire path instead of current node
            # path = [nodes]
        # when we deque the current node is "path at -1" # last index inside the path
        # once we find vertex, return the path

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            print(q.queue)
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                else:
                    visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # _COPY_ THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                else:
                    visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # _COPY_ THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited:
            visited.add(starting_vertex)
        else:
            visited = set()
            path = []
        path.append(starting_vertex)
        last_vertex = path[-1]

        if starting_vertex in visited:
            return
        
        
        # visited.add(starting_vertex)
        path.append(starting_vertex)

        if last_vertex not in visited:
            if last_vertex == destination_vertex:
                return path
            else:
                visited.add(last_vertex)

        for neighbor in self.get_neighbors(last_vertex):
            # if neighbor in neighbors
            result = self.dft_recursive(neighbor, destination_vertex, visited, path)
            if result is not None:
                return result





        if visited:
            visited(starting_vertex)
        else:
            visited = set()

        v = starting_vertex

        if v in visited:
            return
        
        print(v)
        visited.add(v)

        for neighbor in self.get_neighbors(v):
            self.dft_recursive(neighbor, visited)



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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 7))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))