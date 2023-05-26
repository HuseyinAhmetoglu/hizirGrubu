karakter1 = {"renk": "sarı", "hız": "orta", "x_ekseni": 0}

ilerleme = 0

if karakter1["hız"] == "yavaş":
    ilerleme = 5
elif karakter1["hız"] == "orta":
    ilerleme = 15
elif karakter1["hız"] == "hızlı":
    ilerleme = 25

print("eski karakter")
print(karakter1)
karakter1["x_ekseni"] = karakter1["x_ekseni"] + ilerleme
print("yeni karakter")
print(karakter1)
