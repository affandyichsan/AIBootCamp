
from functools import reduce

numbers = [1,2,3,4]
product = reduce(lambda x,y : x * y, numbers )
print(product)


evenList = filter(lambda x: x % 2 == 0, numbers)
# print(list(evenList))

numbers = [1,2,3,4]
squares = map(lambda x: x**2, numbers)
# print(list(squares))



# expression for item in iterable if conditional

# create a list of squares
squares = [x**2 for x in range(10)]
# print(squares)

# fileter even numbers
evens = [x for x in range(100) if x % 2 != 0]
# print(evens)

# lambda arguments expression 
add = lambda x, y: x + y
# print(add(3,5))
