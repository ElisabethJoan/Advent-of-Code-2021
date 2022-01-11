def solution(inp):
    initial = [x for x in inp.split('\n') if x]
    nums = [int(x) for x in initial[0].split(',')]
    boards = [x.split() for x in initial[1:]]
    cards = {}

    for i in range(len(boards) // 5):
        temp = [list(map(int, x)) for x in boards[(i * 5):(i * 5) + 5]]
        cards[i] = [set(x) for x in temp]
        for j in range(5):
            cards[i].append(set([x[j] for x in temp]))

    for k in range(5, len(nums) + 1):
        for l in range(10):
            idx = [i for i, x in enumerate(cards.values()) if x[l].issubset(set(nums[0:k]))]
            if (len(idx) > 0):
                unmarked = set().union(*cards[idx[0]]) - set(nums[0:k])
                return sum(unmarked) * nums[k - 1]


raw = open('input.txt').read().rstrip()
print(solution(raw))