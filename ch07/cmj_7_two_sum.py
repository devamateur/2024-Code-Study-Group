class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new_sum = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                new_sum = nums[i] + nums[j]
                if new_sum == target:
                    return [i, j]
    
    def twosum2(self, nums: List[int], target: int) -> List[int]:
        # 두 수의 합 x+y = target이면
        # target - x = y 이므로 이를 이용해 O(n)만에 두수의 합을 구할 수 있음

        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:          # 다른 두 수의 합이므로 자기자신(i)은 포함되지 않음
                return [i, nums[i+1:].index(target-nums[i])+i+1]   # nums가 i+1만큼 밀려났으므로 인덱스도 i+1만큼 더함
            
    def twosum_using_dict(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}        # 딕셔너리에 {숫자: 인덱스} 저장

        for i in range(len(nums)):
            if target - nums[i] in sum_dict:      # 값을 초기화하기 전에 먼저 비교 -> 서로 다른 두 수의 합임을 보장함
                return [i, sum_dict[target-nums[i]]]
            sum_dict[nums[i]] = i 