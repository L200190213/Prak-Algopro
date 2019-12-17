from Tkinter import *
my_app=Tk()
my_app.title("Bagun Ruang Geometri")
judul = Label(my_app,text="Bangun Geometri", font=("Arial", 24))
judul.grid(row=0, column=0, sticky="W")
nama = Label (my_app, text="Nama")
nama.grid(row=1, column=0, sticky="W")

isinama= Label(my_app, text=":Bola")
isinama.grid(row=1, column=1, sticky="W")

dimensi= Label(my_app, text= "Dimensi")
dimensi.grid(row=2, column= 0, sticky="W")

isidimensi= Label(my_app, text= ":3 dimensi")
isidimensi.grid(row=2, column=1, sticky="W")

contohbenda= Label(my_app, text= "Contoh benda")
contohbenda.grid(row=3, column=0, sticky="W")

isicontoh= Label(my_app, text=": Bola Basket")
isicontoh.grid(row=3, column=1, sticky="W")

jari=Label(my_app, text="Jari-Jari")
jari.grid(row=4, column=0, columnspan=3, sticky="W")
angka1=StringVar()
isijari=Entry(my_app,textvariable=angka1)
isijari.grid(row=4, column=1, columnspan=3)
def luas():
    a=float(angka1.get())
    hasil = 4*3.14*a*a
    Hasil.config(text=hasil)
B1 =Button(my_app,text="HitungLuas", command= luas)
B1.grid(row=5, column=3)
Hasil=Label(my_app,text="0")
Hasil.grid(row=5, column=0)
    

my_app.mainloop()
