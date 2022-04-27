# heapq

# heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
# PriorityQueue 라이브러리를 사용 할 수도있지만 코테 환경에서는 보통 heapq가 빠르다.
# 파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도가 O(NlogN)에 오름차순 정렬이 완료된다.

import heapq


def minHeapsort(iterable):
    h = [] # 최소 힙으로 저장되어 있는 리스트
    result=[]
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) # heappush(힙을 저장할 리스트, value) : 리스트에 최소힙으로 value값을 넣는다

    for i in range(len(h)):
        result.append(heapq.heappop(h)) #heappop(힙을 저장한 리스트) : 힙에서 원소를 힙의 성질을 유지하면서 뺀다
                                        # 이 때 결국 정렬이 되어 오름차순으로 원소가 나오게 된다.
    return result

def maxHeapsort(iterable): # 기본적으로 파이썬의 heapq 라이브러리는 최소 힙 이기 때문에 루트노드에 가장 작은 원소가 들어가게 된다
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value) # 이 성질을 역으로 이용하면 최대 힙을 구성할 수 있게 되고
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 따라서 최대 힙의 결과에 따라 내림차순으로 결과값을 가질 수 있다.
    return result
minHeap_result = minHeapsort([1,3,5,7,9,2,4,6,8])
maxHeap_result = maxHeapsort([1,3,5,7,9,2,4,6,8])
print(minHeap_result)
print(maxHeap_result)

