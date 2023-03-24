class Solution1:

    """
    미완성 코드입니다.
    """
    def solution(self, answers):
        # 수포자는 정확히 3명이라고 언급함
        rule1 = [1, 2, 3, 4, 5]
        rule2 = [2, 1, 2, 3, 2, 4, 2, 5]
        rule3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        rule_list = [rule1, rule2, rule3]
        iteration_list = []

        # zip()을 활용할 것이기 때문에 주어진 answers의 길이와 수포자 각각의 규칙이 반복되는 총 길이가 비슷해야 한다.
        # 정확히는 len(answers) < len(수포자 규칙)
        # 수포자의 규칙이 반복되어야 하는 횟수는 기본적으로 몫을 이용한다.
        # 하지만 항상 나누었을 때 딱 떨어지는 것이 아니고, 만약 나머지가 생긴다면 반복횟수가 1회 더 추가되어야 한다.
        for i in rule_list:
            # rule의 길이보다 answers의 길이가 짧다면 zero division error가 발생하기 때문에
            # 이러한 경우 rule의 반복횟수를 1로 지정한다.
            if len(answers) // len(i) == 0:
                iteration_list.append(1)
            else:
                iteration_list.append(len(answers) // len(i))
        
        for i in iteration_list:
            # answers의 길이를 rule의 길이로 나누었을 때 나머지가 발생하면 반복횟수가 1회 더 추가
            if len(answers) % len(rule_list[i]) is not None:
                iteration_list[i] += 1

        return iteration_list


class Solution2:
    def solution(self, answers):
        seq1 = [1, 2, 3, 4, 5]
        seq2 = [2, 1, 2, 3, 2, 4, 2, 5]
        seq3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

        scores = [0, 0, 0]
        for idx, answer in enumerate(answers):
            if answer == seq1[idx % len(seq1)]:
                scores[0] += 1
            if answer == seq2[idx % len(seq2)]:
                scores[1] += 1
            if answer == seq3[idx % len(seq3)]:
                scores[2] += 1

        answer = []
        for idx, score in enumerate(scores):
            if score == max(scores):
                answer.append(idx + 1)
        return answer

