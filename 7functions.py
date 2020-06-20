from math import ceil, fsum


def plus(a, b):
    if (type(a) is (int or float)) and (type(b) is (int or float)):
        return int(a) + int(b)
    else:
        return None


def minus(a, b):
    if (type(a) is (int or float)) and (type(b) is (int or float)):
        return int(a) - int(b)
    else:
        return None


def multiply(a, b):
    if (type(a) is (int or float)) and (type(b) is (int or float)):
        return int(a) * int(b)
    else:
        return None


def devide(a, b):
    if (type(a) is (int or float)) and (type(b) is (int or float)):
        return int(a) / int(b)
    else:
        return None


def negation(a):
    if type(a) is int or float:
        return -a
    else:
        return None


def power(a, b):
    if (type(a) is (int or float)) and (type(b) is (int or float)):
        return a ** b
    else:
        return None


print(plus(5, "3"))
print(minus(5, True))
print(multiply(2, 5))
print(negation(2.1))

print(ceil(1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))
