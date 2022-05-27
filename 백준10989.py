# 수 정렬하기 3
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 5 초 (하단 참고)	8 MB (하단 참고)	165151	38003	28411	23.434%
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7
# 출처
# 문제를 만든 사람: baekjoon
# 데이터를 추가한 사람: cgiosy
# 문제의 오타를 찾은 사람: joonas
# 비슷한 문제
# 2750번. 수 정렬하기
# 2751번. 수 정렬하기 2
# 알고리즘 분류
# 보기
#
# 시간 제한
# Java 8: 3 초
# Java 8 (OpenJDK): 3 초
# Java 11: 3 초
# Kotlin (JVM): 3 초
# Java 15: 3 초
# 메모리 제한
# Java 8: 512 MB
# Java 8 (OpenJDK): 512 MB
# Java 11: 512 MB
# Kotlin (JVM): 512 MB
# Java 15: 512 MB

# 정렬 할 데이터들의 범위가 작다.
# 즉 계수정렬 사용이 가능하다.
import sys
N = int(sys.stdin.readline())
count = [0]*10001
for i in range(N):
    num = int(sys.stdin.readline())
    count[num] = count[num]+1
for i in range(10001):
    if count[i]!=0:
        for k in range(count[i]):
            print(i)


