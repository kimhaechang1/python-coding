# 1<=N,M<=100,000
# 포켓몬번호는 1번부터 시작
# 2<=포켓몬 이름의 길이<=20
# 첫글자만 대문자 + 나머지 소문자 or 마지막문자만 대문자
# 알파벳으로 들어오면 => 번호
# 번호로 들어오면 => 포켓몬 이름
"""
N개의 포켓몬을 전부 리스트에 저장
M개의 문제도 리스트에 저장

M개의 문제를 하나씩 꺼내었을 때 numeric이라면 -1한 값을 인덱스로 가지는 value를 N에서 찾기
M개의 문제를 하나꺼냈는데 포켓몬 이름이라면 index를 통해 인덱스 번호 출력

-> 역시나 index 함수는 금방 시간초과가 뜨기 마련이더라
따라서 포켓몬번호가 인덱스인 리스트를 역으로
포켓몬 이름이 key, 번호가 value인 cold 작
그 후 똑같이 numeric으로 검사하기
"""


import sys
import collections
n, m = map(int, sys.stdin.readline().split())

col = []
p = []
cold = collections.defaultdict(int)
result = []
for i in range(n):
    poke = sys.stdin.readline().strip()
    col.append(poke)
    cold[poke]=i+1
for i in range(m):
    p = sys.stdin.readline().strip()
    if p.isnumeric():
        result.append(col[int(p)-1])
    else:
        result.append(str(cold[p]))

for i in result:
    print(i)



