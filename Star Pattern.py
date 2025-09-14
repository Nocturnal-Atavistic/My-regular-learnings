for i in range(5):
    print("*", end="\n")
    for j in range(i)  :# in range (5):
        # if i <5 and  j < 5:
        print("*", end="")
print("\n-------------------------------------")

for i in range(5):
    print("*", end="")
    for j in range(5):
        print("*", end="")
print("\n-------------------------------------")


for i in range(1,5):
    print("*", end="")
    print("", end="\n")
    
    for j in range(i):
        print("*",end="" )   

# Inverted right triangle
n = 5
for i in range(n):
    print("")
    for j in range (n-i):
        print("", end="")
    print("*", end="")
    for k in range(j):
        print ("*", end="")

# Right Triangle:
print("\n-------------------------------------")
for i in range (n-1):
    print("*")
    for j in range (i+1):
        print("*", end="")
        for k in range(j-1):
            print("*", end="")

