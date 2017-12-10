"""
--- Part Two ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
How many non-canceled characters are within the garbage in your puzzle input?

Although it hasn't changed, you can still get your puzzle input.

day09_input.txt
"""

input1 = "<>"
input2 = "<random characters>"
input3 = "<<<<>, 3 characters."
input4 = "<{!>}>, 2 characters."
input5 = "<!!>, 0 characters."
input6 = "<!!!>>, 0 characters."
input7 = """<{o"i!a,<{i<a>"""


def score(string):
    result = 0
    flag_garbage = False
    flag_ignore = False

    for c in string:
        if flag_ignore:
            flag_ignore = False
            continue
        if c == "!":
            flag_ignore = not flag_ignore
        elif flag_garbage:
            if c == ">":
                flag_garbage = False
            else:
                result += 1
        elif c == "<":
            flag_garbage = True

    return result


assert score(input1) == 0
assert score(input2) == 17
assert score(input3) == 3
assert score(input4) == 2
assert score(input5) == 0
assert score(input6) == 0
assert score(input7) == 10

with open('day09_input.txt', 'r') as f:
    print score(f.read())
