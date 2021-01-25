#아니대체뭐가달라?
#https://pacific-ocean.tistory.com/149
n=int(input())
points=[]
for _ in range(n):
    points.append(int(input()))
points.append(0)
points.append(0)
dp=[0 for _ in range(n+2)]
dp[0]=points[0]
dp[1]=points[0]+points[1]
dp[2]=max(points[1]+points[2],points[0]+points[2])

for i in range(3,n):
    dp[i]=max(dp[i-2]+points[i],dp[i-3]+points[n]+points[n-1])
print(dp[n-1])