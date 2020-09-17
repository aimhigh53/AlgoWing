def put_queen(num, chess, x, y):
    for i in range(num):
        chess[x][i] += 1
        #chess[i][y] += 1
        #if x - i >= 0 and y - i >= 0:
        #    chess[x - i][y - i] += 1
        if x + i < num and y + i < num:
            chess[x + i][y + i] += 1
        if x - i >= 0 and y + i < num:
            chess[x - i][y + i] += 1
        #if x + i < num and y - i >= 0:
        #    chess[x + i][y - i] += 1

def put_away_queen(num, chess, x, y):
    for i in range(num):
        chess[x][i] -= 1
        #chess[i][y] -= 1
        #if x - i >= 0 and y - i >= 0:
        #    chess[x - i][y - i] -= 1
        if x + i < num and y + i < num:
            chess[x + i][y + i] -= 1
        if x - i >= 0 and y + i < num:
            chess[x - i][y + i] -= 1
        #if x + i < num and y - i >= 0:
        #    chess[x + i][y - i] -= 1

def solution(num, chess, y, count):
    if count == num:
        return 1
    if y >= num:
        return 0
    ans = 0
    check = False
    for i in range(num):
        if chess[i][y] == 0:
            check = True
            put_queen(num, chess, i, y)
            temp = solution(num, chess, y+1, count+1)
            put_away_queen(num, chess, i, y)
            if temp == -1 :
                continue
            ans += temp
    if not check :
        return -1
    return ans


num = int(input())
chess = [[0 for i in range(num)] for i in range(num)]
print(solution(num,chess,0,0))

