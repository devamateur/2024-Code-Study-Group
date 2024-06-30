'''
371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/description/

[time] 5m
[문제] 두 정수의 합을 구하기.(+,-연산자 사용 불가)
[풀이방식]
- and, XOR 풀이를 활용하여 계산
    - XOR은 둘 중 하나만 1이면 1, and는 둘다 1이어야 1
    - 즉, and값이 있으면 왼쪽으로 이동(쉬프트), XOR의 값을 더하면 됨.
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        and_ = (a&b)
        or_=(a^b)

        if and_ :
            and_ = and_<<1

        return and_+or_