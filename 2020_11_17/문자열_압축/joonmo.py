# 길이가 0일 때 케이스 항상 생각하기
# 쓸때없이 코드가 길고 더럽다. 
# 나중에 꼭 고쳐봐야겠다.

from collections import deque

def solution(s):
    answer_lst = []
    n = len(s)
    half = n//2
    
    # my_dict = dict()

    for i in range(1, half+2):
        answer = ''
        repeat_num =  n//i
        stack = deque()
        tmp_num = 0

        for j in range(repeat_num):

            start = j*i
            end = (j+1) * i
            tmp = s[start:end]

            # 스택에 없을때
            if not stack:
                stack.append(tmp)
                tmp_num += 1
            
            # 스택에 벌써 있을때
            else:
                # 안같으면
                if tmp not in stack:
                    repeat_str = stack.pop()
                    if tmp_num == 1:
                        answer += repeat_str
                    else:
                        answer += str(tmp_num) + repeat_str
                    
                    stack.append(tmp)
                    tmp_num = 1
                else:
                    tmp_num += 1

        repeat_str = stack.pop()
        if tmp_num == 1:
            answer += repeat_str
        else:
            answer += str(tmp_num) + repeat_str

        if end:
            answer += s[end:]
        
        # print(answer)
        answer_lst.append(len(answer)) 

    return min(answer_lst)