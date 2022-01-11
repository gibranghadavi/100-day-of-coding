#day 31
golongan =int(input("masukkan golongan :"))
if golongan == 1 :
    gaji_pokok = 1500000
elif golongan == 2 :
    gaji_pokok = 1200000
elif golongan == 3 :
    gaji_pokok = 1000000

print("gaji pokok :",gaji_pokok)
tahun_masuk_kerja =int(input("tahun masuk kerja :"))
tahun_kerja = 2011
total_kerja = tahun_masuk_kerja - tahun_kerja
print("total_kerja :",total_kerja)
masa_kerja_karyawan =int(input("masukkan masa kerja karyawan :"))

if masa_kerja_karyawan >=7 :
    bonus = 150000
else:
    bonus = 0 
gaji_bersih = gaji_pokok + bonus
print("bonus :",format(bonus))
print("gaji_bersih :",gaji_bersih)
