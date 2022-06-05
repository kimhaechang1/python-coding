# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys

s = []
n = int(sys.stdin.readline())
for i in range(n):
    s.append(int(sys.stdin.readline()))

s = sorted(s)

for i in s:
    print(i)