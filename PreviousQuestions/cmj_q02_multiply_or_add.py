class Solution:
    def multiply_or_add(self):
        '''
            모든 숫자 사이에 X 혹은 +를 넣어 연산 결과, 가장 큰 수를 구하는 문제
            단, X를 먼저 계산하는 일반적인 연산과 달리
            모든 연산은 왼쪽에서 차례대로 수행
        '''

        nums = input()

        result = int(nums[0])

        # 0, 1을 제외한 모든 수를 곱하면 최대
        for i in range(1, len(nums)):
            if result > 1 and int(nums[i]) > 1:
                result *= int(nums[i])
            else:
                result += int(nums[i])
        print(result)

s = Solution()
s.multiply_or_add()