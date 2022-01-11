def solution(inp):
    data = [int(x.rstrip()) for x in inp.split('\n')]
    count = 0
    prev = float('inf')
    for i in range(3, len(data) + 1):
        if prev < sum(data[i - 3: i]):
            count = count + 1
        prev = sum(data[i - 3: i])
    return count


raw = open('input.txt').read().rstrip()
print(solution(raw))