import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
# Toplam erkek ve kadın sayısı
total_men = len(df_titanic[df_titanic["Sex"] == "male"])
total_women = len(df_titanic[df_titanic["Sex"] == "female"])

# Ölen erkek ve kadın sayısı
dead_men = len(df_titanic[(df_titanic["Sex"] == "male") & (df_titanic["Survived"] == 0)])
dead_women = len(df_titanic[(df_titanic["Sex"] == "female") & (df_titanic["Survived"] == 0)])

# Oranlar
ratio_men = dead_men / total_men
ratio_women = dead_women / total_women

print(f"Ölen erkek oranı: {ratio_men:.2%}")
print(f"Ölen kadın oranı: {ratio_women:.2%}")
