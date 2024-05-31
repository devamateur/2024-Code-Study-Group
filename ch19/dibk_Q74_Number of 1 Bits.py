'''
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/description/

[time] 1m
[문제] 입력 받은 정수를 이진표현으로 바꾸고, 1비트의 수를 구하기.
[풀이방식]
- Q70과 같은 풀이
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')