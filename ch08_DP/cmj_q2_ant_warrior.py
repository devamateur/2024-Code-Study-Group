class Solution:
    def take_food(self):
        N = int(input())
        foods = list(map(int, input().split()))
        
        foods[1] = max(foods[0], foods[1])
        foods[2] = max(foods[1], foods[0]+foods[2])       # 이제보니 이 식이 답지의 점화식과 같다

        # 이 점화식이 답은 나오는데 중간 합계값이 좀 틀림
        for i in range(3, len(foods)):
            foods[i] = max(foods[i] + foods[i-2], foods[i]+foods[i-3])         

        print(foods)
        print(max(foods))

    # 답지
    def take_food2(self):
        # 정수 N을 입력 받기
        n = int(input())
        # 모든 식량 정보 입력 받기
        array = list(map(int, input().split()))

        # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
        d = [0] * 100

        # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
        d[0] = array[0]
        d[1] = max(array[0], array[1]) 
        for i in range(2, n):
            d[i] = max(d[i - 1], d[i - 2] + array[i])          # d[i-1]: 이전의 최대합, d[i-2]+array[i]: i-2번째 + 현재값

        # 계산된 결과 출력
        print(d[n - 1])
s = Solution()
s.take_food()