
#Listeler
#İndeksleme
#Python'daki listeleri inceleyeceğiz. Bir liste, tamsayılar, metinsel ifadeler ve diğer değişkenler saklandığı gibi diğer listeler gibi farklı nesnelerin sıralı bir koleksiyonudur. Bir listedeki her bir öğenin adresine bir index adı verilir. Bir liste içindeki öğelere erişmek ve bunlara atıfta bulunmak için bir index kullanılır.

L = ["Mike Tyson", "June 30", 1966]
print(L)

#Listedeki her elemanı ekrna yazdıralım
print('negatif ve pozitif indeksleme kullanarak aynı element: \ n Pozitif:',L[0],
'\n Negatif:' , L[-3])
print('negatif ve pozitif indeksleme kullanarak aynı element:\n Pozitif:',L[1],
'\n Negatif:' , L[-2])
print('negatif ve pozitif indeksleme kullanarak aynı element:\n Pozitif:',L[2],
'\n Negatif:' , L[-1])

#Listeleri Dilimleme
L[3:5]

#Listeye öğeler eklemek için extend() methodunu kullanın
L = ["Mike Tyson", "June 30", 1966]
L.extend(['Boxer', 53])
L

#Listeye öğeler eklemek için append() kullanın
L = ["Mike Tyson", "June 30", 1966]
L.append(['Boxer', 53])
L

#"append()" ve "extend()" methodlarını kullandıktan sonra elde ettiğin çıktıları mukayese edin. Eğer "extend()" uygularsak listeye iki yeni eleman ekleriz.

#Liste'de index'e göre elemanı değiştirme
A = ["disco", 10, 1.2]
print('Değişiklikten Önce:', A)
A[0] = 'hard rock' # 0. indexte bulunan "disco" elemanı yerine "hard rock" elemanını yerleştiriyoruz
print('Değişiklikten Sonra:', A)

#Liste'de index değerine göre eleman silme
A = ["disco", 10, 1.2]
print('Değişiklikten Önce:', A)
del(A[0]) #"del()" methodu ile 
print('Değişiklikten Sonra:', A)

#Split
#Bir string'i split kullanarak listeye dönüştürebiliriz. Örneğin, split yöntemi, boşlukla ayrılmış her karakter grubunu listedeki bir öğeye çevirir:

'Mike Tyson'.split()# String'i böl, varsayılan boşluk