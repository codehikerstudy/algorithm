'''
- 프로그래머스 42842번 문제: 카펫
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42842
- 해당 풀이는 직접 푼 풀이입니다.

- 문제 풀이 방법:
1. 해당 문제의 핵심은 다음과 같다고 생각하였습니다.
    - 가로가 세로보다 길거나 같다는 점
    - yellow의 가로, 세로가 핵심이며 yellow의 크기에 따라 brown의 크기가 결정된다는 점
        ex) yellow의 가로, 세로 길이의 +2가 brown의 가로, 세로 길이이다.
    이러한 생각을 통해 문제를 풀어나갔습니다.
2. 우선 yellow의 가로, 세로 길이를 구하기 위해 yellow의 길이를 순회하며 약수를 구한다.
    이 때, 세로가 가로보다 길 경우 스킵한다.
    for i in range(1, yellow + 1):
        if (yellow % i == 0) :
            yellow_width = i           # 가로
            yellow_height = yellow // i # 세로
            if yellow_height > yellow_width:  # 세로가 더 길 경우 스킵한다.
                continue
3. yellow의 가로와 세로 길이가 정해지면, 이에 따른 brown의 가로, 세로 길이를 구한다. 
    여기서 brown의 길이는 yellow의 +2라는 점을 고려한다.
    brown_width = yellow_width + 2
    brown_height = yellow_height + 2
4. 만약 brwon의 가로 * 세로 길이(사각형의 크기) - yellow가 brown의 개수와 같다면 최종적인 width와 height를 구할 수 있다.
    if (brown_width * brown_height) - yellow == brown:
                width = brown_width
                height = brown_height

    return [width, height]
'''

def solution(brown, yellow):

    for i in range(1, yellow + 1):
        if (yellow % i == 0) :
            yellow_width = i           # 가로
            yellow_height = yellow // i # 세로
            if yellow_height > yellow_width:  # 세로가 더 길 경우 스킵한다.
                continue
            brown_width = yellow_width + 2
            brown_height = yellow_height + 2
            if (brown_width * brown_height) - yellow == brown:
                width = brown_width
                height = brown_height


    return [width, height]                
                

print(solution(24, 24))