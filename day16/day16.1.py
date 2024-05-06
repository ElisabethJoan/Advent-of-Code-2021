def solution(inp):
    global tape, pos, ver
    tape = bin(int(inp, 16))[2:].zfill(len(inp) * 4)
    pos = ver = 0

    total = identify()
    return total


def identify():
    global ver
    ver += read(3)
    if read(3) == 4:
        cont = read(1)
        total = read(4, literal = True)
        while cont:
            cont = read(1)
            total += read(4, literal = True)
        total = int(total, 2)
    elif read(1):
        l = read(11)
        identify()
        for _ in range(l - 1): 
            identify()
    else: 
        l = read(15) + pos
        identify()
        while pos < l:
            identify()

    return ver


def read(count, literal = False):
    global tape, pos
    pos += count

    read = tape[:count]
    tape = tape[count:]

    if literal:
        return read
    else:
        return int(read, 2)

            

raw = open('input.txt').read().rstrip()
print(solution(raw))




# def solution(inp):
#     global tape, ver
#     ver = 0
#     tape = bin(int(inp, 16))[2:].zfill(len(inp) * 4)
#     identify(tape)

#     return ver
            
# def identify(pac):
#     global tape, ver
#     t_pac = pac
#     while t_pac is not None and t_pac != '' and len(t_pac) > 0 and int(t_pac, 2) > 0 and len(t_pac) > 7:
#         ver += int(t_pac[0:3], 2)
#         tid = t_pac[3:6]
#         t_pac = t_pac[6:]
#         if int(tid, 2) == 4:
#             t_pac = literal_packet(t_pac)
#         else:
#             ind = t_pac[0]
#             t_pac = t_pac[1:]
#             if ind == '1':
#                 lab = t_pac[:11]
#                 t_pac = t_pac[11:]
#                 t_pac = operator_packet_t1(t_pac, lab)
#             else:
#                 t_pac = operator_packet_t0(t_pac)
#     return (False, int(ver, 2))

# def literal_packet(mbin):
#     val = ''
#     i = 0
#     while True:
#         val += mbin[(i * 5) + 1: (i + 1) * 5]
#         if (mbin[i * 5] == '0'):
#             break
#         i += 1
#     res = mbin[((i + 1) * 5):]
#     if res == '' or len(res) * '0' == res:
#         return ''
#     else:
#         return mbin[((i + 1) * 5):]


# def operator_packet_t0(pac):
#     lab = pac[:15]
#     n_pac = pac[15:15 + int(lab, 2)]
#     while len(n_pac) != 0:
#         val, i = identify(n_pac)
#         if not val:
#             return pac[15 + int(lab, 2):]
#         else:
#             n_pac = n_pac[((i + 1) * 5) + 6:]


# def operator_packet_t1(pac, lab):
#     n_pac = pac
#     for i in range(int(lab, 2)):
#         val, i = identify(n_pac)
#         if not val:
#             return '0'
#         else:
#             n_pac = n_pac[((i + 1) * 5) + 6:]


# raw = open('testl.txt').read().rstrip()
# print(solution(raw))