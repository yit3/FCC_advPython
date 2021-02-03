#lambda arguments: expression

add10 = lambda x : x+10

print(add10(5))


def add10_func(x):
    return x + 10

print(add10_func(5))

mult = lambda x,y: x*y

print(mult(5,3))

################
points2D = [(1,2), (15,1), (5,-1), (10,4)]

points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)
###################

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print("map function")
print(list(b))

c = [x*2 for x in a]
print(c)

### filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda  x: x%2==0, a)
print("filter function")
print(list(b))

c = [x for x in a if x%2==0]
print(c)

### reduce(func, seq)
from functools import reduce
a = [1,2,3,4]

product_a = reduce(lambda x, y: x*y, a)
print(product_a)