class Solution:
    def reverseString(self, s: List[str]) -> None:

        # 리스트 중간까지
        # 리스트의 왼쪽 원소 <-> 오른쪽 원소 교환
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
        # s[:] = s[::-1]로 간단히 해결가능한 문제였는데
        # 생각을 잘못해서 s = s[::-1]로 새 변수에 할당해서 굳이 교환하는 방법을 택했다..