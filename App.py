import os
from time import sleep
import pandas as pd
import csv
import tabulate 

red = '\033[91m'
end = '\033[0m'

source = os.path.join(os.getcwd(),'DataHasilPanen.csv')
df = pd.read_csv(source)
data = df.values.tolist()

def login(name,password) :
    sukses = False
    with open("logindata.txt","r") as f:
        file = f.readlines()
    file = [i.replace("\n","") for i in file]
    for i in file :
        a,b = i.split(",")
        if (a == name and b == password) :
            sukses = True
            break
    if (sukses) :
        print("")
        print(20*"=")
        print("Login Berhasil".center(20))
        print(20*"=")
        print("")
    else :
        loading("Mencari Akun")
        print("")
        print(40*"=")
        print(red+"Akun Belum Terdaftar,Silahkan Registrasi".center(30)+end)
        print(40*"=")
        print("")
        access(register)

def header_file():
    print("-"*44)
    print("|","SELAMAT DATANG DI PROGRAM".center(40),"|")
    print("|","PENDATAAN HASIL PANEN".center(40),"|")
    print("-"*44)

def register(name,password) :
    file = open("logindata.txt","a")
    file.write("\n"+name+","+password)
    file.close()

def loading(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        sleep(0.5)

def access(option):
    global name, password
    if option == "1":
        print("")
        name = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        login(name, password)
        loading("Sedang Masuk ")
        clear()
        main()
    else:
        print("")
        print("Masukkan Username dan Password Baru")
        name = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        file = open("logindata.txt", "r")
        usernames = []
        for i in file:
            a, b = i.split(",")
            b = b.strip()
            usernames.append(a)
        file.close()
        if name in usernames:
            print("Username sudah terdaftar, sehingga username anda ditambah dengan v2")
            name2 = "v2"
            name += name2
        if name == password:
            print("Password tidak bisa sama dengan username!!!")
            access(option="2")
        else:
            register(name, password)
            print("")
            print(20 * "=")
            print("Registrasi Berhasil".center(20))
            print(20 * "=")
            print("")
            access(option="1")



# def access(option) :
#     global name,password
#     if (option == "1") :
#         print("")
#         name = input("Masukkan Username : ")
#         password = input("Masukkan Password : ")
#         login(name,password)
#         loading("Sedang Masuk ")
#         clear()
#         main()
#     else :
#         print("")
#         print("Masukkan Username dan Password Baru")
#         name = input("Masukkan Username : ")
#         password = input("Masukkan Password : ")
#         acc = False
#         file = open("logindata.txt", "r")
#         for i in file:
#             a,b = i.split(",")
#             b = b.strip()
#             if a == name:
#                 acc = True
#                 break
#         if acc:
#             print("Username sudah terdaftar, silahkan menggunakan username lain")
#             access(option="2")
#         else:
#             if name == password:
#                 print("Password tidak bisa sama dengan username!!!")
#                 access(option="2")
#             else:
#                 register(name,password)
#                 print("")
#                 print(20*"=")
#                 print("Registrasi Berhasil".center(20))
#                 print(20*"=")
#                 print("")
#                 access(option="1")

# def access(option):
#     global name, password
#     if option == "1":
#         print("")
#         name = input("Masukkan Username : ")
#         password = input("Masukkan Password : ")
#         login(name, password)
#         loading("Sedang Masuk ")
#         clear()
#         main()
#     else:
#         print("")
#         print("Masukkan Username dan Password Baru")
#         name = input("Masukkan Username : ")
#         password = input("Masukkan Password : ")
#         file = open("logindata.txt", "r")
#         usernames = []
#         for i in file:
#             a, b = i.split(",")
#             b = b.strip()
#             usernames.append(a)
#         file.close()
#         if name in usernames:
#             print("Username sudah terdaftar, silahkan menggunakan username lain")
            # name2 = input(f"Masukkan tambahan kata : {name}")
#             name += name2
#             while name in usernames:
#                 print("Username masih sama, tambahkan kata lain")
#                 name2 = input(f"Masukkan tambahan kata : {name}")
#                 name += name2
#         if name == password:
#             print("Password tidak bisa sama dengan username!!!")
#             access(option="2")
#         else:
#             clear()
#             x = input(f"Apakah benar username anda {red}{name}{end} dan password anda adalah {red}{password}{end} ? (y/n)")
#             if x == "y":
#                 register(name, password)
#                 print("")
#                 print(20 * "=")
#                 print("Registrasi Berhasil".center(20))
#                 print(20 * "=")
#                 print("")
#                 access(option="1")
#             elif x == "n":
#                 access(option="2")
#             else:
#                 print("Salah input")
#                 access(option="2")

def begin():
    global option
    print("""=========== WELCOME TO OUR APPLICATION ===========
==================================================
=  ____   _____   _   _     __     ____   _____  =
= |    \ | ____| | |_| |  /    \  |    \ | ____| =
= |  __/ | __|_  |  _  | |  __  | |  __/ | __|_  =
= |_|    |_____| |_| |_| |_|  |_| |_|    |_____| =
=    P E N D A T A A N   H A S I L   P A N E N   =
==================================================""")

    print("\n1. Login \n2. Registrasi")
    option = input("[1/2] : ")
    if (option != "1" and option != "2") :
        clear()
        print(red+"\nMOHON PILIH 1 ATAU 2 SAJA!\n"+end)
        begin()

def clear():
    os.system("cls")

def load_data():
    data = []
    with open('DataHasilPanen.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

def save_data(data):
    with open('DatahasilPanen.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nama Tanaman', 'Tanggal Panen', 'Hasil Panen', 'Harga Per Kilo'])
        writer.writerows(data)

def create_data(data):
    id_tanaman = input("Masukkan ID tanaman: ")
    nama_tanaman = input("Masukkan nama tanaman: ")
    tanggal_panen = input("Masukkan tanggal panen (format: YYYY-MM-DD): ")
    hasil_panen = int(input("Masukkan hasil panen (dalam ton): "))
    harga_per_kilo = input("Masukkan harga per kilo: ")
    data.append([id_tanaman, nama_tanaman, tanggal_panen, hasil_panen, harga_per_kilo])
    save_data(data)
    clear()
    print("Data berhasil ditambahkan!")

def read_data(data):
    print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))

