#!/usr/bin/env python3

with open('input.txt') as fh:
    input_data = fh.read().splitlines()

twos = 0
threes = 0

for line in input_data:
    chars = set(line)
    if any(line.count(char) == 2 for char in chars):
        twos += 1
    if any(line.count(char) == 3 for char in chars):
        threes += 1

# Part 1
print(twos * threes)


def count_different(str1, str2):
    pos = 0
    dif_pos = []
    pairs = zip(str1, str2)

    for pair in pairs:
        if pair[0] != pair[1]:
            dif_pos.append(pos)
        pos += 1

    if len(dif_pos) == 1:
        return (str1, dif_pos[0])
    return None


# Part 2
for i in range(len(input_data)):
    cur = input_data[i]
    for test in range(i+1, len(input_data)-i):
        found_id = count_different(cur, input_data[test])
        if found_id:
            box_id, dif = list(found_id[0]), found_id[1]
            del box_id[dif]
print(''.join(box_id))
