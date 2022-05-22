#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	168302	47418	33394	26.729%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def make(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    p = []
    for i in range(2, int((max)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j]= False
    for i in range(max+1):
        if isPrime[i]:
            p.append(i)
    return p
def solution(m,n):
    p = make(n)
    for i in p:
        if i >=m and i<=n:
            print(i)


m, n = map(int, input().split())
solution(m, n)

