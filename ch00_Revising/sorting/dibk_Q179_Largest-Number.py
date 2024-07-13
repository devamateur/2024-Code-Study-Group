'''
🍪문제 번호 :
179. Largest Number
https://leetcode.com/problems/largest-number/description/

🍈문제 정의 :
양수로 이뤄진 nums 배열이 있다. 요소들로 가장 큰 숫자를 형성하기.
*문자열로 반환

🍊풀이 시간 :
20분

🍒풀이 방법 :
nums의 요소를 정렬하는데, 
요소들을 str로 바꾸고 해당 요소를 10번 곱하기(같은 문자를 반복시키기)하여 정렬하기


'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 10^9 = 1000000000

        nums = list(map(str,nums))
        nums.sort(key = lambda x : x*10,reverse = True)

        return ''.join(nums) if nums[0] !='0' else '0'