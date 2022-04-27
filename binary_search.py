# bisect
# 파이썬에서는 이진 탐색을 쉽게구현 할 수 있도록 bisect 라이브러리를 제공한다.
# 특히나 이진탐색은 '정렬 되어있는' 배열에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.

# bisect의 주요 함수로는
# bisect_left와 bisect_right가 있고 이 두 함수 모두 시간복잡도는 O(logN)에 해당된다.
# bisect_left(반복 가능한 객체, x) : 정렬된 객체에서 x원소가 위치할 수있는 가장 왼쪽의 인덱스
# bisect_right(반복 가능한 객체, x) : 정렬된 객체에서 x원소가 위치할 수 있는 가장 오른쪽의 인덱스

import bisect

a=[1,2,4,4,8]
print(bisect.bisect_right(a,5))
print(bisect.bisect_left(a,1))

# 이것을 응용하면 배열의 원소에서 특정 범위 안에 들어가는 값의 개수를 구하는 함수를 만들 수 있다.
# 물론 시간복잡도는 O(logN)이다.

import bisect

def count_by_range(iterable, left_value, right_value):
    left = bisect.bisect_left(iterable, left_value)
    right = bisect.bisect_right(iterable, right_value)
    return right - left

print(count_by_range([1,2,3,3,3,4,4,8,9],-1,3))

