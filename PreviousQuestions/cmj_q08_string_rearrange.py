class Solution:
    def rearrange(self):
        alpha_nums = input()

        alpha = []       # 알파벳만 저장하는 리스트
        nums = 0         # 숫자 합

        for char in alpha_nums:
            if char.isdigit():       # 숫자인 경우, 합 계산
                nums += int(char)
            else:
                alpha.append(char)   # 숫자가 아니면 리스트에 저장

        alpha.sort()              # 리스트 오름차순 정렬

        print("".join(alpha)+str(nums))
s = Solution()
s.rearrange()