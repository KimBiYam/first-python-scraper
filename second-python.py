def say_hello(name, age):
    return f"Hello {name} you are {age} years old"


def plus(a, b):
    print(a + b)


def minus(a, b=0):
    print(a - b)


plus(2, 5)
minus(b=30, a=1)

print(say_hello(age="12", name="nico"))
