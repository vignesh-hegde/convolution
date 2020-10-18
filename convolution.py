def mulsum(a,b):
    temp=0
    for i in range(len(a)):
        temp+=a[i]*b[i]
    return temp

def matmul(x,y,printmat):
    if(len(y)==len(x[0])):
        temp1=[]
        for i in range(len(x)):
            temp=[]
            for j in range(len(y[0])):
                temp.append(mulsum(x[i],[k[j] for k in y]))
            temp1.append(temp)
        if(printmat):
            for i in range(len(x)):
                print(x[i],y[i])
        return temp1
    else:
        print("Invalid matrix order")

def rotate(x):
    temp=[]
    for i in range(len(x)):
        temp.append(x)
        x=[x[-1]]+x[:len(x)-1]
    temp2=[]
    for i in range(len(temp)):
        temp2.append([0]*len(temp))

    for i in range(len(x)):
        for j in range(len(x)):
            temp2[j][i] = temp[i][j]
    return temp2


def circular(X,H,printmat=False):
    x=X[::]
    h=H[::]
    Loop = len(h)-1
    for i in range(Loop):
        x.insert(0,0)
    for i in range(len(h)):
        h[i]=[h[i]]
    if len(x)>len(h):
        for i in range(len(x)-len(h)):
            h.append([0])
    res=matmul(rotate(x),h,printmat)    
    res=res[Loop:]+res[:Loop]
    for i in range(len(res)):
        res[i]=res[i][0]
    return res
