print("1")
for i in range(5):
    print("*", end="\n")
    for j in range(i)  :# in range (5):
        # if i <5 and  j < 5:
        print("*", end="")
print("\n-------------------------------------")

print("2")
for i in range(5):
    print("*", end="\n")
    for j in range(i):
        print("*", end="")
print("\n-------------------------------------")

print("3")
for i in range(1,5):
    print(" ", end="")
    print("*", end="\n")
    
    for j in range(i):
        print("*",end="" )   


print("\n-------------------------------------")

print("4")
# Inverted right triangle
n = 5
for i in range(n):
    print("")
    for j in range (n-i):
        print("", end="")
    print("*", end="")
    for k in range(j):
        print ("*", end="")
print("\n-------------------------------------")
print("5")
# Right Triangle:

for i in range (n-1):
    print("*")
    for j in range (i+1):
        print("*", end="")
        for k in range(j-1):
            print("*", end="")

print("\n-------------------------------------")
# k=5
# j=5
print("6")
for i in range (n):
    print("")
    for j in range (i-1):
        print(" ", end="")
        for k in range(j+1):
            print("*", end="")
    print()
print("\n-------------------------------------")

print("7")
#Pyramid
n = 5
for i in range(n):
    # 1. Print leading spaces
    for j in range(n - 1 - i):
        print(" ", end="")
    
    # 2. Print the stars
    for k in range(2 * i + 1):
        print("*", end="")
        
    # 3. Move to the next line
    print()
print("\n-------------------------------------")

print("8")
# Square
for i in range (n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\n-------------------------------------")
# down triangle
print("9")
for i in range (n):
    for j in range(i,n):
        print("*", end="")
    print()

print("\n-------------------------------------")


# increasing triangle
print("10")

for i in range (n):
    for j in range(i+1):
        print("*", end="")
    print()

print("\n-------------------------------------")
# Right side triangle
print("11")

for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")

    print()

print("\n-------------------------------------")
print("12")
# Right side downward triangle
for i in range (n):
    for j in range(i+1):
        print(" ", end="")
    for k in range(i,n):
        print("*", end="")
    print()



# Pyramid
print("13")
n=5
for i in range(n):

    for j in range(i,n):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    for p in range(k):
        print("*", end="")

    print()

print("\n-------------------------------------")

# Reverse Pyramid
print("14")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for k in range(i,n-1):
        print("*", end="")
    for p in range(i,n):
        print("*", end="")

    print()
