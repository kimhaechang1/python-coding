# 파이썬에서 진법변환
# 특수한 진법으로 표시된 문자열 숫자는 int('숫자문자열',밑수)를 통해 10진수로 변환 가능하다.
print(int('1200',3)) # 3진법으로 표시된 '1200'을 10진법으로 변환

# 10진수는 2, 8, 16 진법으로 변환 가능하다
bin()
oct()
hex()

# sorted의 key 람다함수를 잘 써먹어보자
# 우선 딕셔너리에서 딕셔너리.items()는 key,value로 되어있는 튜플값들이 모인 리스트를 형성한다.
# 딕셔너리에서 key 값을 기준으로 정렬
# sorted(딕셔너리.items())

# 딕셔너리에서 value 값을 기준으로 정렬
# 여기서 중요한 점은 딕셔너리.items()로 형성된 리스트 속 튜플 중 두 번째 값을 꺼내야 한다는 점이다.
# 따라서 p.items()를 통해 리스트 속 튜플요소들을 꺼내고 그 것을 람다함수에서 두 번째 값을 기준으로 한다고 정의 해야한다.
# sorted(딕셔너리.items(),key = lambda item : item[1])

