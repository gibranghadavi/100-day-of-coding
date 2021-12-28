penghasilan =int(input("masukkan penghasilan :"))
jenis_pekerjaan =input("masuk jenis pekerjaan :")

if (penghasilan >= 3000000 and 5000000 ):
    pajak = (5/100) + (10/100)+ (0/100)
    gaji_bersih = penghasilan - pajak
elif (jenis_pekerjaan == "PNS" ):
    pajak = (5/100)+ (10/100)+ 5
    gaji_bersih = penghasilan - (5/100)
elif (jenis_pekerjaan == "non"):
    pajak = (0/100)
    gaji_bersih = penghasilan - (0/100)
print("gaji_bersih:",gaji_bersih)

                
