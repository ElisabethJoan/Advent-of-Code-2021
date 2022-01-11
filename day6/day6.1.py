def solution(inp, days):
    fish = [int(x) for x in inp.split(',')]
    for i in range(days):
        fish = fish + ([9] * fish.count(0))
        fish = [x - 1 if x > 0 else x + 6 for x in fish]
    return len(fish)


raw = open('test.txt').read().rstrip()
print(solution(raw, 18))
