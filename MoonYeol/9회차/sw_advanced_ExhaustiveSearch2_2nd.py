def solution(x, y, visited, weight):
    global array
    if visited + 1 == 1 << (len(array) + 1):
        global results
        results.append(weight + array[x][y] + array[y][0])
        return

    for i, j in enumerate(array[x]):
        if not (visited & 1 << i):
            solution(y, i, visited | 1 << i, weight + array[x][y])
    return

if __name__ == "__main__":
    T = int(input())
    testCases = []
    visited = []
    for i in range(T):
        temp = []
        n = int(input())
        temp2 = (1 << n) | 1
        for i in range(n):
            temp.append(list(map(int, input().split())))
        testCases.append(temp)
        visited.append(temp2)

    for idx, array in enumerate(testCases):
        results = []
        solution(0, 0, visited[idx], 0)
        answer = min(results)
        print("#" + str(idx + 1) + " " + str(answer))
