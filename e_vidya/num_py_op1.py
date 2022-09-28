import numpy as np
# filter data
hp=[123,678,456,345,567]
array=np.array(hp)
filter_arr=array>500
new_arr=array[filter_arr]
print(filter_arr)
print(new_arr)

#sorting data

print('oroginal array:',array)
print('sorted: ', np.sort(array))
print('the original array:',array)

print('The original array:',array)
array.sort()
print('original array after sorting: ',array)

# mathematical operations
print(np.sum(hp))
extra=[1,23,4,3,53]
print(np.add(hp,extra))
print(np.subtract(hp,extra))
print(np.power(hp,extra))
print(np.mod(hp,extra))
print(np.divide(hp,extra))

#2D array
stu_marks=np.array([[67,45],[98,34],[45,67]])
#broadcasting
stu_marks+=[5,10]
print(stu_marks)
