from typing import List

'''
- 리트코드 해시: letter-combinations-of-a-phone-number
- 해당 문제 풀이는 dfs를 활용한 풀이입니다.
- 문제를 해결하지 못하여 책과 인터넷을 서치한 뒤 다시 풀어본 문제입니다.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs 재귀 함수 생성
        def dfs(index, path):
            # 끝까지 탐색할 경우 백트래킹
            if len(path) == len(digits):
                result.append(path)
                # 함수 호출을 종료
                return 

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
    
        if not digits:
            return []
        
        # 휴대폰 숫자와 숫자에 해당되는 알파벳들을 딕셔너리에 저장
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result

    

    