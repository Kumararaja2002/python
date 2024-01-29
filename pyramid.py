n = int(input("enter a num:"))
for i in range(n):
    a = 2*i+1
    for j in range(n-1):
        print(" ",end=" ")
    n-=1
    for k in range(a):
        print("*",end=" ")
    print("\n")
