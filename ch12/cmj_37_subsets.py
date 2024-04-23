class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subset = []
        visited = [False]*len(nums)

        def dfs(idx: int):
            
            for i in range(idx, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    subset.append(nums[i])
                    dfs(i)
                    subset.pop()
                    visited[i] = False

            if subset:                      ### for문 앞에 있던 if문을 뒤로 가져왔더니 문제 해결...
                result.append(subset[:])
                return
        
        dfs(0)

        return result