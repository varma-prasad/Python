import numpy as np
day_no=[1,2,3,4,5,6,7,8,9,10]
steps_walked=[6012,7079,6886,7230,4598,5564,6971,7763,8032,9569]
walk_arr=np.array([day_no,steps_walked])
print('the asked array is: ',walk_arr)

extra_steps=[2000]*10
print('the addition of extra steps')
add_steps=np.add(walk_arr[1],extra_steps)
print(add_steps)

print('steps walked in sorted orde: ',np.sort(walk_arr[1]))

greater_9000=np.where(add_steps>9000)
print(add_steps[greater_9000])

add_steps.sort()
lee_steps=np.array([day_no,add_steps])
print(lee_steps)

filter_arr = walk_arr[1]>9000
print(filter_arr)
new_arr=walk_arr[1][filter_arr]
print('the required steps: ',new_arr)
