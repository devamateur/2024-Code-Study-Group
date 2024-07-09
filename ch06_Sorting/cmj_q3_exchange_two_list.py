class Solution:
    def exchange(self):
        # N: 배열 크기, K: 최대 바꿔치기 횟수

        N, K = map(int, input().split())

        # 배열 A가 최대가 되려면
        # 배열 A의 작은 수와 배열 B의 큰 수가 교체되면 됨
        # 즉, A는 오름차순 B는 내림차순 정렬한 뒤 교체

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        a = sorted(a)
        b = sorted(b, reverse=True)

        idx = 0
        while K > 0 :
            if b[idx] > a[idx]:
                a[idx], b[idx] = b[idx], a[idx]
            else:
                break
            K -= 1
            idx += 1

        return sum(a)
    
solution = Solution()
print(solution.exchange())
