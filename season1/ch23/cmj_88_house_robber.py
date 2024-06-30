class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0]*len(nums)

        if len(nums) == 1:
            return nums[0]

        money[0] = nums[0]
        money[1] = nums[1]

        for i in range(2, len(nums)):
            money[i] = max(money[i-2]+nums[i], money[i-3]+nums[i])           # 두 칸 or 세 칸 건너 집에 있는 돈 중 최대를 택함
        
        return max(money)