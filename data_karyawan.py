import csv
import os

def tambah_karyawan(nama, jabatan):
    with open('karyawan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, jabatan])
    print("Karyawan berhasil ditambahkan.")

def hapus_karyawan(nama):
    if not os.path.exists('karyawan.csv'):
        print("File tidak ditemukan.")
        return

    rows = []
    found = False
    with open('karyawan.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != nama:
                rows.append(row)
            else:
                found = True

    if found:
        with open('karyawan.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Karyawan {nama} berhasil dihapus.")
    else:
        print(f"Karyawan {nama} tidak ditemukan.")

def lihat_karyawan():
    if not os.path.exists('karyawan.csv'):
        print("File tidak ditemukan.")
        return

    with open('karyawan.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        print("Data Karyawan:")
        for row in reader:
            print(f"Nama: {row[0]}, Jabatan: {row[1]}")

def menu():
    while True:
        print("\n--- Sistem Manajemen Data Karyawan ---")
        print("1. Tambah Karyawan")
        print("2. Hapus Karyawan")
        print("3. Lihat Karyawan")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            nama = input("Masukkan nama karyawan: ")
            jabatan = input("Masukkan jabatan karyawan: ")
            tambah_karyawan(nama, jabatan)
        elif pilihan == '2':
            nama = input("Masukkan nama karyawan yang akan dihapus: ")
            hapus_karyawan(nama)
        elif pilihan == '3':
            lihat_karyawan()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
if __name__ == "__main__":
    menu()