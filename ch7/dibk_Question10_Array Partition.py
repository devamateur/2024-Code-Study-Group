class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for idx in range(1,len(nums),2):
            ans +=min(nums[idx-1],nums[idx])
            
        # for idx in range(0,len(nums),2):
        #     ans +=nums[idx]
    
        return ans