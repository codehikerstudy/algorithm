'''
- 프로그래머스 84512번 문제: 모음 사전
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/84512
- 해당 문제 풀이는 인터넷을 참고하여 풀이하였습니다.
    - 해당 문제는 중복 순열을 활용하여 문제를 풀이하였습니다.
    - 전에 순열과 조합을 활용한 문제들을 접했는데, 중복 순열과 중복 조합도 배울 수 있는 좋은 계기가 되었습니다.
'''
from itertools import product   # 중복 순열

def solution(word: str):
    alph = ['A', 'E', 'I', 'O', 'U']    # 'A', 'E', 'I', 'O', 'U'가 들어 있는 배열 생성
    alph_all = []   # 중복 순열을 활용해 alph의 요소들을 담을 배열 생성
    for i in range(1, 6):   # 1~5까지 순회하는 for문 (최대 5자리이기 때문)
        for j in list(product(alph, repeat=i)): # 1번 중복~5번 중복까지 허용하는 중복 순열 순회
            alph_all.append(''.join(j)) # 중복 순열을 통해 생성된 변수 j를 alph_all 배열에 담음. 이 때 리스트로 되어 있는 j를 문자열로 변환해준다.

    alph_all.sort() # 배열을 정렬
        
    return alph_all.index(word) + 1

print(solution('A'))

    