# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
#
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 입출력 예
# arr	result
# [2,6,8,14]	168
# [1,2,3]	6



# 가장 큰 수 와 두 번째 수 사이의 최소 공배수를 구한다
# 그 구한 수와 나머지 수들 사이에서 전부 나누어떨어진다면
# 나머지 수들중에서 가장 작은 수와의 최소 공배수를 구한다
# 만약 나누어떨어지지 않은 수가 있다면 그 수와 최소 공배수를 다시 구한다.
import math
def lcm(a,b):
    return (a*b)//math.gcd(a,b)

def solution(arr):
    arr = sorted(arr)
    m = lcm(arr[-1],arr[-2])
    arr.pop()
    arr.pop()
    for i in arr:
        if m%i != 0:
            m = lcm(m,i)
    answer = m
    return answer