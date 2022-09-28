import numpy as np
import pandas as pd
marks_A = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40]}
df1=pd.DataFrame(marks_A,index=['subodh','ram','abdul','john'])
marks_B = {'Chemistry': [72,45,60,98], 
        'Physics': [78,34,72,95]}
df2=pd.DataFrame(marks_B,index=['nandini','zoya','shivam','james'])
df=pd.concat([df1,df2],sort=False)
print(df)
                 
