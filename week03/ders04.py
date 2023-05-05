sinif = ["ayşe", "mehmet", "zeynep", "ali", "fatma", "123", "!123"]
print(sinif)
print(sorted(sinif))
print(sinif)
sinif.reverse()
print(sinif)
uzunluk = len(sinif)
mesaj = f"Sinifimda {uzunluk} adet öğrencim var!"
print(mesaj)
sinif.pop()
uzunluk = len(sinif)
mesaj = f"Sinifimda {uzunluk} adet öğrencim var!"
print(mesaj)
sinif.append('hasan')
print(sinif)
uzunluk = len(sinif)
mesaj = f"Sinifimda {uzunluk} adet öğrencim var!"
print(mesaj)
sonEleman = sinif[uzunluk-1]
mesaj = f"Sınıfımdaki son kişi {sonEleman}"
print(mesaj)


