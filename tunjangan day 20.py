 #day 20
nama_karyawan =input("masukkan nam karyawan :")
jumlah_anak =int(input("masukkan jumlah anak :"))
gaji_pokok = int(input("masukkan gaji pokok :"))
tunjangan_istri = (20/100) * gaji_pokok
tunjungan_anak = (5/100) + jumlah_anak * gaji_pokok
total_tunjangan = tunjangan_istri + tunjungan_anak
gaji_kotor = gaji_pokok + total_tunjangan
pajak = 10/100
gaji_bersih = gaji_kotor - pajak
                 
print("tunjangan_istri :",tunjangan_istri)
print("tunjungan_anak :",tunjungan_anak)
print("total_tunjangan :",total_tunjangan)
print("gaji_kotor :",gaji_kotor)
print("pajak :",pajak )
print("gaji_bersih :",gaji_bersih)

