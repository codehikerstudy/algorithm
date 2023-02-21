'''
- 프로그래머스 43165번 문제: 타겟 넘버
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/43165
- 해당 문제는 인터넷을 참고하여 풀었습니다. 풀이 방식은 dfs입니다.
    - 해당 문제를 참고한 영상입니다. 여러모로 도움이 많이 된 것 같아 링크를 남깁니다.
    - 영상 출처: https://www.youtube.com/watch?v=S2JDw9oNNDk&ab_channel=%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A1%9C%EC%B7%A8%EC%A7%81%ED%95%98%EA%B8%B0
'''

'''
- 재귀함수가 어려워 일일이 동선을 파악해가며 풀어보았습니다. 아래의 문제 동선은 numbers= [1,1,1], target= 1 일 경우입니다.
dfs(0, 0) ->    dfs(1, 1) ->    dfs(2, 2) ->    dfs(3, 3)  -> return
                                dfs(2, 2) ->    dfs(3, 1)  -> answer +1, return
                dfs(1, 1) ->    dfs(2, 0) ->    dfs(3, 1)  -> answer +1, return
                                dfs(2, 0) ->    dfs(3, -1) -> return
dfs(0, 0) ->    dfs(1, -1) ->   dfs(2, 0) ->    dfs(3, 1)  -> answer +1, return
                                dfs(2, 0) ->    dfs(3, -1) -> return
                dfs(1, -1) ->   dfs(2, -2) ->   dfs(3, -1) -> return
                                dfs(2, -2) ->   dfs(3, -3) -> return
'''
def solution(numbers, target):

    answer = 0

    def dfs(index, sum):
        # 1. 탈출 조건
        if index == len(numbers):      
            if sum == target:   
                # nonlocal 문은 전역변수을 제외한 바로 위의 함수에서 사용되는 변수와 바인딩되어 참조
                nonlocal answer 
                answer += 1
            return
        else:
            # 2. 수행 동작
            dfs(index + 1, sum + numbers[index])
            dfs(index + 1, sum - numbers[index])
            

    dfs(0 ,0)

    return answer

print(solution([1,1,1], 1))