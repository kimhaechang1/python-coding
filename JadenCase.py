# JadenCase 문자열 만들기
# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.
# 입출력 예
# s	return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"

def solution(s):
    #s = "1Aaa         aa"
    strings = s.split(" ")
    temp = []
    for i in strings:
        if i == '':
            temp.append('')
        elif i[0].isdigit():
            i = i[0]+i[1:].lower()
            temp.append(i)
        else:
            i = i[0].upper()+i[1:].lower()
            temp.append(i)
    answer = " ".join(temp)
    return answer


# replace로 풀려고 했을때 문제점이 발생하였다
# 즉 replace는 해당 문자열 내에 특정한 문자열이 존재 할 경우 다른 문자열로 교체하는건데
# 내가 원하는 범위를 교체하는 것이 아니다!
# 범위를 지정하여 교체하고 싶다면 새로 문자열을 만들어서 합치는게 낫다
