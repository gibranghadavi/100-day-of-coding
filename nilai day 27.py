nilai_MTK = int(input("masukkan nilai MTK :"))
nilai_B_ingg = int(input("masukkan nilai B.ingg :"))
nilai_B_indo = int(input("masukkan nilai B.indo :"))
minat = input("masukkan minat :")
minat_jurusan = ["1.teknik elektro","2.teknik mesin","3.pariwisata"]
print(minat_jurusan)
rata_rata_nilai =(nilai_MTK+nilai_B_ingg+nilai_B_indo)/3
if rata_rata_nilai <70 :
    print("skor anda dinyatakan tidak lolos karena skor anda adlah skor")
elif rata_rata_nilai == 70 :
    print("skor anda adalah skor , anda dinyatakan lolos kebidang berikut ")
    if minat == 1:
        print("teknik elektro")
    elif minat == 2:
        print("teknik mesin")
    else:
        print("pariwisata")
elif rata_rata_nilai > 70 :
    print("anda bebas memilih yang anda suka")


