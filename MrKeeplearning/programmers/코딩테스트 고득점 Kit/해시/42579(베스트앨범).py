def solution(genres, plays):
    answer = []

    # zip 객체는 이터레이터이기 때문에 한 번 반복을 완료했다면 다시 재사용할 수 없다.
    # 따라서 `playlist = zip(genres, plays)`와 같이 변수에 할당했을 때 두 번 사용하는 것이 안됨.

    # 장르 별 총 재생 횟수
    genre_plays = {}

    # key: 장르명, value: (곡명, 재생 횟수)
    music_info = {}

    # enumerate함수를 사용하면 인덱스와 원소에 동시 접근이 가능하다.
    for i, (g, p) in enumerate(zip(genres, plays)):
        # (곡명, 재생횟수)형태의 튜플을 생성한다.
        if g not in music_info:
            music_info[g] = [(i, p)]
        else:
            music_info[g].append((i, p))

        # 장르 별 총 재생 횟수를 기록
        if g not in genre_plays:
            genre_plays[g] = p
        else:
            genre_plays[g] += p

    # sorted(genre_plays.items(), key=lambda item: item[1], reverse=True)
    # 튜플을 원소로 가지는 리스트의 두 번째 요소에 해당하는 value(총 재생 횟수)를 기준으로 내림차순 정렬을 한다.
    for (genre_name, total_genre_play) in sorted(genre_plays.items(), key=lambda item: item[1], reverse=True):
        # 앞의 for문에서 선택된 장르 중 상위 2개 곡만 선정하여 answer에 곡명만 담는다.
        for (music, music_play) in sorted(music_info[genre_name], key=lambda item: item[1], reverse=True)[:2]:
            answer.append(music)

    return answer