'''
- 프로그래머스 해시 42579번: 베스트앨범
- 해당 문제 풀이는 해시를 활용한 풀이입니다.
- 결과적으로 문제를 풀지 못하여 인터넷 서치를 한 뒤 학습을 통해 재작성한 코드입니다.
- 해당 문제 풀이는 아직 제대로 숙지하지 못해서 다시 공부할 예정입니다.

- 문제 풀이 방법
1. 딕셔너리 2개를 준비한다.
    genres_dict = defaultdict(int)  # 어떤 장르가 몇 회 재생되었는지 나타내는 딕셔너리
    genres_freq = defaultdict(list) # 장르 별 곡의 인덱스와 재생 횟수를 묶어서 갖고 있는 딕셔너리
2. 각 딕셔너리를 추가한다.
3. 재생 횟수를 기준으로 내림차순으로 정렬한다.
4. 장르 별 많이 재생된 곡 2곡 이하를 집어넣기 위해 genre_freq 0번 요소인 인덱스를 sol에 추가시킨다.

'''
from collections import defaultdict

def solution(genres: list, plays: list):
    sol = []
    genres_dict = defaultdict(int)  # 어떤 장르가 몇 회 재생되었는지 나타내는 딕셔너리
    genres_freq = defaultdict(list) # 장르 별 곡의 인덱스와 재생 횟수를 묶어서 갖고 있는 딕셔너리

    for i in range(len(genres)):
        genres_dict[genres[i]] += plays[i]
        genres_freq[genres[i]].append((i, plays[i]))

    # 재생 횟수를 기준으로 내림차순 정렬
    genres_dict = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)
    for g in genres_freq:
        genres_freq[g].sort(key=lambda x: x[1], reverse=True)

    for g, _ in genres_dict:
        sol.append(genres_freq[g][0][0])
        if len(genres_freq[g]) > 1 :
            sol.append(genres_freq[g][1][0])

    return sol
