gaji = int (input ("masukkan gaji perbulan : "))
if gaji >= 10000000 :
    pajak = 2/100
    total_pajak = pajak * gaji
    gaji_bersih = gaji - total_pajak
elif gaji >= 20000000:
    pajak = 5/100
    total_pajak = pajak - total_pajak
elif  gaji < 10000000:
    gaji_bersih = gaji

print (gaji_bersih)
