n=int(input())
weights=list(map(int,input().split()))
weights.sort()

sum=1
for i in weights:
    if sum<i:
        break
    sum +=i

print(sum)