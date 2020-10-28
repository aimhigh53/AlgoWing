#배울점: 분할정복은 재귀로 해결하려고 노력해라

# 1. 어떻게 쪼갤것인가
# 2. eval을 아는가?
# 3. str의 형태를 어떻게 처리할 것인가
# 4. case setting을 어떻게 잘 해줄 것인가

def sol(case,n,expression):
    if n==2:
        return str(eval(expression))
    elif case[n]=="*":
        res=eval('*'.join([sol(case, n+1, e) for e in expression.split('*')]))
    elif case[n]=="+":
        res=eval('+'.join([sol(case, n+1, e) for e in expression.split('+')]))
    elif case[n]=="-":
        res=eval('-'.join([sol(case, n+1, e) for e in expression.split('-')]))
    return str(res)
    

def solution(expression):
    
    answer=0
    cases=[
        ['+','-','*'],
        ['+','*','-'],
        ['-','+','*'],
        ['-','*','+'],
        ['*','-','+'],
        ['*','+','-']
    ]
    for case in cases:
        res=int(sol(case,0,expression))
        answer = max(answer, abs(res))
    return answer

