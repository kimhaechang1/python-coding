# 좌표 압축
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	34472	14870	11323	40.933%
# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
#
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
#
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#
# 입력
# 첫째 줄에 N이 주어진다.
#
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
#
# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
#
# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109
# 예제 입력 1
# 5
# 2 4 -10 4 -9
# 예제 출력 1
# 2 3 0 3 1
# 예제 입력 2
# 6
# 1000 999 1000 999 1000 999
# 예제 출력 2
# 1 0 1 0 1 0


"""
l : 원본 배열
copy : 원본배열을 중복제거한 새로운 배열
rank : 등수를 저장할 dict
copy 배열을 정렬한다
원소를 하나씩 꺼내면서
  0  1   2   3   4
-10 -9   2   4   4
 인덱스 : value, 값을 key로 갖는 rank dict 형성
 원본배열 원소를 돌며 rank의 value값 추출
"""

import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

copy = sorted(list(set(l)))
rank = dict()

for index, value in enumerate(copy):
    rank[value] = index

for num in l:
    print(rank[num],end=" ")