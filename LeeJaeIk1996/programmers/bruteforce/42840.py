'''
- 리트코드 42840번 문제: 모의고사
- 문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/42840
- solution은 직접 푼 풀이입니다.
'''

def solution(answers):  # 매개변수 answers: 1번 문제부터 마지막 문제까지의 정답
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    # 예외 처리
    if not answers:
        return []

    for index in range(len(answers)):
        if answers[index] == student_1[index % 5]:
            cnt_1 += 1
        
        if answers[index] == student_2[index % 8]:
            cnt_2 += 1

        if answers[index] == student_3[index % 10]:
            cnt_3 += 1

    student_cnt = [cnt_1, cnt_2, cnt_3]
    max_answer = max(student_cnt)
    sol = []


    for index in range(len(student_cnt)):
        if student_cnt[index] == max_answer:
            sol.append(index+1)

    return sol

print(solution([1,2,3,4,5]))
