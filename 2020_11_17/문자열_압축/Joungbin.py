def solution(s) :
    ans=len(s)
    for i in range(1, len(s)//2+1) :
        xlist=[]
        k=0
        cnt=1
        new_s=''
        rest=''
        for j in range(len(s)//i) :
            x=''
            while(len(x)!=i) :
                x+=s[k]
                k+=1
            xlist.append(x)
        for j in range(i*len(xlist), len(s)) :
            rest+=s[j]
        for j in range(len(xlist)-1) :
            if(xlist[j]==xlist[j+1]) :
                cnt+=1
                if(j==len(xlist)-2) : new_s+=(str(cnt)+xlist[j])
            else :
                if(cnt>=2) : new_s+=(str(cnt)+xlist[j]); cnt=1
                else : new_s+=xlist[j]
        if(cnt==1) : new_s+=xlist[-1]
        new_s+=rest
        if(len(new_s)<ans) : ans=len(new_s)
    return ans

s=input()
solution(s)