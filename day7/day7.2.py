def solution(inp):
    crabs = [int(x) for x in raw.split(',')]

    average = sum(crabs) / len(crabs)
    target = int(average // 1)
    
    return sum([(abs(x - target)) * (abs(x - target) + 1) // 2 for x in crabs])


raw = open('input.txt').read().rstrip()
print(solution(raw))