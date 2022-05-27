# 체스판 다시 칠하기
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	67578	31877	25660	47.270%
# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
#
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
#
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
#
# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
#
# 예제 입력 1
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# 예제 출력 1
# 1
# 예제 입력 2
# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB
# 예제 출력 2
# 12
# 예제 입력 3
# 8 8
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# 예제 출력 3
# 0
# 예제 입력 4
# 9 23
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBB
# BBBBBBBBBBBBBBBBBBBBBBW
# 예제 출력 4
# 31
# 예제 입력 5
# 10 10
# BBBBBBBBBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBWBWBWBWB
# BWBWBWBWBB
# BBBBBBBBBB
# 예제 출력 5
# 0
# 예제 입력 6
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWWWB
# BWBWBWBW
# 예제 출력 6
# 2
# 예제 입력 7
# 11 12
# BWWBWWBWWBWW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBWWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# 예제 출력 7
# 15

#  8<=NM<=50
# 입력값의 범위가 2500이므로 완전탐색으로 해결 가능
# M = 열, N = 행
# 미리 체스판의 영역을 두가지로 만들어 놓음
# 4중 for문 사용,가장 바깥쪽 2중 for문은 안쪽에서 돌 8x8의 체스판의 이동범위 결정
# 체스판의 인덱스 합이 짝수인 경우와 홀수인 경우로 나눈다.
# 그기에서 시작에 따라 다른 결과가 나오므로 개별적으로 카운팅


def chk(i,k,m):
    fw= 0
    fb = 0
    for n in range(i,i+8):
        for j in range(k,k+8):

            if (n+j) %2 == 0: #(0,2)(0,4) (2,0)
                # 시작이 w인 경우
                if m[n][j] != "W":
                    fw+=1
                # 시작이 B인 경우
                if m[n][j] !="B":
                    fb +=1
            else: #(0,1)
                # 시작이 w인 경우
                if m[n][j] !="B":
                    fw+=1
                # 시작이 B인 경우
                if m[n][j] !="W":
                    fb+=1
    return fw, fb


def solution(N,M,m):
    result = []
    for i in range((N-8)+1):
        for k in range((M-8)+1):
            a1, a2 = chk(i,k,m)
            result.append(a1)
            result.append(a2)
    print(min(result))
N, M = map(int,input().split())
m = []
for i in range(N):
    m.append(list(map(str,input())))

solution(N,M,m)

# 체스판과 같이 번갈아가면서 0과 1의 의미를 가지는 2차원 배열의 경우
# 인덱스의 합이 짝수냐 홀수냐에 따라 그리고 시작값이 0이냐 1이냐에 따라 조건을 나눌 수 있다.

