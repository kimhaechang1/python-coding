# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
#
# 제한 조건
# n은 길이 10,000이하인 자연수입니다.
# 입출력 예
# n	return
# 3	"수박수"
# 4	"수박수박"

def solution(n):
    answer = ''
    word = "수박"
    ord_word="수"
    print("수박"*n)
    if n==1:
       answer+="수"
    elif n%2 == 0:
        print("수박"*(n//2))
    else:
        answer+=("수박"*(n//2))
        answer+=ord_word
    return answer

print(solution(3))

# 슬라이싱을 활용하면 좀 더 쉽게 풀 수 있다


def solution(n):
    answer="수박"*n
    return answer[:n]

print(solution(4))