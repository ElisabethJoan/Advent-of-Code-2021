def solution(inp):
    commands = [tuple(line.strip().split(' ')) for line in inp.split('\n')]
    nav = { 'forward': 0, 'up': 0, 'down': 0, 'depth': 0 }
    for cmd, val in commands:
        if cmd == 'forward':
            nav['depth'] += int(val) * (nav['down'] - nav['up'])
        nav[cmd] += int(val)

    return nav['forward'] * nav['depth']


raw = open('input.txt').read().rstrip()
print(solution(raw))
