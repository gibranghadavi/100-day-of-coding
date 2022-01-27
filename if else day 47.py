gaji_pensiun =int(input("masukkan gaji pensiunan :"))
if gaji_pensiun >= 5000000 :
    bunga =5/100 * gaj_pensiun
    potongan = gaji_pensiun - bunga
    print ("bunga 5%")

elif gaji_pensiun < 5000000 :
    bunga =3/100 * gaji_pensiun
    potongan = gaji_pensiun - bunga
    print ("bunga 3%")
else:
    print("tidak memiliki bunga")
    
print("potongan :",potongan)
