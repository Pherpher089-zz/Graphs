'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
'''


def get_neighbors(node, islands):
    row, col = node
    neighbors = []

    step_north = step_east = step_south = step_west = False

    if col > 0:
        step_north = col - 1
    if row > 0:
        step_east = row - 1
    if col < len(islands) - 1:
        step_south = col + 1
    if row < len(islands) - 1:
        step_west = row + 1

    if step_north is not False and islands[step_north][col]:
        neighbors.append((step_north, col))
    if step_south is not False and islands[step_south][col]:
        neighbors.append((step_south, col))
    if step_east is not False and islands[row][step_east]:
        neighbors.append((row, step_east))
    if step_west is not False and islands[row][step_west]:
        neighbors.append((row, step_west))

    return neighbors


def dft_recursive(node, visited, islands):
    visited.add(node)
    neighbors = get_neighbors(node, islands)
    for n in neighbors:
        if n not in visited:
            dft_recursive(n, visited, islands)


def island_counter(islands):
    visited = set()
    island_count = 0
    for i in range(len(islands) - 1):
        for j in range(len(islands[i]) - 1):
            node = (i, j)

            if node not in visited and islands[i][j] == 1:
                island_count += 1
                dft_recursive(node, visited, islands)

    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))  # returns 4

# Graph termanology
# Nodes[1]
