from Tkinter import Tk, Label, Button
from tkMessageBox import showinfo

my_app = Tk(className ="Aplikasi Data Diri")
judul = Label(my_app, text="Data Diri", font = ("Arial",24))
judul.grid(row=0, column= 0, sticky="W")
nama = Label(my_app, text="Nama ")
nama.grid(row= 1, column= 0, sticky="W")
isinama = Label(my_app, text = ":Calvin Alvito Dinova")
isinama.grid(row=1, column= 1, sticky="W")
nim = Label(my_app, text="NIM ")
nim.grid(row= 2, column= 0,sticky="W")
isinim= Label(my_app, text= ":L200190213")
isinim.grid(row= 2, column=1, sticky= "W")
buku = Label(my_app, text = "Buku Favorit ")
buku.grid (row=3, column=0, sticky="W")
isibuku= Label(my_app, text= ":Buku Pelajaran")
isibuku.grid(row=3, column= 1, sticky= "W")
idola = Label(my_app, text= "Idola di Klangan Sahabat")
idola.grid (row= 4, column= 0, sticky="W")
isiidola= Label(my_app, text=":Umar Bin Khattab")
isiidola.grid(row=4, column=1, sticky= "W")
motto= Label(my_app, text="Motto ")
motto.grid (row=5, column= 0, sticky="W")
isimotto = Label(my_app, text=":Menjaga Hati untuk Dia")
isimotto.grid(row= 5, column= 1, sticky="W")
def tutup():
    my_app.quit()
keluar= Button(my_app, text="Quit", command="Quit")
keluar.grid(row=6, column= 1, sticky="W")


my_app.mainloop()
