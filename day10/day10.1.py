def solution(inp):
    nav = [line for line in inp.split('\n')]
    lookup = {')': 3, ']': 57, '}': 1197, '>': 25137 }

    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    errors = []

    for line in nav:
        pending = []
        for char in line:
            if char in opens:
                pending.append(char)
            else:
                idx = closes.index(char)
                if pending.pop(len(pending) - 1) != opens[idx]:
                    errors.append(char)

    score = 0
    for i in set(errors):
        score += lookup[i] * errors.count(i)
    return score


raw = open('input.txt').read().rstrip()
print(solution(raw))
