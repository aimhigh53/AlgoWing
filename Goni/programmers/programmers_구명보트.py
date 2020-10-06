def solution(people, limit):
    answer=0

    #혼자밖에 못타는 사람들 뺌
    #people.sort(reverse=True)
    # for i,each in enumerate(people):
    #     if limit-40>=each:
    #         answer+=i
    #         break
    # people=people[i:]
    #위에꺼로 하면 정확성 55점 효울성 빵점
    #아래꺼로 하면 정확성 다맞고(75) 효율성땜에 85

    for i,each in enumerate(people):
        if limit - 40 < each:
             answer+=1
             people[i]=0

    people=[_ for _ in people if _!=0]
    people.sort()

    # 둘이서 탈 가능성이 있는 친구들
    for i in range(len(people)):
        if people[i] != 0:
            for j in range(i+1,len(people)):
                if people[i-j]!=0 and people[i]+people[i-j]<=limit:
                    answer+=1
                    people[i]=0
                    people[i-j]=0
                    break
    for i in people:
        if i!=0:
            answer+=1
    return answer

people=[70, 80, 50,50,40,90,30,60]
limit=100

print(solution(people,limit))