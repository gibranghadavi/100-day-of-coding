i=0
while i <1:
    print("pilih menu di bawah ini:")
    print('[1].meter ke centimeter')
    print('[1].meter ke kilometer')
    i+=1
menu = int(input("masukkan manu 1 atau menu 2 :"))
def nama(bilangan):
    if menu == 1:
        centimeter = bilangan*25
        return centimeter
    elif menu == 2:
        kilometer = bilangan/25
        return kilometer
    else:
        print("menu yang anda masukkan tidak ada")
cetak=nama(40)
print(cetak)
