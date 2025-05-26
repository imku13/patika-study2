# 4. Kazada ölen kadınların yaş ortalaması


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
mean_age_dead_women = df_titanic[
    (df_titanic["Survived"] == 0) & (df_titanic["Sex"] == "female")]["Age"].mean()
print("Kazada ölen kadınların yaş ortalaması:", mean_age_dead_women)
