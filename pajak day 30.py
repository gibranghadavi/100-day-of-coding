harga =int(input("masukkan harga :"))
luas =int(input("masukkan luas :"))
if harga >= 1000000:
    pajak = 10/100 * harga
    dijual = pajak * luas
   
elif harga >= 100000:
    pajak = 5/100 * harga
    dijual = pajak * luas
potongan = dijual - harga
print("potongan :",potongan)
print("dijual :",dijual)
