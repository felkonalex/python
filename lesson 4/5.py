from functools import reduce
list = [i for i in range(100, 1001, 2)]
def func(a, b):
    return a * b
print(reduce(func, list))