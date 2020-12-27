öğrenci_bilgisi = ("Şefik Sapancı")

isim_soyisim = input("isim ve soyisim giriniz: ")
while True:
    if isim_soyisim == öğrenci_bilgisi:
        print("Welcome", öğrenci_bilgisi)
    else:
        print("lütfen bilgileri kontrol edip tekrar giriniz!")
        isim_soyisim = input("isim ve soyisim giriniz: ")
        if isim_soyisim == öğrenci_bilgisi:
            print("Welcome", öğrenci_bilgisi)
        else :
            print("lütfen bilgileri kontrol edip tekrar giriniz!")
            isim_soyisim = input("isim ve soyisim giriniz: ")
            if isim_soyisim == öğrenci_bilgisi:
                print("Welcome", öğrenci_bilgisi)
            else :
                print("Lütfen daha sonra tekrar deneyiniz!!")
            break

if isim_soyisim == öğrenci_bilgisi:

    ders1 = input("ders1'i giriniz: ")
    ders2 = input("ders2'yi giriniz: ")
    ders3 = input("ders3'ü giriniz: ")
    ders4 = input("ders4'ü giriniz: ")
    ders5 = input("ders5'i giriniz: ")

    Dersler = [ders1, ders2, ders3, ders4, ders5]
    print("Tüm dersler: ", Dersler)

    print("""En az 3, en fazla 5 ders alabilirsiniz """)

    ders_sayısı = int(input("Aldığınız ders sayısını giriniz: "))

    if 3 <= ders_sayısı <= 5:
        ders = input("Ders seçiniz: ")
        vize = int(input("vize puanı: "))
        final = int(input("final puanı: "))
        proje = int(input("proje puanı: "))

        ortalama = (vize * 3 / 10) + (final / 2) + (proje / 5)
        puan = round(ortalama)
        if puan > 90:
            print("AA aldınız")
        elif 70 < puan < 90:
            print("BB aldınız")
        elif 50 < puan < 70:
            print("CC aldınız")
        elif 30 < puan < 50:
            print("DD aldınız")
        elif puan < 30:
            print("FF aldınız")
            print("Dersten kaldınız")



    elif ders_sayısı < 3:
        print("You failed in class")
    else:
        print("Yanlış ders sayısı girdiniz lütfen kontrol edip tekrar deneyiniz!!")
