from graph import Graph
from util import Queue

# LECTURE


class MyGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, parent, child):
        self.nodes[child].add(parent)

    def get_neighbors(self, node):
        return self.nodes[node]


class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)


def dft(graph, starting_node):
    s = Stack()
    s.push((starting_node, 0))
    visited_pairs = set()
    while s.size() > 0:
        current_pair = s.pop()
        current_node = current_pair[0]
        current_distance = current_pair[1]
        visited_pairs.add(current_pair)
        parents = graph.get_neighbors(current_node)

        for i in parents:
            parent_distance = current_distance + 1
            s.push((i, parent_distance))

        longest_distance = -1
        aged_one = -1
        for pair in visited_pairs:
            node = pair[0]
            distance = pair[1]
            if distance > longest_distance and node != starting_node:
                longest_distance = distance
                aged_one = node
        return aged_one


# def earliest_ancestor(ancestors, starting_node):
#     graph = MyGraph()
#     for parent, child in ancestors:
#         graph.add_node(parent)
#         graph.add_node(child)
#         graph.add_edge(parent, child)

#     earliest_ancestor = dft(graph, starting_node)
#     return earliest_ancestor
    # MY SOLUTION


def find_parents(ancestors, child):
    parents = []
    for i in ancestors:
        if i[1] == child[0]:
            parents.append(i[0])
    if len(parents) > 0:
        return parents
    else:
        return []


def earliest_ancestor(ancestors, starting_node):
    stack = Stack()
    stack.push((starting_node, 0))
    with_gen = []
    while stack.size() > 0:
        child = stack.pop()
        with_gen.append(child)
        parents = find_parents(ancestors, child)
        if len(parents) > 0:
            for i in parents:
                stack.push((i, child[1] + 1))
        elif child[0] == starting_node:
            return -1

    highest_gen_list = []
    highest_gen = 0

    for i in with_gen:
        if i[1] > highest_gen:
            highest_gen_list = []
            highest_gen_list.append(i[0])
            highest_gen += 1
        elif i[1] == highest_gen:
            highest_gen_list.append(i[0])

    # Finding lowest id of earliest ancestors
    lowest_id = None
    for i in highest_gen_list:
        if lowest_id == None or i < lowest_id:
            lowest_id = i

    return i
# Will find the parents of any child node


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                  (5, 7), (4, 5), (4, 8), (8, 9),
                  (11, 8), (10, 1)]
print("survey says:")
print(earliest_ancestor(test_ancestors, 6))
