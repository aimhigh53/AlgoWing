def reach(play, score, p):
    if(play == 6):
        alist = [[i, 0] for i in range(4)]
        for i in range(4) :
            alist[i][1]=score[i]
        alist.sort(key=lambda x : x[1], reverse=True)
        a, b, c, d=alist[0], alist[1], alist[2], alist[3]
        if(b[1] != c[1]):
            prob[a[0]] += p
            prob[b[0]] += p
        elif(a[1] == b[1] and c[1] == d[1]):
            prob[a[0]] += (p / 2)
            prob[b[0]] += (p / 2)
            prob[c[0]] += (p / 2)
            prob[d[0]] += (p / 2)
        elif(a[1] == b[1]):
            prob[a[0]] += (p * 2 / 3)
            prob[b[0]] += (p * 2 / 3)
            prob[c[0]] += (p * 2 / 3)
        elif(c[1] == d[1]):
            prob[a[0]] += p
            prob[b[0]] += (p / 3)
            prob[c[0]] += (p / 3)
            prob[d[0]] += (p / 3)
        else:
            prob[a[0]] += p
            prob[b[0]] += (p / 2)
            prob[c[0]] += (p / 2)
        return
    a=cause[play][0]
    b=cause[play][1]
    score[a] += 3
    reach(play + 1, score, p*cause[play][2])
    score[a] -= 3

    score[a] += 1
    score[b] += 1
    reach(play + 1, score, p*cause[play][3])
    score[a] -= 1
    score[b] -= 1

    score[b] += 3
    reach(play + 1, score, p*cause[play][4])
    score[b] -= 3


def f(x) :
    return float(x)

country=[*map(str, input().split())]
cause=[]
score=[0]*4
prob=[0, 0, 0, 0]
d=dict()
k=0

for i in country :
    d[i]=k
    k+=1

for i in range(6) :
    a=[*map(str, input().split())]
    cause.append((d[a[0]], d[a[1]], f(a[2]), f(a[3]), f(a[4])))

reach(0, score, 1)
for i in prob :
    print('%.10f'%i)
