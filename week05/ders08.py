import math

print("ax^2+bx+c=0")
a = 1
b = 5
c = 4
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"({a})x^2+({b})x+({c})=0")

delta = b**2 - 4 * a * c
print(f"delta={delta}")

if delta < 0:
    print("Denklemin Reel Kökleri Yoktur!")
elif delta > 0:
    print("Denklemin iki kökü vardır:")
    kok1 = (-b + math.sqrt(delta)) / 2 * a
    kok2 = (-b - math.sqrt(delta)) / 2 * a
    print(f"x1 = {kok1}")
    print(f"x2 = {kok2}")
else:
    print("Denklemin tek kökü var!")
    kok = -b / (2 * a)
    print(f"x1,x2 = {kok}")
