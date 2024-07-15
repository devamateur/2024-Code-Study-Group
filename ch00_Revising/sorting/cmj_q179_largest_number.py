class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # 사전순으로 뒤에 있는 문자가 앞에 오면 됨
        nums = list(map(str, nums))       # 원소를 문자열 타입으로 변환
        nums = sorted(nums, key=lambda x: x*10, reverse=True)    # 10곱하는 이유: 입력에서 0 <= nums[i] <= 10의 9승 이므로
        
        if nums[0] == '0':           # nums = [0, 0]인 경우 위 코드로는 '00'이 리턴되므로
            return '0'

        return ''.join(nums)
