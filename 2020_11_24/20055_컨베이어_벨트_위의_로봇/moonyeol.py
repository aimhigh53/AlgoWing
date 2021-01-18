from collections import deque
import sys
input=sys.stdin.readline

def step1(N, belt):
    belt = deque(belt)
    belt.rotate()
    belt = list(belt)
    belt[N-1][1] = False
    return belt

def step2(N,belt):
    for i in range(N-1,0,-1):
        if belt[i][0] > 0 and not belt[i][1] and belt[i-1][1]:
            belt[i - 1][1] = False
            belt[i][1] = True
            belt[i][0] -= 1
    belt[N - 1][1] = False

def step3(belt):
    if belt[0][0] > 0 and not belt[0][1]:
        belt[0][1] = True
        belt[0][0] -= 1


def step4(K,belt):
    count = 0
    for b in belt:
        if b[0] ==0:
            count +=1
    if count >=K:
        return False
    else:
        return True

N, K = map(int,input().split())
As = list(map(int,input().split()))
belt = [[As[i], False] for i in range(2*N)]
belt = step1(N,belt)
step2(N,belt)
step3(belt)
Flag = step4(K,belt)
answer = 1
while Flag:
    belt = step1(N,belt)
    step2(N, belt)
    step3(belt)
    Flag = step4(K,belt)
    answer +=1
print(answer)
