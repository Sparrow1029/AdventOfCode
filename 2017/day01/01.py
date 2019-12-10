def sequence_sum(data: list):
    data = data[:] + [data[0]]  # make 'circular' by adding first digit to end

    sum_ = 0
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            sum_ += data[i]
    return sum_

def part_two(data: list):
    sum_ = 0
    len_data = len(data)
    compare = len_data//2
    for i in range(len_data):
        if data[i] == data[(i+compare) % len_data]:
            sum_ += data[i]
    return sum_

with open('input.txt', 'r') as f:
    data = f.read().strip()
    data = list(map(int, list(data)))  # Cast to ints

    print(sequence_sum(data))
    print(data[-2:])
    print(part_two(data))
