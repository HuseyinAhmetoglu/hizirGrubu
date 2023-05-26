malzeme_envanteri = ["mantar", "zeytin", "mısır", "sarımsak", "soğan", "peynir"]

siparis = ["mantar", "peynir", "tavuk", "sarımsak", "domates"]

for malzeme in siparis:
    if malzeme in malzeme_envanteri:
        print(f"{malzeme} pizzanıza eklendi")
    else:
        print(f"Üzgünüz elimizde hiç {malzeme} kalmadı :(")
print("Siparişiniz tamamlandı! :)")
