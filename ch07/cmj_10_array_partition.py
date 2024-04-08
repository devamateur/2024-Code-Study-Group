class Solution:
    # 원소가 2n개인 숫자 리스트에서 min(a, b) 페어들의 합이 최대가 되는 경우 구하기
    def arrayPairSum(self, nums: List[int]) -> int:

        # 오름차순으로 정렬해서 짝수번의 숫자를 더하면 됨
        # ex) [1, 4, 3, 2] -> [1, 2, 3, 4] 1+3 = 4
        nums.sort()

        sum_ = 0
        for i in range(0, len(nums)-1, 2):
            sum_ += nums[i]
        
        return sum_