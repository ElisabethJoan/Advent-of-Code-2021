def solution(inp):
    data = [x.rstrip() for x in inp.split('\n')]
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        f = frequency([code[i] for code in data])
        gamma = gamma + f[0]
        epsilon = epsilon + f[1]

    return int(gamma, 2) * int(epsilon, 2)


def frequency(l):
    return max(l, key = l.count), min(l, key = l.count)


raw = open('input.txt').read().rstrip()
print(solution(raw))