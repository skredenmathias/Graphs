class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''


def earliest_ancestor(ancestors, starting_node):
    # say we're looking for ancestor of 6.
    # we want to append each path
        # for tuple in ancestors:
            # if tuple[1] == path[-1]:
                # append tuple[0] to path
        # repeat
    # return the longest path
    longest_path_arr = []
    all_paths_arr = []
    visited = set()
    q = Queue()
    q.enqueue([starting_node])

    while q.size() > 0:
        path = q.dequeue() # [6, 3]

        cur_ancestor = path[-1] # 3

        if cur_ancestor not in visited:
            visited.add(cur_ancestor)

            # base case here
            found_ancestor = False

            for tupl in ancestors:
                if tupl[1] == cur_ancestor:
                    found_ancestor = True
                    # create list of tuple to get longest list
                    path_copy = list(path)
                    path_copy.append(tupl[0]) 
                    q.enqueue(path_copy) # [6, 3, 1, 10], [6, 5, 4]
            if not found_ancestor:
                all_paths_arr.append(path)
                # print(all_paths_arr)

            # longest_path = max(Queue.queue, key=len)

# "return" the longest path
    all_paths_arr.sort(key=len) # loop through to find longest, equal, lowest value, instead of sorting. To avoid excess loops.
    longest_path = all_paths_arr[-1] # or [-1] #?
    # if more than one earliest ancestor
        # return the lowest numeric ID

    # index into the last element
    final_ancestor = longest_path[-1]
        # return it
    return final_ancestor
    # if more than one earliest ancestor
        # return the lowest numeric ID
# if tupl[1] != cur_ancestor
    # return -1

test_ancestors = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), 
    (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 9))