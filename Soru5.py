#Soru-5 Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.

# Kullanıcıdan bir sayı alınız.
sayi = int(input("Bir sayı girin: "))

print(f"{sayi} sayısının asal çarpanları:")    #f ifadesi, Python'da "f-string" veya "format string" olarak bilinen bir özellikle kullanılır. F-string, metin içinde değişkenleri veya ifadeleri gömülü olarak kullanmanızı sağlar.

bolen = 2
while sayi > 1:
    if sayi % bolen == 0:
        sayi //= bolen
        print(bolen)
    else:
        bolen += 1