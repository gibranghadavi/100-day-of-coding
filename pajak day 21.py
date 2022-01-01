#day 21
gaji =int(input("masukkan gaji :"))
jenis_pekerjaan =input("masukkan jenis pekerjaan :")
if gaji >= 10000000 :
    pajak = 30/100
    gaji_bersih = gaji - pajak
elif gaji >= 20000000 :
    pajak = 20/100
    gaji_bersih = gaji - pajak
elif jenis_pekerjaan =="pns" :
    pajak = 15/100
    gaji_bersih = gaji - pajak
    
print("gaji_bersih :",gaji_bersih)
