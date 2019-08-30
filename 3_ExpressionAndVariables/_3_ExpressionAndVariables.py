
#İfade(Expressions)
#Python'daki ifadeler, uyumlu tipler arasındaki işlemleri içerebilir (örneğin, tam sayılar ve değişkenler). Örneğin, birden fazla sayı eklemek gibi temel aritmetik işlemler:

#Toplama İşlemi
43+60+16+41

#Çıkarma İşlemi
50 - 60

#Çarpma
5 * 5

#Bölme
25 / 5
25 / 6


#Python, matematiksel ifadeleri değerlendirirken işlem önceliğini takip eder. Aşağıdaki örnekte Python, çarpımın sonucuna 30 ekler.
30 + 2 * 60 #Output:150

(30 + 2) * 60 #Output:1920, işlem önceliği parantez içindeki işlemde olduğu için sonuç farklı çıktı

#Değişkenler
#Çoğu programlama dilinde olduğu gibi, değerleri değişkenlerde saklayabiliriz, böylece daha sonra kullanabiliriz.
x = 43 + 60 + 16 + 41 # Değeri değişkene sakla, toplama işleminin sonucunu "x" değişkenine atadık(assignment).
print(x) # toplama işleminin sonucunu ekrana bastık
y = x / 60 # toplama işleminin sonucunu 60 bölerek elde edilen sonucu "y" değişkenine atadık
print(y) 


# Python'da yeni değer önceden yaratılmış değişkenin üzerine yazılabilir
x = x / 60
print(x)

toplam = 43 + 42 + 57
print(toplma)
type(toplam) #yarattığımız "toplam"  değişkeninin tipine bakalım

toplam_saat = (43 + 42 + 57) / 60
print(toplam_saat)

