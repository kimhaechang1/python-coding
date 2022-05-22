def make_isPrime(n):
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int((n+1)**(1/2))+1):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j] = False
    return isPrime

def isPrime(n):
    isPrime = make_isPrime(n)
    if isPrime[n]:
        answer = "소수입니다."
    else:
        answer = "소수가 아닙니다."
    return answer
