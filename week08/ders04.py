kullanicilar = {
    "i_efe": {"ad": "ibrahim", "soyad": "atmaca", "lokasyon": "erzurum"},
    "h_2323": {"ad": "hüseyin", "soyad": "ahmetoğlu", "lokasyon": "mardin"},
    "nur_sena": {"ad": "nursena", "soyad": "kolikoğlu", "lokasyon": "ankara"},
}

for kullanici_adi, bilgiler in kullanicilar.items():
    print(f"Kullanıcı adı: {kullanici_adi}")
    tam_ad = f"{bilgiler['ad'].title()} {bilgiler['soyad'].upper()}"
    print(f"Tam ad: {tam_ad}")
    konum = bilgiler["lokasyon"].title()
    print(f"Konum: {konum}")
    print("-------------------------")
