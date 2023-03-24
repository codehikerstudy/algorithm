import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        defaultdict 생성자에 list함수를 넘겼기 때문에
        dictionary에 어떤 글자가 key로 존재하지 않을 경우,
        키에 대한 기본값을 비어있는 리스트로 세팅해준다.

        주어진 문자열 배열에서 단어를 하나씩 추출해서
        알파벳 순으로 정렬하여 해당 값은 key로, 원래 값은 value로 딕셔너리에 저장한다.
        딕셔너리는 중복을 허용하지 않기 때문에 anagram이라면
        정렬했을 때 동일한 키 값을 가지게 되고, 이들끼리 그룹을 지을 수 있다.
        """
        dictionary = collections.defaultdict(list)
        for word in strs:
            dictionary[''.join(sorted(word))].append(word)
        return list(dictionary.values())
