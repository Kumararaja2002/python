a = []
num = int(input("enter the size:"))
for i in range(num):
    a.append(int(input("enter a num:")))
second_largest = a.sort()
print(f"{a[-2]} is the second largest")