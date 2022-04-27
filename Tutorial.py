# 리스트 컴프리핸션

# 리스트를 초기화 하는 방법 중 하나

# 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화 할 수 있다.

# ex1) 0~19중 홀수만 포함하는 리스트를 만들고 출력하시오

array = [i for i in range(0,20) if i % 2 !=0]
# [리스트 안에 출력 될 변수 for 그 변수 in range(x>= and <x) if 조건]
print(array)

# ex2) 1~9까지의 수의 제곱 값을 포함하는 리스트를 만들고 출력하시오

array = [i*i for i in range(1,10)]
print(array)

# ex3) NxM 크기의 2차원 리스트를 초기화 하십시오 (단, N = 3, M = 4로 고정한다)

N = 3
M = 4

array = [[0]*M for _ in range(N)]
print(array)
# 특정 크기의 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리핸션을 쓰도록 해야한다.
# [[초기화 값]*가로길이 for _ in range(세로길이)]
# _ : 반복을 위한 변수를 무시하고자 할 때 씀

# 이스케이프 문자를 활용하여 큰 따옴표와 같은 특수문자를 출력 할 수 있다.
# 특수한 문자 앞에 백슬래쉬를 사용하여 출력한다.

print("Okay bye \"kim hae chang\"")

# 파이썬의 기본 자료구조
# 파이썬의 기본 자료구조에는 튜플, 리스트, 딕셔너리, 집합이 존재한다.

# 튜플
# 튜플은 리스트와 거의 비슷하나 한번 선언된 값은 바꿀수 없고 소괄호를 사용한다.

a = (1,2,3,4)
print(a)
# a[3] = 7 는 오류가 발생한다.

# 이러한 튜플은 그래프 알고리즘에서 주로 사용된다
# 최단경로 알고리즘과 같은 곳에서 우선순위 큐를 보통 사용하는데, 이 때 우선순위 큐를 튜플로 작성하여
# 변경 되면 안되는 값이 변경되는 일이 일어나지 않도록 할 수 있다.
# 또한 튜플은 리스트에 비해 상대적으로 공간이 효율적이고, 일반적으로 각 원소의 성질이 서로 다를 때 주로 사용한다.

# 딕셔너리(사전)
# 키(key)와 값(value)로 이루어진 자료구조이다.
# 파이썬의 딕셔너리는 내부적으로 해시 테이블을 이용하므로
# 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리가 가능하다.

data = dict()
data['사과'] = "apple"
data['바나나'] = "banana"
data['코코넛'] = "coconut"

print(data)

# 또한 딕셔너리 자료구조에서 in 키워드를 사용하면 특정 원소가 존재하는지 확인 할 수 있다.

if "사과" in data:
    print("\"사과\"를 가진 원소가 data에 존재합니다.")

# 마지막으로 key값만 리턴 받으려면 keys()함수를, value값만 리턴 받기위해서는 values()함수를 사용한다.
print(data.keys())
print(data.values())

# Set(집합)

# 다른 언어와 마찬가지로 중복 X, 순서 X
# 특정 원소가 존재하는지 검사하는 연산의 시간 복잡도는 O(1)
# 따라서 remove(), add() 함수 모두 시간 복잡도는 O(1)이다

# 집합 자료구조를 초기화 할때는
# 1. set()함수 속에 리스트 선언
# 2. {}를 통해 초기화

# 말 그대로 집합이다 보니 차집합(-), 교집합(&), 합집합(|)의 집합연산이 가능하다

a = {1, 2, 3, 4, 5}
b = set([3,4,5,6,7])

print("합집합 = ",a | b)
print("교집합 = ",a & b)
print("차집합 = ",a - b)

# add() : 원소 넣기, remove() : 해당하는 원소 삭제, update([]) : 리스트 형태의 원소 입력(여러개 입력 할 때)

data = set([1,2,3])

data.add(4)
data.remove(2)
data.update([5,6])

# 파이썬의 입출력
# 각 데이터를 공백으로 분리하여 입력받을 때 (리스트로)

# n = int(input())
# m = list(map(int, input().split()))
# print(m)
# map(조건함수, 리스트) : 리스트의 원소 중 조건 함수에 맞는 원소만을 리스트에 남긴다.
# 위의 경우에는 int가 조건이고 input().split()은 입력값을 띄어쓰기에 따라 분리하는데
# 이 분리된 입력값들이 곧 리스트를 이룬다.

# 세가지 변수에 분리하여 입력값을 저장 할 때

# n, m, k = map(int, input().split())

# print(n,m,k, end=" ")

# 하지만 java나 다른 언어에서도 기본적으로 알려주는 것 외에 속도가 빠른 입력 함수가 있다.
# 파이썬의 기본 입력 함수는 input()이지만, 입력값이 수십만개 되고 많을 경우
# sys 라이브러리에 정의 되어있는 sys.stdin.readline() 함수를 이용한다.

import sys
a = sys.stdin.readline().rstrip()
print(a)
# 관형적으로 sys.stdin.readline()뒤에는 rstrip() 함수가 붙는데
# 이는 마지막 입력을 마쳤을 경우 엔터를 칠때 엔터 값 마져 들어가게 되는데
# 이러한 공백 문자를 제거하는 용도로 사용된다.

# f-String
# 출력 할 시 문자열 앞에 f를 붙임으로서 중괄호 안에 변수를 집어넣으면 곧바로 출력된다.

a = 7
print(f"{a}")

# 주요 라이브러리의 문법과 유의점

# 파이썬의 내장함수들
# sum(리스트, 튜플, 딕셔너리) : 원소들의 합 리턴
# min(argvs) : 원소들 중 가장 작은 값 리턴
# max(argvs) : 원소들 중 가장 큰 값 리턴
# sorted(반복 가능한 객체, key = 기준 람다식,reverse=True) : 반복 조건에 따라 정렬한다.
print(sum([20,30,40])) # 반복 가능한(리스트, 튜플, 딕셔너리) 객체를 다 더해준다.
print(sorted([('김회창',50),('Fwang',20),('cheol',30)],key=lambda x : x[1], reverse=True))

# Itertools
# permutations : 리스트와 같은 반복 가능한 객체에서 r개의 데이터를 뽑아 일열로 나열하는 모든 경우(순열)을 계산해준다ㅓ.

from itertools import permutations

data=['a','b','c']
print(list(permutations(data,3)))

# combinations : 리스트와 같은 반복 가능한 객체에서 r개의 데이터를 순서에 상관없이 뽑는다.(조합)

from itertools import combinations

data = ['a','b','c']
print(list(combinations(data,2)))

# product(반복가능한 객체, repeat=뽑을 개수) : 중복 순열
from itertools import product

print(list(product(data,repeat=2)))

# combinations_with_replacement(반복가능한 객체, 뽑을 개수)
from itertools import combinations_with_replacement

print(list(combinations_with_replacement(data,2)))

# Math 라이브러리 속 유용한 함수들

import math

print(math.pi) # pi값 출력
print(math.gcd(12,24)) # 최대 공약수 출력
print(math.factorial(5)) # 5!
print(math.lcm(12,24)) # 최소 공배수 출력

