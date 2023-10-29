#Soru-4 Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

# Asal sayılar, sadece iki pozitif tam sayı böleni olan, kendisine ve 1 sayısına kalansız bölünebilen, 1'den büyük sayma sayılarıdır.

# Kullanıcıdan bir sayı alınız.
sayi = int(input("Bir sayı giriniz: "))

if sayi > 1:
    # 2'den başlayarak sayının kareköküne kadar olan tüm sayıları kontrol etmeliyiz.
    for i in range(2, int(sayi ** 0.5) + 1):
        if (sayi % i) == 0:
            print(sayi, "asal bir sayı değildir.")
            break               #break ifadesi, Python'da bir döngüden çıkmak veya döngüyü sonlandırmak için kullanılan bir kontrol ifadesidir. 
    else:
        print(sayi, "asal bir sayıdır.")
else:
    print(sayi, "asal bir sayı değildir.")