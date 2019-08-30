

#Tuples(Demetler)
#Python'da farklı veri türleri vardır: string, integer ve float. Bu veri türlerinin tümü demetler içeriisnde saklanabilir.

tuple1 = ("burak",10,1.2 ) # demeti burada yaratıyoruz ve faklı tiplerdeki değişkenleri sakladığını görebilrisiniz
print(tuple1) # output: tuple
type(tuple1) #output: tuple

#İndeksleme
#Bir dizinin her bir öğesine bir dizin üzerinden erişilebilir. Her eleman, demet adıyla ve ardından indeks numarasına sahip bir köşeli ayraçla elde edilebilir:

tuple1 = ("burak",10,1.2 )
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Son elemanın değerini almak için negatif indeksi kullanın
tuple1 [-1]

#Demetleri birleştirme
# "+" işareti ile demetleri birleştirebilir yada onları karıştırabiliriz
tuple2 = tuple1 + ("hard rock", 10) # tuple1'e ilgili elemanları ekledik ve sonucu tuple2'ye atadık
print(tuple2)

#Dilimleme
#Demetleri dilimleyerek, ilgili elementlerle yeni tekiller elde edebiliriz:

# 0 dizininden 2 dizinine dilim
tuple2 [0: 3]

#Demetin son iki elementini elde edebiliriz:
#Dizin 3'ten dizin 4'e dilim
tuple2 [3: 5]

#Length komutunu kullanarak bir tuple uzunluğunu elde edebiliriz:
len(tuple2) #len() işlevi ile demet içeriisnde bulunan eleman sayısı bize teslim edilir

#Sıralama
#Aşağıdaki grubu göz önünde bulundurun:

# Örnek bir demet
Derecelendirmeler = (0, 9, 6, 5, 10, 8, 9, 6, 2)

#Değerleri bir diziye sıralayabilir ve yeni bir diziye kaydedebiliriz:

# Grubu sırala
Derecelendirmeler_Sıralandı = sorted(Derecelendirmeler)
print(Derecelendirmeler_Sıralandı)

