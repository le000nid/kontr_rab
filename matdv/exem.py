import io
f=io.open('mat_dv.txt', 'r', encoding='utf-8')
l = [i.strip() for i in f]
alg=0
algindex=[]
geom=0
geomindex=[]
dvb8=0
dvb8index=[]
dvb9=0
dvb9index=[]
dvb10=0
dvb10index=[]
dvb11=0
dvb11index=[]
for i in range(len(l)):
    p1=l[i].find(' ')
    p2=l[i].find(' ', p1+1)
    p3=l[i].find(' ', p2+1)
    p4=l[i].find(' ', p3+1)
    if int(l[i][p2:p3])==8 and int(l[i][p3:p4])+int(l[i][p4:])>dvb8:
        dvb8=int(l[i][p3:p4])+int(l[i][p4:])
        dvb8index=[i]
    elif int(l[i][p2:p3])==8 and int(l[i][p3:p4])+int(l[i][p4:])==dvb8:
        dvb8index.append(i)
    if int(l[i][p2:p3])==9 and int(l[i][p3:p4])+int(l[i][p4:])>dvb9:
        dvb9=int(l[i][p3:p4])+int(l[i][p4:])
        dvb9index=[i]   
    elif int(l[i][p2:p3])==9 and int(l[i][p3:p4])+int(l[i][p4:])==dvb9:
        dvb9index.append(i)
    if int(l[i][p2:p3])==10 and int(l[i][p3:p4])+int(l[i][p4:])>dvb10:
        dvb10=int(l[i][p3:p4])+int(l[i][p4:])
        dvb10index=[i]   
    elif int(l[i][p2:p3])==10 and int(l[i][p3:p4])+int(l[i][p4:])==dvb10:
        dvb10index.append(i)
    if int(l[i][p2:p3])==11 and int(l[i][p3:p4])+int(l[i][p4:])>dvb11:
        dvb11=int(l[i][p3:p4])+int(l[i][p4:])
        dvb11index=[i]   
    elif int(l[i][p2:p3])==11 and int(l[i][p3:p4])+int(l[i][p4:])==dvb11:
        dvb11index.append(i)
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
for i in range(len(dvb8index)):
    p1=l[dvb8index[i]].find(' ')
    p2=l[dvb8index[i]].find(' ', p1+1)
    p3=l[dvb8index[i]].find(' ', p2+1)
    p4=l[dvb8index[i]].find(' ', p3+1)
    print(l[dvb8index[i]][:p3], dvb8)
for i in range(len(dvb9index)):
    p1=l[dvb9index[i]].find(' ')
    p2=l[dvb9index[i]].find(' ', p1+1)
    p3=l[dvb9index[i]].find(' ', p2+1)
    p4=l[dvb9index[i]].find(' ', p3+1)
    print(l[dvb9index[i]][:p3], dvb9)
for i in range(len(dvb10index)):
    p1=l[dvb10index[i]].find(' ')
    p2=l[dvb10index[i]].find(' ', p1+1)
    p3=l[dvb10index[i]].find(' ', p2+1)
    p4=l[dvb10index[i]].find(' ', p3+1)
    print(l[dvb10index[i]][:p3], dvb10)
for i in range(len(dvb11index)):
    p1=l[dvb11index[i]].find(' ')
    p2=l[dvb11index[i]].find(' ', p1+1)
    p3=l[dvb11index[i]].find(' ', p2+1)
    p4=l[dvb11index[i]].find(' ', p3+1)
    print(l[dvb11index[i]][:p3], dvb11)
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

