from prettytable import PrettyTable

buku_list = [
    {"ID Buku": 22457,"Nama Buku":"Look Back","Nama Penulis":"Tatsuki Fujimoto","Kategori":"Komik","Harga": 45000,"Stock": 30},
    {"ID Buku": 28762,"Nama Buku":"Detektif Conan","Nama Penulis":"Gosho Aoyama","Kategori":"Komik","Harga": 99000,"Stock":40},
    {"ID Buku": 23419,"Nama Buku":"Laut Bercerita","Nama Penulis":"Leila S. Chudori","Kategori":"Novel","Harga": 115000,"Stock":60},
    {"ID Buku": 25683,"Nama Buku":"Bumi Manusia","Nama Penulis":"Pramoedya Ananta Toer","Kategori":"Novel","Harga": 132000,"Stock":50},
    {"ID Buku": 29821,"Nama Buku":"Filosofi Teras","Nama Penulis":"Henry Manampiring","Kategori":"Pengembangan Diri","Harga": 108000,"Stock":50},
    {"ID Buku": 23219,"Nama Buku":"Thinking, Fast & Slow","Nama Penulis":"Daniel Kahneman","Kategori":"Pengembangan Diri","Harga": 148000,"Stock":60}
]

def menu_utama():
    print("\n---------------Selamat Datang di Toko Buku Media Online---------------\n")
    print("List Menu :")
    print("1. Menampilkan Daftar Buku")
    print("2. Menambah Buku")
    print("3. Menghapus Buku")
    print("4. Membeli Buku")
    print("5. Exit Program")
    print("----------------------------------------------------------------------")


def menu_1():
    print("+++++++++Daftar Seluruh Buku++++++++")
    print("1. Tampilkan seluruh buku")
    print("2. Tampilkan buku berdasarkan buku_id")
    print("3. Tampilkan buku berdasarkan kategori")
    print("4. Kembali Ke Menu Utama")
    
    try:
        pilihan_menu_1 = int(input("Pilih angka dari 1-4: "))
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    tabel = PrettyTable()
    tabel.field_names = ["ID Buku","Nama Buku", "Nama Penulis", "Kategori", "Harga", "Stock"]
    
    if pilihan_menu_1 == 1:
        for buku in buku_list:
            tabel.add_row([buku["ID Buku"], buku["Nama Buku"], buku["Nama Penulis"], buku["Kategori"], buku["Harga"], buku["Stock"]])
        print(tabel)
    
    elif pilihan_menu_1 == 2:
        try:
            book_id = int(input("Masukkan ID Buku yang ingin ditampilkan: "))
        except ValueError:
            print("ID Buku harus berupa angka!")
            return
        
        found = False
        for buku in buku_list:
            if buku["ID Buku"] == book_id:
                tabel.add_row([buku["ID Buku"], buku["Nama Buku"], buku["Nama Penulis"], buku["Kategori"], buku["Harga"], buku["Stock"]])
                found = True
        
        if found:
            print('\n', tabel)
        else:
            print(f"\nBuku dengan ID {book_id} tidak ditemukan.")

    elif pilihan_menu_1 == 3:
        book_category = input("Masukkan Kategori Buku yang ingin ditampilkan: ")
        found = False
        for buku in buku_list:
            if buku["Kategori"].lower() == book_category.lower():
                tabel.add_row([buku["ID Buku"], buku["Nama Buku"], buku["Nama Penulis"], buku["Kategori"], buku["Harga"], buku["Stock"]])
                found = True
        
        if found:
            print('\n', tabel)
        else:
            print(f"\nTidak ada buku dalam kategori '{book_category}'.")

    
    elif pilihan_menu_1 == 4:
        return
    else:
        print("Pilihan tidak valid, Silakan pilih angka 1-4.")

def menu_2():
    try:
        id_book = int(input("Masukkan ID Buku: "))
    except ValueError:
        print("ID Buku harus berupa angka!")
        return

    if any(buku["ID Buku"] == id_book for buku in buku_list):
        print(f'\nBuku dengan ID {id_book} sudah ada, silakan masukkan ID.')
        return
    
    book_name = input("Masukkan Nama Buku: ")
    book_writer = input("Masukkan Nama Penulis Buku: ")
    book_category = input("Masukkan Kategori Buku: ")
    
    try:
        book_price = int(input("Masukkan Harga Buku: "))
        book_stock = int(input("Masukkan Jumlah Stok Buku: "))
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        return

    buku_list.append({
        "ID Buku": id_book, "Nama Buku": book_name, "Nama Penulis": book_writer,
        "Kategori": book_category, "Harga": book_price, "Stock": book_stock
    })
    print(f'\nBuku {id_book} berhasil ditambahkan.')


