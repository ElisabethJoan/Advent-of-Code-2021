def solution(inp):
    data = [int(x.rstrip()) for x in inp.split('\n')[:-1]]
    count = 0 
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            count = count + 1
    return count

raw = open('input.txt').read()
print(solution(raw))