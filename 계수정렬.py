# 주어진 데이터의 크기범위가 제한될때(작을때) 사용가능한 정렬
# 파이썬에서는 append를 사용 할 경우 메모리 낭비가 발생하므로
# 입력값의 범위가 잡힌 경우에는 배열 선언을 충분히 해 준다.

import sys
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]*10001
for i in array:
    count[i]= count[i]+1
for i in range(10001):
    if count[i]!=0:
        for k in range(count[i]):
            print(i)