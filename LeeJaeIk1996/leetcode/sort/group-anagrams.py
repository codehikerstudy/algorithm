'''
- 리트코드 49번 문제: group-anagrams
- 문제 출처: https://leetcode.com/problems/group-anagrams/
- 해당 문제 풀이는 sorted와 defaultdict을 활용하여 풀이하였습니다.

- 문제 풀이 방법
1. 매개변수 str에 있는 애너그램을 저장할 anagrams 변수를 생성한다.
    같은 문자를 갖고 있는 str의 배열 요소들을 담기 위해 defaultdict을 활용한다.
    defaultdict을 활용할 경우 input이 ["eat","tea","tan","ate","nat","bat"]라면
    defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
    과 같은 결과를 만들어 낼 수도 있다.
2. 매개변수 str을 순회한다.
3. 매개변수 str에 들어 있는 문자를 알파벳 순으로 정렬하여 key로 저장한 뒤, 해당 문자를 value에 저장한다.
    anagrams[''.join(sorted(word))] -> 문자(word)를 알파벳 순으로 정렬하여 key로 저장
    .append(word) -> 해당 문자를 value에 저장
4. 딕셔너리로 되어 있는 anagrams를 output으로 필요한 value값만 추출하여 list로 반환한다.
    return list(anagrams.values())
'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)    # str에 있는 애너그램을 저장할 anagrams

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())

print(Solution.groupAnagrams('', ["eat","tea","tan","ate","nat","bat"]))