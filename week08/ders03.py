sinif1 = {"şube": "A", "liste": ["ali", "ayşe", "mehmet"]}
sinif2 = {"şube": "B", "liste": ["ahmet", "kerem", "fatma"]}
sinif3 = {"şube": "C", "liste": ["veli", "hasan", "hüseyin"]}

siniflar = [sinif1, sinif2, sinif3]
isimler = []

for sinif in siniflar:
    for isim in sinif["liste"]:
        isimler.append(isim)

for isim in isimler:
    print(f"Selam {isim.title()}")
