oyuncular = []

for oyuncu_no in range(15):
    yeni_oyuncu = {"oyuncu_no": oyuncu_no, "renk": "yeşil", "puan": 5, "hız": "yavaş"}
    oyuncular.append(yeni_oyuncu)
print("-----------------------------------------------")
for oyuncu in oyuncular:
    print(oyuncu)

print(f"Toplam oyuncu sayısı: {len(oyuncular)}")

print("-----------------------------------------------")

for oyuncu in oyuncular[:5]:
    oyuncu["renk"] = "Sarı"
    oyuncu["puan"] = 10
    oyuncu["hız"] = "orta"

for oyuncu in oyuncular:
    print(oyuncu)

print(f"Toplam oyuncu sayısı: {len(oyuncular)}")

print("-----------------------------------------------")

for oyuncu in oyuncular[5:10]:
    oyuncu["renk"] = "Mavi"
    oyuncu["puan"] = 15
    oyuncu["hız"] = "hızlı"

for oyuncu in oyuncular:
    print(oyuncu)

print(f"Toplam oyuncu sayısı: {len(oyuncular)}")

print("-----------------------------------------------")

for oyuncu in oyuncular:
    if oyuncu["renk"] == "yeşil":
        oyuncu["puan"] = 0


for oyuncu in oyuncular:
    print(oyuncu)

print(f"Toplam oyuncu sayısı: {len(oyuncular)}")
