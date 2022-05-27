# k진수에서 소수 개수 구하기
# 문제 설명
# 문제 설명
# 양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.
#
# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.
# 예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.
#
# 정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.
#
# 제한사항
# 1 ≤ n ≤ 1,000,000
# 3 ≤ k ≤ 10
# 입출력 예
# n	k	result
# 437674	3	3
# 110011	10	2
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
#
# 입출력 예 #2
#
# 110011을 10진수로 바꾸면 110011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 11, 11 2개입니다. 이와 같이, 중복되는 소수를 발견하더라도 모두 따로 세어야 합니다.
#
# 제한시간 안내
# 정확성 테스트 : 10초

import math
def isPrime(n):
    if n == 1:
        return False
    if n==2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def convert(n, k):
    result = ""
    p = 0
    while True:
        if n - (k ** p) < 0:
            p -= 1
            break
        elif n - (k ** p) == 0:
            break
        p += 1
    for i in range(p, -1, -1):
        if n - (k ** i) >= 0:
            u = n // (k ** i)
            result += str(u)
            n = n-u*(k**i)
        else:
            result+=str(0)
    return result

def solution(n, k):
    answer=0
    if k == 10:
        o = str(n)
    else:
        o = convert(n, k)
    s = o.split('0')
    for value in s:
        if len(value) and isPrime(int(value)):
            answer+=1
    return answer


# 결과적으로 쓸데없는 if문 때문에 헷갈리게 되었다
# 여기서 말하고자 하는 것은 0으로 구분되는 수 들 중 소수의 개수를 구하는거다.
# 그걸 알았으면 진작 다 푼것
