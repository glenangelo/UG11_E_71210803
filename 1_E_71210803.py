def pangkatAngka(angkaPangkat):
    print("ingin memodifikasi pangkat ? (yes/no)")
    p = input(": ")
    if p == "yes":
        aa = float(input("Masukkan nilai pangkat : "))
        hasil1 = a ** aa
        print("Hasil dari",a,"^",aa," = ",hasil1)

    elif p == "no":
        hasil2 = a ** 2
        print("Hasil dari",a,"^2"," = ",hasil2)

    else :
        print("input tidak diketahui")

def akarBilangan(angkaAkar):
    print("ingin memodifikasi akar ? (yes/no)")
    p = input(": ")
    if p == "yes":
        aa = float(input("Masukkan nilai akar : "))
        hasil1 = a ** (1/aa)
        print("Hasil akar pangkat ", aa, " dari ", a, " = ",'{0:.2f}'.format(hasil1))
    elif p == "no":
        hasil2 = a ** (1/2)
        print("Hasil akar pangkat 2 dari",a," = ",'{0:.2f}'.format(hasil2))
    else :
        print("input tidak diketahui")

if __name__ == '__main__':
    print("""
    Menu Program Yang Tersedia
    1. pangkatkan angka
    2. akarkan bilangan""")
    pilihan = int(input("Masukkan pilihan yang diinginkan : "))

    if pilihan == 1:
        print("Masukkan angka yang ingin di Pangkatkan")
        a = float(input("Angka : "))
        pangkatAngka(a)

    elif pilihan == 2:
        print("Masukkan angka yang ingin di akar")
        a = float(input("Angka : "))
        akarBilangan(a)
    else :
        print("input tidak diketahui")
