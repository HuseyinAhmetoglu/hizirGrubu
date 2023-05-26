diller = {
    "ali": "c",
    "ayşe": "python",
    "mehmet": "java",
    "fatma": "go",
    "hasan": "python",
}

for isim, dil in diller.items():
    print(f"{isim.title()}, {dil.upper()} kullanıyor.")

print("--------------------")
print("Kullandığımız diller..")
for dil in diller.values():
    print(dil.upper())
print("--------------------")   
print("Kullandığımız diller..")
for dil in set(diller.values()):
    print(dil.upper())