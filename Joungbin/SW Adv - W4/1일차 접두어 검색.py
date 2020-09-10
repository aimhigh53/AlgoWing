t=int(input())

for tc in range(t) :
    n, m=map(int, input().split())
    a=[]
    ans=0
    for i in range(n) :
        a.append(input())
    for i in range(m) :
        b_word=input()
        for words in a :
            if(words[0:len(b_word)]==b_word) :
                ans+=1
                break
    print('#%d'%(tc+1), ans)