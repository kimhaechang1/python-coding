# 문자열 집합
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초 (하단 참고)	1536 MB	12154	6701	4785	55.913%
# 문제
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
#
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
#
# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
#
# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
#
# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
#
# 출력
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.
#
# 예제 입력 1
# 5 11
# baekjoononlinejudge
# startlink
# codeplus
# sundaycoding
# codingsh
# baekjoon
# codeplus
# codeminus
# startlink
# starlink
# sundaycoding
# codingsh
# codinghs
# sondaycoding
# startrink
# icerink
# 예제 출력 1
# 4

"""
s.intersection(issub)를 통해 교집합의 개수를 검사
-> 중복된 원소가 검사해야할 문자열 리스트에는 존재하므로
-> Counter를 통해 검사 해야할 문자들의 각각 개수를 구한 뒤
집합S에 있는 원소를 하나하나 돌면서 개수를 더해주면 끝
"""
import sys
import collections
n, m = map(int,sys.stdin.readline().split())

s = list()
issub = list()


for i in range(n):
    s.append(sys.stdin.readline().strip())
for k in range(m):
    issub.append(sys.stdin.readline().strip())

i = collections.Counter(issub)
sum = 0
print(i)
for sn in s:
    sum+=i[sn]
print(sum)
