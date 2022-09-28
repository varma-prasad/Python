import pandas as pd


df=pd.read_csv('auto.csv') # read dataset
df.info()
df.dropna(inplace=True) #eliminate rows containing null values
df.info()
# define target and predictors
X=df.iloc[:,1:8]
Y=df.iloc[:,0]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit_transform(X_train)
scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,Y_train)
m=reg.coef_
c=reg.intercept_
Y_pred_train=reg.predict(X_train)
Y_pred_test=reg.predict(X_test)

from sklearn.metrics import r2_score
r2_s=r2_score(Y_train,Y_pred_train)
print(r2_s)
r2_s=r2_score(Y_test,Y_pred_test)
print(r2_s)
