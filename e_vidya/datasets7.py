# merge vs concat
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Jyoti', 'Sapna', 'Raj', 'Ramaswamy'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(pd.concat([df1,df2],sort=False))
print(pd.merge(df1,df2))

