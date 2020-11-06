from collections import deque


def balanced(w):
    op=0
    cp=0
   
    for i in range(len(w)):
        if '('==w[i]:
            op+=1
        else:
            cp+=1
        if op==cp:
            return w[:i + 1], w[i + 1:] 
   
def positive(u):
    stack = []

    for p in u:

        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True
    
def solution(w):
   
    if not w:
        return ""
    
    u,v=balanced(w)

    if positive(u):
        #여기가 중요한 부분
        return u+solution(v)
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        # 1단계로부터 재귀를 돈다고 했으니 또 돌아야지...
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        
        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        # 과정 4-5
        return answer
