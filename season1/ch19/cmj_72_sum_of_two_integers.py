class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32비트 정수의 최대값
        MAX = 0x7FFFFFFF
        # 32비트 마스크
        mask = 0xFFFFFFFF
        
        while b != 0:
            # 캐리 계산
            carry = (a & b) << 1
            # 올림수를 제외한 합 계산
            a = (a ^ b) & mask
            # 올림수 할당
            b = carry & mask
        
        # 음수 처리
        return a if a <= MAX else ~(a ^ mask)