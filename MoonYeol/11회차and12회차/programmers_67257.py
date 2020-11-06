import re
import copy

def calc(a,b,operator):
    if operator == '*':
        return a*b
    elif operator == '+':
        return a+b
    elif operator == '-':
        return a-b

def resursion(opers,visited,operator,ans):
    new_opers = []
    last = -1
    is_calc = False
    for idx, value in enumerate(opers):
        if is_calc:
            pre = new_opers[last]
            new_opers[last] = calc(int(pre), int(value), operator)
            is_calc = False
        else:
            if value == operator:
                is_calc =True
                continue
            else:
                new_opers.append(value)
                last += 1
    if len(new_opers) == 1:
        if new_opers[0] <0:
            new_opers[0] = -new_opers[0]
        ans.append(new_opers[0])
    for i in range(3):
        if not (1 << i & visited):
            if i == 0:
                resursion(new_opers, visited | 1 << i,"-",ans)
            elif i == 1:
                resursion(new_opers, visited | 1 << i, "+",ans)
            else:
                resursion(new_opers, visited | 1 << i, "*",ans)


def solution(expression):
    answer = []
    opers = re.split('([-*+])', expression)
    visited = 1 << 3
    # 0: -,1: +,2: *
    resursion(opers,visited | 1 << 0,"-",answer)
    resursion(opers, visited | 1 << 1, "+",answer)
    resursion(opers, visited | 1 << 2, "*",answer)
    print(answer)
    return max(answer)

ans = solution("100-200*300-500+20")
print(ans)