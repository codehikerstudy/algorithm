from typing import List
from collections import defaultdict

'''
- 리트코드 해시 문제: group-anagrams
- 해당 문제 풀이는 defaultdict을 활용하여 문제를 풀이하였습니다.
- 해당 문제는 이전에 풀었던 기억이 있어 다시 복기하며 문제를 풀었습니다.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # defaultdict을 활용
        counter = defaultdict(list)

        for word in strs:
            # 정렬을 한 뒤 딕셔너리에 추가
            tmp = ''.join(sorted(word)) # aet
            counter[tmp].append(word)

        return list(counter.values())
