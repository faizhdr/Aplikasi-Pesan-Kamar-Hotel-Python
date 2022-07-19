# output dari hotel bintang lima
print("---------------------------------")
print("|~~~~~ HOTEL BINTANG LIMA ~~~~~~|")
print("|~~~~~~~~ Faiz & Qadri ~~~~~~~~~|")
print("---------------------------------")
print()

# input untuk melanjutkan 
input("~~TEKAN ENTER UNTUK MELANJUTKAN~~")

# membuat perulangan untuk pesanan hotel 
while(True):

    # input memasukkan nama kedalam variabel namaSaya 
    namaSaya = input("Masukkan Nama lengkap : ")

    # output pemilihan gender/jenis kelamin
    print("       ----------------     ")
    print("       | 1. Laki-laki |     ")
    print("       | 2. Perempuan |     ")
    print("       ----------------     ")

    # input untuk memasukkan pilihan kedalam variable gender
    gender = input("Jenis kelamin (Pilih 1/2) : ")

    # membuat variable kosong untuk memasukkan nilai kedalam variable tersebut 
    jenisKel = ""

    # jika memilih angka 1 maka output laki-laki
    if gender == "1":
        jenisKel = "Laki-laki"
        print(jenisKel)

    # selain itu,jika memilih angka 2 maka output perempuan
    elif gender == "2":
        jenisKel = "Perempuan"
        print(jenisKel)

    # selain memilih angka 1 dan 2 maka program akan berhenti 
    else:
        print("Inputan tidak diketahui")
        break

    # input untuk memasukkan alamat kedalam variable alamat 
    alamat = input("Masukkan Alamat anda : ")

    # output untuk memilih jenis kamar serta harganya
    print()
    print("~~~~~~~~~PILIH JENIS KAMAR~~~~~~~~~")
    print("1. Classic Room = Rp.200.000 / hari")
    print("2. Elite Room   = Rp.400.000 / hari")
    print("3. Premium Room = Rp.600.000 / hari")
    print("4. VIP Room     = Rp.800.000 / hari")
    print("-----------------------------------")

    # membuat variable kosong untuk memasukkan nilai kedalam variable tersebut 
    harga = ""
    jenis = ""
    
    # membuat input pilihan jenis kamar  kedalam variable jenisKamar 
    jenisKamar = int(input("Pilih jenis kamar yang anda inginkan : "))

    # jika memilih angka 1 maka output yang dikeluarkan yaitu "classic room" serta harganya "200.000"
    if jenisKamar == 1:
        print("Classic Room")
        jenis = "Classic Room"
        harga = 200000
    
    # selain itu,jika memilih angka 2 maka output yang dikeluarkan yaitu "elite room" serta harganya "400.000"
    elif jenisKamar == 2:
        print("Elite Room")
        jenis = "Elite Room"
        harga = 400000

    # selain itu,jika memilih angka 3 maka output yang dikeluarkan yaitu "premium room" serta harganya "600.000"
    elif jenisKamar == 3:
        print("Premium Room")
        jenis = "Premium Room"
        harga = 600000

    # selain itu,jika memilih angka 4 maka output yang dikeluarkan yaitu "vip room" serta harganya "800.000"
    elif jenisKamar == 4:
        print("VIP Room")
        jenis = "VIP Room"
        harga = 800000

    # selain memilih angka 1 sampai 4 maka program akan berhenti 
    else:
        print("inputan tidak diketahui")
        break

    # membuat inputan waktu dihotel
    hari = int(input("Untuk berapa hari : "))

    # membuat perkalian hari dan harga yang dimasukkan kedalam variable hasil untuk menghasilkan total harga 
    hasil = (hari*harga)

    # output dari semua inputan yang telah dibuat 
    print()
    print("=========== SUB TOTAL ============")
    print("Nama          :",namaSaya)
    print("Jenis Kelamin :",jenisKel)
    print("Alamat        :",alamat)
    print("Jenis Kamar   :",jenis)
    print("Selama        :",hari,"hari")
    print("Total Harga   : Rp.",hasil)
    print()
    print("~~~~Terima kasih telah mamesan :)~~~")
    print("Struk anda telah tersimpan di bon.txt")
    print()

    # variabel bon berfungsi untuk memasukkan data ke dalam bon.txt untuk membuat struk/bon
    bon = open("bon.txt", "w")
    print("---------------------------------", file=bon)# terdapat "file=bon" yang berfungsi memindahkan tulisan kedalam file bon.txt
    print("|~~~~~ HOTEL BINTANG LIMA ~~~~~~|", file=bon)
    print("|~~~~~~~~ Faiz & Qadri ~~~~~~~~~|", file=bon)
    print("---------------------------------", file=bon)
    print(file=bon)
    print("============= STRUK ==============", file=bon)
    print("Nama          :",namaSaya, file=bon)
    print("Jenis Kelamin :",jenisKel, file=bon)
    print("Alamat        :",alamat, file=bon)
    print("Jenis Kamar   :",jenis, file=bon)
    print("___________________________________", file=bon)
    print("Selama        :",hari,"hari", file=bon)
    print("Total Harga   : Rp.",hasil, file=bon)
    print(file=bon)
    print("~~~~Terima kasih telah mamesan :)~~~", file=bon)
    print(file=bon)
    bon.close() # bon.close berfungsi penutup dari varaiabel bon

    # status jika ingin memesan kamar hotel tersebut,jika memilih "y" maka program akan diulang kembali,jika memilih "n" maka program akan berhenti 
    status = input("Apakah ingin memesan lagi? (y = ya, n = tidak) : ")
    print()
    if status == "n":
        break
    elif status == "y":
        print("Silahkan pesan kamar hotel")
    else:
        print("Maaf inputan anda tidak diketahui :(")
        break