def update_data(data):
    id_tanaman = input("Masukkan id tanaman yang akan diupdate: ")
    for row in data:
        if row[0].lower() == id_tanaman.lower():
            row[1] = input("Masukkan nama tanaman: ")
            row[2] = int(input("Masukkan tanggal panen (format: YYYY-DD-MM): "))
            row[3] = input("Masukkan hasil panen (dalam ton): ")
            row[4] = input("Masukkan harga per kilo: ")
            save_data(data)
            print("Data berhasil diupdate!")
            return
    print("ID tanaman tidak ditemukan!")

def delete_data(data):
    id_tanaman = input("Masukkan id tanaman yang akan dihapus: ")
    for row in data:
        if row[0].lower() == id_tanaman.lower():
            data.remove(row)
            save_data(data)
            print("Data berhasil dihapus!")
            return
    print("ID tanaman tidak ditemukan!")

def main():
    os.system('cls')
    data = load_data()
    while True:
        print("""
===================================
=  _   _   _____   __  _   _   _  =
= | \_/ | | ____| |  \| | | | | | =
= |  _  | | __|_  |  _  | | |_| | =
= |_| |_| |_____| |_| |_|  \___/  =
=                                 =
===================================

[1]. Tampilkan Data
[2]. Tambah Data
[3]. Update Data 
[4]. Hapus Data
[5]. Sorting Data 
[6]. Searching Data
[0]. Back
""")
        choice = input("Pilihan Anda (1/2/3/4/5/6/0) : ")

        if choice == "1":
            read_data(data)
        elif choice == "2":
            create_data(data)
            save_data(data)
        elif choice == "3":
            update_data(data)
            save_data(data)
        elif choice == "4":
            delete_data(data)
            save_data(data)
        elif choice == "5":
            sorting()
        elif choice == "6":
            searching()
        elif choice == "0":
            save_data(data)
            os.system('cls')
            print("""
========================================================================
=  _____   _   _    ___    __  _   _   __     __   __  ____    _    _  =
= |_   _| | |_| |  /   \  |  \| | | |_/ /     \ \_/ / / __ \  | |  | | =
=   | |   |  _  | |  _  | |  _  | |  _ |       \   / | |__| | | |__| | =
=   |_|   |_| |_| |_| |_| |_| \_| |_| \_\       |_|   \____/   \____/  =
=                                                                      =
========================================================================
====================== FOR USING THIS APPLICATION ======================
""")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def partition(array, low, high, indexx):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j][indexx] <= pivot[indexx]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high, indexx):
    if low < high:
        pi = partition(array, low, high, indexx)
        quickSort(array, low, pi - 1, indexx)
        quickSort(array, pi + 1, high, indexx)

