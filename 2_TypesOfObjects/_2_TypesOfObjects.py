

#Python nesne yönelimli bir dildir. Python'da birçok farklı nesne türü vardır. Strings, integers ve floats en yaygın nesne türleridir. 

#Değişken tiplerinin detayları için aşağıdaki documentation inceleyiniz
#https://docs.python.org/3/

# Integer​
11

# Float​
2.14

# String
"Hello, Python 101!"

#Python içerisinde gömülü olarak bulunan "type()" işlevini kullanarak Python'un bir ifade türünü size bildirmesini sağlayabilirsiniz. Python'un tamsayıları int olarak ifade ettiğini, ondalıklı sayıları float olarak  ve karakter yahut metin değerlerini str olarak gördüğünü fark edeceksiniz.

# Type of 12​
type(12)

# Type of 2.14​
type(2.14)

# Type of "Hello, Python 101!"​
type("Hello, Python 101!")

#Bir nesne türünden farklı bir nesne türüne dönüştürme
#Nesnenin türünü Python'da değiştirebilirsiniz; buna typecasting denir. Örneğin, bir tamsayıyı bir float'a dönüştürebilirsiniz (örneğin 2 ila 2.0).

type(2) #Bunun bir tam sayı olduğunu doğrulayın
float(2) #2 bir float'a dönüştür
type(float(2)) #2 tamsayısını bir float'a dönüştürün ve türünü kontrol edin

#Bir tamsayıyı bir float'a dönüştürdüğümüzde, sayının değerini (yani, anlamını) gerçekten değiştirmeyiz. Fakat bazı bilgileri potansiyel olarak kaybedebiliriz. Örneğin, float 1.1'i tamsayıya çevirirsek 1 alırız ve ondalık bilgiyi kaybederiz (ör. 0.1):

# 1.1'i tamsayıya float'a cast etmek bilgi kaybına neden olur
int (1.1)

#Metinsel ifadeleri tamsayılara veya float'a dönüştürme
#Bazen içinde bir sayı içeren bir dize olabilir. Bu durumda, sayıyı temsil eden değeri "int()" kullanarak bir tamsayıya çevirebiliriz:

# Bir metinsel değeri bir tamsayıya dönüştürme
int('1')

#Sayıların metinsel ifadeye dönüştürülmesi
#Metinsel ifadeleri sayılara dönüştürebilirsek, sayıyıları metinsel ifadelere dönüştürebileceğimizi varsaymak doğaldır, değil mi?

# Bir tamsayıyı dönüştürme
str (1)

# Bir float'ı dönüştürme
str (1.2)

#Boole veri türü
#Boolean, Python'da bir başka önemli türdür. Boolean tipi bir nesne iki değerden birini alabilir: Doğru veya Yanlış:

# Değer doğru
True
#True değerinin büyük bir "T" olduğuna dikkat edin. Aynısı False için de geçerlidir (yani "F" büyük harfini kullanmanız gerekir).

# Değer yanlış
False

#Python'dan bir boolean nesnesinin türünü görüntülemesini istediğinizde, boolean anlamına gelen bool gösterilecektir:

# Gerçek Türü
tipi (Doğru)
bool
# Yanlış Tipi

tipi (False)
#Boole nesnelerini diğer veri türlerine yayınlayabiliriz. Eğer bir integer or float True değeri olan bir boolean yaparsak bir tane alırız. Eğer bir integer or float bir False değeri olan bir boolean yaparsak, sıfır alırız. Benzer şekilde, eğer Boolean'a 1 atarsak, True olur. Ve eğer bir Boole'ye 0 atarsak, False oluruz.

# İnt'ı int'a çevir
int(True)
1
# 1'i boolean değerine dönüştür
bool(1)

# 0 değerini boolean değerine dönüştür
bool(0)

#Yüzdürmek için Gerçek Dönüştür
float(True)



