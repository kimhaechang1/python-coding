# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
#
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
# 입출력 예 설명
# 입출력 예 #1
#
# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
#
# 입출력 예 #2
#
# 모든 사람이 2문제씩을 맞췄습니다.

def solution(answers):
    answer = [1,2,3]
    answer_score = { 1 : 0, 2: 0, 3:0 }
    s = [0]*3
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if num1[i%5] == answers[i]:
            answer_score[1]+=1
            s[0]+=1
        if num2[i%8] == answers[i]:
            answer_score[2]+=1
            s[1]+=1
        if num3[i%10]== answers[i]:
            answer_score[3]+=1
            s[2]+=1
    answer = sorted(answer, key= lambda x : answer_score[x], reverse=True)

    print(answer)

    if s.count(answer_score[answer[0]]) == 2:
        answer = answer[:2]
    if s.count(answer_score[answer[0]]) == 1:
        answer = answer[:1]
    return answer

# for index, value in enumerate(iterable Object) :
# 반복가능한 객체에서 값을 하나씩 꺼내는데 이때 인덱스 번호도 함께 꺼낸다
# 따라서 지금같은 상황에서는 어짜피 인원이 3명으로 정해져 있으므로
# 스코어 배열을 만들어서 최대 점수값과 동일한 녀석의 인덱스만을 answer 에 추가하면된다.
# 정렬을 무조건적으로 하려고하지말고, 생각해보자!