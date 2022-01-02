#day 22
jumlah_yang_dibeli =int(input("masukkan jumlah yang dibeli :"))
satu_semen = 50000
if jumlah_yang_dibeli == 100 :
    potongan = 2.5/100 
    total_yang_dibayar =  satu_semen  * jumlah_yang_dibeli - potongan
elif jumlah_yang_dibeli == 200 :
    potongan = 10/100 
    total_yang_dibayar =  satu_semen * jumlah_yang_dibeli - potongan
else:
    print("tidak ada potongan")
print(" total_yang_dibayar :", total_yang_dibayar)


