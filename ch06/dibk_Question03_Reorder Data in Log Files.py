class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()
        
        for log in logs :
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else :
                letter_logs.append(log)
        
        letter_logs.sort(key = lambda x : (x.split()[1:],x.split()[0]) )

        return letter_logs + digit_logs
    
    
'''
- decimal : 십진수를 표현하는 문자(1,2,3,,), 각 나라의 고유 십진수 문자
- isdigit : decimal + 위,아래첨자 십진수 + 기타 표현 십진수
isnumeric : decimal + isdigit + 분수,로마 숫자, 중국어 숫자

'''