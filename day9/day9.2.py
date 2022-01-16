def solution(inp):
    cavern = [[float('inf')] + list(map(int, line)) + [float('inf')] for line in inp.split('\n')]
    cavern.insert(0, [float('inf')] * len(cavern[0]))
    cavern.append([float('inf')] * len(cavern[0]))

    basins = []
    for y, row in enumerate(cavern[1:-1], 1):
        for x, point in enumerate(row[1:-1], 1):
            if all(point < cavern[adj_y][adj_x] for adj_x, adj_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]):
                basins.append(find_basin(x, y, cavern))

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


def find_basin(x, y, cavern):
    basin = []
    path = [(x, y)]

    for x, y in path:
        if cavern[y][x] != float('inf') and (x, y) not in basin:
            basin.append((x, y))
            path += traverse_point(x, y, cavern[y][x], cavern)
    return len(basin)


def traverse_point(x, y, point, cavern):
    basin_members = []
    for adj_x, adj_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            adj_point = cavern[adj_y][adj_x]
            if adj_point != 9 and adj_point > point:
                basin_members.append((adj_x, adj_y))
    return basin_members


raw = open('input.txt').read().rstrip()
print(solution(raw))

