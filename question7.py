# 7. Kazadan kurtulan toplam kişi sayısı


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
total_survivors = len(df_titanic[df_titanic["Survived"] == 1])
print("Kazadan kurtulan toplam kişi sayısı:", total_survivors)
