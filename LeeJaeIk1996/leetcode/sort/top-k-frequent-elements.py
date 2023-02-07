'''
- 리트코드 347번 문제: top-k-frequent-elements
- 문제 출처: https://leetcode.com/problems/top-k-frequent-elements/
- Solution은 직접 푼 풀이이고, Solution2는 책을 참고한 풀이입니다.
'''

'''
- 해당 문제 풀이는 직접 푼 풀이입니다.
- collections.Counter를 활용하여 빈도 수를 파악하였고, 
    sorted()를 활용하여 딕셔너리의 value(= 빈도 수)를 내림차순으로 정렬하였습니다.

- 문제 풀이 방법:
1. collections.Counter를 활용하여 매개변수 nums 배열의 요소들의 개수를 파악한다.
    nums_cnt = Counter(nums)
2. 해당 문제는 k개 까지 가장 많은 빈도를 보이는 요소를 출력하는 문제이기 때문에
    가장 많은 개수를 갖고 있는 요소부터 가장 적은 개수를 갖고있는 요소까지 내림차순으로 정렬한다.
    또한 sorted는 리스트를 반환해주기 때문에 dict()을 활용하여 딕셔너리로 변환한다.
    nums_cnt = dict(sorted(nums_cnt.items(), key=lambda x:x[1], reverse=True))
3. nums_cnt를 순회하며 k개 까지의 요소들을 넣어서 반환한다.
    for key in nums_cnt:
        if k == 0:
            break
        sol.append(key)
        k -= 1

    return sol
'''
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sol = []    # output 배열 변수 선언

        nums_cnt = Counter(nums)

        # value 값을 기준으로 내림차순으로 정렬
        nums_cnt = dict(sorted(nums_cnt.items(), key=lambda x:x[1], reverse=True))
    
        for key in nums_cnt:
            if k == 0:
                break
            sol.append(key)
            k -= 1

        return sol


'''
- 해당 문제 풀이는 책을 참고한 풀이입니다.
- collections.Counter()를 활용하여 배열 요소의 개수를 파악하였고, heappush와 heappop을 활용하여 순서대로 반환할 수 있도록 하였습니다.
- 아직까지는 heapq 모듈이 와닿지가 않습니다. (ex: 이것보단 Solution에서 풀었던 것처럼 풀면 되지 않나..) 아직 heapq를 활용한 문제 풀이를 두 번밖에 접하진 못했지만
    heapq와 관련된 두 문제 풀이를 보았을 때 'heappop을 통해 작은 수부터 반환할 수 있다'는 것을 활용해 문제를 풀 수도 있다는 것을 알게 되었습니다.
'''
from heapq import *

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []

        # 힙에 음수로 삽입 (내림차순으로 구하기 위해)
        for f in freqs:
            heappush(freqs_heap, (-freqs[f], f))
        
        topk = []
        # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heappop(freqs_heap[1]))

        return topk




print(Solution.topKFrequent('',[1],1))
