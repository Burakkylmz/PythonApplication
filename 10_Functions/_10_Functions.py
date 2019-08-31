
#Bir fonksiyon, ilgili bir fonksiyonu gerçekleştirmek için kullanılan organize, yeniden kullanılabilir kod bloğudur. Fonksiyonlar, uygulamanız için daha iyi modülerlik ve yüksek derecede kod kullanımı sağlar. Bildiğiniz gibi, Python size print () gibi birçok yerleşik fonksiyon sunar, ancak kendi işlevlerinizi de oluşturabilirsiniz. Bu fonksiyonlara kullanıcı tanımlı fonksiyonlar denir.

liste =[1,2,3,4,5]
type(liste) # yarattığım objenin tipini göreme
liste.insert(5,6) #python2da gömülü olarak bulunan "insert()" methodu ile listemize ilgili değerleri giriyoruz
print(liste)
#output: [1, 2, 3, 4, 5, 6]

liste =[1,2,3,4,5]
liste.append("Python")
print(liste)
#output: [1, 2, 3, 4, 5, 'Python']


liste =[1,2,3,4,5]
liste.pop()# pop() fonksiyonu listede bulunan son elemanı çıkartır
liste
#output:[1, 2, 3, 4]


help(liste.append) # help bize bir methodun ne işe yaradığını söyler
"""
Help Methodunun Output'u
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.
"""
#aşağıda selam adında bir method tanımladık, bu methodun görevi ekrana merhaba yazdırmaktır
def selamla():
    print("Merhaba")
    
selamla() #fonksiyonu çağırdık
#Output:Merhaba
type(selamla)
#Output: Function

#bir method tanımlayıp içerisine isim adında bir parametre gönderiyorum
def isimleSelamlama(isim):
    print("Merhaba", isim)
    
isimleSelamlama("Burak")#methodumuzu çağırdık
#output:Merhaba Burak

def toplama(x,y):
    z = x+y
    print("Sonuc:",z)
    #print("Toplamları: ",x+y)
toplama(2,4)
#output: Sonuc: 6

def faktoriyel(x):
    faktoriyel = 1
    if (x == 0 or x == 1):
        print("Faktoriyel", faktoriyel)
    else:
        while(x>=1):
            faktoriyel *= x
            x -= 1
        print("Faktoriyel", faktoriyel)
        
faktoriyel(5)
#output: Faktoriyel 120

#Fonksiyonalarda Return
#Return: Fonksiyonun işlemi bittikten sonra bize değer döndürmesidir. 
#Böylelikle bize döndürülen değeri bir değişkende depolayabilir ve programların her hangi 
#bir yerinde kullanılabilir.
def carpma(x,y):
    return x*y
​
carpma(2,3)
#output:6

def topla(x,y,z):
    return x+y+z
    print("Sonuc:",x+y+z) # bu kod çalıştırılmaz
​    
topla(2,3,5)
​#output:10

#Return kullanılmayan fonksiyonalra void denir.
#Fonksiyonlarda parametre türleri ve varsayılan parametrelere dikkat ediniz


#def selamla(isim)://#Bu method çalışmayacaktır çünkü parametrenin varsayılan değeri bulunmamaktadır
    #print("Merhaba",isim)
    
#selamla()
​
def selamla(isim = "Burak"):
    print("Merhaba", isim)
    
selamla()
#output:Merhaba Burak


def ogrenciBilgileri(ad = "Bilgi Yok", soyad = "Bilgi Yok", numara = "Bilgi Yok"):
    print("Ad:",ad,"\nSoyad:",soyad, "\nNumara:",numara)
    
ogrenciBilgileri()
"""
output
Ad: Bilgi Yok 
Soyad: Bilgi Yok 
Numara: Bilgi Yok
"""
ogrenciBilgileri("Burak","Yılmaz","B1450.00300")#methodun parametrelerine değerleri burada verdik, outputu inceleyiniz
"""
Ad: Burak 
Soyad: Yılmaz 
Numara: B1450.00300
"""
#sadece öğrenci numarası gösterilecekse
ogrenciBilgileri(numara = "N1450.56550")
"""
Ad: Bilgi Yok 
Soyad: Bilgi Yok 
Numara: N1450.56550
"""

#aralara işaret atma
print("Burak","Yilmaz","B1450.000300",sep="/")
#output:Burak/Yilmaz/B1450.000300
