#day 18
gaji =int(input("masukkan gaji :"))
jenis_pekerjaan = "PNS" , "honor"
if (gaji >= 5000000 and 10000000 ):
    pajak = (10/100)+(20/100)
    gaji_bersih = gaji * pajak
elif(gaji >= 10000000 ):
    pajak = (20/100)
    gaji_bersih = gaji * pajak
elif(jenis_pekerjaan == PNS):
    pajak = (35/100)
    gaji_bersih = jenis_pekerjaan * pajak
elif(jenis_pekerjaan == honor):
    pajak = (0/100)
    gaji_bersih = jenis_pekerjaan*pajak
print("gaji bersih :",gaji_bersih)
