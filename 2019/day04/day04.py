#!/usr/bin/env python3

import time
from itertools import groupby

RANGE = range(145852, 614943)


def valid_pwd(pwd: list):  # Part1
    # Take reverse list of ints and check for Part 1 criteria
    double = False
    for n in range(len(pwd)-1):
        if pwd[n] < pwd[n+1]:
            return False
        if pwd[n] == pwd[n+1]:
            double = True
    if double:
        return True

    return False


def valid_pwd2(pwd: list):
    # Take reverse list of ints and check for Part 2 criteria
    for n in range(len(pwd)-1):
        if pwd[n] < pwd[n+1]:
            return False
    grouped = [sum(1 for i in g) for _, g in groupby(pwd)]
    return grouped.count(2) >= 1


def get_digits(num):
    # Convert integer to list of ints (reversed)
    rev_num = []
    while num > 0:
        dm = divmod(num, 10)
        rev_num.append(dm[1])
        num = dm[0]

    return rev_num


# Part 1
count1 = 0
start1 = time.time()
for i in RANGE:
    if valid_pwd(get_digits(i)):
        count1 += 1
print(f"time: {time.time()-start1}")
print(f"Part 1: {count1}")

# Part 2
count2 = 0
start2 = time.time()
for i in RANGE:
    if valid_pwd2(get_digits(i)):
        count2 += 1
print(f"time: {time.time()-start2}")
print(f"Part 2: {count2}")
