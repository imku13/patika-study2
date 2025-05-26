# 2. Kazada ölenlerin bilet fiyatlarının ortalamasını ve medyanını bulunuz.
# Survived == 0 olanlar kazada ölenlerdir.


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
dead_fares = df_titanic[df_titanic["Survived"] == 0]["Fare"]
mean_fare_dead = dead_fares.mean()
median_fare_dead = dead_fares.median()
print("Kazada ölenlerin bilet fiyatı ortalaması:", mean_fare_dead)
print("Kazada ölenlerin bilet fiyatı medyanı:", median_fare_dead)
