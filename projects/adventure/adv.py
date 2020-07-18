from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
backtrack_array = []

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def backwards(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'
    if direction == 'e':
        return 'w'


def dft():
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    s = Stack()
    starting_directions = player.current_room.get_exits()
    
    # for direction in starting_directions:
    #     s.push(direction)
    s.push(random.choice(starting_directions))

    visited = {} # This will be traversal_path #?

    visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    forwards = True
    while (len(visited) < len(world.rooms)):
        # Pick a direction
        chosen_direction = s.pop()
        backwards_direction = backwards(chosen_direction)
        room = player.current_room.id

        # Move
        player.travel(chosen_direction)
        # Log
        traversal_path.append(chosen_direction)
        if forwards:
            backtrack_array.append(chosen_direction)
        # Get directions
        available_directions = player.current_room.get_exits()
        if player.current_room.id not in visited:
            visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        # link old room and current room
        visited[room][chosen_direction] = player.current_room.id
        # link current room and old room
        visited[player.current_room.id][backwards_direction] = room
        
        # Loop
        valid_directions = []
        for direction in available_directions:
            if visited[player.current_room.id][direction] == '?':       
                valid_directions.append(direction)
        if len(valid_directions) == 0:
            backtrack_direction = backwards(backtrack_array.pop())
            forwards = False
            s.push(backtrack_direction)
        else:
            forwards = True
            s.push(random.choice(valid_directions))

dft()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
