# 참고: https://velog.io/@someh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD
# datetime 패키지 익숙해지기

from datetime import datetime, timedelta

def compare(time, moment):
    # start-end 는 로그의 시작 or 끝 부분부터 시작하는 1초간의 구간.
    start = time
    end = time + timedelta(milliseconds=999) # => second=1을 인수를 줬을 때, 오류가 생김.
    
    # 1초간의 구간 안에 로그가 겹치는 경우는 3가지 경우만 있음.
    # 1. 구간의 시작보다 로그의 시작이 작고, 구간의 시작보다 로그의 끝이 큰 경우,
    # 2. 구간의 끝보다 로그의 시작이 작고, 구간의 끝보다 로그의 끝이 큰 경우,
    # 3. 구간의 시작보다 로그의 시작이 크고, 구간의 끝보다 로그의 끝이 작은 경우 (구간에 포함 될때)
    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True
    
    return False

def solution(lines):
    logs = []

    for line in lines:
        tmp = line.split(' ')
        date = tmp[0] + ' ' + tmp[1]
        # print(date)
        
        # 처리시간
        # print(tmp[2])
        if '.' in tmp[2]:
            delay = tmp[2].split('.')
            delay[1] = delay[1][:-1]
            
        else:
            delay = list(tmp[2][:-1])
            delay += ["0"]
        
        # print(delay)

        end = datetime.fromisoformat(date)
        start = end - timedelta(seconds=int(delay[0]), milliseconds= int(delay[1])-1)
        # print(start)
        logs.append([start, end])
    
    # print(logs)
    answers = []

    # 예시: [[datetime.datetime(2016, 9, 14, 23, 59, 57, 1000), datetime.datetime(2016, 9, 15, 0, 0)]]
    
    for timelist in logs:
        # print(timelist)
        for time in timelist:
            # print(time)
            answer = 0
            for moment in logs:
                if compare(time, moment) == True:
                    answer +=1
            answers.append(answer)

    # print(answers)

    return max(answers)