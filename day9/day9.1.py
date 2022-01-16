def solution(inp):
    cavern = [[float('inf')] + list(map(int, line)) + [float('inf')] for line in inp.split('\n')]
    cavern.insert(0, [float('inf')] * len(cavern[0]))
    cavern.append([float('inf')] * len(cavern[0]))

    lowest = []
    for y, row in enumerate(cavern[1:-1], 1):
        for x, point in enumerate(row[1:-1], 1):
            if all(point < cavern[y1][x1] for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]):
                lowest.append(point)

    return sum(lowest) + len(lowest)


raw = open('input.txt').read().rstrip()
print(solution(raw))
