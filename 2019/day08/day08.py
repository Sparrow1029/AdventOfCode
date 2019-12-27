#!/usr/bin/env python3
from collections import Counter

with open('input.txt', 'r') as f:
    image_data = f.read()


def layers(image_data, w, h):
    area = w * h
    # num_layers = len(image_data) // area
    for i in range(0, len(image_data)-area, area):
        yield image_data[i:i+area]


# Part 1
least_zeroes = None  # Counter object

get_layers = layers(image_data, 25, 6)
for layer in get_layers:
    # print(Counter(layer))
    cur_layer = Counter(layer)
    if not least_zeroes:
        least_zeroes = cur_layer
    if cur_layer['0'] < least_zeroes['0']:
        least_zeroes = cur_layer

print(least_zeroes['1'] * least_zeroes['2'])

# Part 2
