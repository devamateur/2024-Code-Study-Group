class Solution:
    def reverse_sort(self):
        N = int(input())

        num = []

        for _ in range(N):
            num.append(int(input()))

        num = sorted(num, reverse=True)

        result = ''
        for i in range(len(num)):
            result += str(num[i]) + ' '

        return result
    
solution = Solution()
print(solution.reverse_sort())