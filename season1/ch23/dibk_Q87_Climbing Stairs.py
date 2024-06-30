'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/

[time] 10m, failed
[문제] n층의 계단을 오르는 경우의 수를 구하기(한 번 오를 때 1step,2step만 가능)
[풀이방식] :
- 처음에는 조합 or DFS로 생각함.
- 하지만, 피보나치 문제과 같은 풀이.
    - 누적된 값을 활용하는 문제에 데해서는 dp방법론을 떠오르면 좋겠다.
- 재귀방법은 시간초과.

'''

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        if self.dp[n]: return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.dp[n]
    
# solution이었지만 시간초과
class Solution:
    result = 0
    def climbStairs(self, n: int) -> int:
        if n == 1 : return 1
        if n == 2 : return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
# n = 36까지 가능, 이상의 값에 대해서는 타임아웃
class Solution:
    result = 0
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        

        def func(stairs):
            if stairs == n :
                self.result +=1
                return 
            elif stairs > n : return
            
            for step in steps :
                func(stairs+step)

            return
        
        func(0)
        return self.result

        
