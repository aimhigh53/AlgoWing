## 02_이진수2

T = int(input())

for t in range(1, T+1):
  num = float(input())
  answer = ''

  temp = num
  count = 0
  while True:
    temp = temp*2
    if temp >= 1:
      answer += '1'
      temp -= 1
    else:
      answer += '0'

    count += 1

    if temp.is_integer():
      break

    if count > 12:
      answer = 'overflow'
      break

  print('#{} {}'.format(t, answer))