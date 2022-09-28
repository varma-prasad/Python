import numpy as ny
import pandas as pd
marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)

marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
print(marks_df)

marks_df.drop(columns = 'Total', inplace = True)
print(marks_df)
