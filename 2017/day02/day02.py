import csv
import itertools

def checksum_1(csv_reader):
    checksum = 0
    for row in csv_reader:
        line = list(map(int, row))
        checksum += abs(max(line) - min(line))

    return checksum

def checksum_2(csv_reader):
    checksum = 0
    for row in csv_reader:
        line = list(map(int, row))
        for a, b in itertools.combinations(line, 2):
            div, mod = divmod(max(a,b), min(a,b))
            if mod == 0:
                checksum += div
                break

    return checksum


f = open('input.txt', 'r')
reader = csv.reader(f, delimiter='\t')
print(checksum_1(reader))
f.close()

f = open('input.txt', 'r')
reader = csv.reader(f, delimiter='\t')
print(checksum_2(reader))
f.close()
