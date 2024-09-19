class Solution:
    max_val = -int(1e9)
    min_val = int(1e9)
    def make(self):
        N = int(input())       # 숫자 개수
        
        nums = list(map(int, input().split()))       # 숫자
        op_count = list(map(int, input().split()))   # 덧셈, 뺄셈, 곱셈, 나눗셈 개수


        def dfs(depth, result):
            if depth == N:
                self.max_val = max(self.max_val, result)
                self.min_val = min(self.min_val, result)
                return
        
            for i in range(4):
                if op_count[i] > 0:
                    op_count[i] -= 1
                    if i == 0:
                        dfs(depth+1, result+nums[depth])
                    if i == 1:
                        dfs(depth+1, result-nums[depth])
                    if i == 2:
                        dfs(depth+1, result*nums[depth])
                    if i == 3:
                        dfs(depth+1, int(result/nums[depth]))        ## result//nums[depth]로 했더니 틀림..
                    op_count[i] += 1

        dfs(1, nums[0])

        print(self.max_val)
        print(self.min_val)
s = Solution()
s.make()