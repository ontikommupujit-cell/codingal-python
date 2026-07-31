def palind(a):
    e=len(a)-1
    s=0
    while(s<e):
        if(a[s]!=a[e]):
            return False
        s+=1
        e-=1
    return True
a=(10,20,30,40,50,40,30,20,10)
if palind(a):
    print('the muumber is palindrom')
else:
    print('the number is not palindrom')
