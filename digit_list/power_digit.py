"""
All the functions return the union of the square power for each number
use list comprehension, int(), divmod(), sum(), enumerate, str() functions. 

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

* Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.
"""


def dig_pow(num, p):
    suma = 0
    str_num = str(num)
    for iteration in range(len(str_num)):
        suma += int(str_num[iteration]) ** (p + iteration)

    k = 0
    while k * num <= suma:
        if k * num == suma:
            return k
        k += 1

    return -1


def dig_pow2(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s / n if s % n == 0 else -1


def dig_pow3(n, p):
    k, fail = divmod(sum(int(d) ** (p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k


print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)

print(dig_pow2(89, 1), 1)
print(dig_pow2(92, 1), -1)

print(dig_pow3(89, 1), 1)
print(dig_pow3(92, 1), -1)
