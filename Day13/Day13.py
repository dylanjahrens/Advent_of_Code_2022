from functools import cmp_to_key
#from math import prod

with open('input.txt', "r") as input_file:
    data = input_file.read().strip()

pairs = [list(map(eval, p.split("\n"))) for p in data.split("\n\n")]

def compare(l, r):
    #returns positive number if packets are in correct spot, negative if not 
    l = l if isinstance(l, list) else [l]
    r = r if isinstance(r, list) else [r]
    for l2, r2 in zip(l, r):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(r) - len(l)


def part1():
    total_sum = 0
    for i, (l,r) in enumerate(pairs, 1):
        if compare(l,r) > 0:
            total_sum += i
    return print(total_sum)


def part2():
    divider_packets = [[[2]], [[6]]]
    packets = [y for x in pairs for y in x] + divider_packets
    sorted_packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    key = 1
    for i, p in enumerate(sorted_packets, 1):
        if p in divider_packets:
            key *= i
    return print(key)

part1()
part2()
#print(f"Part 1: {sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) > 0)}")
#print(f"Part 2: {prod([n for n, p in enumerate(packets, 1) if p in divider_packets}")
