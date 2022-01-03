#day 23
bayaran =int(input("masukkan bayaran:"))
jml_yang_dibelih =int(input("masukkan jml yang dibelih :"))
if jml_yang_dibelih >= 10 and 19 :
    diskon = 20/100
    diskon_yang_didapat = jml_yang_dibelih - diskon
    juamlah_yang_di_hemat = bayaran - diskon
elif jml_yang_dibelih >= 20 and 49 :
    diskon = 30/100
    diskon_yang_didapat = jml_yang_dibelih - diskon
    juamlah_yang_di_hemat = bayaran - diskon
elif jml_yang_dibelih >= 50 and 69 :
    diskon = 35/100
    diskon_yang_didapat = jml_yang_dibelih - diskon
    juamlah_yang_di_hemat = bayaran - diskon
elif jml_yang_dibelih >= 70 and 99 :
    diskon = 40/100
    diskon_yang_didapat = jml_yang_dibelih - diskon
    juamlah_yang_di_hemat = bayaran - diskon
elif jml_yang_dibelih >= 100 :
    diskon = 50/100
    diskon_yang_didapat = jml_yang_dibelih - diskon
    juamlah_yang_di_hemat = bayaran - diskon
else:
    print("tidak ada diskon")

print("diskon_yang_didapat :",diskon_yang_didapat)
print("juamlah_yang_di_hemat :",juamlah_yang_di_hemat)
