print("""**********
      2 HARFLİ ANLAMLI  KELİME BULMA OYUNU
KURALLAR:
    1- 2 HARFTEN OLUŞAN ANLAMLI BİR KELİME BULMANIZ GEREKİYOR.
    2- EĞER İLK GİRDİĞİNİZ HARF KELİMEDE YOKSA 2 HAKKA DAHA SAHİP OLUYORSUNUZ.
    3- EĞER BİR HARFİ DOĞRU BİLDİĞİNİZ TAKTİRDE TOPLAMDA 1 YANLIŞ HAKKINIZ BULUNUR.
    4- PROGRAM SONLANDIĞINDA TEBRİKLER MESAJI ALMAZ İSENİZ KAYBETMİŞ OLUYORSUNUZ.
**********""")

name = input("Lütfen isminizi giriniz: ")
print("Hoşgeldin", name)













Kelimeler = {"ak", "at", "ot", "al", "ak", "on", "ok", "an", "az", "er", "eş","aş","ön","aç","ev","öz","üç"}
liste = list(Kelimeler)
while True:
    Harf_giriniz = input("Bir harf giriniz: ")
    if Harf_giriniz == liste[0][0]:
        print("İlk harfi:", Harf_giriniz)
        Harf_giriniz1 = input("Bir harf giriniz.: ")
        if Harf_giriniz1 != liste[0][1]:
            Harf_giriniz4 = input("Bir harf giriniz.: ")
            if Harf_giriniz4 == liste[0][1]:
                print("ikinci harfi:", Harf_giriniz4, "Sonuç: ", Harf_giriniz, Harf_giriniz4)
                print("Tebrikler: ",name)
                break
            elif Harf_giriniz4 != liste[0][0]:
                break

        if Harf_giriniz1 == liste[0][1]:
            print("ikinci harfi:", Harf_giriniz1, "Sonuç: ", Harf_giriniz, Harf_giriniz1)
            print("Tebrikler:",name)
            break
    if Harf_giriniz == liste[0][1]:
        print("İkinci harfi:", Harf_giriniz)
        Harf_giriniz2 = input("Bir harf giriniz: ")
        if Harf_giriniz2 != liste[0][0]:
            Harf_giriniz3 = input("Bir harf giriniz.: ")
            if Harf_giriniz3 == liste[0][0]:
                print("ikinci harfi:", Harf_giriniz3, "Sonuç: ", Harf_giriniz3, Harf_giriniz)
                print("Tebrikler:",name)
                break
            elif Harf_giriniz3 != liste[0][0]:
                break

        elif Harf_giriniz2 == liste[0][0]:
            print("ikinci harfi:", Harf_giriniz2, "Sonuç: ", Harf_giriniz2, Harf_giriniz)
            print("Tebrikler:",name)
            break

    elif Harf_giriniz != liste[0][0] and Harf_giriniz != liste[0][1]:
        Harf_giriniz = input("Bir harf giriniz: ")
        if Harf_giriniz == liste[0][0]:
            print("İlk harfi:", Harf_giriniz)
            Harf_giriniz1 = input("Bir harf giriniz.: ")
            if Harf_giriniz1 != liste[0][1]:
                Harf_giriniz4 = input("Bir harf giriniz.: ")
                if Harf_giriniz4 == liste[0][1]:
                    print("ikinci harfi:", Harf_giriniz4, "Sonuç: ", Harf_giriniz, Harf_giriniz4)
                    print("Tebrikler:",name)
                    break
                elif Harf_giriniz4 != liste[0][0]:
                    break

            if Harf_giriniz1 == liste[0][1]:
                print("ikinci harfi:", Harf_giriniz1, "Sonuç: ", Harf_giriniz, Harf_giriniz1)
                print("Tebrikler:",name)
                break
        if Harf_giriniz == liste[0][1]:
            print("İkinci harfi:", Harf_giriniz)
            Harf_giriniz2 = input("Bir harf giriniz: ")
            if Harf_giriniz2 != liste[0][0]:
                Harf_giriniz3 = input("Bir harf giriniz: ")
                if Harf_giriniz3 == liste[0][0]:
                    print("ikinci harfi:", Harf_giriniz3, "Sonuç: ", Harf_giriniz3, Harf_giriniz)
                    print("Tebrikler:",name)
                    break
                elif Harf_giriniz3 != liste[0][0]:
                    break

            elif Harf_giriniz2 == liste[0][0]:
                print("ikinci harfi:", Harf_giriniz2, "Sonuç: ", Harf_giriniz2, Harf_giriniz)
                print("Tebrikler:",name)
                break
        else:
            Harf_giriniz = input("Bir harf giriniz: ")
            if Harf_giriniz == liste[0][0]:
                print("İlk harfi:", Harf_giriniz)
                Harf_giriniz1 = input("Bir harf giriniz: ")
                if Harf_giriniz1 != liste[0][1]:
                    Harf_giriniz4 = input("Bir harf giriniz: ")
                    if Harf_giriniz4 == liste[0][1]:
                        print("ikinci harfi:", Harf_giriniz4, "Sonuç: ", Harf_giriniz, Harf_giriniz4)
                        print("Tebrikler:",name)
                        break
                    elif Harf_giriniz4 != liste[0][0]:
                        break

                if Harf_giriniz1 == liste[0][1]:
                    print("ikinci harfi:", Harf_giriniz1, "Sonuç: ", Harf_giriniz, Harf_giriniz1)
                    print("Tebrikler:",name)
                    break
            if Harf_giriniz == liste[0][1]:
                print("İkinci harfi:", Harf_giriniz)
                Harf_giriniz2 = input("Bir harf giriniz: ")
                if Harf_giriniz2 != liste[0][0]:
                    Harf_giriniz3 = input("Bir harf giriniz: ")
                    if Harf_giriniz3 == liste[0][0]:
                        print("ikinci harfi:", Harf_giriniz3, "Sonuç: ", Harf_giriniz3, Harf_giriniz)
                        print("Tebrikler:",name)
                        break
                    elif Harf_giriniz3 != liste[0][0]:
                        break

                elif Harf_giriniz2 == liste[0][0]:
                    print("ikinci harfi:", Harf_giriniz2, "Sonuç: ", Harf_giriniz2, Harf_giriniz)
                    print("Tebrikler:",name)
                    break


    break