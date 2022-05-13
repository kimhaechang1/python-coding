# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
#
# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.

import itertools
def isPrime(k):
    print(k)
    result = True
    for j in range(2,k):
        if k%j == 0:
            result = False
            break;
    print(result)
    return result

def solution(nums):
    answer= 0
    for i in itertools.combinations(nums,3):
        temp = sum(i)
        if isPrime(temp):
            answer+=1

    return answer

import itertools
# itertools엔 조합, 순열, 중복조합, 중복순열을 만들어서 튜플형태로 저장한다.
# 따라서 for문을통해 뽑아준다.
# 순서 ㅇㅈ = 순열 (나열) permutaions(iterable Object, 뽑는개수)
# 순서 그딴거 왜필요함? = combinations(iterable Object, 뽑는 개수)
# 중복허용한 조합 = combinations_with_replacement (iterable Object, 뽑는 개수)
# 중복허용한 순열 = product(iterable Object, repeat=뽑는개수)
# 혹은 product(iterable Object1, iterable Object2)
itertools.combinations_with_replacement()
itertools.combinations()
itertools.permutations()
itertools.product()