class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        
        # for idx_,num in enumerate(nums)
        for idx_ in range(len(nums)):
            val_ = target - nums[idx_]
            if val_ in dict_.keys():
                return [dict_[val_], idx_]
            
            dict_[nums[idx_]] = idx_
        
        return