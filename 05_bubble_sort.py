# Tugas 05 - Sorting Bubble Sort
# Nama: Raka Sendjaya
# NIM: 22/123456/TK/12345

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    print("=== Bubble Sort ===")
    input_user = input("Masukkan angka dipisah spasi: ")
    angka = list(map(int, input_user.split()))
    
    print(f"Sebelum sorting: {angka}")
    hasil = bubble_sort(angka.copy())
    print(f"Sesudah sorting: {hasil}")

main()
