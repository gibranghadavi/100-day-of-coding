nama = "gibran_ghadavi"
nim = "D0221001"
gaji_pokok = 1000000
gaji_lembur_perjam = 5000
lama_lembur = 1
gaji_lembur = gaji_lembur_perjam * lama_lembur
pajak =10/100

gaji_kotor = gaji_pokok + gaji_lembur
potongan = gaji_kotor * pajak
gaji_bersi = gaji_kotor - potongan

print("nama :",nama,"(",nim,")")
print("gaji_pokok :",gaji_pokok)
print("gaji_lembur :",gaji_lembur)
print("gaji_kotor :",gaji_kotor)
print("pajak :",pajak)
print("potongan :",(potongan))
print("gaji_bersi :",(gaji_bersi))
