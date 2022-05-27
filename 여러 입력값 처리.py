
# 띄어쓰기로 분리된 여러 숫자 입력받기

import sys
#n = list(map(int, sys.stdin.readline().split()))

# 한줄 한줄 숫자 입력받기

M = sys.stdin.readline()
p = [0]*M
for i in range(M):
    p[i]=int(sys.stdin.readline())

# 2차원 리스트로 숫자 입력 받기

M, N =map(int, sys.stdin.readline().split())
t = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(t)

# 2차원 리스트로 문자열 입력받아 띄어쓰기 기준으로 분리하여 저장하기

n = int(sys.stdin.readline())
t = [list(sys.stdin.readline().split()) for _ in range(n)]
print(t)

# 문자열 n줄을 입력받아 리스트에 저장할 때
n = int(sys.stdin.readline())
t = [sys.stdin.readline().strip() for _ in range(n)]
print(t)