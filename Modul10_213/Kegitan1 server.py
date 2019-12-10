import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50003))
s.listen(5)
print "Print Komunikasi Tentang Data Diri"
data =''
kamus = {'nama':'Calvin Alvito Dinova',
         'NIM':'L200190213',
         'anggkatan':'19',
         'keluar':'siap',}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        if data.lower() == "keluar":
            s.close()
            break
        print "pertanyaan:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, Perintah tidak dimengerti")
