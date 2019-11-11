Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Calvin Alvito Dinova'
>>> NIM = 213
>>> Tinggi = 1.71
>>> Berat = 60
>>> Tahunlahir = 2001
>>> Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
>>> Data = [Tahunlahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena Aku merupakan deretan objek dan ditulis dengan tanda kurung maka disebut type data tuple
>>> Aku[0]
2001
>>> #Memanggil data ke 0 di data Aku maka akan keluar Tahunlahir ya itu 2001
>>> a = NIM % 4; Aku[a]
60
>>> #Karena 213 % 4 menghasilkan 1 maka menunjukan pada berat badan
>>> type(Aku[a])
<class 'int'>
>>> #Karena a merupakan berat badan maka termasuk type data int
>>> Aku[ a:4 ]
(60, 1.71, 213)
>>> #Perintah diatas memnggil data Aku ke a sampai 4 yaitu Berat, Tinggi dan NIM
>>> type(Aku[4])
<class 'str'>
>>> #Karena berisi tulisan dan diawal dan akhir diberi tanda petik
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #Error dikarenakan elemen tuple tidak dapat diubah
>>> type(Data)
<class 'list'>
>>> #Termasuk type data list dikarenakan terdapat tanda kurung siku
>>> type(Data[4])
<class 'str'>
>>> #Dikarenakan diawali dan diakhiri dengan tanda petik
>>> Data[4][5]
'n'
>>> #Menunjukan data ke 5 dari Nama
>>> Data[4][a:6]
'alvin'
>>> #Karena a dimulai dari a sampai data ke 6 yaitu n
>>> Data[0] = 'oke'; Data
['oke', 60, 1.71, 213, 'Calvin Alvito Dinova']
>>> #Data ke 0 diubah yaitu tahun lahir diganti dengan str 'oke'
>>> Data[-a]
'Calvin Alvito Dinova'
>>> #Karena memanggil elemen paling akhir
>>> range(a)
range(0, 1)
>>> #Karena menunjukan dari nol sampai 'a'
