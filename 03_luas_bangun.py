# Tugas 03 - Menghitung Luas Bangun Datar
# Nama: Raka Sendjaya
# NIM: 22/123456/TK/12345

import math

def luas_bangun():
    print("=== Luas Bangun Datar ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Segitiga")

    pilihan = input("Pilih bangun (1/2/3/4): ")

    if pilihan == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi ** 2
        print(f"Luas persegi = {luas}")
    elif pilihan == "2":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        luas = p * l
        print(f"Luas persegi panjang = {luas}")
    elif pilihan == "3":
        r = float(input("Masukkan jari-jari: "))
        luas = math.pi * r ** 2
        print(f"Luas lingkaran = {luas:.2f}")
    elif pilihan == "4":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga = {luas}")
    else:
        print("Pilihan tidak valid!")

luas_bangun()
