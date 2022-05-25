import math
def convert(time):
    H,M = time.split(":")
    return int(H) * 60 + int(M)
def solution(fees, records):
    answer = []
    dm = fees[0] # 기본시간
    df = fees[1] # 기본요금
    pm = fees[2] # 단위시간
    pf = fees[3] # 단위요금
    startTime = {}
    result = {}

    for r in records:
        time, num, inout = r.split()
        if inout == 'IN': # 먼저 입차한 차량의 시간을 저장 (번호 : 시간(분))
            startTime[num] = convert(time)
            if num not in result:
                result[num] = 0 # 누적 결과시간에 존재하지 않는다면 일단 0으로 초기화
        else:
            result[num] += convert(time)-startTime[num] # OUT인 경우엔 출차시간이 time에 있을 것
                                                        # 따라서 출차시간에서 해당 차량번호의 입차 시간을 빼준것을 누적 결과시간에 해당하는 차량번호에 기입
            del startTime[num] # 차량이 나갔으므로 입차 데이터에서 삭제해준다.
    for key, value in startTime.items(): # 입차만 존재하는 차량을 처리
        result[key] += 23*60+59-value # 결국 누적시간에 23:59에서 마지막으로 입차한 시각을 빼준 양을 누적
    for key, value in sorted(result.items()):
        if value <= dm:
            answer.append(df) # 기본시간보다 작거나 같다면 기본요금
        else:
            answer.append(df+ math.ceil((value-dm)/pm)*pf) # 그 반대라면 추가요금(누적시간-기본시간)을 단위시간으로 나누어 단위 요금을 곱해준다.
    return answer


# 먼저 진행과정에 대해서 머리속으로 생각하는 습관을 들여야한다.
# 어떤 자료구조에 어떻게 저장할지 미리 생각하자
# 또한 시간계산같은것은 전처리를 할 함수를 미리 만들어 두자
# 구현문제는 주어진 조건만 잘 따르면 풀 수 있다!
# from collections import defaultdict를 사용하면
# 딕셔너리를 원하는 key값으로 초기화 하기 편해진다.
# 사용법은 collections에서 defaultdict을 불러오고
# defaultdict(원하는 자료형)을 해주면 된다.
