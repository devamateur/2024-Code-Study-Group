'''
🍪문제 번호 :
*슬라이딩윈도우
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description/

🍈문제 정의 :
문자열 s에서 최대 k번 문자를 바꿔서 같은 문자가 연속하도록 하여 그 길이의 최대길이 구하기.

🍊풀이 시간 :
failed

🍒풀이 방법 :
two pointer 방법으로 해결하기(left, right)
- 문자열 s를 순회하는 포인터 right와 후발 체크 포인터 left를 활용
- right가 움직인 만큼의 문자열 빈도 딕셔너리(frequency)를 생성하고, 윈도우 길이(right-left)안에 max빈도를 뺀 값이 k보다 커야 left를 움직이도록 한다.
    - 윈도우 길이(right-left)가 <k일때는 k만큼 바꿀 문자가 없으므로 패스
    - (right-left)가 > k일때는 k빈도 이상을 바꿀 수 없으므로 left를 옮겨야 한다.
    *윈도우 길이(right-left)이므로 right는 1부터 시작해야한다. ex) 문자열 길이가 4인 경우, 윈도우 길이의 최대값은 4로 정의 되어야 하는데, right를 0으로 시작하게 하면 right-left는 3이 되어버림.

'''
# solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0

        for right,ch in enumerate(s,1):                     # right를 1부터 시작해야한다. :: 인덱스 위차값이 아닌 문자열의 길이를 확인해야하므로.
            frequency[ch] = frequency.get(ch,0) +1
            
            max_ = max(frequency.values())

            if right - left - max_ > k :
                frequency[s[left]] -=1
                left+=1
        
        return right - left