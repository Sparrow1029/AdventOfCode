#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

# Part 1
print(sum(map(int, input_data)))

# Part 2
frequency = 0
unique = set()
data = list(map(int, input_data))
while frequency not in unique:
    for i in data:
        if frequency in unique:
            print(frequency)
            break
        unique.add(frequency)
        frequency += i
