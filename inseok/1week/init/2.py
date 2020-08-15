N=int(input())

def divide(n,tmp,i):
    global anslist
    if i<=-14:
        print('#%d'%(n),'overflow')
        return

    if tmp>=2**(i):
        tmp=tmp-2**(i)

        if tmp!=0:
            anslist.append(1)
            i=i-1
            divide(n,tmp,i)
        else:
            anslist.append(1)  
            print('#%d'%(n),''.join(map(str,anslist)))
            return 
    else:             
        anslist.append(0)
        i=i-1
        divide(n,tmp,i)
            

for p in range(N):
    anslist=[]
    tmp=float(input())
    divide(p+1,tmp,-1)
