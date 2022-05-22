# 골드바흐의 추측 다국어
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	57679	24059	18332	40.226%
# 문제
# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
#
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
#
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
#
# 제한
# 4 ≤ n ≤ 10,000
# 예제 입력 1
# 3
# 8
# 10
# 16
# 예제 출력 1
# 3 5
# 5 5
# 5 11


# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. = 골드 바흐의 수
# 짝수를 두 소수의 합으로 나타내는 표현 = 골드바흐 파티션


# 8 = 3 + 5
# 10 = 3 + 7 = 5 + 5
import time

T = int(input())
n = []
for i in range(T):
    n.append(int(input()))

start_time = time.time()
def make(max):
    isPrime = [True]*(max+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((max)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, max+1, i):
                isPrime[j]=False
    return isPrime
def solution(numbers):
    for num in numbers:
        p = make(num)
        a,b = num//2, num//2
        for _ in range(num//2):
            if p[a] and p[b]:
                print(a,b)
                break
            else:
                a -=1
                b +=1
solution(n)
end_time = time.time()

#print("time :", end_time-start_time)

# 당연히 에라토스테네스의 체 자체는 문제가 없다
# 처음에 어떻게 하면 최대한 차가 좁혀질까? 를 생각하였을때 가운데 숫자에서부터 가까워야 한다는점을 안 순간
# 가운데숫자에서 양방향으로 포인터를 똑같이 이동하면 합이 무조건 같기 때문에
# 가장 가운데숫자에서 가까운 두 수를 찾으면 된다
# 그래서 for문의 범위는 숫자의 절반인데 이는 어짜피 돌수있는건 양쪽으로 전체길이의 절반만큼만 이동할 수 있기 때문이다.