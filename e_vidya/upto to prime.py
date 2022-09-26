#print prime numbers upto n
# n is the upper limit

n=int(input('enter the upper limit'))
for x in range(2,n):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x)
    
   

    
    

 


