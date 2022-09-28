import numpy as np
cars=np.array(['tata','maruti','toyota','honda'])
print(cars)
print(cars.dtype)
print(cars.shape)
# Accessing element from 1D array.
print(cars[1])

car_names=['tata','maruti','toyota','honda']
hp=[100,200,300,400]
value=[1,2,3,4]
car_array=np.array([car_names,hp,value])
print(car_array)
print(car_array.dtype)
print(car_array.shape)
# Accessing element from 2D array.
print(car_array[1])
print(car_array[1][-1])

#Slicing from 1D array
print(cars[1:3])

#Slicing from 1D array
print(car_array[0:2])
print(car_array[0:2,1:3])

# Mean and Median
hp=[100,345,634,140]
hp_array=np.array(hp)
print('mean:', np.mean(hp_array))
print('median:', np.median(hp_array))

# min and max horse power
print('min: ',np.min(hp_array))
print('max: ',np.max(hp_array))

# index of min and max values
print('min: ',np.argmin(hp_array))
print('max: ',np.argmax(hp_array))

# where function
# to find values less than 150

x=np.where(hp_array<150)
print(x)
print(hp_array[x])

