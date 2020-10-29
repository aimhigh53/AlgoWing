def findLevel(lst):
    minval=0
    idx=0
    idx=lst.index(min(lst))

    return idx

def calc(lst,val):
    if len(set(lst))==1:

        return lst[0]*len(lst)

    #탈출조건
    if len(lst)<=1:
        return val

    if len(lst)==2:
        idx=findLevel(lst)
        minval=max(max(lst),lst[idx]*2)
        return minval

    idx=findLevel(lst)

    if len(lst)>2:
        #왼쪽
        leftlst=lst[0:idx]
#         print(idx,leftlst)
        leftval=max(val,calc(leftlst,val))

        #오른쪽
        rightlst=lst[idx+1:len(lst)]
        rightval=max(val,calc(rightlst,val))
        

        result=max(leftval,rightval)

        return result

def solution(numlst):
    numlst=numlst[1:numlst[0]+1]

    answer=calc(numlst,0)    
    return answer



while True:
    numlst=list(map(int,input().split(' ')))
    
    if numlst==[0]:
        break
    print(solution(numlst))



    
    ##힌트 참고 가장 낮은 높이를 기준으로 풀이

    #최소 level을 찾아내는 func

##TC는 모두 돌지만,, 메모리초과가 뜹니다 ㅠ