def sorting():
    print(""" 
 ====================
 |    _        _    |
 |   / \      | |   | [1]. Sorting Bedasarkan ID
 |  /   \     | |   | [2]. Sorting Bedasarkan Nama Tanaman
 | /_   _\   _| |_  | [3]. Sorting Bedasarkan Tanggal Panen 
 |   | |    \     / | [4]. Sorting Bedasarkan Hasil Panen
 |   | |     \   /  | [5]. Sorting Bedasarkan Harga/kg
 |   |_|      \_/   | [0]. Back
 |                  | 
 ====================
 """)
    jawab = input("Pilihan Anda (1/2/3/4/5/0) : ")
    while True:
        if jawab == "1":
            quickSort(data, 0, len(data) - 1, 0)
            print("\n=====================================================================")
            print("=============== Hasil Sorting Berdasarkan ID Tanaman ================")
            print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))
            sorting()
            break
        elif jawab == "2":
            quickSort(data, 0, len(data) - 1, 1)
            print("\n=====================================================================")
            print("============== Hasil Sorting Berdasarkan Nama Tanaman ===============")
            print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))
            sorting()
            break
        elif jawab == "3":
            quickSort(data, 0, len(data) - 1, 2)
            print("\n=====================================================================")
            print("============== Hasil Sorting Berdasarkan Tanggal Panen ==============")
            print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))
            sorting()
            break
        elif jawab == "4":
            quickSort(data, 0, len(data) - 1, 3)
            print("\n=====================================================================")
            print("============== Hasil Sorting Berdasarkan Hasil Panen ================")
            print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))
            sorting()
            break
        elif jawab == "5":
            quickSort(data, 0, len(data) - 1, 4)
            print("\n=====================================================================")
            print("================ Hasil Sorting Berdasarkan Harga/kg =================")
            print(tabulate.tabulate(data, headers=["ID","Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"], tablefmt="fancy_grid"))
            sorting()
            break
        elif jawab == "0":
            main()
            break
        else:
            print("Inputan yang anda masukkan tidak terdapat dalam opsi, silahkan coba kembali")
            sleep(3.0)
            sorting()
            break

def searching():
    print(""" 
 ====================
 |      ______      | 
 |    / ______ \    | [1]. Searching Bedasarkan ID
 |   | |      | |   | [2]. Searching Bedasarkan Nama Tanaman
 |   | |______| |   | [3]. Searching Bedasarkan Tanggal Panen 
 |    \ ___    /    | [4]. Searching Bedasarkan Hasil Panen
 |          \  \    | [5]. Searching Bedasarkan Harga/kg
 |           \ _\   | [0]. Back
 |                  | 
 ====================
 """)
    option = int(input("Pilihan Anda (1/2/3/4/5/0) : "))
    while True :
        if option == 1:
            read_data(data)
            id = input("ID : ")
            print_binary_search(data, id, 0)
            searching()
            break
        elif option == 2:
            read_data(data)
            nama = input("Nama : ")
            print_binary_search(data, nama, 1)
            searching()
            break
        elif option == 3:
            read_data(data)
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            print_binary_search(data, tanggal, 2)
            searching()
            break
        elif option == 4:
            read_data(data)
            panen = input("Hasil Panen : ")
            print_binary_search(data, panen, 3)
            searching()
            break
        elif option == 5:
            read_data(data)
            harga = input("Harga : ")
            print_binary_search(data, harga, 4)
            searching()
            break
        elif option == 0:
            clear()
            sleep(0.5)
            main()
            break
        else:
            print("Inputan yang anda masukkan tidak terdapat dalam opsi, silahkan coba kembali")
            sleep(3.0)
            searching()
            break

def binary_search(arr, target, column):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        current_value = arr[mid][column]

        if column == 1:
            current_value = current_value.lower()
        else:
            current_value = current_value

        if current_value == target:
            return mid
        elif current_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def print_binary_search(data, target, column):
    matching_data = []

    for row in data:
        if str(row[column]).lower() == target.lower():
            matching_data.append(row)

    if len(matching_data) > 0:
        table_result = tabulate.tabulate(matching_data,
                                         headers=["ID", "Nama Tanaman", "Tanggal Panen", "Hasil Panen", "Harga Per Kilo"],
                                         tablefmt="fancy_grid")
        print("------------- Table -------------")
        print(table_result)
    else:
        print("Data tidak ditemukan dalam tabel.")

begin()
access(option)