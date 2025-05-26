# 9. 1., 2. ve 3. sınıf bilet fiyatlarının ortalama ve medyanlarını karşılaştırınız.
#(Pclass değişkeni bilet sınıfını gösteriyor.)
#Açıklama: Pclass == 1, 2, 3 → 1., 2. ve 3. sınıf yolcular.


import pandas as pd


df_titanic = pd.read_csv('Titanic_dataset.csv')
for cls in [1, 2, 3]:
    avg = df_titanic[df_titanic["Pclass"] == cls]["Fare"].mean()
    med = df_titanic[df_titanic["Pclass"] == cls]["Fare"].median()
    print(f"{cls}. sınıf - Ortalama: {avg:.2f}, Medyan: {med:.2f}")
