# 하노이 탑 문제
def recu(n,a,b,c):
    if  n == 1:
        print("if")
        print(a,c,"if문 속 출력")
    else:
        print("else")
        recu(n-1,a,c,b)
        print(a,c)
        recu(n-1,b,a,c)
def solution(n):
    recu(n,1,2,3)
n = int(input())
print(2**n-1)
solution(n)





