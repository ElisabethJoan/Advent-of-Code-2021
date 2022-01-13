def solution(inp):
    lines = [x for x in inp.split('\n')]

    total = 0
    for line in lines:
        inputs, outputs = [x.split(' ') for x in line.split(' | ')]
        inputs = sorted([set(s) for s in inputs], key = lambda x : len(x))

        nums = {}
        nums[1] = inputs.pop(0)
        nums[7] = inputs.pop(0)
        nums[4] = inputs.pop(0)
        nums[8] = inputs.pop(-1)
        
        for i in inputs[0:3]:
            if i >= nums[1]:
                nums[3] = i
            elif len(i & nums[4]) == 3:
                nums[5] = i
            else: 
                nums[2] = i

        for i in inputs[3:]:
            if i >= nums[4]:
                nums[9] = i
            elif len(i & nums[7]) == 2:
                nums[6] = i
            else: 
                nums[0] = i

        output = ''
        for i in outputs:
            output += ''.join([str(x) for x, y in nums.items() if set(i) == y])
        
        total += int(output)
    return total


raw = open('input.txt').read().rstrip()
print(solution(raw))


# ---------------------- WHERE IDIOCY GOES TO DIE ----------------------
# def solution(inp):
#     lines = [x for x in inp.split('\n')]

#     total = 0
#     for line in lines:
#         inputs, outputs = [x.split(' ') for x in line.split(' | ')]
#         inputs = sorted([set(s) for s in inputs], key = lambda x : len(x))

#         nums = {}
#         nums[1] = inputs.pop(0)
#         nums[7] = inputs.pop(0)
#         nums[4] = inputs.pop(0)
#         nums[8] = inputs.pop(-1)

#         segs = {}
#         segs[0] = nums[7] - nums[1]

#         for i in [x for x in inputs if len(x) >= 5]:
#             if len(i & nums[4]) == 2:
#                 nums[2] = i
#             if len(i & nums[4]) == 4:
#                 nums[9] = i
#         inputs.remove(nums[2])
#         inputs.remove(nums[9])

#         segs[2] = nums[1] & nums[2] & nums[4]
#         segs[5] = nums[1] - segs[2]

#         for i in [x for x in inputs if len(x) == 6]:
#             if len(i & set.union(*segs.values())) == 2:
#                 nums[6] = i
#             else:
#                 nums[0] = i
#         inputs.remove(nums[6])
#         inputs.remove(nums[0])

#         for i in [x for x in inputs]:
#             if len(i & nums[6]) == 5:
#                 nums[5] = i
#             else:
#                 nums[3] = i

#         output = ''
#         for i in outputs:
#             output += str([x for x, y in nums.items() if set(i) == y].pop())

#         total += int(output)
#     return total