class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        left = [1]*len(nums)
        right = [1]*len(nums)

        # 현재 숫자 i를 제외한 왼쪽 부분의 곱
        # i=0일 때는 왼쪽 숫자가 없으므로 1
        for i in range(1, len(nums)):
            left[i] *= nums[i-1]*left[i-1]

        # 현재 숫자 i를 제외한 오른쪽 부분의 곱
        # i=len(nums)-1일때는 오른쪽 숫자가 없으므로 1
        for i in range(len(nums)-2, -1, -1):
            right[i] *= nums[i+1]*right[i+1]

        return [left[i]*right[i] for i in range(len(left))]
    
'''
시간 초과..
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            times = 1
            for j in range(len(nums)):
                if i!=j:       # 인덱스가 다를 때에만 곱함
                    times *= nums[j]
            result.append(times)
        return result
'''