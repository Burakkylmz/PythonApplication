#Hangi Python sürümünü kullanıyoruz?

#Günümüzde kullanılmakta olan Python programlama dilinin iki popüler sürümü vardır: Python 2 ve Python 3. Python topluluğu Python 2'den Python 3'e geçmeye karar verdi ve birçok popüler kütüphane Python 2'yi artık desteklemeyeceklerini açıkladı.

import sys
print(sys.version)

#Not: sys, kullanılan Python sürümü de dahil olmak üzere sisteme özgü birçok parametre ve işlevi içeren yerleşik bir modüldür. 

#Python'da "Merhaba Dünya" 
#Yeni bir programlama dili öğrenirken, "merhaba dünya" örneği ile başlamak gelenekseldir. Bu kadar basit bir kod satırı, çıktıda bir dizenin nasıl yazdırılacağını ve çıktı alma fokssiyonunu size göstermektedir.

print('Hello, Python!')

#İki Satıra Merhaba Dünya Deyin
#Merhaba ve Dünya'yı iki ayrı satıra yazdıralım. İpucu: Dizenin ortasındaki "\n", yeni bir satır karakteri gibi davranır. Örneğin. yazdırma ("satır 1 \nsatır 2")

print('Hello Python World..!\nThis world is mine..!')

""""
Python'da yorum yazmak

Kod yazmanın yanı sıra, kodunuza yorum eklemenin her zaman iyi bir fikir olduğunu unutmayın. Başkalarının neyi başarmaya çalıştığınızı anlamalarına yardımcı olacaktır (verilen bir kod parçasını yazmanızın nedeni). Bu sadece diğer kişilerin kodunuzu anlamalarına yardımcı olmakla kalmaz, haftalar veya aylar sonra tekrar size geldiğinde size hatırlatma görevi de görür.

Python'da yorum yazmak için, yorumunuzu yazmadan önce "#" sayı sembolünü kullanın. Kodunuzu çalıştırdığınızda, Python verilen satırdaki "#" işaretinden sonraki her şeyi yok sayar.
"""
