# 듣보잡
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	47926	20081	15036	40.338%
# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
#
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
#
# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.
#
# 예제 입력 1
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
# 예제 출력 1
# 2
# baesangwook
# ohhenrie

"""
교집합 찾아서 sorted 한 뒤
교집합의 크기 및 한줄씩 출력
intersection()
"""

import sys

n, m = map(int, sys.stdin.readline().split())

d = set()
b = set()
for i in range(n):
    d.add(sys.stdin.readline().strip())
for i in range(m):
    b.add(sys.stdin.readline().strip())
inter = sorted(d.intersection(b))
print(len(inter))
for k in inter:
    print(k)


# sys.stdin.read().splitlines()를 사용하면 한줄에 하나씩 분리하여 입력 받게 된다.
# 그렇게 입력받은 것은 리스트 형태로 저장되어 리스트 슬라이스를 통해 분리할 수 있다.

