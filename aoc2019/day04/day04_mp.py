#!/usr/bin/env python3

import time
from itertools import groupby
from multiprocessing import Pool, Value, Lock

RANGE = range(145852, 614943)


class Counter(object):
    def __init__(self, initval=0):
        self.val = Value('i', initval)
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.val.value += 1

    def value(self):
        with self.lock:
            return self.val.value

    def __repr__(self):
        return str(self.val.value)


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


if __name__ == '__main__':
    # Part 1
    counter = Counter(0)

    def mp_func1(i, counter=counter):
        if valid_pwd(get_digits(i)):
            counter.increment()

    starttime = time.time()
    with Pool(processes=12) as pool:  # 'processes' defaults to num CPU cores
        pool.map(mp_func1, RANGE)

    print(f"time: {time.time()-starttime}")
    print(f"Part 1: {counter}")

    # Part 2
    counter = Counter(0)

    def mp_func2(i, counter=counter):
        if valid_pwd2(get_digits(i)):
            counter.increment()

    starttime = time.time()
    with Pool(processes=12) as pool:
        pool.map(mp_func2, RANGE)

    print(f"time: {time.time()-starttime}")
    print(f"Part 2: {counter}")
