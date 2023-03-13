def solution(numbers, target):
    answer = 0
    def dfs(index, sum):
        """
        :param index: 현재 dfs call에서 더하거나 빼야 할 숫자가 위치한 인덱스
        :param sum: 여태까지의 누적합
        :return: target을 출력하는 조합의 수
        """
        nonlocal answer

        # 1. 탈출조건
        # 인덱스가 numbers 배열의 길이와 같아지는 순간 더 이상 더하거나 뺄 것이 없으므로
        # 재귀함수를 더 이상 호출하지 않아야 한다.
        if index == len(numbers):
            # 만약 sum이 target과 같다면
            # 원하는 결과를 얻은 것이기 때문에 answer의 카운트 값을 올려준다.
            if sum == target:
                answer += 1
            return

        # 2. 수행동작
        # 현재 받은 인덱스 값에 1을 더해서 다음 인덱스로 이동한다. -> index + 1 로 표현
        # 두 번째 파라미터인 sum은 dfs 재귀함수를 call했을 때, 현재까지의 누적합을 담고 있다.
        # 따라서 재귀함수를 call할 때는 call하기 전의 인덱스 값을 sum에 더해주어 작성한다.
        # 더하기와 빼기 두 가지 연산이 있기 때문에 두 가지 경우에 대한 재귀함수를 작성한다.
        dfs(index + 1, sum + numbers[index])
        dfs(index + 1, sum - numbers[index])
    dfs(0, 0)
    return answer
