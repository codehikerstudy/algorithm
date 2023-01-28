'''
- 리트코드 56번 문제: merge-intervals
- 문제 출처: https://leetcode.com/problems/merge-intervals/
- 해당 문제는 너무 미련이 남아 주말에 좀 풀어보겠습니다.
'''
from typing import List

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# intervals[i].length == 2
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         sol: List[List[int]] = []
#         sol2: List[List[int]] = []
#         start = 1
        
#         intervals.sort(key= lambda x: x[0])
        
#         for x, y in intervals:
#             if start <= len(intervals)-1 and  y >= intervals[start][0]:
#                 if y >= intervals[start][1]:
#                     sol.append([x, y])
#                 else:
#                     sol.append([x, intervals[start][1]])
#                 if x >= intervals[start][0]:
#                     sol.pop()
#                     sol.append([intervals[start][0], intervals[start][1]])
#                 intervals.pop(start)
#                 start += 1
#             elif start <= len(intervals)-1 and y >= intervals[start][0] and y >= intervals[start][1]:
                
#                 sol.append([intervals[start][0], y])
#                 intervals.pop(start)
#                 start += 1 
#             else:
#                 sol.append([x, y])

#             start +=1

#         start = 1

#         for x, y in sol:
#             if start <= len(sol)-1 and  y >= sol[start][0]:
#                 if y >= sol[start][1]:
#                     sol2.append([x, y])
#                 else:
#                     sol2.append([x, sol[start][1]])
#                 if x >= sol[start][0]:
#                     sol2.pop()
#                     sol2.append([sol[start][0], sol[start][1]])
#                 sol.pop(start)
#                 start += 1
#             elif start <= len(sol)-1 and y >= sol[start][0] and y >= sol[start][1]:
                
#                 sol2.append([sol[start][0], y])
#                 sol.pop(start)
#                 start += 1 
#             else:
#                 sol2.append([x, y])
            
#             start +=1

        
#         return sol2

        



