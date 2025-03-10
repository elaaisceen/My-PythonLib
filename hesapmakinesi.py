# Kullanıcıdan değer  almak için input fonksiyonu kullanılır.

while True:
    process = input("Hangi matematiksel işlemi yapmak istersiniz: ")
    match process:
        case "+":
            toplamasayisi = int(input("kac tane sayı toplamak istersin: "))
            toplam = 0
            for i in range(toplamasayisi):
                sayi = int(input("sayı giriniz: "))
                toplam = toplam + sayi
            print("Toplam: ", toplam)
        case "-":
            eksiltmesayisi = int(input("kaç tane sayı eksiltmek istersin: "))
            cikartma = 0
            for i in range(eksiltmesayisi):
                sayi = int(input("sayı giriniz: "))
                cikartma = cikartma - sayi
            print("Çıkartma: ", cikartma)
        case "*":
            carpimsayisi = int(input("kaç tane sayı çarpmak istersin: "))
            carpma = 1
            for i in range(carpimsayisi):
                sayi = int(input("sayı giriniz: "))
                carpma = carpma * sayi
            print("Çarpma: ", carpma)       
        case "/":
            bolumsayisi = int(input("kaç tane sayı bölmek istersin: "))
            bolme = 0
            for i in range(bolumsayisi):
                sayi = int(input("sayı giriniz: "))
                bolme = bolme / sayi
            print("Bölme: ", bolme)    
        case _:
            print("Geçersiz işlem")