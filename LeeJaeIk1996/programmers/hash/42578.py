'''
프로그래머스 해시 42578번: 위장
- 해당 문제는 해시를 활용한 풀이입니다.
- 최종적으로 문제를 풀지 못하여 인터넷을 서치하여 공부한 뒤 재작성한 코드입니다.

풀이 과정
1. 의상의 종류 별 갯수를 파악하여 딕셔너리에 저장한다.
ex) {
        "headgear" :  2,
        "eyewear"  :  1
    }

2. 의상의 종류에 따라 입는다/입지 않는다로 나뉜다는 것을 기억하며 문제를 파악한다.
우선 headgear의 경우,
- yellow_hat을 입는다
- green_turban을 입는다
- 둘 다 입지 않는다.
총 3가지의 경우로 나뉜다. 그 다음 eyewear의 경우,
- blue_sunglasses를 입는다.
- 입지 않는다
총 2가지의 경우로 나뉜다. 이는 즉, "의상의 종류 + 1" 이라는 것을 알 수 있으며,
각각 의상의 종류의 경우의 수를 곱한다.
이는 아래의 풀이에서 cnt *= (dict_clothes[i] + 1)에 해당한다.

3. 해당 문제에서 "스파이는 하루에 최소 한 개의 의상은 입습니다." 라는 문구가 있으므로 반환할 때 -1을 한다.
'''
def solution(clothes):
    
    dict_clothes = {}
    for a, b in clothes:
        dict_clothes[b] = dict_clothes.get(b, 0) + 1
        
    cnt = 1
    for i in dict_clothes:
        cnt *= (dict_clothes[i] + 1)
    
    return cnt - 1
    
        