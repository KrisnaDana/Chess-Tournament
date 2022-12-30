from os import system #import package system buat manggil cmd pada system agar bisa digunakan pada python contoh: system("cls")
import mysql.connector #import package untuk koneksi mysql

# MDI_KLP2_2005551084_I Putu Ngurah Krisna Dana
# menggunakan sistem poin yang diotomatisasi berdasarkan hasil pertandingan
# hasil pertandingan ada 3 jenis: peserta 1 menang (poin +1), peserta 2 menang(poin +1) ,  draw (masing-masing peserta poin +0.5)
# ranking berdasarkan jumlah poin terbanyak

def menu1(): #Menu Awal
    print("=============TURNAMEN CATUR=============")
    print("1. DATA PESERTA")
    print("2. DATA PERTANDINGAN")
    print("3. LIHAT RANKING")
    print("4. KELUAR")
    print("========================================")
    input_menu1 = input("MASUKKAN PILIHAN [1/2/3]: ") #Input Pilihan Menu
    print(input_menu1)
    if input_menu1 == "1":
        _ = system("cls")
        menu1_1() #Ke Menu Data Peserta
    elif input_menu1 == "2":
        _ = system("cls")
        menu1_2() #Ke Menu Data Pertandingan
    elif input_menu1 == "3":
        _ = system("cls")
        lihat_ranking() #Ke Menu Lihat Rangking
    elif input_menu1 == "4":
        quit() #Exit Program
    else: #Ulang input pilihan
        print("========================================")
        print("PILIHAN YANG DIMASUKKAN SALAH")
        _ = system("cls")
        menu1()

def menu1_1(): # Menu Data Peserta
    print("============ DATA PESERTA =============")
    print("1. LIHAT DATA PESERTA")
    print("2. INPUT DATA PESERTA")
    print("3. UBAH DATA PESERTA")
    print("4. HAPUS DATA PESERTA")
    print("5. KEMBALI")
    print("6. KELUAR")
    print("========================================")
    input_menu1_1 = input("MASUKKAN PILIHAN [1/2/3/4/5/6]: ") #Input Pilihan Menu
    if input_menu1_1 == "1":
        _ = system("cls")
        lihat_peserta() # Ke Menu Lihat Peserta
    elif input_menu1_1 == "2":
        _ = system("cls")
        input_peserta() # Ke Menu Input Peserta
    elif input_menu1_1 == "3":
        _ = system("cls")
        ubah_peserta() # Ke Menu Ubah Peserta
    elif input_menu1_1 == "4":
        _ = system("cls")
        hapus_peserta() # Ke Menu Hapus Peserta
    elif input_menu1_1 == "5":
        _ = system("cls")
        menu1() # Kembali ke Menu Awal
    elif input_menu1_1 == "6":
        quit() # Exit Program
    else: # Ulang input pilihan
        print("========================================")
        print("PILIHAN YANG DIMASUKKAN SALAH")
        _ = system("cls")
        menu1_1()

