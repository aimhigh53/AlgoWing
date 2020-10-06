def solution(people, limit):

    
    sortedpeople=sorted(people,reverse = True)
    cnt=len(people)
    start,end=0,len(people)-1
    
    while start<end:
        if sortedpeople[start]+sortedpeople[end]<=limit:
            end-=1
            cnt-=1
        start+=1
        
    return cnt
