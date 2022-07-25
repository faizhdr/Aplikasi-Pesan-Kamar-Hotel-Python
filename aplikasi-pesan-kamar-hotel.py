import random
import os
from datetime import datetime

os.system('cls')

while True:
    now = datetime.now()
    time = now.strftime("%B %d, %Y | %H:%M:%S")
    header = """
\t------------------------------------
\t|               HOTEL              |
\t|             ~SYARIAH~            |
\t------------------------------------
    """
    print(header)

    print()
    input("\t~~TEKAN ENTER UNTUK MELANJUTKAN~~")
    print()
    
    namaSaya = input("\tMasukkan Nama lengkap : ")
    print()


    print("\t\t----------------")
    print("\t\t| 1. Laki-laki |")
    print("\t\t| 2. Perempuan |")
    print("\t\t----------------")

    opsiGender = input("\tJenis kelamin (Pilih 1/2) : ")
    if opsiGender == "1":
        jenisKel = "Laki-laki"
        print("\t(Laki-laki)")
    elif opsiGender == "2":
        jenisKel = "Perempuan"
        print("\t(Perempuan)")
    else:
        print("\tProgram berhenti (ᗒᗣᗕ)՞")
        break
    print()


    usia = int(input("\tMasukkan usia anda : "))
    if usia < 18 :
        print("\tMaaf anda belum cukup umur ಠ_ಠ")
        break
    elif usia >= 18 :
        print("\tLanjut (☞ ͡° ͜ʖ ͡°)☞")

    print()

    alamat = input("\tMasukkan Alamat anda : ")

    print()
    print("\t~~~~~~~~~PILIH JENIS KAMAR~~~~~~~~~")
    print("\t1. Classic Room = Rp.200.000 / hari")
    print("\t2. Elite Room   = Rp.400.000 / hari")
    print("\t3. Premium Room = Rp.600.000 / hari")
    print("\t4. VIP Room     = Rp.800.000 / hari")
    print("\t-----------------------------------")

    harga = ""
    jenis = ""
    jenisKamar = int(input("\tPilih jenis kamar yang anda inginkan : "))
    if jenisKamar == 1:
        print("\tClassic Room")
        jenis = "Classic Room"
        harga = 200000

    elif jenisKamar == 2:
        print("\tElite Room")
        jenis = "Elite Room"
        harga = 400000

    elif jenisKamar == 3:
        print("\tPremium Room")
        jenis = "Premium Room"
        harga = 600000

    elif jenisKamar == 4:
        print("\tVIP Room")
        jenis = "VIP Room"
        harga = 800000

    else:
        print("\tMaaf, inputan tidak diketahui, Program akan berhenti (ᗒᗣᗕ)")
        break

    print()

    hari = int(input("\tUntuk berapa hari : "))

    hasil = (hari*harga)
    tes = "bon",random.randint(0, 10)
    total = """  

\tSUB TOTAL : 
\t{}

\t{}
\tNama          : {}
\tJenis Kelamin : {}
\tUmur          : {}
\tAlamat        : {}
\tJenis Kamar   : {}
\tSelama        : {} hari
\tTotal Harga   : RP.{}

\t~~TERIMA KASIH TELAH MEMESAN ~~
    """.format(header, time, namaSaya, jenisKel, usia, alamat, jenis, hari, hasil)
    print(total)
    print("\tStruk anda telah tersimpan di bon.txt\n")
    bon = open ("Aplikasi sederhana/bon.txt", "a")
    bon.write(total)
    bon.close() 

    status = input("\tApakah ingin memesan lagi? (y = ya, n = tidak) : ")
    print()
    if status == "n":
        break
    elif status == "y":
        print("\tSilahkan pesan kamar hotel")
    else:
        print("\t Maaf, inputan tidak diketahui, Program akan berhenti (ᗒᗣᗕ)")
        break

    