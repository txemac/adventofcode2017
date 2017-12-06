"""
--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already
been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?

Although it hasn't changed, you can still get your puzzle input.
"""

input = """5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"""

#input = """0    2   7   0"""

history = []
input = map(int, input.split())

steps = 0
flag = False
aux = None

while True:
    history.append(input[:])

    index_max = input.index(max(input))
    index_start = index_max + 1
    index_end = index_start + input[index_max]

    input[index_max] = 0

    for i in range(index_start, index_end):
        index = i
        while index >= len(input):
            index = index - len(input)
        input[index] += 1

    if input in history:
        if aux == input:
            break
        if aux is None:
            aux = input[:]
            steps = 1
        else:
            steps += 1

print steps
