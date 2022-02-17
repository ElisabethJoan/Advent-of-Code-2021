def solution(inp):
    page = [line.rstrip() for line in inp.split('\n\n')]
    dots = [tuple(map(int, coords.split(','))) for coords in page[0].split('\n')]
    folds = [(i[0][-1], int(i[1])) for fold in page[1].split('\n') for i in [fold.split('=')]]

    x = max(dots, key=lambda item:item[0])[0]
    y = max(dots, key=lambda item:item[1])[1]

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
        break

    total = 0
    for line in code:
        total += bin(line).count('1')
    return total


raw = open('input.txt').read().rstrip()
print(solution(raw))


# ---------------------- WHERE IDIOCY GOES TO DIE ----------------------
# def solution(inp):
#     page = [line.rstrip() for line in inp.split('\n\n')]
#     dots = [tuple(map(int, coords.split(','))) for coords in page[0].split('\n')]
#     folds = [(i[0][-1], int(i[1])) for fold in page[1].split('\n') for i in [fold.split('=')]]

#     mx = max(dots, key=lambda item:item[0])[0]
#     my = max(dots, key=lambda item:item[1])[1]

#     code = [[0] * (mx + 1)  for i in range(my + 1)]
#     for coord in dots:
#         code[coord[1]][coord[0]] += 1

#     for fold in folds:
#         if fold[0] == 'x':
#             temp = [[row[0:fold[1]], row[fold[1]+1:len(row)][::-1]] for row in code]
#             if len(temp[0][0]) > len(temp[0][1]):
#                 n = len(temp[0][0]) - len(temp[0][1])
#                 temp[0][1] + [0] * n
#             else:
#                 n = len(temp[0][1]) - len(temp[0][0])
#                 temp[0][0] + [0] * n
#             temp1 = []
#             for i in temp:
#                 temp1.append([a + b for a, b in zip(i[0], i[1])])
#             code = temp1
#         else:
#             code.pop(fold[1])
#             temp = []
#             for i in range(len(code) // 2):
#                 temp.append([a + b for a, b in zip(code[i], code[-1-i])])
#             code = temp
#         break


#     total = 0
#     for i in code:
#         total += len(i) - i.count(0)
#     return total
