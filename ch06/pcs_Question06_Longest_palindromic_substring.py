class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:  #일단 문자열이 하나이거나 0개이면 그냥 출력
            return s
        
        Max_Len=1 
        Max_Str=s[0]

        for i in range(len(s)-1): #첫 왼쪽에서부터 시작하는 인덱스 번호 설정
            for j in range(i+1,len(s)): #순차적으로 2,3개 ... 씩 지정해서
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]: #각각 비교해서 같으면 
                    Max_Len = j-i+1 #대응되는 문자열의 길이 새롭게 업데이트
                    Max_Str = s[i:j+1] #대응되는 문자열 새롭게 업데이트

        return Max_Str