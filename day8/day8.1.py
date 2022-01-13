def solution(inp):
    lines = [x for x in inp.split('\n')]
    uniques = 0

    for line in lines:
        _, outputs = [x.split(' ') for x in line.split(' | ')]
        uniques += len([x for x in outputs if len(x) in [2, 3, 4, 7]])

    return uniques


raw = open('input.txt').read().rstrip()
print(solution(raw))
