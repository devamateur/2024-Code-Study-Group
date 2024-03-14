class Solution:
    '''
    # https://velog.io/@ilov1112/Leetcode-5.-Longest-Palindromic-Substring-with-Python
    IDEA :
    - 짝수 window, 홀수 window 를 활용하여 좌->우 방향으로 확인하기
    - 작은 사이즈 window에서 사이즈를 키워가는 방식
    
    Note :
    - window 크기를 짝수로만 진행한 점, 확인 방향을 문자열 중간부터하려고 했던 점이 문제해결 실패 요인
    '''

    def windows(self, s, left, right):
            # left가 -1이 되거나 right가 문자열 사이즈를 넘어가고, 값이 다르면 while break
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # s[left]와 s[right]가 같았던 부분까지 return
            return s[left+1:right]
        
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1 or s == s[::-1]: return s
        
        result = ''
        
        # 좌->우 방향으로 확인하기
        for left in range(len(s)-1):
            even_window = self.windows(s, left, left+1)         # 짝수윈도우 : 2크기부터 +2씩 확인하기
            odd_window = self.windows(s, left, left+2)          # 홀수윈도우 : 3크기부터 +2씩 확인하기
            result = max(result, even_window,odd_window, key=len)   # 비교
        return result



'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        IDEA :
        - 포인터 2개 사용(인덱스의 위치) : left, right
        - 1. left, right를 비교하기
        - 2-1. left == right이면, 각자 +1,-1   :: end_idx == right, flag =T, 인덱스 위치값 저장!
        # - 2-2. left != right이면, (left위치 + right위치)//2 의 위치로 right 위치로 바꾸기
        - 2-1. left != right이면, right -1 --> 1번 반복
        - 3.flag =T, 
        - 3-1. left != right이면, right는 원래 end_idx로 변경, flag =F
        - 3.2. 1번 반복
        
        Note :
        - 2문자 이하는 오류 발생
        - 문자열의 맨 앞,뒤부터 시작하여 비교하기 때문에 연산시간이 길다.(가장 큰 문자열 기준)
        """

        left, end_idx = 0, len(s)-1
        flag = True
        left_idxs, right_idxs = list(),list()

        while left < end_idx :

            for right in range(end_idx,left,-1):
                if s[left] == s[right] :
                    flag = True
                    left_idxs.append(left)
                    right_idxs.append(right)
                    end_idx = right-1
                    break

            else :
                end_idx = len(s)-1
                flage= False
                left +=1
                continue

            if not flag :
                left_idxs.pop()
                right_idxs.pop()
            
            left +=1
        
        return s[left_idxs[0]:right_idxs[0]+1]

        
# 시간 복잡도
# 1000만 데이터 이하(연산횟수)이면 O(N) 알고리즘 가능
https://wikidocs.net/222560
https://1-day-1-coding.tistory.com/42

'''