import numpy as np
import pandas as pd
# from single series object
car_price_dict={'swift':70000,
                'civic':800000,
                'Altis':180000,
                'Gallardo':300000}
car_price=pd.Series(car_price_dict)
print(car_price)
print(pd.DataFrame(car_price,columns=['car price']))

#from list of dictionaries

data=[{'name':'varma','marks':98},
      {'name':'vishwa','marks':90},
       {'name':'venu','marks':100},
        {'name':'bhagya','marks':90}]
print(pd.DataFrame(data))

print(pd.DataFrame([{'subodh':20,'ram':23},
                    {'abdul':28,'john':25}],
                   index=['maths','physics']))
