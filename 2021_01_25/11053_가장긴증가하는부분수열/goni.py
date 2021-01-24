n=int(input())
num_list=list(map(int,input().split()))
ans_list=[0 for _ in range(n)]
ans_list[0]=0
for i in range(n):
    for j in range(i):
        if num_list[j]<num_list[i]:
            if ans_list[i]<ans_list[j]:
                ans_list[i]=ans_list[j]
    ans_list[i]+=1

print(max(ans_list))