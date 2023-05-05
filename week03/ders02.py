sinif = ["ali", "mehmet", "ayşe", "fatma"]
print(sinif)
sinif[0] = "hüseyin"
print(sinif)
sinif.append("ali")
print(sinif)

sinif = []
print(sinif)
sinif.append("ali")
sinif.append("mehmet")
sinif.append("ayşe")
sinif.append("fatma")
sinif.append("hüseyin")
print(sinif)

sinif.insert(3, "zeynep")
print(sinif)

del sinif[4]
print(sinif)

ogrenci = sinif.pop()
print(ogrenci)
print(sinif)

ogrenci = sinif.pop(1)
print(ogrenci)
print(sinif)

sinif.remove("ayşe")
print(sinif)

silinmesi_gereken = 'ali'
sinif.remove(silinmesi_gereken)
print(sinif)


# sinif.remove('hasan')
# print(sinif)
