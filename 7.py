#تمرین1.7
a="a"
b="x"
#ترتیب کاراکترها براساس ترتیب حروف در الفبا است.
if(a != b):
    print("تمرین1.7","yes1")
if (a == b):
    print("تمرین1.7","yes2")
if (a >= b):
    print("تمرین1.7","yes3")
if (a <= b):
    print("تمرین1.7","yes4")
if (a < b):
    print("تمرین1.7","yes5")
if (a > b):
    print("تمرین1.7","yes6")

#تمرین2.7

def c(b,x):

    if(not(b in x)):
        return False
print("تمرین2.7",c("abb","abc"))

#تمرین3.7
txt="moein.txt"
a=open(txt)
print("تمرین3.7",a.readlines())
#print(a.readline())

#تمرین4.7
m=["ali",False,"moein","ali",32,54,4.5,True]
for i in m:
    print("تمرین4.7",i)
#تمرین5.7
m.reverse()
for i in m:
    print("تمرین5.7",i)
#تمرین6.7
if(m==m.reverse()):
    print("true")
else:
    print("تمرین6.7","false")
#تمرین7.7
c="moein "
print("تمرین7.7",4*c)

