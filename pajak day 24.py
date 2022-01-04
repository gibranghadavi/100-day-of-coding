harga_tanah =int(input("masukkan harga tanah :"))
luas = int(input("masukkan luas :"))
if harga_tanah >= 100000000 :
    pajak = 5/100
    potongan = harga_tanah * pajak
    dijual = luas * potongan
    print("pajak 5%")
elif harga_tanah >= 50000000 :
    pajak = 3/100
    potongan = harga_tanah * pajak
    dijual = luas * potongan
    print("pajak 3%")
elif harga_tanah < 50000000 :
    pajak = 1/100
    potongan = harga_tanah * luas
    dijual = pajak* potongan
    print("pajak 1%")
print("potongan :",potongan )
print("dijual :",dijual)
