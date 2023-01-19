'''
- 리트코드 문제: set-matrix-zeroes
- 문제 출처: https://leetcode.com/problems/set-matrix-zeroes/
- 해당 문제 풀이는 배열을 활용하여 문제를 풀이하였습니다. 해시 테이블과 관련된 문제라곤 하나, 
    왜 해시 테이블과 연관 있는지는 잘 모르겠습니다..
'''
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = []  # 0이 들어가는 행 값
        row = []     # 0이 들어가는 열 값

        # 값이 0인 경우 각각의 column과 row를 저장
        for c in range(len(matrix)):
            for r in range(len(matrix[c])):
                if matrix[c][r] == 0:
                    # column을 배열에 저장
                    column.append(c)
                    # row를 배열에 저장
                    row.append(r)

        # column들을 0으로 바꿈
        for i in column:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        # row들을 0으로 바꿈
        # 이 부분에서 범위를 벗어났다고(out of range) 계속 오류가 났었으나, 해결함
        for i in row:
            for j in range(len(matrix)):
                matrix[j][i] = 0

        return matrix




        