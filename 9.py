#تمرین1.9
b={"ali":20,"al":20}
print("تمرین1.9","ali" in b)

#تمرین2.9
print("تمرین2.9",0 in b)

#تمرین3.9

a={"moein":20,"askari":21,"20":22}
c={"moein":20,"askari":21,"20":22}
a=sorted(a)
print("تمرین3.9",a)
#a=sum(a)ارور
#print(a)
del a[0]
print("تمرین3.9",a)
#تمرین4.9

a.pop(1)
print("تمرین4.9",a)
a.append(2)
print("تمرین4.9",a)
a.remove(2)
print("تمرین4.9",a)

#تمرین5.9

r="moein"
t=""
for i in c:
    t=i
    if(r==t):
        print("تمرین5.9",t)

#تمرین6.9
v={}
for i, h in c.items():

    v[i]=h

print("تمرین6.9",v)
