class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 엣지 케이스
        if len(nums) == 1:
            return nums[0]

        # s: 부분 배열의 합을 저장
        s = [0]*len(nums)

        s[0] = nums[0]        # 첫 값은 nums[0]으로 초기화

        for i in range(1, len(nums)):
            if nums[i] >= s[i-1]:          # 이전 구간까지 합보다 더 큰 숫자가 나오면
                s[i] = max(nums[i], s[i-1]+nums[i])           # 숫자와 이전 구간 합+숫자 중 max를 택함
            else:              # 이전 구간까지 합보다 작은 숫자가 나오면
                s[i] = s[i-1] + nums[i]         # 이전 구간 합 + 숫자

        return max(s)         # 배열 합 중 최대 리턴          