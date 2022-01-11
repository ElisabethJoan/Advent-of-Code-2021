def solution(inp):
    data = [tuple(x.strip().split(' ')) for x in inp.split('\n')]
    nav = { 'forward': 0, 'up': 0, 'down': 0 }
    for cmd, val in data:
        nav[cmd] += int(val)

    return nav['forward'] * (nav['down'] - nav['up'])


raw = open('input.txt').read().rstrip()
print(solution(raw))
