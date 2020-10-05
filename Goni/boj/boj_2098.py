import itertools

city_num=int(input())
w=[]
for _ in range(city_num):
    w.append(list(map(int,input().split())))

temp=[i for i in range(1,city_num)]
candi=list(itertools.permutations(temp, 3))

min_candi=[]

for each in candi:
    if w[0][each[0]]!=0 and w[each[0]][each[1]]!=0 and w[each[1]][each[2]]!=0 and w[each[2]][0]!=0:
        temp=w[0][each[0]]+w[each[0]][each[1]]+w[each[1]][each[2]]+w[each[2]][0]
        min_candi.append(temp)
        temp = 0
print(min_candi)
print(min(min_candi))
