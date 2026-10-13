def wf(x):
    print(x)
    s=x.split()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)