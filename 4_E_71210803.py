import random

def generate(level):
    operasi = ['+', '-', '/', '*']
    if level == 1:
        n = random.randint(20,50)
        m = random.randint(20,50)
        operator = random.choice(operasi)
        print("Berapakah hasil dari ",n,operator,m)
        hasil = eval(str(n) + operator + str(m))
        hasil2 = '{0:.3f}'.format(hasil)
        jawaban = float(input("Masukkan Jawaban Anda : "))
        jawaban2 = '{0:.3f}'.format(jawaban)

        cekHasil(hasil2,jawaban2)

    elif level == 2:
        a = random.randint(20,50)
        b = random.randint(20,50)
        c = random.randint(20,50)

        operator = random.choice(operasi)
        operator2 = random.choice(operasi)

        print("Berapakah hasil dari ", a, operator, b, operator2, c)
        hasil = eval(str(a) + operator + str(b) + operator2 + str(c))
        hasil2 = '{0:.3f}'.format(hasil)
        jawaban = float(input("Masukkan Jawaban Anda : "))
        jawaban2 = '{0:.3f}'.format(jawaban)

        cekHasil(hasil2,jawaban2)

    elif level == 3:
        a = random.randint(20, 100)
        b = random.randint(20, 100)
        c = random.randint(20, 100)
        d = random.randint(20, 100)

        operator = random.choice(operasi)
        operator2 = random.choice(operasi)
        operator3 = random.choice(operasi)

        print("Berapakah hasil dari ", a, operator, b, operator2, c, operator3, d)
        hasil = eval(str(a) + operator + str(b) + operator2 + str(c) + operator3 + str(d))
        hasil2 = '{0:.3f}'.format(hasil)
        jawaban = float(input("Masukkan Jawaban Anda : "))
        jawaban2 =  '{0:.3f}'.format(jawaban)
        cekHasil(hasil2,jawaban2)
    else:
        print("Pilihan level tidak tersedia sob !")

def cekHasil(hasil, jawaban):
    if jawaban == hasil:
        print("Jawaban Anda Benar !")
    else:
        print("Jawaban Anda Masih Salah !")

if __name__ == '__main__':
    print("""
    =====Program test aritmatika dasar=====
    Pilihan level yang tersedia :
    1. Easy
    2. Medium
    3. Hard""")

    level = int(input("Masukkan tingkatan yang ingin anda coba : "))
    generate(level)