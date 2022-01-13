def solution(inp):
    nums = [int(coord) for line in inp.split('\n') for coords in line.split(' -> ') for coord in coords.split(',')]
    points = {}
    for i in range(0, len(nums), 4):
        coords = nums[i:i + 4]
        if coords[0] == coords[2] or coords[1] == coords[3]:
            for point in list(bresenhams(*coords)):
                if point in points:
                    points[point] += 1
                else:
                    points[point] = 1

    return sum(overlap > 1 for _, overlap in points.items())
    

def bresenhams(x0, y0, x1, y1):
    x, y = x0, y0
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            yield x, y
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            yield x, y
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    yield x, y


raw = open('input.txt').read().rstrip()
print(solution(raw))


# ---------------------- WHERE IDIOCY GOES TO DIE ----------------------
# def solution(inp):
#     nums = [int(z) for x in inp.split('\n') for y in x.split(' -> ') for z in y.split(',')]
#     coords = [[tuple(nums[i:i+2]), tuple(nums[i+2:i+4])] for i in range(0, len(nums), 4)]
#     grid = [[0] * (max(nums) + 1) for x in range(max(nums) + 1)]
#     gridt = list(map(list, zip(*grid)))
#     for i in coords:
#         if i[0][0] == i[1][0]:
#             gridt[i[0][0]][min(i[0][1], i[1][1]):max(i[0][1], i[1][1]) + 1] = [x + 1 for x in gridt[i[0][0]][min(i[0][1], i[1][1]):max(i[0][1], i[1][1]) + 1]]
#         if i[0][1] == i[1][1]:
#             grid[i[0][1]][min(i[0][0], i[1][0]):max(i[0][0], i[1][0]) + 1] = [x + 1 for x in grid[i[0][1]][min(i[0][0], i[1][0]):max(i[0][0], i[1][0]) + 1]]

#     for i in range(3):
#         gridt = list(map(list, zip(*gridt)))

#     final_grid = []
#     for x, y in zip(grid, gridt):
#         final_grid.append([a + b for a, b in zip(x, y)])

#     counter = 0
#     for i in final_grid:
#         counter += sum(x > 1 for x in i)
#     return counter
