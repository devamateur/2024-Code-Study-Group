class Solution:
    def reverse(self):
        s = input()

        zeros = 0
        ones = 0
        zeros_result = 0
        ones_result = 0

        # 다른 패턴이 나올때마다 카운트 증가
        # ex) 11111-> 모두 다 1이므로 0 출력, 00000001 -> 1일 때, 0값들에 대한 zero_result를 증가함
        for i in range(len(s)):
            if s[i] == '1':       # 1일 때
                if zeros > 0:         # 이전에 0값들이 있었으면, 0 카운트 증가
                    zeros_result += 1
                    zeros = 0
                ones += 1
            else:                 # 0일 때
                if ones > 0:
                    ones_result += 1
                    ones = 0
                zeros += 1
        print(max(zeros_result, ones_result))

s = Solution()
s.reverse()