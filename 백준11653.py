# 소인수분해
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	58237	31163	24324	52.238%
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
#
# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
#
# 예제 입력 1
# 72
# 예제 출력 1
# 2
# 2
# 2
# 3
# 3
# 예제 입력 2
# 3
# 예제 출력 2
# 3
# 예제 입력 3
# 6
# 예제 출력 3
# 2
# 3
# 예제 입력 4
# 2
# 예제 출력 4
# 2
# 예제 입력 5
# 9991
# 예제 출력 5
# 97
# 103


def make(n):
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    prime = []
    for i in range(2, int((n+1)**(1/2))):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j] = False
    for i in range(n+1):
        if isPrime[i] :
            prime.append(i)
    return prime

def solution(n):
   if n == 1:
       return
   else:
    p = make(n)
    k = 0
    while True:
        if n == 1:
            break
        elif n % p[k] == 0:
            n = n / p[k]
            print(p[k])
        else:
            k+=1

solution(int(input()))