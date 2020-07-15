import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        # Create friendships
        # but not duplicate combinations
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle them
        random.shuffle(possible_friendships)

        # Choose the first X out of the list. X = (num_users * avg_friendships) // 2
        if i in range(num_users * avg_friendships // 2):
            # Set up those friendships
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # Do BFT
            # return {friend_id: [path]} for each friend
        for key, value in sg.friendships.items():
            if value is not set():
                print(value)
                if key == value:
                    visited[key] = "path"
                if value == key:
                    visited[value] = "path"
            # Notes:
            # path is the shortest path
            # to get path, we might have to consider the island traversal.
        return visited

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)

        # visited = set() # change

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited: # change?
                print(v)
                visited.add(v) # change # visited[]

                for neighbor in self.get_neighbors(v): # add get_neighbors / create it
                    q.enqueue(neighbor)



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
            # print(q.queue)
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
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
