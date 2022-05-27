def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
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

print(solution(45, 3))
print(convert(45,3))