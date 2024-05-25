class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 최소값 찾아 피봇 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:         # 회전이 발생한 경우
                left = mid + 1                 # 구간을 오른쪽으로 이동
            else:
                right = mid
        
        pivot = left
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            mid_pivot = (mid+pivot)%len(nums)        ######

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1
    
    ''' 190 / 195 testcases passed
    피봇을 찾는 과정과 이진 검색을 한 반복문에서 처리하려고 하다보니 꼬인 것 같다...

    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        if len(nums) >= 2 and nums[1] == target:
            return 1

        left, right = 0, len(nums)-1

        # 회전이 발생한 경우
        while left <= right:
            mid = (left+right)//2
            curr = nums[mid]          # 현재 값
            #print(f'{mid}: {curr}')
            
            if curr == target:
                return mid
            elif curr < target:
                left += 1
            else:       # target보다 큰 경우
                diff_left = abs(target-nums[left])
                diff_right = abs(target-nums[right])

                if diff_left > diff_right and nums[left] > nums[right]:
                    left += 1
                else:
                    right -= 1


        return -1
    '''