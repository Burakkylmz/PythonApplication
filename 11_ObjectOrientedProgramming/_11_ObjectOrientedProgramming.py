
#Sınıflara ve Nesnelere Giriş
#Bir Sınıf Yaratmak

#Aşağıda Araba isimli bir class yaratıyorum ve bu class'a üç tane özellik (property) veriyorum ayrınca özelliklere varsayılan değerler atıyorum
class Araba():
    model= "Ford Ranger"
    renk = "Black"
    motor = 100

araba1 = Araba() #Araba sınıfından araba1 isimli bir instance(örneklem) aldım.
araba2= Araba()

araba1.model# araba1 örnekleminin model bilgisini ekrana yazdım
'Ford Ranger'
araba2.model
'Ford Ranger'

#dir() fonksiyonu ile belirtilen nesnenin tüm özelliklerini ve yöntemlerini, değerleri olmadan döndürür. Bu işlev tüm özellikleri ve yöntemleri, tüm nesneler için varsayılan olan yerleşik özellikleri bile döndürür.
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

"""
__init__, bir sınıfın yapıcısıdır(constructor). Self parametresi, nesnenin örneğini belirtir. X ve y parametreleriniz yığındaki değişkenlerde saklanır ve init yöntemi kapsam dışına çıktığında atılır.
"""
class Student():
    def __init__(self,studentId,firstName,lastName):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
student1 = Student("B1450.03300","Burak","Yılmaz")
student2 = Student("B1278.04445","Can","Oğuz")

student1.firstName
'Burak'
student2.firstName
'Can'

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


