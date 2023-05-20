maas = 0
yas = 35

if yas < 18:
    maas = 8000
elif yas < 30:
    maas = 10000
elif yas < 40:
    maas = 12000
else:
    maas = 15000

print(f"merhaba {yas} yaşındasınız ve maaşınız {maas} TL")
