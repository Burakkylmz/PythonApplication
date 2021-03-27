# Object Oriented Programming (Nesne Yönelimli Programlama)

# MIT OpenCourseWare
# 6.0001 Introduction to Computer Science and Programming in Python
# https://www.youtube.com/watch?v=nykOeWgQcHM&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA

# OOP bize kendi objelerimizi yani nesnelerimizi tanımlamaa imkanı veren, bu yarattığımız objelere özellikler ve yetenekler kazandırma şansı veren bir yapıdır. 
# Bu tanımlamarı sınıf (class) olarak isimlendirdiğimiz ifadelerle gerçekleştiriyoruz.

# Object Oriented Programmig Prensipleri
# 1. Inheritance
# 2. Encapsulation
# 3. Abstraction
# 4. Polymorphsim
# 5. Constructer

# Class (Sınıf) Nedir?
# Sınıf Python içerisinde oluşturduğumuz kendi objelermizin prototiplerdir. Objelerin kendi karakteristik özellikleri sınıf içerisinde oluşturucağımız değişkenler 
# ve veri üyeleri sayesinde tanımlanabilir. Class ile oluşturduğumuz objelerin tüm davranışları fonksiyon ile tanımlanır.

# Bir sınıf tanımlarken "class" anahtar sözlüğü ile başlıyoruz. İlgili sınıfa proje içeriisndeki görevi ve yapacağı iş doğruştusunda anlamlı bir isim veririr. 
# Class isimleri Python'da kullanılan best practice dediğimiz kabu görmüş yapıalra uymak gerekir.

# Class (Sınıf) Tanımlama
# class class_adı:
    # alacağı yada barındıracağı özellik ve davranışları yazıyoruz

class myFirstClass:
    pass

# "pass" anahtar sözcüğü ile yaratılan sınıfın içeriğinin daha sonra dolduruşacağını derleyiciye bildiriyoruz. Bu anahtar sözcüğü kullanmasaydık hata alırdır. 
# Burada bu sınıf ile şuanlık herhangi bir iş yapmayacağımı belirtiyorum. Bu anahtar kelime methot içinde kullanılabilinir. Sınıfa hemen özellik ve yetenek yüklenecekse 
# pass kullanmanın bir anlamı bulunmamaktadır.

# Sınıf adı, standart Ptyhon değişkeni adlandırma kurullarına (bir harf veya alt çizgi ile başlanmalı ve yanlızca harfler, altçizgiler veya sayılar içermelidir) 
# uyulmalıdır. Ayrıca Python stil rehberi için PEP 8 diye internette aratştırma yapabilirsiniz.

# https://www.python.org/dev/peps/pep-0008/ => PEP 8 -- Style Guide for Python Code

# Pythonda sınıfların camelCase gösterimi kullanılarak adlandırılması önerilir.

# Python'da bütün sınıflar "object" sınıfından kalıtım alır. Python 3 ile object yazmaya gerek kalamadı.
class employee(object):
    """
        Bu satır class dokümantasyonudur. Class ile ilgili bilgileri barındırır.
        Bu sınıf (class) çalışan bilgilerini içerir.
    """
    # Yarattığımız sıfımıza özellikler (property) kazandıralım
    firstName = ""
    lasName = ""
    departmant = ""
    # Yukarıda sınıfımıza 3 tane özellik kazandırdır.

# Yaratılan sınıfın kullanımı
# Yaratılan sınıfın kullanımı için, ilgili sınıfın "örneklemi (instance)" alınır.
# Instance (Örneklem) => Örneklem alma yada örneklem çıkarma olarak isimlendirilen bu işlem, yarattığımız sınıfın özelliklerine ve yetneklerine sahip nesneler 
# üretmemize olanak sağlar. Bu bu işlemi istediğimiz kadar yapabiliriz.

calisan_1 = employee() # instance aldık.Bu yöntem ile istediğimiz kadar çalışan üretebiliriz.
calisan_1.firstName = "Burak"
calisan_1.lasName = "Yılmaz"
calisan_1.departmant = "Zalım & Gecelerin Yargıcı"

