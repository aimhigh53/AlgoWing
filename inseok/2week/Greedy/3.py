T=int(input())
 
 
for TC in range(T):
 
 
    givennums=[int(x) for x in input().split()]
    player_one=sorted(givennums[0::2])
    player_two=sorted(givennums[1::2])
    players=[player_one,player_two]
    diclist=[]
    winlose=[0,0]
    dx=[0,0,0]
 
    #같은거 3개 있는지 판단
    for cnt in range(2):
        dic={}        
        for i in players[cnt]:
            try:dic[i]+=1
            except:dic[i]=1
        diclist.append(dic)
    print(diclist) 
    for i in range(2):
        for j in diclist:
            for k in j.values():
                if k>=3:
                    winlose[i]=1
    #연속수 판단
    for i in range(2):
        for j in diclist:
            for k in j:
                if k+1 in j:
                    if k+2 in j:
                        winlose[i]=1
 
    if winlose[0]==winlose[1]:
        print('#%d'%(TC+1),0)
    elif winlose[0]>winlose[1]:
        print('#%d'%(TC+1),1)
    elif winlose[0]<winlose[1]:
        print('#%d'%(TC+1),2)
