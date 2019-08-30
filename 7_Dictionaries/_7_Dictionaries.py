
#Sözlükler
#Sözlükler nedir?
#Sözlük, anahtarlardan ve değerlerden oluşur. Bir sözlüğü bir listeyle karşılaştırmak faydalı olacaktır. Liste gibi sayısal dizinlerin yerine sözlüklerde anahtarlar bulunur. Bu tuşlar sözlükteki değerlere erişmek için kullanılan tuşlardır.

# Sözlüğü oluştur
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, ( 0, 1): 6}
print(dict)

#Not:Anahtaralar string olabilir

# Anahtar ile değere erişim
Dict [ "anahtar1"] #output: 1

#Anahtarlar, tuple gibi değiştirilemez herhangi bir nesne olabilir

# Anahtar ile değere erişim
Dict[(0, 1)] #output: 6 // buradaki kod ilgili değerin anahtarını bize teslim eder. Sözlüğü inceleyiniz...

#Her anahtar, değerinden iki nokta üst üste ":" ile ayrılır. Virgüller öğeleri ayırır ve sözlüğün tamamı kıvrımlı parantez içine alınır. Herhangi bir öğe içermeyen boş bir sözlük, "{}" gibi, sadece iki kaşlı ayraçla yazılmıştır.

# Örnek bir sözlük oluşturun

release_year_dict = {"Gerilim": "1982", "Geri Siyah": "1980","Ayın Karanlık Yüzü": "1973", "Koruma": "1992", "Cehennem Dışı Bat": "1977", "En Büyük Vuruşları (1971-1975)": "1976", "Cumartesi Gecesi Ateşi": "1977", "Söylentiler": "1977"}
print(release_year_dict)

# Sözlükteki tüm anahtarları al
release_year_dict.keys ()

# Sözlükteki tüm değerleri al
release_year_dict.values ()

# Anahtar ile değeri sözlük içine ekle
release_year_dict ['Mezuniyet'] = '2007'
release_year_dict

# Girdileri anahtarla sil
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict