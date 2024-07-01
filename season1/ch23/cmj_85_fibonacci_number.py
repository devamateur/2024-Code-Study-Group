class Solution:
    def fib(self, n: int) -> int:
        cache = [0]*(n+1)

        # 예외 케이스
        if n == 0 or n == 1:
            return n

        cache[1] = 1

        for i in range(2, n+1):
            cache[i] = cache[i-1]+cache[i-2]

        return cache[n]