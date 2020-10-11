def histogram(i):
    while(len(s) != 0 and a[s[-1]] > a[i]):
        # 스택에 요소가 남아있고 이전 것의 높이가 그 이전(2번째 이전) 것의 높이보다 낮은 경우
        idx = s.pop()
        if(len(s) == 0): # 스택에 남아있었던 마지막 요소인 경우
            ans.append(a[idx] * (i-1)) # 왼쪽의 모든 직사각형의 높이가 그것보다 높거나 같다고 판단,
                                       # (높이 * (이전 것의 직사각형의 번호))를 넓이 리스트에 추가
        else: # 아닌 경우
            ans.append(a[idx] * ((i-1) - s[-1])) # 스택에 남아있는 마지막 요소(직사각형의 번호)
                                                 # 바로 오른쪽이 시작점

while True:
    a = [*map(int, input().split())]
    n = a[0] # 히스토그램을 이루는 사각형의 개수
    if(n == 0): break
    s = [] # 스택 구현
    ans = [] # 넓이 리스트
    for histo_element in range(1, n+1): # 히스토그램을 이루는 사각형
        if(histo_element != 1 and a[histo_element-1] > a[histo_element]):
            # 첫 번째가 아니면서 현재 것의 높이가 이전 것의 높이보다 낮은 경우
            histogram(histo_element)
        s.append(histo_element) # 스택에는 무조건 현재의 것을 집어넣음
    for j in range(len(s)): # 마지막 직사각형까지 조사했는데 스택에 남아있는 경우 가장 오른쪽이 끝점
        idx = s.pop() # 하나하나 빼면서 진행
        if(len(s) == 0): # 스택에 남아있었던 마지막 요소인 경우
            ans.append(a[idx] * n) # 모든 직사각형의 높이가 그것보다 높거나 같다고 판단,
                                   # (높이 * 직사각형의 개수)를 넓이 리스트에 추가
        else: # 아닌 경우
            ans.append(a[idx] * (n-s[-1])) # 스택에 남아있는 마지막 요소(직사각형의 번호)
                                           # 바로 오른쪽이 시작점
    print(max(ans)) # 넓이의 최댓값 출력

'''입력 : 10 2 1 3 4 5 4 5 1 3 3, 4 1 4 3 3, 4 2 3 2 1
   출력 : 16, 9, 6'''