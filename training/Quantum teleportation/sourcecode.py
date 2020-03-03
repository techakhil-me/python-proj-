f = open('i.txt', 'r')
l = list(f)
f.close()
T = int(l[0].replace('\n', ''))
for p in range(1,T+1):
    x,y = l[p].replace('\n', '').split(" ")
    x0,y0 = l[p+1].replace('\n', '').split(" ")
    z = l[p+2].replace('\n', '')
    L=[]
    x,y,x0,y0,z = int(x),int(y),int(x0),int(y0),int(z)
    for q in range(1,z+1):
        xi,yi,xo,yo = l[p+2+q].replace('\n', '').split(" ")
        xi,yi,xo,yo = int(xi),int(yi),int(xo),int(yo)
        L.append([xi,yi,xo,yo])
        
    print(L)