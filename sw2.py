secim = int(input("sinema için 1 tiyatro için 2 giriniz:"))
yas = int(input("yaşınız:"))
while secim == 1:

        if yas < 18 :
            print("tutar=7.5 tl")
        elif yas > 18 :
            print("tutarınız=15 tl")
        else:
            print("lütfen geçerli bir değer giriniz.")
        break
while secim == 2:

            if yas < 18:
                print("tutar=5 tl")
            elif yas > 18:
                print("tutarınız=10 tl")
            else:
                print("lütfen geçerli bir değer giriniz.")
            break