# Yukarıda nesne isimi + "." operatörü ile ilgili sınıfın nesneye atanmış özelliklerine eriştik ve onlara ihtiyacımız olan değerleri atadık.

# Ödev => Instance alındığında, alınan bu örneklem RAM'in hangi alanına çıkartııyor. Neden? Ayrıca normal int, string, dictionary yarattığımızdan bu nesneler 
# RAM'in neresine çıkartılıyor? Neden RAM'ın "STACK & HEAP" alanları var?

print(
    "Çalışan Bilgileri\nAdı: {}\nSoyadı: {}\nDepartmanı: {}\n".format(
        calisan_1.firstName, calisan_1.lasName, calisan_1.departmant
    )
)

calisan_2 = employee()
calisan_2.firstName = "Halil"
calisan_2.lasName = "İbo"
calisan_2.departmant = "Playboy"

print(
    "Çalışan Bilgileri\nAdı: {}\nSoyadı:{}\nDepartmanı: {}\n".format(calisan_2.firstName,calisan_2.lasName,calisan_2.departmant)
)

# "dir()" fonksiyonu ile belirtilen nesnenin tüm özelliklerine ve yeteneklerine atanmış değerleri olamadan döndürür. Bu işlev tüm özellikleri, 
# yetenekleri ve yerleşik olarak nesne üzerinde bulunan metotları döner.
print(dir(employee))

# Class'a iat bazı özellikleri görmek için aşağıdaki ifadeleri kullanabilirsiniz:
# __dict__ => TÜm class namespaclerini teslim eder.
# __doc__ => TÜm class dökümantasyonunu teslim eder.
# __name__ => Class isimini teslim eder.

print("__dict__ Attribute => {}".format(employee.__dict__))
print("__doc__ Attribute => {}".format(employee.__doc__))
print("_name__ Attribute => {}".format(employee.__name__))

class boxer():
    firstName = ""
    lastName = ""
    born = ""
    alias = ""
    division = ""
    aggressivness = ""
    weight = ""
    height = ""
    totalFight = ""
    wins = ""
    losess = ""

boxer_1 = boxer()
boxer_1.firstName = input("First Name:")
boxer_1.lastName = input("Last Name: ")
boxer_1.born = input("Birth Date: ")
boxer_1.alias = input("Alias: ")
boxer_1.division = input("Division: ")
boxer_1.aggressivness = input("Aggressivness: ")
boxer_1.weight = input("Weight: ")
boxer_1.height = input("Height: ")
boxer_1.totalFight = input("Total Fight: ")
boxer_1.wins = input("Wins: ")
boxer_1.losess = input("Losess: ")

print(boxer_1.firstName, " - ", boxer_1.lastName)

# dir() Methodu
#Aşağıda Araba isimli bir class yaratıyorum ve bu class'a üç tane özellik (property) veriyorum ayrınca özelliklere varsayılan değerler atıyorum
class Araba():
    model= "Ford Ranger"
    renk = "Black"
    motor = 100

araba1 = Araba() #Araba sınıfından araba1 isimli bir instance(örneklem) aldım.

araba1.model# araba1 örnekleminin model bilgisini ekrana yazdım
'Ford Ranger'

#dir() fonksiyonu ile belirtilen nesnenin tüm özelliklerini ve yöntemlerini, değerleri olmadan döndürür. Bu işlev tüm özellikleri ve yöntemleri, tüm nesneler için varsayılan 
# olan yerleşik özellikleri bile döndürür.
dir(Araba)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'model',
 'motor',
 'renk']


import math

