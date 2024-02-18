import os
class Kutuphane:

    def __init__(self):
        self.ktp_dosyasi = "kitaplar.txt"

        if not os.path.exists(self.ktp_dosyasi):
            with open(self.ktp_dosyasi, "w") as dosya:
                pass
## kitaplar.txt dosyasını oluşturdum.

        self.dosya = open(self.ktp_dosyasi, "a+")

    def __del__(self):
        self.dosya.close()

##class

    def kitap_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(",")
            kitap_adi, yazar, tarih, sayfa_sayisi = kitap_bilgisi
            print("Kitap Adı: {}, Yazar: {}".format(kitap_adi, yazar))

    def kitap_ekle(self, kitap_adi, yazar, tarih, sayfa_sayisi):
        kitap_bilgisi = "{},{},{},{}\n".format(kitap_adi, yazar, tarih, sayfa_sayisi)
        self.dosya.write(kitap_bilgisi)

    def kitap_kaldir(self, kitap_baslik):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        self.dosya.seek(0)
        self.dosya.truncate()

        for kitap in kitaplar:
            if kitap_baslik not in kitap:
                self.dosya.write(kitap)

## Ana program
def program():
    kutuphane = Kutuphane()

    while True:

        from colorama import Fore, Style

        print(Fore.BLUE + "*** MENÜ ***")
        print(Fore.LIGHTYELLOW_EX + "1) Kitapları Listele")
        print(Fore.LIGHTGREEN_EX + "2) Kitap Ekle")
        print(Fore.RED + "3) Kitap Kaldır")
        print(Fore.RED + "4) Çıkış" + Style.RESET_ALL)


        secenek = input("Lütfen bir seçenek girin (1/2/3/4): ")


        if secenek == "1":
            kutuphane.kitap_listele()

        elif secenek == "2":
            kitap_adi = input("Kitap Adı: ")
            yazar = input("Yazar: ")
            tarih = input("Yayın Tarihi: ")
            sayfa_sayisi = input("Sayfa Sayısı: ")
            kutuphane.kitap_ekle(kitap_adi, yazar, tarih, sayfa_sayisi)
            print("*Kitap eklendi...")

        elif secenek == "3":
            kitap_baslik = input("Silmek istediğiniz kitabın adını girin: ")
            kutuphane.kitap_kaldir(kitap_baslik)
            print("*Kitap silindi...")

        elif secenek == "4":
            print("*Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçenek! Lütfen 1, 2, 3 veya 4'ü seçin.")

        devam_et = input(Fore.YELLOW +"**Başka bir işlem yapmak istiyor musunuz? (E/H): ")

        if devam_et.upper() != "E":
            devam_et = False
            print(Fore.LIGHTBLUE_EX +"Çıkış yapılıyor...")
            break

if __name__ == "__main__":
    program()
