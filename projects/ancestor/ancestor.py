

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


def populate_graph(ancestors):
    # Convert data into an adjencency list
    # for easy lookup of neighbors

    graph = {}
    # scan thru ancestors and create all the vertices
    for parent_child_pair in ancestors:
        parent = parent_child_pair[0]
        child = parent_child_pair[1]
        graph[parent] = set()
        graph[child] = set()
    
    # scan thru ancestors again and build edges
    for parent_child_pair in ancestors:
        parent = parent_child_pair[0]
        child = parent_child_pair[1]
        # instead of adding vertices, I want to make edges between child and parent
        graph[child].add(parent)

    

    return graph





def earliest_ancestor(ancestors, starting_node):

    # BFS and DFS are possible

    graph = populate_graph(ancestors)
    
    # Using BFS
    queue = Queue()
    visited_set = set()
    queue.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_vertex = current_path[-1]
        if current_vertex not in visited_set:
            visited_set.add(current_vertex)

            # Do something cool while you traverse
            if len(current_path) > longest_path:
                longest_path = len(current_path)
                earliest_ancestor = current_vertex
            elif (len(current_path) == longest_path and current_vertex < earliest_ancestor):
                # We have a tie for longest path, choose the vertex with smallest ID
                earliest_ancestor = current_vertex


            for neighbor in graph[current_vertex]:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)
    return earliest_ancestor


    





# Driver code 
if __name__ == '__main__': 

    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

  
  
    starting_node = 6
    earliest_ancestor(ancestors, starting_node) 
