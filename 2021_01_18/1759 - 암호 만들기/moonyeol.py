import sys
input=sys.stdin.readline

vowels = ('a','e','i','o','u')

def dfs(i,string):
    if len(string) >= L:
        count_vowels = 0
        count_consonant = 0
        for s in string:
            if s in vowels:
                count_vowels +=1
            else:
                count_consonant +=1
            if count_vowels>=1 and count_consonant>=2:
                print(string)
                break
        return
    for k in range(i,len_chars):
        dfs(k+1,string+chars[k])


L, C = map(int,input().split())

chars = input().split()
len_chars = len(chars)
chars.sort()
dfs(0,"")
