gaji_perbulan = 5000000
pajak = 2.5/100
tidak_hadir = int(input("masukkan jumlah alpa:"))

if tidak_hadir > 5 :
    potongan = 25000 * tidak_hadir
    gaji_bersi = gaji_perbulan - potongan - pajak
    print("gaji perseorangan karyawan perbulan : Rp.",gaji_perbulan)
    print("gaji bersi karyawan:Rp",gaji_bersi)
    print("pajak:",pajak)
else:
    gaji_bersi = gaji_perbulan - pajak
    print("gaji bersi:Rp.",gaji_bersi)
