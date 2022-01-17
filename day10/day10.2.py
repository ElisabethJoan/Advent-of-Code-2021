def solution(inp):
    nav = [line for line in inp.split('\n')]
    lookup = {'(': 1, '[': 2, '{': 3, '<': 4 }

    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    scores = []

    for line in nav:
        pending = []
        for char in line:
            if char in opens:
                pending.append(char)
            else:
                idx = closes.index(char)
                if pending.pop(len(pending) - 1) != opens[idx]:
                    pending = []
                    break

        if len(pending) > 0:
            score = 0
            for i in reversed(pending):
                score *= 5
                score += lookup[i]
            scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]


raw = open('input.txt').read().rstrip()
print(solution(raw))
