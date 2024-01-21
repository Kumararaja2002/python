num = int(input("enter a num:"))
no_of_prime = 0

for i in range(2,100):
    count=0
    for j in range(2,20):
        if(j==1 or j==i):
            continue
        elif(i%j==0):
            count+=1
        
    if count==0:
        print(i)
        no_of_prime+=1
        if(num == no_of_prime):
            break