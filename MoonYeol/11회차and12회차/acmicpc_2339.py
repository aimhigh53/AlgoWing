
def is_possible(x,y,startX,startY,endX,endY, direction):
    global slate
    if direction == 1:
        for i in range(startX,endX+1):
            if i == x:
                continue
            if slate[i][y] == 2:
                return False
    elif direction == -1:
        for i in range(startY,endY+1):
            if i == y:
                continue
            if slate[x][i] == 2:
                return False
    return True



def solution(startX,startY,endX,endY,direction):
    #direction  1: 가로, -1 : 세로, 0 : 처음
    global slate
    answer = 0
    jewelry =0
    foreign =0
    global visitedX
    global visitedY
    visited_x = visitedX
    visited_y = visitedY

    for x in range(startX,endX+1):
        for y in range(startY,endY+1):
            if slate[x][y] == 1:
                foreign += 1
                if not is_possible(x,y,startX,startY,endX,endY,direction):
                    pass
                else:
                    temp1, temp2 = -1, -1
                    if direction == 1:
                        if visited_y & 1 << y :
                            continue
                        visited_y = visited_y | 1 << y
                        if y > startY:
                            temp1 = solution(startX, startY, endX, y - 1, -1)
                        if y < endY:
                            temp2 = solution(startX, y+1, endX, endY, -1)
                    if direction == -1:
                        if visited_x & 1 << x:
                            continue
                        visited_x = visited_x | 1 << x
                        if x > startX:
                            temp1 = solution(startX, startY, x-1, endY, 1)
                        if x < endX:
                            temp2 = solution(x+1, startY, endX, endY, 1)
                    if temp1 > 0 and temp2 > 0:
                        answer += temp1 * temp2
                    elif temp1 == -1 and temp2 == -1:
                        pass
                    elif temp1 == -1 or temp2 == -1:
                        answer += max(temp1, temp2)
            elif slate[x][y] == 2:
                jewelry += 1

    if jewelry == 1 and foreign == 0:
        return 1
    elif jewelry == 0 and foreign == 0:
        return 0
    elif jewelry > 1 and foreign == 0:
        return 0
    elif jewelry == 0 and foreign > 0:
        return 0
    return answer




N = int(input())
visitedX = 1 << N
visitedY = 1 << N
slate = []
for i in range(N):
    slate.append(list(map(int, input().split())))
jewelry =0
foreign =0
for x in range(N):
    for y in range(N):
        if slate[x][y] == 1:
            foreign +=1
        if slate[x][y] == 2:
            jewelry +=1
if jewelry == 1 and foreign == 0:
    print(1)
elif jewelry == 0 and foreign == 0:
    print(-1)
elif jewelry > 1 and foreign == 0:
    print(-1)
elif jewelry == 0 and foreign > 0:
    print(-1)
else :
    ans = solution(0,0,N-1,N-1,-1) + solution(0,0,N-1,N-1,1)
    if ans == 0:
        ans = -1
    print(ans)