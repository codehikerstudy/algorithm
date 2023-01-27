'''
- 프로그래머스 42747번 문제: H-Index
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42747
- 해당 문제는 sort와 max를 활용하여 문제를 풀이하였습니다.
- solution은 직접 풀이한 문제이며, solution2는 solution을 작성하기 전에 틀렸던 오답입니다.
    solution2 오답을 작성하고 난 뒤, 무엇이 잘못되었는지 한참 고민하다가 'h번 이상'의 뜻을 잘못 이해하고 있었다는 것을 깨달았습니다.
    solution2는 h가 citations 배열 안에 있는 요소가 들어가야 된다고 생각하여 코드를 작성하였는데, 문제가 계속 틀려 다시보니 문제를 잘못 이해하고 있었다는 것을 깨달았습니다.
    - 문제를 이해하기 전: h는 citations 배열 안에 있는 요소다. 예를 들어 ciations = [3, 0, 6, 1, 5] 이면, 3번 이상이라는 것이 ciations 배열 안의 3이라는 요소를 의미한다.
    - 문제를 이해한 후: ciations = [3, 0, 6, 1, 5] 이면 h가 3은 맞는데, 이는 단순히 3번 이상이라는 뜻이지, ciations 안에 있는 요소를 의미하는 것이 아니다.
'''
# ciations ex) [3, 0, 6, 1, 5], n = 5, h = 3
def solution(citations: list):

    citations.sort()    # [0, 1, 3, 5, 6]
    h_max = 0
    

    # index = citations 배열의 인덱스, citation = 논문
    for index, citation in enumerate(citations):
        if citation >= len(citations) - index:
            h_max = max(h_max, int(len(citations) - index))
        
    return h_max

# ciations ex) [3, 0, 6, 1, 5], n = 5, h = 3
def solution2(citations: list):

    citations.sort()    # [0, 1, 3, 5, 6]
    h_max = 0
    

    # index = citations 배열의 인덱스, citation = 논문
    for index, citation in enumerate(citations):
        if len(citations[index:]) >= citation:
            h_max = max(h_max, citation)

    return h_max
    

print(solution([7, 9, 1, 5]))

print(solution2([7, 9, 1, 5]))