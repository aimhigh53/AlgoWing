num = int(input())
nums = []
for i in range(num):
    nums.append(float(input()))

for i,j in enumerate(nums):
    temp = j
    answer = ""
    while temp > 0:
        temp *= 2
        if temp >=1 :
            temp -= 1
            answer += "1"
        else:
            answer += "0"
        if len(answer) >= 13:
            answer = "overflow"
            break
    print("#" + str(i+1) +" " + answer)

