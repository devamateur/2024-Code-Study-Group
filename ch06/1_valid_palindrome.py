class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numerics = []  # 알파벳과 숫자를 저장하는 리스트

        for word in s:
            if word.isalpha() or word.isdigit():           # 알파벳 또는 숫자인지 확인 isalnum()으로 대체가능
                alpha_numerics.append(word.lower())
        
        if alpha_numerics == alpha_numerics[::-1]:
            return True
