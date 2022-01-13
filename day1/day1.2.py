def solution(inp):
    depths = [int(line.rstrip()) for line in inp.split('\n')]
    count = 0
    prev = float('inf')
    for i in range(3, len(depths) + 1):
        if prev < sum(depths[i - 3: i]):
            count = count + 1
        prev = sum(depths[i - 3: i])
    return count


raw = open('input.txt').read().rstrip()
print(solution(raw))
