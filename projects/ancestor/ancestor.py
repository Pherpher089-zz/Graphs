from graph import Graph
from util import Queue, Stack


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
print(earliest_ancestor(test_ancestors, 2))
