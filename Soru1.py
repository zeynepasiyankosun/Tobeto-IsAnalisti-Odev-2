#Soru1 - İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngüyü yazınız.

#Fibonacci dizisi, her sayının kendinden önceki ile toplanması sonucu oluşan bir sayı dizisidir.

#İlk önce soruda belirtilen dizinin ilk iki elemanını tnımlayalım.
FbSeri = [1,1]

for i in range(2, 20):
    yeniSayi = FbSeri[i - 1] + FbSeri[i - 2]
    FbSeri.append(yeniSayi) #append, bir Python liste nesnesine yeni bir eleman eklemek için kullanılan bir yöntemdir. 

print(FbSeri)
