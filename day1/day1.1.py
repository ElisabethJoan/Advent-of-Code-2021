def solution(inp):
    data = [int(x.rstrip()) for x in inp.split('\n')]
    count = 0 
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            count = count + 1
    return count


raw = open('input.txt').read().rstrip()
print(solution(raw))
