import sys
sys.stdin = open("input.txt", "r")


def dfs(index, sum_taste_score, sum_kcal):
    global max_taste_score
    # 칼로리 합산이 제한 칼로리 L을 넘어설 경우 return
    if sum_kcal > L:
        return
    # 맛에 대한 점수의 합산이 현재 점수보다 넘어설 경우 새롭게 갱신
    if sum_taste_score > max_taste_score:
        max_taste_score = sum_taste_score
    # DFS로 모든 ingredients 리스트를 돌아서 마지막 인덱스에 도달했다면 return
    if index == N:
        return

    taste_score, kcal = ingredients[index]  # 맛에 대한 점수, 칼로리
    # 현재 인덱스의 재료를 사용한 경우
    dfs(index + 1, sum_taste_score + taste_score, sum_kcal + kcal)
    # 현재 인덱스의 재료를 사용하지 않은 경우
    dfs(index + 1, sum_taste_score, sum_kcal)


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())    # N: 재료의 수, L: 제한 칼로리
    ingredients = [list(map(int, input().split())) for _ in range(N)]   # [[맛에 대한 점수, 칼로리], ... ]
    max_taste_score = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {max_taste_score}')
