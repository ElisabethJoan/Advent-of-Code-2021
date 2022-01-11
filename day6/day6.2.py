def solution(inp, days):
    init_fish = [int(x) for x in inp.split(',')]
    fish = [0] * 10
    for i in init_fish:
        fish[i] += 1

    for i in range(days):
        born = fish.pop(0)
        fish[6] += born
        fish[8] += born
        fish.append(0)

    return sum(fish)


raw = open('test.txt').read().rstrip()
print(solution(raw, 256))


# ---------------------- WHERE IDIOCY GOES TO DIE ----------------------
# def solution(inp, days):
#     fish = [int(x) for x in inp.split(',')]
#     for i in range(days):
#         fish = fish + ([9] * fish.count(0))
#         fish = [x - 1 if x > 0 else x + 6 for x in fish]
#     return len(fish)
