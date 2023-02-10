'''
- 프로그래머스 87946번 문제: 피로도
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/87946
- 해당 풀이는 인터넷을 참고하여 풀이하였습니다.
    - 이번 풀이는 아예 접근조차 하지 못했습니다. 아무래도 모든 경우의 수를 다 따져보자는 생각
        자체를 못했기에 접근을 못한게 아닐까 싶습니다.
    - 해당 문제는 던전의 개수가 최대 8개이므로 순열로 접근할 경우 시간복잡도는 n!이며 최대
        8!*8의 시간 안에 풀 수 있습니다.
'''
from itertools import permutations  # 순열

def solution(k, dungeons):
    max_dungeons = 0
    
    for per in list(permutations(dungeons, len(dungeons))):
        tmp_k = k
        count = 0   # 던전 수 초기값이자 0으로 초기화
        for p in per:
            if tmp_k >= p[0]:   # 최소 필요 피로도가 있는지 확인
                tmp_k -= p[1]   # 소모 필요도 빼기
                count += 1      # 던전 수 업데이트
        max_dungeons = max(max_dungeons, count) # 최대 던전 탐험 수
    
    return max_dungeons


print(solution(80, [[80,20],[50,40],[30,10]]))