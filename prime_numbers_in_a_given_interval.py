num = int(input("enter a num:"))

for i in range(2,num+1):
    count=0
    for j in range(2,20):
        if(j==1 or j==i):
            continue
        elif(i%j==0):
            count+=1
        
    if count==0:
        print(i)