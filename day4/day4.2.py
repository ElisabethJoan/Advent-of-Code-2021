def solution(inp):
    initial = [line for line in inp.split('\n') if line]
    nums = [int(num) for num in initial[0].split(',')]
    boards = [board.split() for board in initial[1:]]
    cards = {}

    for i in range(len(boards) // 5):
        board_rows = [list(map(int, board)) for board in boards[(i * 5):(i * 5) + 5]]
        cards[i] = [set(row) for row in board_rows]
        for j in range(5):
            cards[i].append(set([row[j] for row in board_rows]))

    winners = set()
    for k in range(5, len(nums) + 1):
        for l in range(10):
            idx = [i for i, line in enumerate(cards.values()) if line[l].issubset(set(nums[0:k]))]
            if (len(winners) == len(cards) - 1 and len(set(idx) - winners) == 1):
                unmarked = set().union(*cards[(set(idx) - winners).pop()]) - set(nums[0:k])
                return sum(unmarked) * nums[k - 1]
            winners.update(idx)


raw = open('input.txt').read().rstrip()
print(solution(raw))
