import numpy as np
import pandas as pd
marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)

f=marks_df<33
print(marks_df.mask(f,'Fail'))

print(marks_df.sort_values(by ='Physics'))
print(marks_df.sort_values(['Physics','English'],ascending = (1,0)))

print(marks_df.apply(np.sum,axis=0))
print(marks_df.apply(np.sum,axis=1))
print(marks_df.apply(np.mean,axis=0,result_type= 'broadcast'))
