
#Setler
#Bir set Python'da benzersiz bir nesne koleksiyonudur. Bir kümeyi bir küme paranteziyle "{}" belirtebilirsiniz. Python, yinelenen öğeleri otomatik olarak kaldırır:

set1 = {"Muhammed Ali", "Mike Tyson", "Lennox Lewis", "Evander Hollyfield", "Mike Tyson", "Mike Tyson", "Muhammed Ali"}
print(set1)

#Bir list'i set'e dönüştürme
boxer_list = ["Muhammed Ali", "Mike Tyson", "Lennox Lewis", "Evander Hollyfield"]
boxer_set = set(boxer_list)
print(boxer_set)

#Set'e eleman ekleme
boxer_set.add("Rocky Marciano")
print(boxer_set)

#Set'ten öğre kaldırma
boxer_set.remove("Rocky Marciano")
print(boxer_set)

#Set'lerde Mantık Operatörleri
#Setlerle, simetrik farkın, kesişimin ve birleşimin yanı sıra setler arasındaki farkı da kontrol edebilirsiniz.
boxer_set1 = set(["Muhammed Ali", "Mike Tyson", "Lennox Lewis", "Evander Hollyfield"])
boxer_set2 = set(["Rocky Marciano","Joe Louis","Mike Tyson","Muhammed Ali"])

#Her iki set'tede "Mike Tyson" ve "Muhammed Ali" bulunmaktadır, bu durum her iki setin kesişimi olarak temsile dilmektedir.

#Kesişimleri Bulma
intersection = boxer_set1 & boxer_set2
print(intersection)

# Set1 ve Set2'de ki farkları bulma
boxer_set1.difference(boxer_set2)# difference methodu her iki set'te ki farklı olan elemanları bize vermektedir.

#Not: Yalnızca boxer_set1'deki öğeleri göz önünde bulundurmanız gerekir; boxer_set2'deki tüm öğeler, kesişme dahil edilmemiştir.

#Set'leri Birleştirme
boxer_set1.union(boxer_set2) #union() methodu ile her iki set'teki farklı elemanlar alınmaktadır

