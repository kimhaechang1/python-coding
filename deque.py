# Collections 라이브러리의 deque는 파이썬에서 큐를 구현한다.
# Queue라는 라이브러리는 있지만, 자료구조의 큐를 구현하는 라이브러리는 아니라는점을 기억해야한다.

# 기본적으로 리스트는 리스트의 가장 뒤쪽에 원소를 삽입하거나 삭제하므로
# 가장 앞쪽에 원소를 추가하거나 삭제 할 때는 O(N)에 시간이 걸리지만
# deque는 리스트 자료형과는 다르게 연속적으로 나열된 데이터의 시작부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적이다.
# 하지만 deque는 리스트와는 달리 인덱싱, 슬라이싱 기능은 없다.
# deque 상에 왼쪽에 데이터를 넣고 싶다면 left를 붙여보자
# ex) 기본적으로 리스트에 데이터 추가는 append()지만 왼쪽에 추가하고싶다면 appendleft()를 사용하면 된다.

import collections

data = collections.deque([1,2,3,4])

print(data.popleft())
data.append(5)
print(data)
data.appendleft(1)
print(data)
