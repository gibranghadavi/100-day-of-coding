#program 3
total_belanja = int(input("masukkan total belanja :"))
kode_harian = input("masukkan kode harian :")
kode_harian = kode_harian.lower()
if kode_harian == "senin":
    discount = total_belanja*5/100
    
elif kode_harian == "selasa":
    discount = total_belanja*6/100
    
elif kode_harian == "rabu":
    discount = total_belanja*7/100
    
elif kode_harian == "kamis":
    discount = total_belanja*8/100
    
elif kode_harian == "jumat":
    discount = total_belanja*9/100
    
elif kode_harian == "sabtu":
    discount = total_belanja*10/100
    
elif kode_harian == "minggu":
    discount = total_belanja*11/100
else:
    print("kode harian anda salah")

pay = round(total_belanja - discount)
print("diskon hari ini :",format(kode_harian))
print("jumlah discount :",format(discount))
print("jumlah yang harus dibayar :",format (pay))


 


