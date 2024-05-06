def solution(inp):
    global tape, pos
    tape = bin(int(inp, 16))[2:].zfill(len(inp) * 4)
    pos = 0

    total = identify()
    return total


def identify():
    read(3)
    if (tid := read(3)) == 4:
        cont = read(1)
        total = read(4, literal = True)
        while cont:
            cont = read(1)
            total += read(4, literal = True)
        total = int(total, 2)
    elif read(1):
        l = read(11)
        total = identify()
        for _ in range(l - 1): 
            total = choose_op(tid, total, identify())
    else: 
        l = read(15) + pos
        total = identify()
        while pos < l:
            total = choose_op(tid, total, identify())

    return total


def read(count, literal = False):
    global tape, pos
    pos += count

    read = tape[:count]
    tape = tape[count:]

    if literal:
        return read
    else:
        return int(read, 2)


def choose_op(tid, a, b):
    match tid:
        case 0:
            return a + b
        case 1: 
            return a * b
        case 2:
            return min(a, b)
        case 3:
            return max(a, b)
        case 5:
            return a > b
        case 6:
            return a < b
        case 7:
            return a == b


raw = open('input.txt').read().rstrip()
print(solution(raw))