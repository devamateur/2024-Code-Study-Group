# solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        weight = 1
        
        # [1,2,3,4]
        for num in nums:
            ans.append(weight)      # 1, 1, 2, 6
            weight = weight*num     # 1*1, 1*2, 2*3, 6*4
        
        # ans = [1,1,2,6]
        weight = 1
        for idx in range(len(nums)-1,-1,-1):
            ans[idx] = ans[idx]*weight          # 6*1, 2*4, 1*12 , 1*24
            weight = weight*nums[idx]            # 1*4, 4*3, 12*2

        return ans

'''
Time Limit Exceeded

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(math.prod(nums[:i]+nums[i+1:]))
        
        return ans
'''