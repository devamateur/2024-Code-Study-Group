class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i],nums[j],nums[k]] not in answer:
                            answer.append([nums[i],nums[j],nums[k]])
                    else:
                        continue

        return answer