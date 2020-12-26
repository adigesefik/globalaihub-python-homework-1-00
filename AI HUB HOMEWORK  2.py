İsim = input("İsminizi giriniz: ")
Soyisim = input("Soyisiminizi giriniz: ")
Yaş = int(input("Yaşınızı giriniz: "))
Doğum_tarihi = int(input("Doğum tarihinizi giriniz(sadece yıl): "))

if Yaş < 18:
    print("You can't go out because it's too dangerous.")

elif Yaş >= 18:
    print("You can go out to the street.")
