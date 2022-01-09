def solution(inp):
    nums = [int(z) for x in inp.split('\n') for y in x.split(' -> ') for z in y.split(',')]
    coords = [[tuple(nums[i:i+2]), tuple(nums[i+2:i+4])] for i in range(0, len(nums), 4)]
    grid = [[0] * (max(nums) + 1) for x in range(max(nums) + 1)]
    gridt = list(map(list, zip(*grid)))
    for i in coords:
        if i[0][0] == i[1][0]:
            gridt[i[0][0]][min(i[0][1], i[1][1]):max(i[0][1], i[1][1]) + 1] = [x + 1 for x in gridt[i[0][0]][min(i[0][1], i[1][1]):max(i[0][1], i[1][1]) + 1]]
        if i[0][1] == i[1][1]:
            grid[i[0][1]][min(i[0][0], i[1][0]):max(i[0][0], i[1][0]) + 1] = [x + 1 for x in grid[i[0][1]][min(i[0][0], i[1][0]):max(i[0][0], i[1][0]) + 1]]

    for i in range(3):
        gridt = list(map(list, zip(*gridt)))

    final_grid = []
    for x, y in zip(grid, gridt):
        final_grid.append([a + b for a, b in zip(x, y)])
        
    counter = 0
    for i in final_grid:
        counter += sum(x > 1 for x in i)
    return counter

raw = open('input.txt').read().rstrip()
print(solution(raw))