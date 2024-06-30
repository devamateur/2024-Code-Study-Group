'''
207. Course Schedule
https://leetcode.com/problems/course-schedule/description/
[time] Failed
[문제] 링크참고
[풀이방식]
- 
'''
# failed Solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [True]*numCourses

        for sub,prev in prerequisites :
            if visited[prev] :
                visited[sub] = False
            
            else : return False

        return True