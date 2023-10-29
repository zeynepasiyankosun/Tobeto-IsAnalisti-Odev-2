#Soru-3 Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

# Kullanıcıdan iki sayıyı isteyin.
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

# İki sayının kopyalarını oluşturunuz. (Sayıların kopyalarını oluşturmak, aslında EBOB ve EKOK hesaplamasında kullanılan değişkenleri korumak için yapılır.)
x = sayi1
y = sayi2

# EBOB hesaplama
while x != y:
    if x > y:
        x -= y
    else:
        y -= x

ebob = x

# EKOK hesaplama
ekok = (sayi1 * sayi2) // ebob

# Sonuçların yazdırılması
print(f"{sayi1} ve {sayi2} için EBOB: {ebob}")
print(f"{sayi1} ve {sayi2} için EKOK: {ekok}")
