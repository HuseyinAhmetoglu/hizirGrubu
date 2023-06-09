yas = input("Kaç yaşındasınız? -> ")
yas = int(yas)

if(yas < 0):
    print("Doğru değer girmediniz!")
else:
    print(f"Demek {yas} yaşındasınız :)")
    if(yas < 13): 
        print("Çocuksunuz!")
    elif(yas < 30):
        print("Gençsiniz!")
    elif(yas < 45):
        print("Orta yaşlısınız!")
    elif(yas < 75):
        print("Yaşlısınız!")
    elif(yas < 100):
        print("Çok yaşlısınız!")  
    else:
        print("Mevtasınız!")