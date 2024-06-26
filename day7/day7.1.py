def solution(inp):
    crabs = [int(crab) for crab in inp.split(',')]
    crabs.sort()

    n = len(crabs)
    target = crabs[n // 2] if n % 2 == 0 else crabs[(n - 2) // 2] // 2

    return sum([abs(crab - target) for crab in crabs])


raw = open('input.txt').read().rstrip()
print(solution(raw))
