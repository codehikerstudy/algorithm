import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))  # 현재 테스트 케이스의 모든 가격 정보
    answer = 0
    max_cost = 0

    """
    주어진 가격정보를 뒤에서부터 순회를 한다.
    미리 싸게 사서 미래에 높은 가격에 팔아서 이득을 남기는 것은
    미래의 높은 가격에서 현재 싸게 산 가격을 빼는 것이다. 따라서 뒤에서부터 순회하는 것!
    
    중간 중간 최고가가 변동될 수 있기 때문에
    현재 가격이 기존 최고가보다 높다면 갱신을 해준다.
    """
    for i in range(len(cost)-1, -1, -1):
        if cost[i] > max_cost:
            max_cost = cost[i]
        else:
            answer += max_cost - cost[i]

    print(f'#{test_case} {answer}')
