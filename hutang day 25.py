hutang =int(input("masukkan hutang :"))
jenis_pekerjaan =input("masukkan jenis pekerjaan :")
setahun = 12
if jenis_pekerjaan == "pns":
    if hutang >=5000000 and jenis_pekerjaan == "pns":
        bunga = 10/100 + 5/100
        total_hutang = hutang * setahun
        total_hutan_setahun = total_hutang * bunga 
        print(" bunga pns :15%")
elif hutang >= 5000000:
    bunga = 10/100
    total_hutang = hutang * setahun
    total_hutan_setahun = total_hutang * bunga
    print("bunga :10%")
elif hutang < 5000000:
    bunga = 5/100
    total_hutang = hutang * setahun
    total_hutan_setahun = total_hutang * bunga
    print("bunga :5%")

print("total_hutan_setahun :",total_hutan_setahun)
