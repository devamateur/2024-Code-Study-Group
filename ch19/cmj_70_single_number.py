class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        # xor 성질
        # 서로 같은 수를 xor 하면 0이 나오는데, x과 0을 xor 하면 항상 x가 나오는 성질이 있음
        # ex) [4, 1, 2, 1, 2] -> 1 xor 1 = 0, 0 xor 1 = 1, 1 xor 1 = 0, 0 xor 4 = 4
        for num in nums:
            xor ^= num
            
        return xor