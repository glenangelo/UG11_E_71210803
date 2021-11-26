def hurufTengah(kata):
    a = len(kata)

    if a > 4:
       if a % 2 == 0:
            tengah = int(a/2)
            hurufTengah = kata[tengah-1:tengah+1]
            return hurufTengah
       else:
            tengah = int(a/2)
            hurufTengah = kata[tengah-1:tengah+2]
            return hurufTengah
    else:
        if a % 2 == 0:
            tengah = int(a / 2)
            hurufTengah = kata[tengah-1:tengah + 1]
            return hurufTengah
        else:
            tengah = int(a / 2)
            hurufTengah = kata[tengah]
            return hurufTengah

if __name__ == '__main__':
    kata = input("Masukkan kata : ")
    hasil = hurufTengah(kata)
    print("Huruf tengah pada kata",kata,"adalah",hasil)
