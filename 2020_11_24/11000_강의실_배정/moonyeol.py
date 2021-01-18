import sys
import heapq
input = sys.stdin.readline



def solution():
    global lessons, N
    ans = 1
    times = [lessons[0][1]]
    for i in range(1,N):
        now = lessons[i]
        if now[0] >= times[0]:
            heapq.heappop(times)
        else:
            ans +=1
        heapq.heappush(times,now[1])
    return ans

N = int(input())
lessons = []
for i in range(N):
    lessons.append(list(map(int, input().split())))

lessons.sort()
print(solution())
