class Solution:
    '''
        N명의 병사의 전투력이 주어질 때, 
        전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
        -> 배치 과정에서는 특정 병사를 제외함. 그러면서도 남아있는 병사의 수가 최대가 되야 함
    '''
    def deploy(self):
        N = int(input())

        power = list(map(int, input().split()))
        dp = [1] * N

        # LIS
        # 배열 뒤에서부터 부분 수열이 증가하는지 확인
        # 개념을 떠올렸는데 구현을 못했음...
        for i in range(N-2, -1, -1):
            for j in range(N-1, i-1, -1):     # j: i의 뒤에 있는 원소들
                if power[j] < power[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(N-max(dp))

s = Solution()
s.deploy()

'''    
방법 1. 뒤에서부터 전투력이 낮은 병사 제외
맨 뒤 원소가 작은 값일 경우, 중간에 있는 더 큰 값들이 제외될 수 있음
ex) 12 2 5 3 2 10 8 7 15 5 4 3 -> 작은 값인 3을 무조건 포함하게 되므로 전투력이 최대가 될 수 없다
- 이 개념을 좀 확장하면 LIS로 풀 수 있었을 것 같다

class Solution:

    def deploy(self):
        N = int(input())

        power = list(map(int, input().split()))
        no_soldier = 0

        for i in range(N-2, -1, -1):
            if power[i] < power[i+1]:       # 현재 원소 앞에 작은 값이 나오면 제외 병사 증가
                no_soldier += 1
        print(no_soldier) 
        
'''