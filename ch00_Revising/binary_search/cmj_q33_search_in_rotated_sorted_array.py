class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 피봇 인덱스 찾기
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        pivot = left

        # target
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            rotated = (mid+pivot)%len(nums)       # 원래의 중간 인덱스

            if nums[rotated] == target:
                return rotated
            elif nums[rotated] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1