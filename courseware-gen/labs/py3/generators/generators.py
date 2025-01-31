'''
>>> evens = evens_up_to(8)
>>> type(evens)
<class 'generator'>
>>> for even in evens:
...     print(even)
2
4
6
8

>>> squares = squares_up_to(16)
>>> type(squares)
<class 'generator'>
>>> for square in squares:
...     print(square)
1
4
9
16

>>> for square in squares_up_to(15):
...     print(square)
1
4
9

>>> counter = countdown(3)
>>> type(counter)
<class 'generator'>
>>> for count in countdown(3):
...     print(count)
3
2
1
BLASTOFF!

>>> for count in countdown(10):
...     print(count)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!

'''


# Write your code here:
def evens_up_to(max_num):
    value = 2
    while value <= max_num:
        yield value
        value += 2


def squares_up_to(max_num):
    value = 1
    while value ** 2 <= max_num:
        yield value ** 2
        value += 1


def countdown(num):
    while num >= 1:
        yield num
        num -= 1
    yield "BLASTOFF!"


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest

    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
