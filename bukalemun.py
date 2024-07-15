import random
malum_liste = ["tas", "kagit", "makas"]
def sistemin_sectigi():
    bilgisayarin_sectigi = random.sample(malum_liste, 1)

def kullanicinin_sectigi():
    kullanici_secimi = input("bir secim yapiniz.")

def oyun():
    while True:
        if bilgisyarin_sectigi == kullanicinin_sectigi:
            print("tebrikler kazandiniz...")
            secim1 = input("tekrar oynamak istermisiniz?")
            if secim1 == "evet":
                continue
            else:
                break
        else:
            print("kaybettiniz...")
            secim2 = input("tekrar oynamak istermisiniz?")
            if secim2 == "evet":
                continue
            else:
                break

oyun()

