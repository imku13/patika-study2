#1.Kazada ölenlerin yaş ortalamasını bulunuz.


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
mean_age_dead = df_titanic[df_titanic["Survived"] == 0]["Age"].mean()
print("Kazada ölenlerin yaş ortalaması:", mean_age_dead)
