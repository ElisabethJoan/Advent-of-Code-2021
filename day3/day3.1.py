def solution(inp):
    report = [line.rstrip() for line in inp.split('\n')]
    gamma = ''
    epsilon = ''
    for i in range(len(report[0])):
        f = frequency([code[i] for code in report])
        gamma = gamma + f[0]
        epsilon = epsilon + f[1]

    return int(gamma, 2) * int(epsilon, 2)


def frequency(l):
    return max(l, key = l.count), min(l, key = l.count)


raw = open('input.txt').read().rstrip()
print(solution(raw))
