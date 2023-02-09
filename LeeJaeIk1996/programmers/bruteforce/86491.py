'''
- 프로그래머스 86491번 문제: 최소직사각형
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/86491
- 해당 풀이는 직접 풀지 못하여 인터넷을 참고한 풀이입니다.
'''

def solution(sizes):
    
    max_width, max_height = 0, 0

    for width, height in sizes:
        if width < height:
            width, height = height, width
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    
    return max_width * max_height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))