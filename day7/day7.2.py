def solution(inp):
    crabs = [int(x) for x in raw.split(',')]

    target = int(sum(crabs) / len(crabs))
    
    return sum([(abs(x - target)) * (abs(x - target) + 1) // 2 for x in crabs])


raw = open('input.txt').read().rstrip()
print(solution(raw))
