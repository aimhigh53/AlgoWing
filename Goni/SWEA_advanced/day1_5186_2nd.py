T = int(input())

for test_case in range(1, T + 1):
    originalNum = float(input())
    checkingNum = originalNum
    ans = ''
    repeat = 13

    while (repeat):
        checkingNum *= 2
        ans += str(int(checkingNum))
        if checkingNum > 1:
            checkingNum -= 1
            if checkingNum == originalNum:
                print("#{} {}".format(test_case, ans))
                break
        if checkingNum == 1:
            print("#{} {}".format(test_case, ans))
            break

        repeat -= 1

    if repeat == 0:
        print("#{} {}".format(test_case, "overflow"))


