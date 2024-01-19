num = int(input("enter a num:"))
def fact(num):
    if num == 1:
        return num
    else :
        return num*fact(num-1)
print(fact(num))
