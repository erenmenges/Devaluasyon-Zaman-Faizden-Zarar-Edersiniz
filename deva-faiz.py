para = 100000
faizilk = int(input("Faiz oranını girin (nokta veya virgül koymayın ve 4 basamaklı girin [örn:%11,25 --> 1125]):"))
dolar_kuru = float(input("Dolar kurunu girin:"))
places = 4
faiz = faizilk * (10 ** (-1 * places))
faizlipara = para + (para * faiz)
dolargelecek = dolar_kuru
while (faizlipara/dolargelecek) >= (para/dolar_kuru):
    dolargelecek += 0.01
print("Eğer 1 sene sonra dolar kuru ", dolargelecek, " olursa zarar edersiniz.")