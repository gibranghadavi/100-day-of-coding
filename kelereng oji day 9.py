#kelereng oji
kelereng_oji =int(input("kelereng_oji:")) 
kalah_dari_pila =int(input("kalah_dari_pila:"))
oji_membeli_kelereng = 250
jumlah_kelereng_oji_sekarang = kelereng_oji - kalah_dari_pila + oji_membeli_kelereng
print("jumlah_kelereng_oji_sekarang:",jumlah_kelereng_oji_sekarang)

#polpoin
harga_satu_bolpoin =int(input("harga_satu_bolpoin:"))
satu_lusin =int(input("satu_lusin:"))
lembar_uang =5*5000
membayar = harga_satu_bolpoin * satu_lusin - lembar_uang
print("membayar:",membayar)

#if kelereng oji
kelereng_oji =int(input("kelereng_oji:")) 
kalah_dari_pila =int(input("kalah_dari_pila:"))
oji_membeli_kelereng = 250

if(kalah_dari_pila != kelereng_oji):
    jumlah_kelereng_oji_sekarang = kelereng_oji - kalah_dari_pila + oji_membeli_kelereng
    print("jumlah_kelereng_oji_sekarang:",jumlah_kelereng_oji_sekarang)

#if polpoin
harga_satu_bolpoin =int(input("harga_satu_bolpoin:"))
satu_lusin =int(input("satu_lusin:"))
lembar_uang =5*5000
if(satu_lusin !=harga_satu_bolpoin):
    membayar = harga_satu_bolpoin * satu_lusin - lembar_uang
    print("membayar:",membayar)
