## 중복조합, 완전탐색 문제이다.
## 문제의 조건에서 가질수 있는 경우의 수를 따지고
## 해당하는 모든 경우의 수를 하나하나 비교하며 최신 값을 업데이트

from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11),n):
        # 점수가 중복되어 뽑힐 수 있고 순서는 상관없다 (0~10)
        # 즉, 라이언이 가질수 있는 모든 경우의 수 뽑기(중복조합)
        cnt = Counter(comb)
        # 여기서 해당 점수를 맞춘 횟수가 중요하므로 Counter
        print(cnt)
        score1, score2 = 0 ,0 # score1 : ryan, score2 : apeach
        for i in range(1, 11):
           print(cnt[1])
           if info[10-i]< cnt[i]:
                score1 +=i
           elif info[10-i]>0: # info[10-i] = 0 즉, 해당 점수를 못얻는 경우에 대해서는 점수가 안올라야 한다.
                score2 +=i
        diff = score1-score2
        if diff> max_diff:
            max_comb_cnt = cnt
            max_diff = diff
    # 최종적으로 나온 점수별 맞춘 개수와 차 를 토대로 answer 연산
    if max_diff>0:
        # max_diff>0 즉, 라이언이 최종적으로 이겼다는 것
        # max_comb_cnt의 key값이 점수 과녘이고 value가 맞춘 횟수이므로
        answer = [0]*11
        for n in max_comb_cnt:
            answer[10-n] = max_comb_cnt[n]
            # 주의 해야 할 점은 문제에서도 설명했듯이 인덱스와 점수는 서로 반대이다.
        return answer
    else:
        return [-1]
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))


# 원래 없는 key값에 대응하는 value는 출력할 수 없으나
# Counter를 사용하여 dict를 만든 경우 없는 key값에 대해서도 default value 로 0을 가진다.