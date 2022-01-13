def solution(inp):
    data = [line.rstrip() for line in inp.split('\n')]
    gamma = data
    epsilon = data
    for i in range(len(data[0])):
        f = frequency([code[i] for code in gamma], [code[i] for code in epsilon])
        gamma = list(filter(lambda bit:bit[i] == f[0], gamma))
        epsilon = list(filter(lambda bit:bit[i] == f[1], epsilon))

    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def frequency(l1, l2):
    l1.sort(reverse = True)
    l2.sort()
    return max(l1, key = l1.count), min(l2, key = l2.count)


raw = open('input.txt').read().rstrip()
print(solution(raw))
