def solution(num):
    answer = ""
    while num > 0:
        num *= 2
        if num >= 1:
            num -= 1
            answer += "1"
        else:
            answer += "0"
        if len(answer) >= 13:
            answer = "overflow"
            break
    return answer

#main
if __name__ == "__main__":
    T = int(input())
    testcases = []
    for i in range(T):
        testcases.append(float(input()))

    for idx, value in enumerate(testcases):
        print("#" + str(i+1) +" " + solution(value))
