# 유클리드 호제법에 의해 최소 공배수는 두 수의 곱을 두 수의 최대 공약수로 나눈 몫에 해당된다.
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)

