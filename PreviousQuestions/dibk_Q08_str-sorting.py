'''
🍪문제 번호 :
12장 구현 - 08 : 문자열 재정렬

🍈문제 정의 :
입력값으로 알파벳대문자와 숫자로만 구성된 문자열이 입력된다.
알파벳은 오름차순으로 정렬하고, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.

🍊풀이 시간 :
6분

🍒풀이 방법 :
입력값을 str로 받고, for문을 돌면서 알파벳은 새로운 배열에 저장, 숫자는 숫자합을 구한다.
알파벳배열을 정렬한 후, 숫자합을 str로 바꿔서 뒤에 붙이기

'''
class Solution :
    
    def sorting(self):
        input_N = str(input("입력 : "))
        num_sum = 0
        ch_list = []
        
        for ch in input_N:
            if ch.isdigit() :
                num_sum +=int(ch)
            else :
                ch_list.append(ch)
        
        ch_list.sort()
        result = ''.join(ch_list) +str(num_sum)
        
        print(result)
    
test = Solution()
test.sorting()