# collections 라이브러리 Counter 함수
# Counter(반복가능한 객체) : 배열 속에 반복되는 원소들의 개수를 센다
# 원소의 횟수를 알기 위해선 배열['원소명']으로 접근한다
# dict()를 활용하여 딕셔너리 형태로도 사용 가능하다.


import collections

counter = collections.Counter(['red','red','blue','blue','blue','green'])

print(counter['red'])
print(counter['blue'])
print(dict(counter))