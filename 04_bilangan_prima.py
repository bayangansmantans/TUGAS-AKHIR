# Tugas 04 - Bilangan Prima
# Nama: Raka Sendjaya
# NIM: 22/123456/TK/12345

def adalah_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cari_prima():
    print("=== Bilangan Prima ===")
    batas = int(input("Masukkan batas atas: "))
    
    prima = [n for n in range(2, batas+1) if adalah_prima(n)]
    
    print(f"Bilangan prima dari 2 sampai {batas}:")
    print(prima)
    print(f"Total: {len(prima)} bilangan prima")

cari_prima()
