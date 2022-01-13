def solution(inp):
    uniques = 0

    for line in inp.split('\n'):
        _, outputs = [signal_patterns.split(' ') for signal_patterns in line.split(' | ')]
        uniques += len([output for output in outputs if len(output) in [2, 3, 4, 7]])

    return uniques


raw = open('input.txt').read().rstrip()
print(solution(raw))
