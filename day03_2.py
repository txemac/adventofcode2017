"""
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then,
in the same allocation order as shown above, they store the sum of the values in all adjacent squares,
including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following
values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 277678.
"""

input = 277678

                                   279138 266330 130654
  6591   6444   6155   5733   5336   5022   2450 128204
 13486    147    142    133    122     59   2391 123363
 14267    304      5      4      2     57   2275 116247
 15252    330     10      1      1     54   2105 109476
 16295    351     11     23     25     26   1968 103128
 17008    362    747    806    880    931    957  98098
 17370  35487  37402  39835  42452  45220  47108  48065
