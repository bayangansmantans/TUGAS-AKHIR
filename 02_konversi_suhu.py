# Tugas 02 - Konversi Suhu
# Nama: Raka Sendjaya
# NIM: 22/123456/TK/12345

def konversi_suhu():
    print("=== Konversi Suhu ===")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")
    
    pilihan = input("Pilih konversi (1/2/3): ")
    suhu = float(input("Masukkan suhu: "))
    
    if pilihan == "1":
        hasil = (suhu * 9/5) + 32
        print(f"{suhu}°C = {hasil:.2f}°F")
    elif pilihan == "2":
        hasil = (suhu - 32) * 5/9
        print(f"{suhu}°F = {hasil:.2f}°C")
    elif pilihan == "3":
        hasil = suhu + 273.15
        print(f"{suhu}°C = {hasil:.2f}K")
    else:
        print("Pilihan tidak valid!")

konversi_suhu()
