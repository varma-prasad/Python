import numpy as np
import pandas as pd
car_price_dict={'swift':70000,
                'civic':800000,
                'Altis':180000,
                'Gallardo':300000}
car_price_man={'swift':'maruti',
                'civic':'Honda',
                'Altis':'Honda',
                'Gallardo':'Toyota'}
car_price=pd.Series(car_price_dict)
print(car_price)
car_man=pd.Series(car_price_man)
print(car_man)
cars=pd.DataFrame({'price':car_price,'manufacturer':car_man})
print(cars)
print(cars['price'])
print(cars['manufacturer'])
