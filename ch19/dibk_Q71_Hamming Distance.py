'''
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/description/

[time] 5m
[문제] 두 정수의 해밍 거리를 구하기.
[풀이방식]
- 두 정수를 XOR풀이 후, 그 값을 이진수로 바꿔서 '1'숫자를 카운트하기.

*Hamming Distance : 두 개의 길이가 같은 문자열 사이의 거리를 측정. 즉, 둘 중 하나의 문자열에서 몇 개의 문자를 바꿔야 두 문자열이 같아지는 지 측정.
ex) '10'11 and '01'11 :: 2
ex) 'a'bcd'ef' and 'b'bcd'hg' : 3
같은 위치에 있는 두 무자를 비교하여 수를 세는 것.

*해밍 거리 계산 :
두 비트열에 대한 XOR를 하고, 그 값에서 1인 비트의 수를 세면 됨.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x^y
        count = 0

        for i in bin(result):
            if i=='1':
                count+=1
        
        return count
    
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')