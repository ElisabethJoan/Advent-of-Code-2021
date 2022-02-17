def solution(inp):
    page = [line.rstrip() for line in inp.split('\n\n')]
    dots = [tuple(map(int, coords.split(','))) for coords in page[0].split('\n')]
    folds = [(i[0][-1], int(i[1])) for fold in page[1].split('\n') for i in [fold.split('=')]]

    x = max(dots, key=lambda item:item[0])[0]
    # y = max(dots, key=lambda item:item[1])[1]
    y = 894

    code = [0b0 for i in range(y + 1)]
    for coord in dots:
        code[coord[1]] = code[coord[1]] ^ (1 << (x - coord[0]))

    for fold in folds:
        if fold[0] == 'x':
            n = fold[1]
            for idx in range(len(code)):
                low = code[idx] >> n + 1
                mask = (2 ** n) - 1
                high = code[idx] & mask
                
                bitstring = '{:0{width}b}'.format(high, width = n)
                high_rev = int(bitstring[::-1], 2)

                code[idx] = low | high_rev
        else:
            for idx in range(len(code) // 2):
                code[idx] = code[idx] | code[-1 - idx]
            code = code[0:len(code) // 2]

    for line in code:
        print(*['#' if x == '1' else '.' for x in bin(line)])


raw = open('input.txt').read().rstrip()
print(solution(raw))