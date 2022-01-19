def solution(inp):
    global octopuses
    octopuses = [[float('nan')] + list(map(int, line)) + [float('nan')] for line in inp.split('\n')]
    octopuses.insert(0, [float('nan')] * len(octopuses[0]))
    octopuses.append([float('nan')] * len(octopuses[0]))

    step = 0
    flashes = 0
    while flashes != (10 * 10):
        octopuses = [[energy + 1 for energy in line] for line in octopuses]
        for y, row in enumerate(octopuses[1:-1], 1):
            for x, octopus in enumerate(row[1:-1], 1):
                if octopus > 9:
                    increment_neighbours(x, y)

        flashes = 0
        for y, row in enumerate(octopuses[1:-1], 1):
            for x, octopus in enumerate(row[1:-1], 1):
                if octopus == float('inf'):
                    flashes += 1
                    octopuses[y][x] = 0
        step += 1

    return step


def increment_neighbours(x, y):
    if octopuses[y][x] == float('inf'):
        return
    octopuses[y][x] = float('inf')
    neighbours = find_neightbours(x, y)
    for i in neighbours:
        octopuses[i[1]][i[0]] += 1
        if octopuses[i[1]][i[0]] > 9:
            increment_neighbours(i[0], i[1])


def find_neightbours(x, y):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbours.append((x + i, y + j))

    neighbours.remove((x, y))
    return neighbours


raw = open('input.txt').read().rstrip()
print(solution(raw))
