result= []
def back(num,N,M,visited):
    global result
    if num == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i]=True
            result.append(i)
            back(num+1, N, M, visited)
            result.pop()
            visited[i]=False
# 수열의 개수 1~N, 뽑는 개수 M
def solution():
    N, M = map(int, input().split())
    visited=[False]*(N+1)
    print(visited)
    back(0,N,M,visited)
solution()