class point():
    """
        2 boyutlu düzlemde geometrik alanların mesafesini ölçen sınıf
    """
    # Diğer örneklerde olduğu gibi sınıfa özellikleri ataamdık.
    #x = ""
    #y = ""
    def move(self, x, y):
        """
            Bu methot dışarıdan alınan değerleri class içerisindeki property'lere atar.
            Niteliklere verilen argümanları bağlama özelliğine sahiptir.
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        """
            Koordinatları sıfırlayacak methot
        :return:
        """
        self.move(0,0)

    def calucateDistance(self, otherPoint):
        """
            Kullanıcıdan alınan değer bağlamında mesafa hesaplayacak method
        :param otherPoint:
        :return:
        """
        return math.sqrt(
            (self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2
        )

point_1 = point()
point_2 = point()

point_1.reset()
point_2.move(5,0)
print(point_2.calucateDistance(point_1))


# Self Nedir?
# Self sınıfın örneğini temsil eder. Self anahtar sözcüğünu kullanarak sınıfın özeniteliklerine ve yöntemlerine erişebiliriz. Niteliklere verilen argümanlara bağlar. 
# Self "C" ve onun türevi alan "C++ & C#" gibi dillerde "this" anahtar sözcüğüne denk gelir.Yani "self" bulunduğu class'ı işaret eder. Örneğimizi incelediğimizde 
# "self" anahtar sözcüğünün method'a dışarıdan gelen değerleri elde edereki sınıfın ilgili özelliklerine atadı. Bu ana kadar yapmış olduğumuz örneklerde sınıfların 
# özelliklerini elle yarattık. Bu örnekte bu yöntemi tercih etmedik. Bunun nedeni self anatar sözcüğünün sınıf niteliklerini ve yeteneklerin işaret edebilme yetenğidir. 
 # Yani dışarıdan gelen değeri alıp, sınıf için bir "x" ve "y" özelliği yarattı ve bu özelliklerin içerisine değerleri atadı.

# Python'da method'lar instance alma aşamasında otomatik olarak gönderilir ancak otomatik olarak başaltılamazlar. Bu yüzden "instancename" "+" "." operatörü ile 
# çağrılmak zorundadırlar. Aslında bu bizim için bir problemdir. Geliştirm yaparken bu çağırma durumunu gözden kaçırırsak bütün işlem çöker. Bu bağlamda construter 
# methotlar devreye girer ve sınıf örneklemi alındığında kendileri otomatik olarak atama işlemlerini yerine getitir.

assert(point_2.calucateDistance(point_1) == point_1.calucateDistance(point_2))
# assert() => Python'da eğer cümleciği, bir durum test eden bir hata ayıklama yardımcısıdır. Koşul doğruysa hiç birşey yapmaz, lakin koşul tutmazsa "false" değer 
# döndürür ve "AssetionError" istisnai durumu oluşur.

# __init__() => Yapıcı method. Tüm sınıflarda obje oluşturmak içn kullanılır. "C" tabanlı dillerde "Constructor" olarak isimlendirilir. Bu yapı sınıf türetilirken 
# yani instance alınırken nesneye bağlı değil, sınıf kendisine atrama yapmak için kullanılır. Sınıfın örneklemi alındığında yani sınıf başlatıldığında "__ini__" 
# kendisi otomatik olarak çalışır. Bir başka değişle bu yöntem bir sınıftan nesne oluşturduğumuzda çağrılır ve sınıfın niteliklerini başlatılmasına (initilazition) izin verir.

# "__init__()" nesnenin durumunu başlatmak için kullanılır. Yapıcı methot olarak adlandırılan bu yapının görevi bir sınıfın nesnesi oluşturulduğunda sınıfın öznitelikleirni 
# (attributte) yani sınıfın veri üyelerini başlatmak onlara dışarıdan gelen değerleri atamktıdr. Bir sınıf nesnesi somutlaştırıldığında yani sınıf instance'si alındığında 
# __init__ otomatik olarak çalışır.

# aşağıda yaratılan sınıf "object" sınıfından miras almaktadır. Python 3 den sonra bunu belirtmemize gerek kalmadı.
class student:
    def __init__(self, studetId, firstName, lastName):
        self.studentId = studetId
        self.firstName = firstName
        self.lastName = lastName


ogrenci_1 = student(
     input("Öğrenci No: "),
     input("Adı: "),
     input("Soaydı: ")
)

print(
     "Öğrenci Bilgileri\nNo: {}\nAdı: {}\nSoyadı: {}"
         .format(ogrenci_1.studentId, ogrenci_1.firstName, ogrenci_1.lastName)
)

# Örnek
class Employee:
    departmant = "Yazılım" # member
    elemanSayisi = 0 # member

    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        Employee.elemanSayisi += 1

    def showEmployeeCount(self):
        print(f"Toplam Eleman Sayisi: {Employee.elemanSayisi}")

    def showInformationEmployee(self):
        print(f"Ad: {self.Name}\nYaş: {self.Age}\nDepartmant: {self.departmant}")

calisan_1 = Employee("Oguz", "32")
calisan_1.departmant = "Muhassebe"
calisan_1.showInformationEmployee()
calisan_1.showEmployeeCount()

calisan_2 = Employee(
    input("Adınız: "),
    input("Yaş: ")
)
calisan_2.departmant = "ARGE"
calisan_2.showInformationEmployee()
calisan_2.showEmployeeCount()

# Örnek

class SoftwareDeveloper:
    def __init__(self, firstname, lastname, language):
        self.firstName = firstname
        self.lastName = lastname
        self.language = language


    def showInformation(self):
        print("""
        Information of Software Developer
        =================================
        First Name: {}
        Last Name: {}
        Language: {}
        """.format(self.firstName, self.lastName, self.language))

    def addNewLanguage(self, newLanguage):
        print("Processing...!")
        print("New language added..!")
        self.language.append(newLanguage)

developer = SoftwareDeveloper("Burak", "Yılmaz", ["Python","RPA"])
developer.addNewLanguage(
    input("Please type into new language skill: ")
)
developer.showInformation()

# Örnek

class Character:
    def __init__(self, name="", race="", role="", level=0, weapon=0, armour=0, hp=100):
        self.isim = name
        self.meslek = role
        self.irk = race
        self.level = level
        self.silah = weapon
        self.zirh = armour
        self.can = hp

    def Saldir(self):
        return  self.silah + self.level

    def Korun(self):
        return self.zirh + self.level

    def Kac(self):
        print("Savaştan kaçtı..!")


oyuncu = Character("Raider","Savaşçı","Viking",5,20,5)
dusman = Character("Kara Murat","Silahşör","Turk",10,10,0)

while True:
    sonuc = input("Saldırmak için s'ye, kaçmak için k'ye basabilirsiniz..!")

    if sonuc == "s":
        dusman.can -= oyuncu.Saldir() - dusman.Korun()
        oyuncu.can -= dusman.Saldir() - oyuncu.Korun()

        print(f"Verdiğin hasar: {oyuncu.Saldir()-dusman.Korun()}")
        print(f"Aldığın hasar: {dusman.Saldir() - oyuncu.Korun()}")
        print("---------------------------------------")
        print(f"Oyuncu Can: {oyuncu.can}")
        print(f"Düşman Can: {dusman.can}")
    elif sonuc == "k":
        oyuncu.Kac()
        break

    if (dusman.can <=0 and oyuncu.can > 0):
        print("Oyuncu kaznadı..!")
        break
    elif (dusman.can > 0 and oyuncu.can <= 0):
        print("Düşman kazandı..!")
        break
    elif (dusman.can <= 0 and oyuncu.can <= 0 ):
        print("Bu dünya kimseye kalmaz. Savaşma seviş..!")
        break

#Inheritance(Kalıtım)
# Programlama dünyasında, yinelenne kod kötü olarak kabul edilir. Farklı yerlerde aynı ve benzer kodların birden fazla kopyası olmamalıdır. Benzer işlevselliğe 
# sahip kod parçacıklarını ve nesneleri birleştirmenin birçok yolu vardır. Bu yollardan bir taneside kalıtımdır. Kalıtım, bir sınıfın özelliklerini başka bir 
# sınıfa aktarmasıdır. Yazılım dünyasındaki kalıtım ile biyolojideki kalıtım aynı mantıkta çalışmaktadır. Biyoloji de kalıtım yoluyla DNA aktarımı yapılırken 
# yazılımda kalıtım aracılığı ile bir class'ın sahip olduğu özellikler ve yetenekler aktarılır. Yazılım dillerinde kalıtım veren sınıflara "Parent Class or 
# Base Class" denir. Kalıtım alan sınıflara ise "Child Class" denir.

# Python'da yaratılan bütün sınıflar "object" sınıfından kalıtım alır. Bu sınıf veri ve davranışlar açısından çok az şey sağlar ancak tüm nesnelere aynı 
# şekilde davranmasını temin eder.

class Person(object): # Python'da her sınıf "object" sınıfından kalıtım alır. Python 3'den sonra yaratılan sınıflarda bunu belirtmeye gerek kalmamıştır.
    def __init__(self, name):
        self.Name = name

    def getName(self):
        return  self.Name

    def isEmployee(self):
        return False

class Employee(Person): # Employee sınıfını Person sınıfı ile extend ettik. Yani Employee sınıfı Person sınıfından kalıtım vasıtasıyla özellik ve yetenekler kazandı.
    def isEmployee(self):
        return True

emp = Person("Burak")
print(f"Adı: {emp.getName()}\nÇalışan Mı: {emp.isEmployee()}")

emp_1 = Employee("İpek")
print(f"Adı: {emp_1.getName()}\nÇalışan Mı: {emp_1.isEmployee()}")

# Örnek
# Bir kişinin adını ve e-posta adresinin takip eden bir kişi yönetim sistemi. Kişin adını ve e-posta bilgisini saklama yeteneği olsun. Supplier sınfı yaratın. 
# Siparişi ilgi kişiye gönderildiğine dair bilgi versi.

class Contact:
    allContact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.allContact.append(self)


class Supplier(Contact):
    def Order(self, order):
        print(f"we would send {order} order to {self.name}")

c = Contact("Some body","somebody@mail.com")
s = Supplier("Burak Yılmaz", "burak@mail.com")
s.Order(
    input("Plase type into a your order id: ")

# Örnek
# Python'da gömülü olarak bulunan bir nesneyi (lsit, tuple, disctionary vb) generic bir sınıfa kalıtım vasıtasıyla özelleikleri kazandırılabilir.
class ContanctList(list):

    def Search(self,name):
        matchingContact= []
        for item in self:
            if name in item.name:
                matchingContact.append(item)
        return matchingContact


class Contact:
    allContact = ContanctList()
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.allContact.append(self)

c1 = Contact("İpek Yılmaz", "ipek@mail.com")
c2 = Contact("Burak Yılmaz", "burakyilmaz@mail.com")
c3 = Contact("Hakan Yılmaz", "hakan@mail.com")

print([c.name for c in Contact.allContact.Search(
    input("Lütfen aratmak istediğiniz ismi giriniz: ")
)])

# Örnek
# Employee sınıfı yaratın. Bu sınıfın FirstName, LastName, Salary, Departmant member'ları olsun. Show information yeteneği olsun. HumanResource sınıfı yaratın departman 
# bilgisi değiştirme yeteneği olsun. Manager sınıfı yaratın maaş zammı yapma yeteneği olsun

class Employee:
    def __init__(self, firstName, lastName, salary, departmant):
        self.FirstName = firstName
        self.LastName = lastName
        self.Salary = salary
        self.Departmant = departmant

    def showInformation(self):
        print("""
        Employee Informarition
        ======================
        First Name: {}
        Last Name: {}
        Salary: {}
        Departmant: {}
        """.format(self.FirstName, self.LastName, self.Salary, self.Departmant))

class HumanResource(Employee):
    def changeDepartmant(self, newDepartmant):
        self.Departmant = newDepartmant

class Manager(Employee):
    def additionalSalary(self, amount):
        self.Salary += amount

calisan = Employee("Burak","Yılmaz",1000, "ARGE")
ik = HumanResource("İpek","Yılmaz",1000,"IK")
yonetici = Manager("Hakan","Yılmaz",1000,"SuperVisor")
yonetici.additionalSalary(
    int(input("Miktar: "))
)
yonetici.showInformation()


# Method Override
# Parent Sınıfta bulunan bir metodun alt sınfılarda farklı yetenekler kazandırılmasına method oveerride diyoruz.

class Employee:
    def __init__(self, employeeNo, name, salary, departmantNo):
        self.EmployeeNo = employeeNo
        self.Name = name
        self.Salary = salary
        self.DepartmantNo = departmantNo

    def showEmployee(self):
        print("Employee: {}\nEmployee Name: {}\nSalary: {}\nDepartmant: {}\n".format(self.EmployeeNo, self.Name, self.Salary, self.DepartmantNo))

class Saleman(Employee):
    def __init__(self, employeeNo, name, salary, departmantNo, commison):
        self.Commision = commison
        super().__init__(employeeNo, name, salary, departmantNo)

    def showEmployee(self):
        super().showEmployee()
        print("Commision: {}".format(self.Commision))

saleman_1 = Saleman(1, "Burak", 1000, 2, 0.10)
saleman_1.showEmployee()
    
    
# Multiple Inheritance
# Java ve C# çoklu kalıtımı sıcak bakmaz. BU dillerde çoklu kalıtım yapmak için interface'ler kullanılır. Lakin C++ ve python çoklu kalıtımı direk deseklemektedir. 
# Çoklu Kalıtım bir child class birden fazla parent class'tan kalıtım almasına çoklu kalıtım diyoruz.

class BaseClass: # grand parant
    num_base_calls=0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls +=1

class LeftSubClass(BaseClass): # parent
    num_left_class = 0
    def call_me(self):
        print("Calling method on Left sub class")
        self.num_left_class += 1

class RightSubClass(BaseClass): # parent
    num_right_class = 0
    def call_me(self):
        print("Calling method on right sub class")
        self.num_right_class += 1

class SubClass(LeftSubClass, RightSubClass): # grand child
    num_sub_calls = 0
    def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("Calling method Subclass")
        self.num_sub_calls += 1

altsınıf = SubClass()
altsınıf.call_me()
    
# Örnek
# Base class => name member, getName yeteneği
# Child class => name ve age members, getAge yeteneği
# GrandChild=> name, age address members, getAddress yeteği

class Base:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address

g = GrandChild("Burak", 31, "Bakırköy")
print(
    g.getName(),
    g.getAge(),
    g.address()
    
  
# Encapsulation
# Veri gizleme için kullanılan bir yapıdır. Herhangi bir sınıfın üyelerine (member) erişimi kısıtlamak için kullanıyoruz.

class Product:
    def __init__(self):
        self.__ProductID = ""
        self.__ProductName = ""
        self.__Price = ""

    def setProduct(self, productId, productName, price):
        self.__ProductID = productId
        self.__ProductName = productName
        self.__Price = price

    def showProduct(self):
        print(f"Product Id: {self.__ProductID}\nProduct Name: {self.__ProductName}\nPrice: {self.__Price}")

boxingGloves = Product()
boxingGloves.setProduct("1910 Everlast", "Elite Laced", 139.99)
boxingGloves.showProduct()

# Not: Product sınıfımızı başlattığımızda (initilazition) normal şartlar altında sınıfımızın üyelerine erişebilir ve onlara değer atayabiliyorduk. 
# Lakin bu senryoda "boxingGloves"+"." dediğimizde sınıfımızın üyelerine erişemedik, bunun nedeni bu üyeleri erişime kapatmamız yani encapsualion etmemizdir.

print(dir(boxingGloves))
# Not: dir() metodu ile sınıfın üyelerini ve özelliklerini çıktı aldığımızda fark etmişsinizdir, encapsualtion edilmiş üyeler "_Product__Price'" halini almıştır. 
# Artık "_Product__Price'" üzerinden erişebilir.
print(boxingGloves._Product__Price)
print(boxingGloves.__Price) # Erişme kapalı olduğu için erişemedik

# Access Modifiers ||Access Control
# Nesne yönelimli programlama dilelrinde hepsinde erişim belirteçleri mevcuttur.Sınıf içerisinde tasarımsal olarak yani mimarisel açıdan bazı üylere ve yeteneklere 
# erişimin açık olaması yada kapalı olması gerekebilir.

# Java & C ve Türevi dillerde Access Modifiers
# 1.Private: Yanlızca bulunduğu sınıf içerisinde erişilebilir
# 2.Protected: Yanlzıca sınıf ve alt sınıflardan erililebilir
# 3.Public: Proje içerisinde herhangi bir yerden erişilebilir

# Python access modifier kullanmaz. Access modifier yerine best practice diyebileceğimiz guiedlessyapıları destekler. Teknik olarak bir sınıftaki tüm üyeler ve 
# özenitelikler herkese açıktır. Eğer bir metodun ne işe yaradığınız belirtmek istersek docstring yardımıyla bu bilgileri paylaşabiliriz.

# Best Practice of Access Modifiers
# Ornek-1. Kural olarak bir üye yada methodun tek alt çizgi ("_" || underscore) karakteri ile tanımlanması.
# Python developerları tarafından bu özelliğin (_variableName) yada methodun class içerisinde kullanılması gerektiği anlaşılır.

class A:
    # üye önünde tek alt çizgi olduğu için bu üyenin sadece sınıf içerisnde kullanması gerektiğini anlıyor.
    _x = ""

    # aynı durum aşağdaki method içende geçerlidir.
    def _getListofIvırZıvır(self):
        pass

class B:
    # aşağıdaki üyeler önünde herhangi bir "_" işareti olmadığından bunun public olduğu ve herherde kullanabileceğimi anlıyor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Ornek-2. Class dışarsından bir özelliği yada methpoda erişilmemesini istediğimiz durumda "__" (double underscore) kullanılmaktadır.

class SecretString:
    _x = ""
    sezarcrypto = ""
    def __init__(self, plainString, passPhase):
        '''
            Bilgiyi gizlemek için güvenli olmayan yol
        '''
        self.__plainString = plainString
        self.__passPhase = passPhase

    def decrypt(self, passPhase):
        '''
            String değeri sadece passPahe doğru ies bize teslim edilecek
        '''
        if passPhase == self.__passPhase:
            return self.__plainString
        else:
            return ''

gizliBilgi = SecretString("Acme: Top Secret","antwerp")
print(gizliBilgi.decrypt(
    input("Enter the key: ")
))

print(dir(gizliBilgi))
print(gizliBilgi._SecretString__plainString)

    
# Simple Payment Example
    
import datetime
import calendar

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, ratePerDay):
        super().__init__(id, name)
        self.ratePerDay = ratePerDay

    def calculatePayroll(self):
        today = datetime.datetime.now()
        totalDays = calendar.monthrange(today.year, today.month)[1]
        return self.ratePerDay * totalDays

class PartTimeEmployee(Employee):
    def __init__(self, id, name, totolHours, ratePerHour):
        super().__init__(id, name)
        self.totalHours = totolHours
        self.ratePerHour = ratePerHour

    def calculatePayroll(self):
        return self.totalHours * self.ratePerHour

class CommisionEmployee(SalaryEmployee):
    def __init__(self, id, name, ratePerDay, commission):
        super().__init__(id, name, ratePerDay)
        self.commission = commission

    def calculatePayroll(self):
        salary = super().calculatePayroll()
        return salary + self.commission
    
class PayrollManagerSystem:
    def calculatePayroll(self, employees):
        print("Payroll Management System")
        print("=========================")

        for employee in employees:
            print(f"Employee Id: {employee.id}\nEmployee Name: {employee.name}")
            print(f"Amount: {employee.calculatePayroll()}")
            print("___________________")
 
import managersystem
import employee

semp = employee.SalaryEmployee(1, "Ozan", 1000)
pemp = employee.PartTimeEmployee(2, "Halil", 40, 50)
cemp = employee.CommisionEmployee(3, "Ali", 1000, 1500)

payroll_system = managersystem.PayrollManagerSystem()
payroll_system.calculatePayroll([semp, pemp, cemp])   
   

    
#OOP - Sınıf içinde method tanımlama
class SoftwareDeveloper():
    def __init__(self,firstName,lastName,language):
        self.firstName = firstName
        self.lastName = lastName
        self.language = language
    def ShowInformation(self):
        print("""
        Information of Software Developer
        
        First Name : {}
        
        Last Name : {}
        
        Language : {}
        """.format(self.firstName,self.lastName,self.language))

developer = SoftwareDeveloper("Burak","Yılmaz",["C#","Python","C++"])
developer.ShowInformation()

class SoftwareDeveloper():
    def __init__(self,firstName,lastName,language):
        self.firstName = firstName
        self.lastName = lastName
        self.language = language
        
    def ShowInformation(self):
        print("""
        Information of Software Developer
        
        First Name : {}
        
        Last Name : {}
        
        Language : {}
        """.format(self.firstName,self.lastName,self.language))
        
    def AddLanguage(self,newLanguage):
        print("New language is added.....!")
        self.language.append(newLanguage)
developer = SoftwareDeveloper("Burak","Yılmaz",["C#","Python","C++"])
developer.AddLanguage("JavaScirpt")

#Inheritance(Kalıtım)
class Employee():
    def __init__(self,firstName,lastName,salary,departmant):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.departmant = departmant
        
    def ShowInformation(self):
        print("First Name: {}\nLast Name: {}\nSalary: {}\nDepartmant: {}\n" .format(self.firstName,self.lastName,self.salary,self.departmant))
        
    def ChangeDepartmant(self,newDepartmant):
        self.departmant = newDepartmant

class Manager(Employee):#manager class'ı Employee class'ından kalıtım alıyor
    pass # bir yapıyı daha sonra tanımlayacaksanız bu deyimi kullanbilirsiniz

manager = Manager("Burak","Yılmaz",10.000,"ARGE")
manager.ShowInformation()

manager.ChangeDepartmant("IT")
manager.ShowInformation()

class Manager(Employee):
    def AdditionSalary(self,ammount):
        self.salary += ammount
manager = Manager("Can","Oğuz",15.000,"CEO")
manager.AdditionSalary(10.000)
manager.ShowInformation()

#Overriding
class Manager(Employee):
    def __init__(self,firstName,lastName,salary,departmant,personInDepartmant):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.departmant = departmant
        self.personInDepartmant = personInDepartmant
        
    def ShowInformation(self):
        print("First Name: {}\nLast Name: {}\nSalary: {}\nDepartmant: {}\nNumber of Person In Departmant: {}" .format(self.firstName,self.lastName,self.salary,self.departmant,self.personInDepartmant))
    
    def AdditionSalary(self,ammount):
        self.salary += ammount

manager = Manager("İpek","Yılmaz",10.000,"Sale",20)
manager.ShowInformation()

class Employee():
    def __init__(self,firstName,lastName,salary,departmant):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.departmant = departmant
        
    def ShowInformation(self):
        print("First Name: {}\nLast Name: {}\nSalary: {}\nDepartmant: {}\n" .format(self.firstName,self.lastName,self.salary,self.departmant))
        
    def ChangeDepartmant(self,newDepartmant):
        self.departmant = newDepartmant

class Manager(Employee):
    def __init__(self,firstName,lastName,salary,departmant,personInDepartmant):
        
        super().__init__(firstName,lastName,salary,departmant)
        
        self.personInDepartmant = personInDepartmant
        
    def ShowInformation(self):
        print("First Name: {}\nLast Name: {}\nSalary: {}\nDepartmant: {}\nNumber of Person In Departmant: {}" .format(self.firstName,self.lastName,self.salary,self.departmant,self.personInDepartmant))
    
    def AdditionSalary(self,ammount):
        self.salary += ammount
manager = Manager("Burak","Yılmaz",3000,"IT",5)
manager.ShowInformation()

