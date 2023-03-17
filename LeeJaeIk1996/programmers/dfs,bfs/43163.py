'''
- 프로그래머스 43163번 문제: 단어 변환
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43163
- 해당 문제는 bfs를 활용하여 풀이하였습니다.
'''
from collections import deque

# visited: 방문 여부, w: words 배열의 길이
def bfs(begin: str, target: str, words: list, visited: list, w: int):
    
    queue = deque()
    queue.append((begin, 0))

    while queue:

        current_word, cnt = queue.popleft()  # 현재 queue에 들어 있는 단어
        
        if current_word == target:
            return cnt
            
        for i in range(w):          
            sim_cnt = 0 # 한 번에 한 개의 알파벳만 바꿀 수 있음을 고려
            if not visited[i]:  # 아직 words에 있는 해당 인덱스의 단어에 방문하지 않았다면
                for j in range(len(current_word)):  # 해당 인덱스의 단어와 current_word의 단어 비교
                    if current_word[j] != words[i][j]: # 한 번에 한 개의 알파벳만 바꿀 수 있음을 고려
                        sim_cnt += 1
                if sim_cnt == 1:    # 알파벳 하나만 변경되었다면 해당 단어와 함깨 cnt+1을 queue에 저장
                    queue.append((words[i], cnt +1))
                    visited[i] = True   # 방문 처리
                    
    
    # words 안에 없을 경우
    return 0
                      

def solution(begin: str, target: str, words: list):

    w = len(words)  # words 배열의 길이

    visited = [False] * w  # words 배열의 길이 만큼 visited 배열 생성

    
    answer = bfs(begin, target, words, visited, w)

    return answer

print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"] ))