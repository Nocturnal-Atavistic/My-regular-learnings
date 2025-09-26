
# Lamda Function

add= lambda x,y: x+y
result= add(65,42)
print(result)

#Lambda function as parameter for other functions

# map()  function
mylist = [1,2,3,4,5]
result = list(map(lambda x: x**2, mylist))
print(result)

# filter() function
mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
result = list(filter(lambda x: x%2==0, mylist))

print(result)

# reduce() function
from functools import reduce
mylist = [1,2,3,4,5]
result = reduce(lambda x,y: x*y, mylist)
print(result)

# check more about functools!!!!!!!!!!!
