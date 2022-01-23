harga =int(input("masukkan harga :"))
luas =int(input("masukkanan luas :"))
if harga < 1000000 :
    pajak = 2/100 * harga
    harga_jual = harga * luas
    potongan = pajak - harga_jual
    
elif harga >= 1000000:
    pajak = 5/100 * harga
    harga_jual = pajak * luas
    potongan = pajak - harga_jual
    
print("harga jual :",harga_jual)
print("potongan :",potongan)
