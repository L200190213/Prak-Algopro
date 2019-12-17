from Tkinter import *



kalkulator=Tk(className="Membuat Kalkulator Sederhana")
wk = Label(kalkulator, text="Angka1")
wk.grid(row=0, column=0)
angka1= StringVar()
isi= Entry(kalkulator, textvariable= angka1)
isi.grid(row=0, column=1, columnspan= 3)
wkwk = Label(kalkulator, text="Angka2")
wkwk.grid(row=1, column=0)
angka2= StringVar()
isi2= Entry(kalkulator, textvariable= angka2)
isi2.grid(row=1, column=1, columnspan= 3)

def tambah():
    a = float(angka1.get())
    b = float(angka2.get())
    hasil = a+b
    Hasil.config(text=hasil)
B1 =Button(kalkulator,text="+", command= tambah)
B1.grid(row=2, column=0)
def kurang():
    a = float(angka1.get())
    b = float(angka2.get())
    hasil = a-b
    Hasil.config(text=hasil)
B2 =Button(kalkulator,text="-", command= kurang)
B2.grid(row=2, column=1)
def kali():
    a = float(angka1.get())
    b = float(angka2.get())
    hasil = a*b
    Hasil.config(text=hasil)
B3 =Button(kalkulator,text="*", command= kali)
B3.grid(row=2, column=2)
def bagi():
    a = float(angka1.get())
    b = float(angka2.get())
    hasil = a/b
    Hasil.config(text=hasil)
B4 =Button(kalkulator,text=":", command= bagi)
B4.grid(row=2, column=3)
B5 = Button(kalkulator, text="Hasil")
B5.grid(row=2, column=4)
LabelHasil= Label(kalkulator, text= "Hasil")
LabelHasil.grid(row=3, column=0)
Hasil=Label(kalkulator,text="0")
Hasil.grid(row=3, column=3)

kalkulator.mainloop()
