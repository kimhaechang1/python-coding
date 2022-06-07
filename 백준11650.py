# 좌표 정렬하기
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	76881	36304	27860	48.263%
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
#
# 예제 입력 1
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
# 예제 출력 1
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4

"""
x:[] 형태의 딕셔너리를 만들고
해당하는 x좌표의 y좌표점들이 모여있는 배열을 오름차순 정렬하여 2중for문을 통해 꺼낸다
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


# sorted에 key 부분은 알다싶히 원하는 정렬의 기준을 정할 수 있다.
# 여기서 알 수 있는 점은 원소 별로 인자 순서대로 정렬하도록 하게 만들 수 있다는 것이다.
# 튜플로 이뤄진 x,y 좌표를 기준으로
# (,key=lambda x: (x[0],x[1]))로 하면 튜플의 첫 번째 원소를 기준으로 정렬 후 두 번째 원소 기준으로 정렬 하란 의미가 된다.

# 즉, sort나 sorted에서 람다함수를 사용 할 때 xy좌표와 같은 원소를 순서에 맞게 정렬하기 위해서는 함수처럼 인자를 넣는식으로 해결 한다.
# 또한 sort자체의 기능으로 이차원리스트도 오름차순으로 정렬 해 준다.
import sys
n= int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so = sorted(so, key=lambda x : (x[0],x[1]))
for i in so:
    print(i[0],i[1])