#print various types of star patterns

n=int(input("Enter the range: "))
print()
print("Right angled triangle\n")
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
print("\n")
print("Reverse right angled triangle\n")
for a in range(n,0,-1):
    for b in range(a,0,-1):
        print("*",end="")
    print()
print("\n")
print("Mirror right angled triangle\n")
for o in range (1,n+1):
    for space in range(n-o):
        print(" ",end="")
    for star in range(o):
        print("*",end="")
    print()
print("\n")
print("Reversed mirrored right angled triangle\n")
for m in range (0,n):
    for rspace in range(m):
        print(" ",end="")
    for rstar in range(n-m,0,-1):
        print("*",end="")
    print()
print("\n")
print("Centered triangle\n")
for v in range(0,n):
    for cspace in range(n-v,0,-1):
        print(" ",end="")
    print("*"*((2*v)+1),end="")
    print()
print("\n")
print("Reverse Centered triangle\n")
for v in range(n,0,-1):
    for rcspace in range(n-v):
        print(" ",end="")
    print("*"*((2*(v-1))+1),end="")
    print()