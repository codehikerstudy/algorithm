from collections import Counter

'''
1. max_pocketmon = nums 리스트의 max값인 n/2
2. dic_pocketmon = 중복을 배제하기 위해 딕셔너리로 변경
3. min값인 len(dic_pocketmon) 과 max값인 max_pocketmon을 비교하여 min값이 결과로 나오도록 설정
4. 단순히 min 함수를 사용하여 min값을 뽑아내면 됐었는데 if else를 사용하여 코드 수를 낭비한 것 같아서 아쉬움
'''
def solution(nums):
    answer = 0
    
    max_pocketmon = len(nums) / 2
    
    dic_pocketmon = Counter(nums)
    
    if max_pocketmon >= len(dic_pocketmon.keys()):
        answer = len(dic_pocketmon.keys())
        return answer
    else:
        answer = max_pocketmon
        return answer