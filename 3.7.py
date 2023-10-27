#تمرین3.7
def m (b,j):
    if(b==0):
        print("stop")
    else:
        print("b=",b)
        print("j=",j)
        m(b-j,j)


m (22,2)
