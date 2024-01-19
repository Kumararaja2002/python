strname = input("enter a string:")
strset = set(strname)
count=0
a = sorted(strset)
for i in a:
    for j in strname:
        if(i == j):
            count+=1
    print(i,count)
    count = 0

"""
str1 = "GeeksforGeeks"

dict1 = {}
 
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
      + str(dict1))
"""
