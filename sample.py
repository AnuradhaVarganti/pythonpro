f=open("c:ram/sales.py")
lines=f.readlines()
qrep={}
for line in lines:
    w=line.split(',')
    dt=w[0]
    amt=int(w[-1].split('\n')[0])
    m=int(date.split('/')[0])
    q=4
    if m<4:
        q=1
    elif  m<7:
        q=2
    elif  m<10:
        q=3
   if qrep.get(q)==none:
       qrep(q)=amt
lese
        qrep(q)+=amt

    qr=qrep.key()
    q1=[]
    q2=[]
    for v in qr:
        amt=qrep(v)
        info=(v,amt)
        q1.append(info)
        q2.append(info)

clist=[]
for v1 in q1:
    for v2 in q2:
        if v1[0]-v2[0]==1:
            cv=v1[-1]
            pv=v2[-1]
            grate=((cv-pv)/pv)*100
            t=(v1[0],cv,v2[0],pv,grate)
            clist.append(t)
            print(clist)
