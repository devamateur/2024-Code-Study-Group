'''
136. Single Number
https://leetcode.com/problems/single-number/description/

[time] 9m
[문제] 정수 리스트에서 하나를 제외하고 모든 요소는 두번씩 존재한다. 여기서 하나만 존재하는 요소를 찾기.
[풀이방식]
- 정수 빈도 딕셔너리를 생성하고, value값(빈도)이 가장 작은 key값을 리턴.
- XOR풀이) XOR연산자('^')는 같은 이진수가 나오면 0으로 수렴한다. 즉, 같은 숫자가 나오면 0으로 다시 바뀌는 방법을 활용하여 풀이함.
    - 1001^1000 : 0001

*linear runtime complexity : 선형 시간 복잡도 :: O(N)
*constant extra space
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums :
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
        
        return min(num_dict,key=num_dict.get)
    

# solution : XOR풀이
# ex) nums = [4,1,2,1,2]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num           

        return result
'''
# 0^4 : 4
00000^0b100 : 0b100

# 4^1 : 5
0b100^00001 : 0b101

# 5^2 : 7
0b101^0b010 : 0b111

# 7^1 : 6
0b111^0b001 : 0b110

# 6^2 : 4
0b110^0b010 : 0b100

'''