Testcase=int(input())


def recur(count,val):
    global ansstr
    
    tmp=val-2**(count)

    if tmp>0:
        count-=1
        ansstr=ansstr+'1'
        recur(count,tmp)
    elif tmp<0:
        count-=1
        ansstr=ansstr+'0'        
        recur(count,val)
    elif tmp==0.0:
        ansstr=ansstr+'1' 
    
    if count==-13:
        ansstr='overflow'
    
    return ansstr
       
    
for tc in range(1,1+Testcase):
    N=float(input())
    ansstr=""
    
    print("#{}".format(tc),recur(-1,N))
