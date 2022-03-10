def solution(inp, steps):
    template, rules = inp.split('\n\n')
    instructions = dict(x.split(' -> ') for x in rules.split('\n'))

    current = template
    for _ in range(steps):
        working = str(current)
        insertions = 0
        for idx in range(1, len(current)):
            if (instructions[current[idx - 1] + current[idx]]):
                working = str_insert(working, instructions[current[idx - 1] + current[idx]], idx + insertions)
                insertions += 1
        current = str(working)

    frequencies = [current.count(char) for char in set(current)]
    maxi = max(frequencies)
    mini = min(frequencies)

    return maxi - mini


def str_insert(source, insert, idx):
    return ''.join((source[:idx], insert, source[idx:]))


raw = open('input.txt').read().rstrip()
print(solution(raw, 40))