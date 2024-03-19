class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #모두 소문자로 변환
        for i in range(len(s)):
            if i < len(s)-(i+1):
                if (s[i].isalpha()) and (s[len(s)-(i+1)].isalpha()):  #둘 다 알파벳이면 
                    if s[i].isalpha() == s[len(s)-(i+1)].isalpha(): #둘이 같은 알파벳이면
                        continue
                    else:
                        return False # 서로 다르면 False

            elif i == len(s)-(i+1): #서로 비교하다가 같아진 경우 종료
                return True 
