# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
#
# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.
# 입출력 예
# s	    n	result
# "AB"	1	"BC"
# "z"	1	"a"
# "a B z"	4	"e F d"

def solution(s, n):
    answer=""
    for i in range(len(s)):
        if ord(s[i])>= 97 and ord(s[i])<=122:
            if ord(s[i])+n>122:
                answer+=chr(ord('a')+(n-(122-ord(s[i]))-1))
            else:
                answer+=chr(ord(s[i])+n)
        elif ord(s[i])>= 65 and ord(s[i])<=90:
            if ord(s[i])+n>90:
                answer+=chr(ord('A')+(n-(90-ord(s[i]))-1))
            else:
                answer+=chr(ord(s[i])+n)
        elif ord(s[i])==32:
            answer+=" "
    return answer

# 아스키 <-> 정수 변환이 가능한가 물어본 문제
# 대문자 시작점과 끝 소문자 시작점과 끝을 찍어서 범위를 알아낸다
# 모든 알파벳은 25개 있다
# 외워 두면 편함
# a-z : 65~90
# A-Z : 97~122
# ord() : char -> int
# chr() : int -> char