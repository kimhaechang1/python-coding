def recu(n,k):
    if n == k:
        print(n)
        return
    else:
        print(n)
        recu(n+1,k)
    print(n)

k = int(input())
recu(0,k)