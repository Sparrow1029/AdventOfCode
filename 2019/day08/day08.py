#!/usr/bin/env python3
from collections import Counter

WIDTH = 25
HEIGHT = 6
AREA = WIDTH * HEIGHT

with open('input.txt', 'r') as f:
    image_data = f.read().strip()


def build_layers(image_data, w, h):
    area = w * h
    for i in range(0, len(image_data), area):
        yield image_data[i:i+area]


ALL_LAYERS = [list(map(int, list(layer)))for layer in build_layers(image_data, WIDTH, HEIGHT)]


def decode_image(image_data):
    final_image = []
    for i in range(AREA):
        pixel_stack = [row[i] for row in ALL_LAYERS]
        final_image.append(get_color(pixel_stack))

    return final_image


def get_color(pixel_stack):
    for pixel in pixel_stack:
        if pixel != 2:
            return pixel


def render_image(image_data):
    i = 0
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pixel = image_data[i]
            if pixel == 0:
                print(' ', end="")
            elif pixel == 1:
                print('█', end="")
            i += 1
        print()


# Part 1
least_zeroes = None  # Counter object

for layer in ALL_LAYERS:
    cur_layer = Counter(layer)
    if not least_zeroes:
        least_zeroes = cur_layer
    if cur_layer[0] < least_zeroes[0]:
        least_zeroes = cur_layer

print(least_zeroes[1] * least_zeroes[2])

# Part 2
render_image(decode_image(image_data))
