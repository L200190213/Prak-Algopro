
Nama ='Calvin Alvito Dinova'
NIM = 'L200190213'
X ='1'+ NIM [7:]
a = int (X)
b = len (Nama)
type (a)
<class 'int'>
>>> #Dikarenakan type a berisi X yang diubah dari string ke integer
>>> type (b)
<class 'int'>
>>> #Type b merupakan int karena merupakan hasil dari len (Nama) yang menghasilkan 20
>>> a/b
60.65
>>> #a berisi 1213 dan b berisi 20 maka jika dibagikan akan bernilai 60.65
>>> a//b
60
>>> #Merupakan hasil bagi dari a dan b tetapi dibulatkan
>>> 10*(a-999)
2140
>>> #a berisi 1213 dikurangi 999 dan dikali 10 maka menghasilkan 2140
>>> b**2
400
>>> #b berisi 20 maka jika dipangkatkan 2 akan bernilai 400
>>> a%b
13
>>> #a berisi 1213 dan b berisi 20 maka jika dibagi mempunyai hasil bagi 13
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #type c merupakan bilangan desimal maka merupakan type data float
>>> a/c
97.04
>>> #a=1213 dan c=12.5 jika dibagi akan menghasilkan 97.04
>>> a//c
97.0
>>> #Merupakan bentuk bulat dari pembagian sebelumnya yaitu 97.04 menjadi 97.0
>>> a%c
0.5
>>> #Merupakan sisa hasil bagi dari a dan c yaitu 0.5
>>> c>b
False
>>> #Salah karena c = 12.5 lebih kecil dari b = 20
>>> type (c > b)
<class 'bool'>
>>> #Dikarenakan yang menjadi output hanya false dan true maka termasuk type data bool
>>> a>b and b > c
True
>>> #Benar karena a lebih besar dari b dan b lebih besar dari a
>>> a> 1100 or b< 10
True
>>> #Benar karena a lebih besar dari 1100 ataupun b lebih besar dari 10
