import copy


def rotated(arr):
    list_of_tuples = zip(*arr[::-1])
    return [list(elem) for elem in list_of_tuples]

def add_arr(lock, key, x, y, M, N):
    temp = copy.deepcopy(lock)
    i, j = 0, 0
    while y + i < N and i < M:
        j = 0
        while x + j < N and j < M:
            temp[y + i][x + j] += key[i][j]
            j += 1
        i += 1
    return temp


def check(lock, N):
    for i in range(N, N + N):
        for j in range(N, N + N):
            if lock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    temp_lock = [[0 for _ in range(3 * N)] for _ in range(3 * N)]
    for i in range(N, N + N):
        for j in range(N, N + N):
            temp_lock[i][j] = lock[i - N][j - N]
    for i in range(4):
        key = rotated(key)
        for x in range(0, 2 * N):
            for y in range(0, 2 * N):
                if check(add_arr(temp_lock, key, x, y, M, 3 * N), N):
                    return True
    return False
