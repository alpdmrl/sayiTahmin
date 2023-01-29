
import random
sayi = random.randint(1,100)
tahminSayi = 0
hak = 5
while hak > 0:
    tahminSayi += 1
    hak -= 1
    tahmin = int(input("0 ile 100 arasında bir sayı giriniz:\n"))
    if tahmin == sayi:
        print("Tebrikler sayıyı",tahminSayi,"tahminde buldunuz")
        break
    elif hak == 0:
        print("Haklarınız bitti.Sayı= ", sayi)
        break
    elif tahmin < sayi:
        if (sayi - tahmin) < 5:
            print("Çok yaklaştınız. Sayıyı çok az yükseltin. \nKalan hakkınız ", hak , "\n---------")
        elif (sayi - tahmin) < 10:
            print("Yaklaştınız. Sayıyı az yükseltin. \nKalan hakkınız", hak , "\n---------")
        elif (sayi - tahmin) < 99:
            print("Sayıyı yükseltin.\nKalan hakkınız", hak , "\n---------")
    elif tahmin > sayi :
        if (tahmin - sayi) < 5:
            print("Çok yaklaştınız. Sayıyı çok az düşürün.\nKalan hakkınız", hak , "\n---------")
        elif (tahmin - sayi) < 10:
            print("Yaklaştınız. Sayıyı az düşürün. \nKalan hakkınız", hak, "\n---------")
        elif (tahmin - sayi) < 99:
            print("Sayıyı düşürün.\nKalan hakkınız", hak , "\n---------")
