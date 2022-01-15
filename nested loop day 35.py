i = 2
while(i < 100):
    d = 2
    while(d <= (i/d)):
        if not(i%d):break
        d = d + 2
    if ( d > i/d): print(i,"is prime")
    i = i + 1
print("good bay")
        
