def halo(panggilan):
    print ('Halo %s!' % panggilan)
def cetak_maksimal(a, b):
    if a > b:
        print ('%s merupakan nilai maksimal' % a)
    elif a == b:
        print ('%s sama dengan %s' % (a, b))
    else:
        print ('%s merupakan nilai maksimal' % b)
halo('bro')  
halo('nayyyyy')  
cetak_maksimal(10, 100)
x = 6
y = 4
cetak_maksimal(x, y)
