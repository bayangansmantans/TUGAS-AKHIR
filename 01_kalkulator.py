# Tugas 01 - Kalkulator Sederhana
# Nama: Raka Sendjaya
# NIM: 22/123456/TK/12345

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Operasi: +, -, *, /")
    
    angka1 = float(input("Masukkan angka pertama: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))
    
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            print("Error: Pembagi tidak boleh nol!")
            return
        hasil = angka1 / angka2
    else:
        print("Operasi tidak valid!")
        return
    
    print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")

kalkulator()
