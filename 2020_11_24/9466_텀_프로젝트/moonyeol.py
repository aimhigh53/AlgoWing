import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(students, x, visited, done):
    ans = 0
    visited[x] = True
    node = students[x] - 1
    if not visited[node]:
        ans += solution(students, node, visited, done)
    else:
        if not done[node]:
            now = node
            ans += 1
            while now != x:
                now = students[now] - 1
                ans += 1
    done[x] = True
    return ans


T = int(input())
ns = []
testCases = []
for _ in range(T):
    ns.append(int(input()))
    testCases.append(list(map(int, input().split())))

for idx, testCase in enumerate(testCases):
    n = ns[idx]
    answer = n
    visited = [False for _ in range(n)]
    done = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            answer -= solution(testCase, i, visited, done)
    print(answer)
