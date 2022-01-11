def solution(inp):
    nums = [int(z) for x in inp.split('\n') for y in x.split(' -> ') for z in y.split(',')]
    points = {}
    for i in range(0, len(nums), 4):
        coords = nums[i:i + 4]
        for j in list(bresenhams(*coords)):
            if j in points:
                points[j] += 1
            else:
                points[j] = 1

    return sum(y > 1 for _, y in points.items())
    

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
