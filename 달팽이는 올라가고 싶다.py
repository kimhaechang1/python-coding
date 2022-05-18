# 달팽이는 올라가고 싶다 다국어
#
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.15 초 (추가 시간 없음) (하단 참고)	128 MB	149999	41726	35321	29.053%
# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
#
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
#
# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
#
# 예제 입력 1
# 2 1 5
# 예제 출력 1
# 4
# 예제 입력 2
# 5 1 6
# 예제 출력 2
# 2
# 예제 입력 3
# 100 99 1000000000
# 예제 출력 3
# 999999901
# 1 : 낮, 2 : 밤 (홀수때 a더하기, 짝수때 b빼기)
# 올라간 후 에는 미끄러지지 않음



def solution(a,b,v):
    if (v -a)%(a-b) == 0:
        answer = (v-a)//(a-b)
    else:
        answer = (v-a)//(a-b)+1
    return answer+1

A,B,V = map(int,input().split())
print(solution(A,B,V))


# 중요한 것은 결국 a-b+a-b+...으로 나아가는데
# 낮에 끝나냐 밤에 끝나냐로 나뉜다
# 따라서 마지막에 낮에 끝난다고 가정하고 실질적으로 하루 이동한 거리로 나누어떨어진다면
# 마지막에 하루가 더 필요한것
# 만약에 아니라면 이틀이 더 필요하다