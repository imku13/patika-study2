# 8. 10 yaşından küçüklerin bilet fiyatlarının medyanı


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
median_fare_under_10 = df_titanic[df_titanic["Age"] < 10]["Fare"].median()
print("10 yaşından küçüklerin bilet fiyatı medyanı:", median_fare_under_10)
