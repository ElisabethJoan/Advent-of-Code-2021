def solution(inp, days):
    school = [0] * 10
    for fish in inp.split(','):
        school[int(fish)] += 1

    for i in range(days):
        born = school.pop(0)
        school[6] += born
        school[8] += born
        school.append(0)

    return sum(school)


raw = open('input.txt').read().rstrip()
print(solution(raw, 256))


# ---------------------- WHERE IDIOCY GOES TO DIE ----------------------
# def solution(inp, days):
#     fish = [int(x) for x in inp.split(',')]
#     for i in range(days):
#         fish = fish + ([9] * fish.count(0))
#         fish = [x - 1 if x > 0 else x + 6 for x in fish]
#     return len(fish)
