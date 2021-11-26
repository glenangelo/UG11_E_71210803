def hitungKata(kata):
    list = kata.split( )
    jumlah = len(list)
    print(jumlah)

if __name__ == '__main__':
    print("""
    Program Manipulasi String
    Piihan Menu :
    1. Hitung kata
    2. cek kata
    3. ubah kata""")
    pilihan = int(input("Pilihan anda :"))

    if pilihan == 1:
        kata = input("Masukkan sebuah kalimat/kata :")
        hitungKata(kata)