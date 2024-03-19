class Solution:
    # 투포인터
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()            ## 정렬, 투포인터로 구간을 조작할 때  target과 비교해서 오른쪽/왼쪽으로 구간을 이동하기 위함

        num_list = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:           # 같은 값은 스킵
                continue
            target = -nums[i]         # a+b+c=0, b+c = -a 임을 이용

            j = i+1
            k = len(nums)-1

            while j<k:
                if nums[j]+nums[k] == target:
                    num_list.append([nums[i], nums[j], nums[k]])

                    # 같은 값은 스킵
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                else:
                    if nums[j]+nums[k] < target:        # 두 수의 합이 target보다 작으면, 오른쪽으로 이동
                        j += 1
                    elif nums[j]+nums[k] > target:      # 두 수의 합이 target보다 크면, 왼쪽으로 이동
                        k -= 1
        return num_list
    
''' 당연히 시간초과
    def brute_force(self, nums: List[int]) -> List[List[int]]:

        num_list = []

        nums.sort()

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and [nums[i], nums[j], nums[k]] not in num_list:
                        num_list.append([nums[i], nums[j], nums[k]])

        return num_list
'''