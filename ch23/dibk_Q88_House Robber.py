'''
198. House Robber
https://leetcode.com/problems/house-robber/description/

[time] 51~
[문제] 인접하지 않은 위치끼리의 최대 누적값을 구하기
[풀이방식] :
(기존의 풀이)
- 징검다리 풀이로 구현을 했는데, 문제는 한번 건너값과 두번 건너값을 비교해서 더 큰 값을 누적해야 했다.
- dp[0],dp[1]에 원래값(nums[0],nums[1])을 정의 후, idx-2, idx-3을 비교하는 조건문을 작성했지만, out of range 오류를 해결하지 못함.
(답지 참고)
- dp[1]을 nums[0],nums[1] max값으로 정의함으로써 그 다음 idx에서 누적값을 비교할 수 있게 활용됨.
- 즉, dp의 마지막 인덱스는 항상 최대값을 갖게 됨.
- dp[idx-1] 이전값, dp[idx-2]+nums[idx] 건너값과 현재값 : 이 둘을 비교했을 때 더 큰 값을 dp[idx]에 저장.

'''

# solution
# ex) nums = [2,1,1,2]
# dp [2,2,3,4
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2 : return max(nums)
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for idx in range(2,len(nums)):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])
        
        return dp[len(nums)-1]
    
# 징검다리 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2 : return max(nums)

        dp = {}
        def robbing(i):
            if i < 0 : return 0
            if i <2 :
                dp[i] = nums[i]
                return nums[i]
            if i in dp : return dp[i]

            dp[i] = nums[i] + robbing(i-2)
            dp[i-1] = nums[i-1] + robbing(i-3)

            return dp[i]

        robbing(len(nums)-1)

        return max(dp.values())