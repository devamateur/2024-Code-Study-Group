class Solution:
    def install(self):
        '''
            도현이의 집 N개에 C개의 공유기를 설치해서
            가장 인접한 두 공유기 사이 거리가 최대인 경우 구하기

            두 공유기 사이의 거리가 배열 인덱스 차이를 말하는 건 줄 알았는데 그게 아니라
            두 공유기 사이 거리 = 좌표 값 차이
            ex) 1 4 -> 거리 3차이
        '''
        N, M = map(int, input().split())
        houses = []

        for _ in range(N):
            houses.append(int(input()))

        # 집의 좌표를 오름차순 정렬
        houses.sort()

        start = 1 # 가능한 최소 거리(min gap)
        end = houses[-1] - houses[0] # 가능한 최대 거리(max gap)
        result = 0

        while(start <= end):
            mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
            # 첫째 집에는 무조건 공유기를 설치한다고 가정
            value = houses[0]
            count = 1
            # 현재의 mid 값을 이용해 공유기를 설치하기
            for i in range(1, N): # 앞에서부터 차근차근 설치 
                if houses[i] >= value + mid:
                    value = houses[i]
                    count += 1
            if count >= M: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
                start = mid + 1
                result = mid # 최적의 결과를 저장
            else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
                end = mid - 1

        print(result)
s=Solution()
s.install()