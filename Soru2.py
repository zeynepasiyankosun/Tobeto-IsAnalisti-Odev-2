#Soru-2 Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız. 

#Bir sayı, kendisi hariç bölenlerinin toplamı kendisine eşitse mükemmel bir sayıdır.

sayi = int(input("Bir Sayı Giriniz: "))
toplam = 0

for i in range(1, sayi):   #ifadesi, 1'den sayıya kadar olan tüm pozitif tam sayılar için bir döngü oluşturur.
    if sayi % i == 0:      #ifadesi, döngü içinde mevcut değerin sayi'ya tam olarak bölünüp bölünmediğini kontrol eder. Eğer bölen ise, o zaman bu, sayının bir bölenidir.
        toplam += i        #ifadesi, bu böleni toplam adlı bir değişken üzerine ekler. Bu, sayının bölenlerinin toplamını hesaplar.

if toplam == sayi:
    print(sayi, "Mükemmel Bir Sayıdır.")
else:
    print(sayi, "Mükemmel Bir Sayı Değildir.")