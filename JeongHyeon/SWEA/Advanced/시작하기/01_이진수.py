## 01. 이진수

T = int(input())
eng = {
  'A':10,
  'B':11,
  'C':12,
  'D':13,
  'E':14,
  'F':15
}
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T+1):
  answer = ''
  length, num = input().split()
  for i in num:
    if '0' <= i <= '9':
      a = int(i)
    else:
      a = eng[i]

    check = [8, 4, 2, 1]
    for j in check:
      if a & j:
        answer += '1'
      else:
        answer += '0'

  print('#{} {}'.format(t, answer))