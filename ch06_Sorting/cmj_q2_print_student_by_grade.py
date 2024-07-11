class Solution:
    def sort_grade(self):
        N = int(input())

        students = []

        for _ in range(N):
            st = input().split()
            students.append([st[0], int(st[1])])
        
        students = sorted(students, key=lambda x: x[1])
        
        for i in range(len(students)):
            print(students[i][0], end=' ')

solution = Solution()
solution.sort_grade()