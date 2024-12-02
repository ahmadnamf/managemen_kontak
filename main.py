#program manajemen kontak

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak,start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong")
        return 1

def menambah_kontak():
    # ,menambahkan kontak baru
    nama = input("Masukkan Nama : ")
    HP = input("Masukkan No HP: ")
    email = input("Masukkan email : ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak Baru Berhasil disimpan!")

def menghapus_kontak():
    # Menghapus kontak
    if melihat_kontak()==1:
        return
    else:
        i_hapus = int(input("Masukkan no kontak yan akan dihapus: "))
        del kontak[i_hapus - 1]
        print("KOntak berhasil dihapus")


kontak1 = {'nama' : "Andi",'HP' : '102453541', 'email' : 'andi@gmail.com'}
kontak2 = {'nama' : "Ani",'HP' : '945434354', 'email' : 'ani@gmail.com'}

kontak = [kontak1, kontak2]


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("masukkan pilihan menu kontak (1, 2, 3, atau 4): ")

    if pilihan == "1":
        melihat_kontak()

    elif pilihan == "2":
        menambah_kontak()

    elif pilihan == "3":
        menghapus_kontak()

    elif pilihan == "4":
        #Keluar dari Kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")

