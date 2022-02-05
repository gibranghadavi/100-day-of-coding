harga=int(input("masukkan harga:"))
if harga < 100000:
    diskon =2/100*harga
    potongan = diskon-harga
elif harga >= 100000:
    diskon = 4/100*harga
    potongan = diskon-harga
else:
    print("tidak ada diskon")
print("potongan :",potongan)