def menu_3():
    try:
        id_book = int(input("Masukkan ID Buku: "))
    except ValueError:
        print("ID Buku harus berupa angka!")
        return
    
    for buku in buku_list:
        if buku["ID Buku"] == id_book:
            while True:
                x = input('Apakah kamu yakin untuk menghapus data? (Y/N) ').strip().upper()
                if x == 'Y':
                    buku_list.remove(buku)
                    print(f"\nBuku {id_book} berhasil dihapus.")
                    return  # Exit after successful deletion
                elif x == 'N':
                    print(f"\nPenghapusan buku {id_book} dibatalkan.")
                    return  # Exit if user cancels deletion
                else:
                    print("Silakan masukkan hanya 'Y' atau 'N'.")  # Loop continues for invalid input
            break  # Exit loop once deletion or cancellation is confirmed

    print(f"\nBuku {id_book} tidak ditemukan.")  # Runs if ID is not in the list


def menu_4():
    global buku_list
    while True:  
        total = 0
        
        while True:
            try:
                id_book = int(input('\nMasukkan ID Buku yang ingin dibeli: '))
            except ValueError:
                print("Input harus berupa angka!")
                continue  
            
            buku_ditemukan = next((buku for buku in buku_list if buku["ID Buku"] == id_book), None)
            
            if not buku_ditemukan:
                print(f"\nBuku dengan ID {id_book} tidak ditemukan.")
                continue  
            
            while True:  
                try:
                    jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
                    break  
                except ValueError:
                    print("Input harus berupa angka!")
            
            if buku_ditemukan["Stock"] >= jumlah:
                ttl_harga = buku_ditemukan["Harga"] * jumlah
                buku_ditemukan["Stock"] -= jumlah  

                print(f"{buku_ditemukan['Nama Buku']} : {jumlah} x {buku_ditemukan['Harga']} = {ttl_harga}")
                total += ttl_harga
            else:
                print(f"\nMohon maaf, stok {buku_ditemukan['Nama Buku']} hanya tersisa {buku_ditemukan['Stock']}")
            
            tanya = input('Apakah kamu ingin menambahkan buku lain? (Y/N) ').strip().upper()
            while tanya not in ['Y', 'N']:
                print("Silakan masukkan hanya 'Y' atau 'N'.")
                tanya = input('Apakah kamu ingin menambahkan buku lain? (Y/N) ').strip().upper()

            if tanya == 'N':
                break  

        print("Total Harga : ", total)

        while True:  
            try:
                uang_masuk = int(input("Masukkan jumlah uang: "))
                if uang_masuk >= total:
                    break  
                else:
                    print("Uangnya kurang sebesar: ", total - uang_masuk)
            except ValueError:
                print("Input harus berupa angka!")

        print("Terima kasih telah berbelanja!")
        if uang_masuk > total:
            print("Uang kembalian Anda: ", uang_masuk - total)

        print('\n')

        # Hanya tanya apakah ingin belanja lagi, tidak panggil menu_utama() di sini
        i = input('Apakah Anda masih ingin berbelanja? (Y/N) ').strip().upper()
        while i not in ['Y', 'N']:
            print("Silakan masukkan hanya 'Y' atau 'N'.")
            i = input('Apakah Anda masih ingin berbelanja? (Y/N) ').strip().upper()

        if i == 'N':
            return  # Langsung kembali ke menu utama tanpa memanggilnya secara manual


while True:
    menu_utama()
    try:
        pilihan = int(input("Silakan Pilih Main Menu: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue
    
    if pilihan == 1:
        menu_1()
    elif pilihan == 2:
        menu_2()
    elif pilihan == 3:
        menu_3()
    elif pilihan == 4:
        menu_4()
    elif pilihan == 5:
        while True:
            x = input('\nApakah kamu yakin untuk keluar dari halaman ini? (Y/N): ').strip().upper()
            if x == 'Y':
                print("\nTerima kasih telah mengunjungi Toko Buku Media Online!")
                exit()  # Menghentikan program secara langsung
            elif x == 'N':
                break  # Kembali ke menu utama
            else:
                print("Silakan masukkan hanya 'Y' atau 'N'.")
    else:
        print("Silahkan pilih menu 1-5!")
