utang=int(input("masukkan utang:"))
if utang >=100000:
    bunga=10/100
    total_utang=bunga*utang
    potongan=bunga-utang
elif utang <100000:
    bunga=5/100
    total_utang=bunga*utang
    potongan=bunga-utang
else:
    print("tidak ada bunga")
print("total utang:",total_utang)
print("potongan:",potongan)
          

