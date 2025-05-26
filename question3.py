# 3. Kazada ölen erkeklerin yaş ortalamasını bulunuz.


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
mean_age_dead_men = df_titanic[(df_titanic["Survived"] == 0) & (df_titanic["Sex"] == "male")]["Age"].mean()
print("Kazada ölen erkeklerin yaş ortalaması:", mean_age_dead_men)
