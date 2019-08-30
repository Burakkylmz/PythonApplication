
#Durum İfadeleri
#Karşılaştırma Operatörleri
#Karşılaştırma işlemleri bir değeri veya işleneni karşılaştırır ve bir koşula dayanarak bir Boole üretir. İki değeri karşılaştırırken bu operatörleri kullanabilirsiniz:

"""
eşit: ==
eşit değil:! =
şundan büyük:>
şundan az: <
şundan büyük veya eşit:> =
şundan küçük veya ona eşit: <=
"""

# Eşit Koşul :5 değerini "a" değişkenine atayalım. İki değerin eşit olup olmadığını belirlemek için iki eşit "==" işareti ile gösterilen eşitlik operatörünü kullanın. Aşağıdaki örnek, a değişkenini 6 ile karşılaştırır.
a = 5
a == 6 #output: False, Sonuç yanlış çünkü 5 6'ya eşit değil.

i = 6
i > 5 #True


# Eşitsizlik İşareti
i = 2
i != 6 #True

# String'leri karşılaştırmak için Eşitlik işaretini kullanın
"ACDC" == "Mike Tyson" #False

"ACDC" != "Michael Jackson" #True


#If: If durum sorgusu bizlere program içerisinde daha fazla dallanam sağlamaktadır. Dallanma, farklı girdiler için farklı ifadeler çalıştırmamızı sağlar. Bir if ifadesini kilitli bir oda olarak düşünelim, ifade Doğru ise odaya girebiliriz ve programınız önceden tanımlanmış bazı görevleri yerine getirir, ancak ifade Yanlışsa ise program görevi görmezden gelir. Örneğin ehliyet almak istiyen bir kişiyi düşünün, bu durumda kişinin 18 yaşından büyük olması durumunda ehliyet alabilir, değişse ehliyet almak için gerekli başvuruyu gerçekleştiremez.

#If örneği
yaş = 19
if yaş > 18:
    print("Ehliyet başvurusu yapabilirsiniz....!")
else: #Else ifadesi, koşulların hiçbiri else ifadesinden önce Doğru değilse, else altında bulunan kod bloğu çalıştırır.
    print("Ehliyet başvurusu yapamazsınız..!")
###################################
#If-elif-else
age = 18

if age > 18:
    print("you can enter" )
elif age == 18: #eğer ilk durum ifadesi Yanlış ise, ek koşulları kontrol etmemize izin verir. Ve istediğimiz kadar elif yazabiliriz
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

###################################
#And
album_yılı= 1980

if (album_yılı> 1979) and (album_yılı <1990):
    print("Albüm yılı 1980 ile 1989 arasındaydı")
print( "")
print("Sayfalar ..")

#Or
album_yılı = 1990

if (album_yılı <1980) or (album_yılı> 1989):
    print ("1980'lerde albüm yapılmadı")
else:
    print ("Albüm 1980'lerde yapıldı")

#not
album_yılı = 1983

if not(album_yılı == '1984'):
    print("Albüm yılı 1984 değil")

#Klavyeye girilen sayının tek veya çift olup olmadığını öğrenmek için uygulama
sayi = int (input ("Lütfen bir numara yazın:"))

if (sayi% 2 == 0):
    print ("Sayı çift")
else:
    print ("Sayı tek")


# Girilen iki sayının karşılaştırılması (daha büyük veya daha küçük veya eşitlik)

sayi1 = int (input ("Lütfen bir sayı yazın:"))
sayi2 = int (input ("Lütfen bir sayı yazın:"))

if (sayi1 > sayi2):
    print ("{}> {}". formatı (sayi1, sayi2))
elif (sayi1 <sayi2):
    print ("{} <{}". formatı (sayi1, sayi2))
else:
    print ("{} = {}". formatı (sayi1, sayi2))


# Basit not hesaplama
note = float(input("Lütfen not girin: "))

if (note >=90):
    print("AA")
elif (note >= 80):
    print("BB")
elif (note >= 70):
    print("CC")
elif (note >= d0):
    print("DD")
else:
    print("FF")

#Basit hesap makinesi
print("--Menü---")
print("Toplama  --> 1")
print("Çıkarma  --> 2")
print("Çarpma   --> 3")
print("Bölme    --> 4")
print("--------------")

seçim = input("Lütfen menüden bir eylem seçin: ")

a = int(input("Sayı giriniz: "))
b = int(input("Sayi giriniz: "))


if (seçim == "1"):
    print("{} + {} = {}".format(a,b,a+b))
elif (seçim == "2"):
    print("{} - {} = {}".format(a,b,a-b))
elif (seçim == "3"):
    print("{} x {} = {}".format(a,b,a*b))
elif (seçim == "4"):
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Lütfen menüden bir eylem seçin..!")


#İkinci Dereceden Doğrusal Denklemleri Hesapla
a = int(input("Type the first coefficient value  (a): "))
b = int(input("Type the second coefficient value (b): "))
c = int(input("Type the third coefficient value  (c): "))

delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5 / (2 * a))
x2 = (-b + delta ** 0.5 / (2 * a))

print("First root: {}\nSecond root: {}\n".format(x1,x2))

#Basit Login İşlemi
sysUserName = "burak"
sysPassword = "123"

userName = input("Please enter your username")
password = input("Please enter your password")

if (sysUserName == userName and sysPassword == password):
    print("Welcome Major...!")
else:
    print("Your name or password is wrong..!")