def lihat_peserta(): # Menu Lihat Peserta
    mydb = mysql.connector.connect( #Koneksi ke database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_peserta") #Mengambil Data Peserta
    myresult = mycursor.fetchall() #Menyimpan data peserta
    for peserta in myresult: #Tampilkan Data Peserta
        print("================= LIHAT ==================")
        print("ID      : ", peserta[0])
        print("NAMA    : ", peserta[1], peserta[2])
        print("ALAMAT  : ", peserta[3])
        print("TELEPON : ", peserta[4])
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_1() # Kembali Ke Menu Data Peserta

def input_peserta(): # Menu Input Peserta
    mydb = mysql.connector.connect( # Koneksi ke Database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()

    print("============= INPUT =============")
    depan = input("NAMA DEPAN    : ")
    belakang = input("NAMA BELAKANG : ")
    alamat = input("ALAMAT        : ")
    telepon = input("TELEPON       : ")

    sql = "INSERT INTO tb_peserta (nama_depan, nama_belakang, alamat, no_telp, poin) VALUES (%s, %s, %s, %s, %s)" # Perintah SQL Insert
    val = (depan, belakang, alamat, telepon, "0") #Value pada perintah sql di atas
    mycursor.execute(sql, val) #eksekusi perintah sql
    mydb.commit()

    print("========================================")
    print("DATA BERHASIL DIINPUT")
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_1() # Kembali ke menu data peserta

def ubah_peserta():
    mydb = mysql.connector.connect( # Koneksi Database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_peserta") #Ngambil data peserta
    myresult = mycursor.fetchall() #simpan data peserta

    for peserta in myresult: #Tampilkan data peserta
        print("================== UBAH ====================")
        print("ID      : ", peserta[0])
        print("NAMA    : ", peserta[1], peserta[2])
    print("========================================")
    peserta = input("MASUKKAN ID PESERTA: ")

    cek = 0;
    for x in myresult:
        if x == myresult[0]: # Ngecek apakah id yang diinput user terdapat di databasae
            cek = 1;
            id = myresult[0]
    _ = system("cls")

    if cek == 0: #Jika id diinput user tidak ada didatabase tampilkan dibawah ini
        print("========================================")
        print("DATA TIDAK TERSEDIA")
        print("========================================")
        print("KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_1()
    else: #Jika id diinput user ada didatabase
        _ = system("cls")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta pada database berdasarkan id
        val = (peserta, ) #value pada perintah sql diatas
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data yang diambil

        for x in myresult: #tampilkan data yang disimpan sebelumnya
            print("========================================")
            print("ID            : ", x[0])
            print("NAMA DEPAN    : ", x[1])
            print("NAMA BELAKANG : ", x[2])
            print("ALAMAT        : ", x[3])
            print("TELEPON       : ", x[4])
            print("========================================")
            depan = input("NAMA DEPAN    : ")
            belakang = input("NAMA BELAKANG : ")
            alamat = input("ALAMAT        : ")
            telepon = input("TELEPON       : ")
        
        mycursor = mydb.cursor()
        sql = "UPDATE tb_peserta SET nama_depan = %s, nama_belakang = %s, alamat = %s, no_telp = %s WHERE id = %s" #perintah update data peserta
        val = (depan, belakang, alamat, telepon, peserta) #value perintah sql diatas

        mycursor.execute(sql, val) #eksekusi perintah sql
        mydb.commit()
        print("========================================")
        print("DATA BERHASIL DIUBAH")
        print("========================================")
        print("KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_1() #kembali ke menu data peserta

def hapus_peserta(): #Hapus Peserta
    mydb = mysql.connector.connect( #Koneksi Database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_peserta") #perintah ambil data peserta
    myresult = mycursor.fetchall() #Simpan data yang sudah diambil

    for peserta in myresult: #tampilkan data
        print("================= HAPUS ===================")
        print("ID      : ", peserta[0])
        print("NAMA    : ", peserta[1], peserta[2])
    print("========================================")
    peserta = input("MASUKKAN ID PESERTA: ")

    cek = 0;
    for x in myresult:
        if x == myresult[0]: #Ngecek id yang dinput user apakah terdapat didatabase
            cek = 1;
    _ = system("cls")

    if cek == 0: #jika id tidak ada di database tampilkan dibawah ini
        print("========================================")
        print("DATA TIDAK TERSEDIA")
        print("========================================")
        print("KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_1()
    else: #jika id ada di database
        _ = system("cls")
        mycursor = mydb.cursor()
        sql = "DELETE FROM tb_peserta WHERE id = %s" #perintah delete data peserta berdasarkan id
        val = (peserta, ) #value perintah sql diatas

        mycursor.execute(sql, val) #eksekusi perintah sql
        mydb.commit()
        print("========================================")
        print("DATA BERHASIL DIHAPUS")
        print("========================================")
        print("KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_1() #kembali ke menu awal

def menu1_2(): #Menu Data Pertandingan
    print("============= DATA PERTANDINGAN =============")
    print("1. LIHAT DATA PERTANDINGAN")
    print("2. INPUT DATA PERTANDINGAN")
    print("3. UBAH DATA PERTANDINGAN")
    print("4. HAPUS DATA PERTANDINGAN")
    print("5. KEMBALI")
    print("6. KELUAR")
    print("========================================")
    input_menu1_1 = input("MASUKKAN PILIHAN [1/2/3/4/5/6]: ")
    if input_menu1_1 == "1":
        _ = system("cls")
        lihat_pertandingan() # Ke menu lihat pertandingan
    elif input_menu1_1 == "2":
        _ = system("cls")
        input_pertandingan() # Ke menu input pertandingan
    elif input_menu1_1 == "3":
        _ = system("cls")
        ubah_pertandingan() # Ke menu ubah pertandingan
    elif input_menu1_1 == "4":
        _ = system("cls")
        hapus_pertandingan() # Ke menu hapus pertandingan
    elif input_menu1_1 == "5":
        _ = system("cls")
        menu1() #Kembali ke menu awal
    elif input_menu1_1 == "6":
        quit() #exit program
    else: #ulang input pilihan
        print("========================================")
        print("PILIHAN YANG DIMASUKKAN SALAH")
        _ = system("cls")
        menu1_2() 


def lihat_pertandingan():
    mydb = mysql.connector.connect( # Koneksi database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_pertandingan INNER JOIN tb_peserta p1 ON tb_pertandingan.id_peserta_a = p1.id INNER JOIN tb_peserta p2 ON tb_pertandingan.id_peserta_b = p2.id") #mengambil data pertandingan
    myresult = mycursor.fetchall() #simpan data pertandingan
    for pertandingan in myresult: #menampilkan data pertandingan
        print("================ LIHAT ====================")
        print("ID        : ", pertandingan[0])
        print("PESERTA 1 : ", pertandingan[7], pertandingan[8], "[ ID:", pertandingan[6],"]")
        print("PESERTA 2 : ", pertandingan[13], pertandingan[14], "[ ID:", pertandingan[12],"]")
        print("HASIL     : ", pertandingan[3])
        print("MULAI     : ", pertandingan[4])
        print("SELESAI   : ", pertandingan[5])
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_2() #Kembali ke menu data pertandingan

def input_pertandingan(): #input data pertandingan
    mydb = mysql.connector.connect( #koneksi database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_peserta") #perintah ambil data peserta
    myresult = mycursor.fetchall() #simpan data peserta
    for peserta in myresult: #tampilkan data peserta
        print("================ INPUT =====================")
        print("ID      : ", peserta[0])
        print("NAMA    : ", peserta[1], peserta[2])
    print("========================================")
    peserta1 = input("MASUKKAN ID PESERTA 1: ") #imput id peserta 1
    print("========================================")
    peserta2 = input("MASUKKAN ID PESERTA 2: ") # input id peserta 2
    print("========================================")
    print("HASIL: ")
    print("1. Peserta 1 Menang")
    print("2. Peserta 2 Menang")
    print("3. Draw")
    pilih_hasil = input("MASUKKAN HASIL [1/2/3] : ") #input hasil pertandingan
    if pilih_hasil == "1":
        hasil = "Peserta 1 Menang"
    elif pilih_hasil == "2":
        hasil = "Peserta 2 Menang"
    elif pilih_hasil == "3":
        hasil = "Draw"
    else: #kembali ke menu data pertandingan
        print("INPUT SALAH SILAHKAN KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_2()
    print("========================================")
    mulai = input("Masukkan Tanggal dan Waktu Mulai [YYYY-MM-DD HH:mm:ss]: ") #input tanggal dan waktu mulai pertandingan
    print("========================================")
    selesai = input("Masukkan Tanggal dan Waktu Selesai [YYYY-MM-DD HH:mm:ss]: ") #input tanggal dan waktu selesai pertandingan

    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_pertandingan (id_peserta_a, id_peserta_b, hasil, mulai, selesai) VALUES (%s, %s, %s, %s, %s)" #perintah insert data pertandingan ke database
    val = (peserta1, peserta2, hasil, mulai, selesai)
    mycursor.execute(sql, val) #eksekusi perintah sql
    mydb.commit()

    if hasil == "Peserta 1 Menang": #jika hasil pertandingan adalah peserta 1 menang
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            poin = x[5] + 1 #poin peserta 1 sebelumnya ditambah 1
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #perintah update poin peserta1 
            val = (poin, peserta1)
            mycursor.execute(sql, val)
            mydb.commit()

    elif hasil == "Peserta 2 Menang": #jika hasil pertandingan adalah peserta 2 menang
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            poin = x[5] + 1 #poin peserta 2 sebelumnya ditambah 1
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #perintah update poin peserta 2
            val = (poin, peserta2)
            mycursor.execute(sql, val)
            mydb.commit()

    elif hasil == "Draw": #jika hasil pertandingan adalah draw
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            poin = x[5] + 0.5 #poin peserta 1 sebelumnya ditambah 0.5
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #perintah update poin peserta 1
            val = (poin, peserta1)
            mycursor.execute(sql, val)
            mydb.commit()
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            poin = x[5] + 0.5 #poin peserta 2 sebelumnya ditambah 0.5
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #perintah update poin peserta 1
            val = (poin, peserta2)
            mycursor.execute(sql, val)
            mydb.commit()

    print("========================================")
    print("DATA BERHASIL DIINPUT")
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_2() # Kembali ke menu data pertandingan

def ubah_pertandingan(): #Ubah Pertandingan
    mydb = mysql.connector.connect( #Koneksi database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_pertandingan INNER JOIN tb_peserta p1 ON tb_pertandingan.id_peserta_a = p1.id INNER JOIN tb_peserta p2 ON tb_pertandingan.id_peserta_b = p2.id") #Perintah ambil data pertandingan
    myresult = mycursor.fetchall() #simpan data
    for pertandingan in myresult: #tampilkan data
        print("================= UBAH ===================")
        print("ID        : ", pertandingan[0])
        print("PESERTA 1 : ", pertandingan[7], pertandingan[8], "[ ID:", pertandingan[6],"]")
        print("PESERTA 2 : ", pertandingan[13], pertandingan[14], "[ ID:", pertandingan[12],"]")
        print("HASIL     : ", pertandingan[3])
        print("MULAI     : ", pertandingan[4])
        print("SELESAI   : ", pertandingan[5])
    print("========================================")
    pertandingan = input("PILIH ID PERTANDINGAN: ")
    _ = system("cls")

    mycursor = mydb.cursor()
    sql = "SELECT * FROM tb_pertandingan INNER JOIN tb_peserta p1 ON tb_pertandingan.id_peserta_a = p1.id INNER JOIN tb_peserta p2 ON tb_pertandingan.id_peserta_b = p2.id WHERE tb_pertandingan.id = %s" #Perintah ambil data pertandingan berdasarkan id yang dipilih
    val = (pertandingan, ) #value pada perintah sql diatas
    mycursor.execute(sql, val) #eksekusi perintah sql
    myresult = mycursor.fetchall() #simpan data
    for x in myresult: #tampilkan data
        print("========================================")
        print("ID        : ", x[0])
        print("PESERTA 1 : ", x[7], x[8], "[ ID:", x[6],"]")
        print("PESERTA 2 : ", x[13], x[14], "[ ID:", x[12],"]")
        print("HASIL     : ", x[3])
        print("MULAI     : ", x[4])
        print("SELESAI   : ", x[5])
        print("========================================")
        hasil_awal = x[3]
    
    print("========================================")
    peserta1 = input("MASUKKAN ID PESERTA 1: ") #input id peserta 1
    print("========================================")
    peserta2 = input("MASUKKAN ID PESERTA 2: ") #input id peserta
    print("========================================")
    print("HASIL: ")
    print("1. Peserta 1 Menang")
    print("2. Peserta 2 Menang")
    print("3. Draw")
    pilih_hasil = input("MASUKKAN HASIL [1/2/3] : ") #input hasil pertandingan
    if pilih_hasil == "1":
        hasil = "Peserta 1 Menang"
    elif pilih_hasil == "2":
        hasil = "Peserta 2 Menang"
    elif pilih_hasil == "3":
        hasil = "Draw"
    else: #kembali ke menu data pertandingan
        print("INPUT SALAH SILAHKAN KETIK ENTER UNTUK KEMBALI")
        print("========================================")
        x = input("")
        _ = system("cls")
        menu1_2()
    print("========================================")
    mulai = input("Masukkan Tanggal dan Waktu Mulai [YYYY-MM-DD HH:mm:ss]: ") #input tanggal dan waktu pertandingan contoh: 2022-03-01 15:20:12
    print("========================================")
    selesai = input("Masukkan Tanggal dan Waktu Selesai [YYYY-MM-DD HH:mm:ss]: ") #input tanggal dan waktu pertandingan selesai contoh: 2022-03-01 15:20:12

    mycursor = mydb.cursor()
    sql = "UPDATE tb_pertandingan set id_peserta_a = %s, id_peserta_b = %s, hasil = %s, mulai = %s, selesai = %s WHERE id = %s"
    val = (peserta1, peserta2, hasil, mulai, selesai, pertandingan)
    mycursor.execute(sql, val) #
    mydb.commit()

    if hasil_awal == "Peserta 1 Menang": #jika hasil awal peserta 1 yang menang maka poin peserta 1 dikurangi 1
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" # perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult: #tampilkan data
            poin = x[5] - 1 #kurang 1 poin
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #perintah update poin
            val = (poin, peserta1)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    elif hasil_awal == "Peserta 2 Menang": #jika hasil awal peserta 2 yang menang maka poin peserta 2 dikurangi 1
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] - 1 #kurangi 1 poin
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s"  #perintah update poin
            val = (poin, peserta2)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    elif hasil_awal == "Draw": #jika hasil awal draw maka poin peserta 1 dan peserta 2 dikurangi 0.5
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] - 0.5 #kurangi 0.5 poin pada peserta 1
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin
            val = (poin, peserta1)
            mycursor.execute(sql, val)  #eksekusi perintah sql
            mydb.commit()
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] - 0.5 #kurangi 0.5 poin pada peserta 2
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin
            val = (poin, peserta2)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    if hasil == "Peserta 1 Menang": #jika hasil yang diubah menjadi peserta 1 menang maka poin peserta 1 ditambah 1
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val) #eksekusi perintah
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] + 1 #tambah 1 poin pada peserta 1
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin peserta 1
            val = (poin, peserta1)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    elif hasil == "Peserta 2 Menang": #jika hasil yang diubah menjadi peserta 2 menang maka poin peserta 2 ditambah 1
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val) #eksekusi perintah
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] + 1 #tambah 1 poin pada peserta 2
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin peserta 2
            val = (poin, peserta2)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    elif hasil == "Draw": #jika hasil yang diubah menjadi draw maka poin peserta 1 dan peserta 2 ditambah 0.5
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 1
        val = (peserta1, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] + 0.5 #tambah 0.5 poin pada peserta 1
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin peserta 1
            val = (poin, peserta1)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM tb_peserta WHERE id = %s" #perintah ambil data peserta 2
        val = (peserta2, )
        mycursor.execute(sql, val) #eksekusi perintah sql
        myresult = mycursor.fetchall() #simpan data
        for x in myresult:
            poin = x[5] + 0.5 #tambah 0.5 poin pada peserta 2
            mycursor = mydb.cursor()
            sql = "UPDATE tb_peserta SET poin = %s WHERE id = %s" #update poin peserta 2
            val = (poin, peserta2)
            mycursor.execute(sql, val) #eksekusi perintah sql
            mydb.commit()

    print("========================================")
    print("DATA BERHASIL DIUBAH")
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_2() #kembali ke menu data pertandingan

def hapus_pertandingan(): #hapus pertandingan
    mydb = mysql.connector.connect( #koneksi database
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_pertandingan INNER JOIN tb_peserta p1 ON tb_pertandingan.id_peserta_a = p1.id INNER JOIN tb_peserta p2 ON tb_pertandingan.id_peserta_b = p2.id") #perintah ambil data pertandingan
    myresult = mycursor.fetchall() #simpan data
    for pertandingan in myresult: #tampilkan data
        print("================= HAPUS ===================")
        print("ID        : ", pertandingan[0])
        print("PESERTA 1 : ", pertandingan[7], pertandingan[8], "[ ID:", pertandingan[6],"]")
        print("PESERTA 2 : ", pertandingan[13], pertandingan[14], "[ ID:", pertandingan[12],"]")
        print("HASIL     : ", pertandingan[3])
        print("MULAI     : ", pertandingan[4])
        print("SELESAI   : ", pertandingan[5])
    print("========================================")
    pertandingan = input("PILIH ID PERTANDINGAN: ") #input id pertandingan
    _ = system("cls")
    mycursor = mydb.cursor()
    sql = "DELETE FROM tb_pertandingan WHERE id = %s" #perintah delete data pertandingan berdasarkan id
    val = (pertandingan, ) #value pada perintah sql diatas

    mycursor.execute(sql, val) #eksekusi perintah sql
    mydb.commit()
    print("========================================")
    print("DATA BERHASIL DIHAPUS")
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1_2() #kembali ke menu data pertandingan

def lihat_ranking(): #lihat ranking
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ims_pretest"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM tb_peserta ORDER BY poin DESC") #ambil data peserta yand diurutkan berdasarkan poin terbanyak
    myresult = mycursor.fetchall() #simpan data

    print("================= RANKING ===================")

    i = 1; #indeks rangking
    for peserta in myresult: #tampilkan data peserta dan poin serta rangkingnya
        print("ID      : ", peserta[0])
        print("NAMA    : ", peserta[1], peserta[2])
        print("POIN    : ", peserta[5])
        print("RANKING : ", i)
        i = i + 1
        print("========================================")
    print("========================================")
    print("KETIK ENTER UNTUK KEMBALI")
    print("========================================")
    x = input("")
    _ = system("cls")
    menu1() #kembali ke menu awal

menu1() #memanggil fungsi menu awal

