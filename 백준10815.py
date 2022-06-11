# 숫자 카드
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	44402	21728	15248	48.253%
# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다
#
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1
# 1 0 0 1 1 0 0 1

"""
sang 상근이의 숫자카드 집합
pre 추측된 숫자카드들의 집합

ss = collections.Counter(sang)
p  = collections.Counter(pre)

result = defaultdict(int)를 통해 result 저장

상근이가 가지고 있는 카드들을 for문 돌려서 그 카드들만 1 표시

그리고 예상했던 카드들을 key값으로 찾아가며 출력

"""

import sys
import collections
n = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
pre = list(map(int, sys.stdin.readline().split()))

result = collections.defaultdict(int)

for sn in sang:
    result[sn]=1

for p in pre:
    print(result[p],end=" ")

