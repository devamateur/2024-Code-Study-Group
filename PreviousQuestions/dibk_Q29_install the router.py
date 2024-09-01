'''
🍪문제 번호 :
15장 이진탐색 - 29 : 공유기 설치

🍈문제 정의 :
N개의 집이 수직선 위에 있다. 공유기 C개를 설치하려고 하는데, 가장 인접한 두 공유기 사이의 최대 거리를 출력하기.
* 공유기 간의 간격의 최솟값 구하기

🍊풀이 시간 :
failed

🍒풀이 방법 :
문제 해석 : https://kkkdh.tistory.com/entry/BOJ-2110%EB%B2%88-%EA%B3%B5%EC%9C%A0%EA%B8%B0-%EC%84%A4%EC%B9%98-%EB%AC%B8%EC%A0%9C-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-with-C
문제를 정말 구리게 작성한 것 같다. 아니면 내 문해력이 거지 같은 거겠지..
풀이 다시보기

'''
class Solution :
    def setting(self):
            
        # 입력
        N,c = map(int,input('N개, x값 : ').split())
        components = list()
        for _ in range(N):
            components += int(input()),
        
        components.sort()
        start = components[0]
        end = components[-1] - components[0]       # 수정함 : (origin) components[N-1]
        
        while start <= end :
            mid = (start+end)//2                    
            
            value = components[0]
            count = 1
            
            for i in range(1, N): # 앞에서부터 확인
                
                if components[i] >= value + mid:        
                    value = components[i]
                    count += 1
            if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
                start = mid + 1
                result = mid # 최적의 결과를 저장
            else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
                end = mid - 1
        
        print(result)
        return 
    
test = Solution()
test.setting()