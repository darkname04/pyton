#تمرین1.8
a=[122,43,88,44]
a.sort()
print("تمرین1.8",a)
#تمرین2.8
s=[122,43,98,88,44]

print("تمربن2.8",sorted(s))

#تمرین3.8
#w=[122,43,98,"ghujg","moein",'m',88,44]ارور
w=[122,43,98,88,44]
#q=['moein','  askarpoor']
print("تمرین3.8",sum(w))
#print(sum(q))ارور
#تمرین4.8
moein="moKJJHMD545km1323kdfkKDK12313JdjFJKL"
m=[]
n=[]
k=[]

for i in moein:
    if (i.islower()):
        m.append(i)
    elif(not(i.islower() or i.isupper())):
        k.append(i)
    else:
        n.append(i)
print("تمرین4.8",m)
print("تمرین4.8",n)
print("تمرین4.8",k)

#تمرین5.8
w=[122,43,98,88,44]
a=[122,43,88,44,88]
#d=w-aارور
#6.8تمریبن
mm=['moein','askary',979,75,453,544]
k=0
t=len(mm)
for o in mm:

    del mm[k:t]

print("تمرین6.8",mm)
#تمرینن7.8
f=["jj",98,'hj',7,'87']
f.remove('87')
print("تمرین7.8",f)
f.pop(3)
print("تمرین7.8",f)
del f[0:2]
print("تمرین7.8",f)

#تمرین8.8
f=["jj",98,'hj',7,'87']
p=["jj",98,'hj',7,'87']
h=[]
k=0
if(len(f)>=len(p)):
    for i in p:
        h.append(f[k])
        h.append(p[k])
        k+=1
else:
    for i in f:
        h.append(f[k])
        h.append(p[k])
        k+=1
print("تمرین8.8",h)

#تمرین9.8
f=["jj",98,'hj',7,'87']
p=["jj",98,'hj',7,'87']
h=[]
k=0
for i in f:
    h.append(f[k]+p[k])

    k+=1
print("تمرین9.8",h)