# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
# 입출력 예 설명
# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
#
# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

import collections
def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    c = list(set(completion))
    for item in c:
        a[item] = a[item] - b[item]
    print(a)
    for key,value in a.items():
        if value > 0:
            answer = key
    return answer

print(solution(["A", "A", "B"],["A", "A"]))

# 위 문제는 결국 동명이인을 어떻게 처리 하냐 인데
# 동명이인이 사람 2명인걸 나타낼수만 있으면 된다.
# collections.Counter로 생성한 dict이나 set은 객체이므로
# 객체끼리 빼기연산이 가능하다
# 위의 for item in c : 부분을
# collections.Counter(participant) - collections.Counter(completion) 로 바꿀 수 있다.
# dict() 객체는 .items 를 통해 두가지 변수로 출력이 가능하다.
