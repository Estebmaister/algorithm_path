"""
Both functions return the union of the square power for each number
use list comprehension, int() function, str() function and .join() method.  
"""


def square_digits(num):
    # result = map(lambda x: str(int(x) ** 2), result)
    return int("".join([str(int(number) ** 2) for number in str(num)]))


def square_digits2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)


print(square_digits(9119), 811181)
print(square_digits2(9119), 811181)
