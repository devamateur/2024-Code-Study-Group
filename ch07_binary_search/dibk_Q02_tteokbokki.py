'''
🍪문제 번호 :
7장 실전문제 - 떡볶이 떡 만들기

🍈문제 정의 :
떡볶이의 크기를 절단하여 크기 이외의 나머지 떡은 손님이 가져갈 수 있다.
손님이 왔을 때, 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 최대값을 구하기
입력값은 N(떡 개수), M(떡 길이)

🍊풀이 시간 :
25분

🍒풀이 방법 :
우선 입력 떡들을 정렬 후, 중간 값을 기준으로 중간 값 이후부터 맨 끝값까지의 총합과 중간 값 차이를 비교하여 구하기.

'''

class Solution :
    
    def cutting(self):
        # 입력
        N,M = map(int,input("떡의 갯수와 길이 : ").split())
        kki = list(map(int,input().split()))
        kki.sort()
        
        start,end = 0, N-1          # 인덱스 기준
        mid = (start+end)//2

        while mid < end :
            # 중간값 mid를 기준으로 그 이후의 값들을 총합하여 그 갯수만큼 mid값을 뺀다.
            # ex) (kki[mid+1] - kki[mid]) + (kki[mid+2] - kki[mid]) + ...
            result = sum(kki[mid+1:]) - kki[mid]*(end-mid)          
            if M == result :
                break
            elif M > result :                   # 원하는 사이즈M보다 결과가 작으면 mid의 값이 크므로, mid의 위치를 왼쪽으로 움직임.
                mid = (start+mid)//2
                
            elif M < result :
                mid = (mid+end)//2    
        
        print("결과 : ",kki[mid])
                                                 
        
        return 
test = Solution()
test.cutting()