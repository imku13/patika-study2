# 5. Kazadan kurtulanların yaş ortalaması


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
mean_age_survivors = df_titanic[df_titanic["Survived"] == 1]["Age"].mean()
print("Kazadan kurtulanların yaş ortalaması:", mean_age_survivors)
