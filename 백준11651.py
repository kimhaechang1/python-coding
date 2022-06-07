# 좌표 정렬하기 2
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	41633	27002	22956	67.793%
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
#
# 예제 입력 1
# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3
# 예제 출력 1
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4



"""
nums = [] 입력값을 튜플로 된 배열로 받음
y좌표를 기준으로 하므로
y좌표를 key로 x좌표들을 배열로 갖는 딕셔너리 생성
numd = dict()

key값들을 정렬한 keys 리스트
keys리스트를 돌며 x좌표들이 모여있는 values들을 정렬하고 그 정렬된 원소를 하나씩 print
"""

import sys

n = int(sys.stdin.readline())
nums = list()
numd = dict()
keys = list()

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append((x,y))
    numd[y]= []

for x, y in nums:
    numd[y].append(x)
keys = sorted(numd)
for key in keys:
    numd[key] = sorted(numd[key])
    for value in numd[key]:
        print(value, key)

