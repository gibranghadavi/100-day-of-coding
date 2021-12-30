#day 19
harga = int(input("masuk harga :"))
kode_promo =input("masukkan kode promo :")
kode_promo= kode_promo.lower()
if kode_promo == "oppo":
    diskon = harga*40/100
elif kode_promo == "vivo":
    diskon = hatga*45/100
elif kode_promo == "xiomi":
    diskon = harga*60/100
else:
    print("merek hp anda salah")
pay = harga - diskon
print("diskon hari ini:",format(kode_promo))
print("jumlah diskon :",format(diskon))
print("jumlah yang harus di bayar :",format (pay))
                            
