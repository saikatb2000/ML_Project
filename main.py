import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

df = sns.load_dataset('mpg')
# print(df)

df.isnull().sum()
df.dropna(inplace= True)

X = df[['displacement', 'horsepower', 'weight', 'acceleration']]
Y = df.mpg
X_train, X_test, y_train,y_test = train_test_split(X,Y, test_size=0.15, random_state=42)
print(X_train, X_test, y_train,y_test )

from ctypes import LibraryLoader
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)

model.score(X_test,y_test)

from sklearn.tree import DecisionTreeRegressor
model12 = DecisionTreeRegressor(random_state=0)
model12.fit(X_train,y_train)
model12.score(X_test,y_test)

import pickle
filename = 'mpg_regression.sav'
pickle.dump(model,open(filename,'wb'))

# print(model.predict([[307,130,3504,12]]))

loaded_model = pickle.load(open('mpg_regression.sav','rb'))
loaded_model.score(X_test,y_test)






