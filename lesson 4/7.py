from math import factorial
def fact_gen():
    for i in range(1,16):
        yield factorial(i)
x = 1
for el in fact_gen():
    print(f'{x}! = {el}')
    x += 1
    if x > 15:
        break
