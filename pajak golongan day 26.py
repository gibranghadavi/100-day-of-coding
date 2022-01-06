gaji =int(input("masukkan gaji :"))
golongan = input("masukkan golongan :")
if golongan == "pertama" :
    pajak = 20/100 * gaji
    gaji_bersih = gaji - pajak
elif golongan == "kedua" :
    pajak = 15/100 * gaji
    gaji_bersih = gaji - pajak
elif golongan == "ketiga" :
    pajak = 10/100 * gaji
    gaji_bersih = gaji -  pajak
print("pajak :",pajak)
print("gaji bersih :", gaji_bersih)
