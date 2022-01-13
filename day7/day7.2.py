def solution(inp):
    crabs = [int(crab) for crab in inp.split(',')]

    target = int(sum(crabs) / len(crabs))
    
    return sum([(abs(crab - target)) * (abs(crab - target) + 1) // 2 for crab in crabs])


raw = open('input.txt').read().rstrip()
print(solution(raw))
