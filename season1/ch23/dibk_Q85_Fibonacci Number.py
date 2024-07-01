'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/description/

[time] 3m, 10m
[문제] 피보나치 수열 구현하기
[풀이방식] :
- 재귀풀이와 다이나믹풀이로 구현.

'''
class Solution:
    def fib(self, n: int) -> int:
        if n <=1 : return n
        
        return self.fib(n-1)+self.fib(n-2)
    
    
class Solution:
    def fib(self, n: int) -> int:
        if n <=1 : return n

        dp = {}
        def func_fib(num):
            if num <=1 : return num
            if num in dp : return dp[num]

            dp[num] = func_fib(num-1)+func_fib(num-2)

            return dp[num]
        
        func_fib(n)
        
        return dp[n]
