harga =int(input("masukkan harga :"))
if harga < 100000:
    pajak = 2/100 * harga
    potongan = pajak - harga
    print("pajak : 2%")
elif harga >= 100000:
    pajak = 5/100 * harga
    potongan = pajak - harga
    print("pajak : 5%")
print("potongan :",potongan)
