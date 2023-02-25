from typing import List


class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = ["eat","tea","tan","ate","nat","bat"] 일 때 각 요소를 정렬하면 동일한 값이 나오는 것들이 있다.
        이 때, 동일한 값들을 키로 활용해서 hash table을 생성한다.

        dictionary에는 다음과 같이 분류가  되어 있어야 한다.

        dictionary = {
            "aet": ["eat", "tea", "ate"],
            "ant": ["tan", "nat"],
            "abt": ["bat"]
        }
       """
        dictionary = {}
        for word in strs:
            # sorted함수는 정렬된 값을 배열로 전달하기 때문에
            # str()함수를 사용해서 문자열로 만들어 sorted_word에 저장한다.
            sorted_word = str(sorted(word))
            # 만약 정렬된 문자가 dictionary에 없는 상태라면 새롭게 비어있는 리스트를 키에 대한 기본값으로 세팅한다.
            if sorted_word not in dictionary:
                dictionary[sorted_word] = []
            # 키에 대응되는 anagram을 value로 지정
            dictionary[sorted_word].append(word)
        return dictionary.values()


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        배열을 사용한 풀이

        문제의 아이디어: anagram이라면 단어를 구성하는 알파벳의 등장횟수가 동일하다.
        e.g., ate와 eat은 모두 a가 1번, e가 1번, t가 1번 등장한다.

        문제의 제약 조건 중에 다음과 같은 제약 조건이 존재한다.
        strs[i] consists of lowercase English letters.

        알파벳 소문자는 총 26개이고, 26개의 알파벳만 등장할 것이다.
        크기가 26인 정수 배열을 사용해서 문자의 등장 횟수를 저장할 수 있다.

        Solution2의 시간 복잡도
        * 첫 번째 for loop는 입력된 단어 수만큼 반복
        * 두 번째 for loop는 단어의 글자 수만큼 반복
        * 정렬과 같은 시간이 오래 걸리는 작업이 없기 때문에 O(n * w)만큼의 시간이 소요

        Solution2의 공간 복잡도
        * 단어의 길이에 영향을 받지 않음(키로 길이가 26으로 고정된 배열을 사용하기 때문)
        * O(26n) 소요
        """
        dictionary = {}
        for word in strs:
            # counter: 크기가 26인 배열
            counter = [0] * 26
            for ch in word:
                # 배열의 인덱스를 계산하는 방법
                #
                # 파이썬의 ord함수를 사용하면 글자를 넘겼을 때 유니코드를 반환한다.
                # ord(ch) - ord('a')를 사용하면 ch가 a일 때 0이 되고, ch가 b라면 1이 된다.
                # 마찬가지로 ch가 z라면 25가 된다.
                # 이러한 원리를 사용해서 counter[0]에는 알파벳 a가 몇 번 등장했는지,
                # counter[1]에는 알파벳 b가 몇 번 등장했는지 저장하게 된다.
                counter[ord(ch) - ord('a')] += 1

            # 파이썬에서 배열은 변할 수 있는 자료구조이기 때문에 해시테이블의 키로 사용할 수 없다.
            # 따라서 튜플로 변환을 해서 불변하는 자료구조로 만들어야 키로 사용할 수 있다.
            if tuple(counter) not in dictionary:
                # counter가 dictionary에 존재하지 않는다면
                # counter를 키로 가지는 값을 빈 배열로 설정한다.
                dictionary[tuple(counter)] = []
            dictionary[tuple(counter)].append(word)

        return dictionary.values()
