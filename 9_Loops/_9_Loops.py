

#LOOPS

#Range

#Bazen, belirli bir işlemi birçok kez tekrarlamak isteyebilirsiniz. Bunun gibi tekrarlanan işlemler döngüler tarafından gerçekleştirilir. İki tür döngüye bakacağız, loops ve while sırasında.

#Döngülere geçmeden önce "range" nesnesini tartışalım. Range nesnesini sıralı bir liste olarak düşünmek yararlı olur. Şimdilik en basit duruma bakalım. 0'dan 2'ye sıralanan üç öğeyi içeren bir dizi üretmek istiyorsak, aşağıdaki komutu kullanırız:

range(3)

range(0,20) #başlangıç ve bitiş değerlerin belirtilerek 

print(*range(0,20))
#output:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

print(*range(15)) #başlangıç değeri vermedik sadece bitiş değeri
#output:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

print(*range(1,100,2)) #2şer adımlarla ekrana basacak
#output: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

print(*range(20,0,-2))
#output: 20 18 16 14 12 10 8 6 4 2

"""
in operatörü: 'in' operatörü bir değerin bir sırada olup olmadığını kontrol etmek için kullanılır. Belirtilen dizide bir değişken bulursa, aksi takdirde false olarak değerlendirir.

not in operatörü- Belirtilen dizide bir değişken bulamazsa, aksi takdirde false olursa true olarak değerlendirilir.
"""

5 in [1,2,3,4] #output: False, çünkü liste 5'şi içermemektedir

2 in [1,2,3] #output: True

"t" in "Tesla" # False

"elo" in "elon musk" #True

not 4 in (1,2,3) # true

#For Loop nedir?

#For döngüsü bir kod bloğunu birden çok kez çalıştırmanızı sağlar. Örneğin, listedeki her öğeyi yazdırmak istiyorsanız bunu kullanırsınız.

#Liste tarihlerinde verilen tüm yılları yazdırmak için bir for döngüsü kullanalım:
dates = [1982,1980,1973]
N = len(dates) #listenin uzunluğunu "N" değişkenine atadık

for i in range(N):#For listenin uzunluğu kadar dönecek
    print(dates[i])
    

#Listedeki Sayıları Bastırma
print("printing numbers in a list")
listOfNumber = [0,1,2,3,4,5,6,7,8,9]
for item in listOfNumber:
    print(item)

# Bir dizinin tüm elemanlarının toplamının hesaplanması
print("calculating the sum of all elements of an array")
sum = 0
listOfNumber = [0,1,2,3,4,5,6,7,8,9]
for item in listOfNumber:
    sum = sum + item
print(sum)