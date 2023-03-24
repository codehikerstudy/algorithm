from collections import deque


def solution(begin, target, words):
    """
    BFS를 활용한 풀이
    """
    answer = 0
    deq = deque()
    # [단어, 깊이]를 deq에 담는다. 최초 시작점인 begin을 넣어 초기화를 하고 이 때 depth는 0이다. 
    deq.append([begin, 0]) 
    visited = [0] * len(words)

    while deq:
        word, depth = deq.popleft()
        if word == target:
            answer = depth
            break
        for i in range(len(words)):
            # 비교하는 두 개의 단어가 서로 알파벳이 같을 때마다 count가 1 증가한다.
            # 한 번에 바꿀 수 있는 알파벳이 단 한 개이기 때문에 이것을 확인하기 위한 용도이다.
            count = 0
            # 확인을 하지 않은 경우
            if visited[i] == 0:
                for j in range(len(word)):
                    # 해당 단어가 words의 i번째 단어와 다르다면 한 자씩 비교해서
                    # 단 하나의 알파벳만 다른지 확인한다.
                    # 알파벳 하나가 다를 때마다 temp에 1을 더해준다.
                    # 서로 다른 알파벳이 하나만 다를 경우(count == 1)
                    # deq에 넣어 다음 단어와 비교할 준비를 시킨다. 이 때, depth까지 함께 업데이트한다.
                    # 참고: 주어진 begin, target, words에 담긴 모든 단어들은 글자 수가 같다.
                    if word[j] != words[i][j]:
                        count += 1

                if count == 1:
                    deq.append([words[i], depth + 1])
                    visited[i] = 1  # 방문했음을 표시한다.

    return answer