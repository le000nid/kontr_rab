import io
f=io.open('mat_dv.txt', 'r', encoding='utf-8')
l = [i.strip() for i in f]
alg=0
algindex=[]
geom=0
geomindex=[]
for i in range(len(l)):
    p1=l[i].find(' ')
    p2=l[i].find(' ', p1+1)
    p3=l[i].find(' ', p2+1)
    p4=l[i].find(' ', p3+1)
    if int(l[i][p3:p4])>alg:
        alg=int(l[i][p3:p4])
        algindex=[i]
    elif int(l[i][p3:p4])==alg:
        algindex.append(i)
    if int(l[i][p4:])>geom:
        geom=int(l[i][p4:])
        geomindex=[i]
    elif int(l[i][p4:])==geom:
        geomindex.append(i)
for i in range(len(algindex)):
    p1=l[algindex[i]].find(' ')
    p2=l[algindex[i]].find(' ', p1+1)
    p3=l[algindex[i]].find(' ', p2+1)
    p4=l[algindex[i]].find(' ', p3+1)
    print(l[algindex[i]][:p4])
for i in range(len(geomindex)):
    p1=l[geomindex[i]].find(' ')
    p2=l[geomindex[i]].find(' ', p1+1)
    p3=l[geomindex[i]].find(' ', p2+1)
    p4=l[geomindex[i]].find(' ', p3+1)
    print(l[geomindex[i]][:p3],l[geomindex[i]][p4:])

