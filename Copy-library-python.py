# Understanding copy library of the python how it works:


import copy
def fun(c1, c2, c3):
    c1[0].append(1)
    c2[0].append(2)
    c3[0].append(3)

a = ([0],)
c1 = a
c2 = copy.copy(a)
c3 = copy.deepcopy(a)
fun(c1, c2, c3)

print(a)


list_a = [[1,2], [10,11]]
list_b = copy.copy(list_a)
list_c = copy.deepcopy(list_a)

list_b[1].append(999)
print(f"shallow copy of list_b {list_b}")
print(f"Original list {list_a}")
print(f"deep copy output: {list_c}")
