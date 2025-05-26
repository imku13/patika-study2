# 6. Kazadan kurtulanların bilet fiyatlarının ortalaması


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
mean_fare_survivors = df_titanic[df_titanic["Survived"] == 1]["Fare"].mean()
print("Kazadan kurtulanların bilet fiyatı ortalaması:", mean_fare_survivors)
