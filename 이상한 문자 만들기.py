# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"
# 입출력 예 설명
# "try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

def solution(s):
    answer = []
    words = s.split(" ")
    print(words)
    for word in words:
        w=""
        for i in range(len(word)):
            if i %2 == 0 :
                w+=word[i].upper()
            else:
                w+=word[i].lower()
        answer.append(w)

    return " ".join(answer)

print(solution("try           hello world ddff"))

# 해결 방법
# 모든 공백을 없앨려면 split()을 해주면 되지만
# 기준점을 주기 위해서는 split(" ")을 해주어야 한다.
# 공백이 하나 이상임에 주의하자
# 공백이 하나 이상인것은 공백을 세알려야 하는것
# 즉 공백을 인정해야 하는것
# "구분자".join(iterable) 하면 각각의 문자들을 구분자를 포함한 채로 전체 긴 문자열로 만들어 준다.
# split(" ") <<이것과 동일한 의미라고 생각하면됨(기능은 다르겠지만)