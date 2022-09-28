input_list=[0,1,2,3,4,5,6,7,8,9,10]
output_list=[]
for num in input_list:
    if num==0 or num==1:
        continue
    for i in range(2,num):
        if num%i==0:
            break
    else:
        output_list.append(num)
if len(output_list)>0:
    print('the prime numbers are:',output_list)
else:
    print('no prime numbers in the list')
