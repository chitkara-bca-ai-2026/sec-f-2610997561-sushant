
n = int(input("Enter the number of rows: "))

heading1 = "Pattern 1: Star Triangle"
print(heading1)
print("-" * len(heading1))

for i in range(1, n + 1):
    for j in range(i):
      
        print("*", end=" " if j < i - 1 else "")
    print()

print() 

heading2 = "Pattern 2: Number Triangle"
print(heading2)
print("-" * len(heading2))

for i in range(1, n + 1):
    for j in range(1, i + 1):
      
        print(j, end=" " if j < i else "")
    print()

print()

heading3 = "Pattern 3: Inverted Star Triangle"
print(heading3)
print("-" * len(heading3))

for i in range(n, 0, -1):
    for j in range(i):
    
        print("*", end=" " if j < i - 1 else "")
    print()

print() 

heading4 = "Pattern 4: Pyramid"
print(heading4)
print("-" * len(heading4))

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")
    
    num_stars = 2 * i - 1
    for j in range(num_stars):
        print("*", end=" " if j < num_stars - 1 else "")
    print()