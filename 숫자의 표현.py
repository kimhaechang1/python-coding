# 문제 설명
# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
#
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
#
# 제한사항
# n은 10,000 이하의 자연수 입니다.
# 입출력 예
# n	result
# 15	4
# 입출력 예 설명
# 입출력 예#1
# 문제의 예시와 같습니다.

import math
def solution(n):
    answer = 0
    m = math.ceil(n/2)
    cnt = 0
    num =[x for x in range(m+1)]
    start = 1
    b = 2
    end = start+b
    while True:
        if b == len(num)+1:
            break
        if end > len(num):
            start = 1
            b+=1
            end = start+b
        else:
            if sum(num[start:end])!= n:
                start +=1
                end+=1
            elif sum(num[start:end]) == n:
                start=1
                cnt+=1
                b+=1
                end = start+b
    answer = cnt+1
    return answer

# 효율성에서 통과하지 못했다.
# 내가 너무 복잡하게 생각하였다.
# 투 포인터 알고리즘으로 해결하려고 했는데 그게 생각보다 잘 안되었다.
# 그냥 처음부터 for문 2개 돌리고 합계가 n과 동일할때 안쪽 for 문을 break해주면 되었을 것

import math
def solution(n):
    answer = 0
    for i in range(1,n+1):
        s = 0
        for j in range(i, n+1):
            s +=j
            if s == n:
                answer+=1
                break
            elif s>n:
                break
    return answer
