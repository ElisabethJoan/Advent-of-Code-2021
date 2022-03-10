def solution(inp, steps):
    template, rules = inp.split('\n\n')
    instructions = { key: (key[0] + insert, insert + key[1]) for key, insert in [x.split(' -> ') for x in rules.split('\n')] }
    
    pairs = {}
    for idx, elm in enumerate(template[:-1]):
        pair = elm + template[idx + 1]
        pairs[pair] = pairs.get(pair, 0) + 1 

    frequencies = { char: template.count(char) for char in set(template) }
    for _ in range(steps):
        working = pairs.copy()

        for pair, count in pairs.items():
            if count:
                pair1, pair2  = instructions[pair]
                working[pair] = working[pair] - count
                working[pair1] = working.get(pair1, 0) + count
                working[pair2] = working.get(pair2, 0) + count
                frequencies[pair1[1]] = frequencies.get(pair1[1], 0) + count

        pairs = working.copy()

    values = frequencies.values()
    return max(values) - min(values)


raw = open('input.txt').read().rstrip()
print(solution(raw, 40))



## GRAVEYARD

##SOLUTION 1
# def solution(inp, steps):
#     template, rules = inp.split('\n\n')
#     instructions = dict(x.split(' -> ') for x in rules.split('\n'))

#     current = template
#     for step in range(steps):
#         working = str(current)
#         insertions = 0
#         for idx in range(1, len(current)):
#             if (instructions[current[idx - 1] + current[idx]]):
#                 working = str_insert(working, instructions[current[idx - 1] + current[idx]], idx + insertions)
#                 insertions += 1
#         current = str(working)

#     frequencies = [current.count(char) for char in set(current)]
#     maxi = max(frequencies)
#     mini = min(frequencies)

#     return maxi - mini

## ATTEMPT 2
# def solution(inp, steps):
#     template, rules = inp.split('\n\n')
#     instructions = dict(x.split(' -> ') for x in rules.split('\n'))

#     current = str(template)
#     print(template)
#     for step in range(steps):
#         working = list(current)

#         keys = {}
#         for i in [x for x in instructions.keys() if x in current]:
#             for j in list(find_all(current, i)):
#                 keys[j] = instructions[i]

#         for key, value in keys.items():
#             working = str_insert(working, value, key)

#         current = ''.join(working)

#     frequencies = [current.count(char) for char in set(current)]
#     maxi = max(frequencies)
#     mini = min(frequencies)

#     return maxi - mini


# def find_all(a_str, sub):
#     start = 0
#     while True:
#         start = a_str.find(sub, start)
#         if start == -1: return
#         yield start
#         start += 1


# def str_insert(source, insert, idx):
#     source[idx] = source[idx] + insert

#     return source

## ATTEMPT 2
# def solution(inp, steps):
#     template, rules = inp.split('\n\n')
#     instructions = dict(x.split(' -> ') for x in rules.split('\n'))

#     current = str(template)
#     for step in range(steps):
#         working = list(current)
#         pairs = []
#         for i in range(1, len(current)):
#             pairs.append(current[i - 1] + current[i])

#         for idx, pair in enumerate(pairs):
#             if (instructions[pair]):
#                 working[idx] = working[idx] + instructions[pair]

#         current = ''.join(working)

#     frequencies = [current.count(char) for char in set(current)]
#     maxi = max(frequencies)
#     mini = min(frequencies)

#     return maxi - mini