import sys
input = sys.stdin.readline



def binarySearch(stack, n):
    l, r = 1, len(stack) -1
    while l < r:
        m = (l+r) //2
        if stack[m] < n:
            l = m+1
        elif stack[m] > n:
            r = m
        else:
            l = r = m
    return r


N = int(input())
A= list(map(int, input().split()))
stack = [0]

for a in A:
    if stack[-1] <a:
        stack.append(a)
    else:
        stack[binarySearch(stack,a)] = a

print(len(stack) -1)