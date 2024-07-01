class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sum_list = []
        #visited = [False]*len(candidates)        # 원소를 중복으로 사용할 수 있으므로 방문 여부를 표시할 필요가 없음음

        def dfs(idx):
            if sum(sum_list) > target:      # base case
                return

            if sum(sum_list) == target:
                result.append(sum_list[:])
                return
            
            for i in range(idx, len(candidates)):
                sum_list.append(candidates[i])
                dfs(i)
                sum_list.pop()

        dfs(0)

        return result