#تمرین1.5
import math


def sinx(opp,nyp):
    x=opp/nyp
    return x
def cosx(opp,adj):
    y=opp/adj
    return y
m=sinx(43,9)+cosx(6,9)
print( "تمرین1.5:", m)


#تمرین2.5
d=(sinx(43,9)/cosx(6,9))+sinx(43,9)
print( "تمرین2.5:", d)

#تمرین3.5
def m (x,y,t):
    w=math.sqrt((x-y)/t)
    print("تمرین3.5:",w)
m(6,3,9)

#تمرین4.5
def n (x1,a1,h1,y1):
    q=x1-a1*(2*(h1-y1))
    print("تمرین4.5:",q)
n(4,6,7,8)

#تمرین5.5

def a (name):
    x=range(len(name))
    print("تمرین5.5:",x)
a("moein")


#تمرین6.5

def b(name):
    if(name[0]==name[-1] and name[1]==name[-2]):
        print("تمرین6.5:","palindrame")
    else:
        print("تمرین6.5:","notpalindrame")
b("abbe")
b("abba")