class Solution:
    def climbStairs(self, n: int) -> int:
    
        # 0번째 항이 1인 피보나치 수열
        step = [1]*(n+1)
        step[1] = 1

        for i in range(2, n+1):
            step[i] = step[i-1]+step[i-2]
            
        return step[n]