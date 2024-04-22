class Solution:
    def dfs(self, idx, digits, letter_map, alpha, result):
        # 경로 한 개 탐색이 끝나면 리턴
        if len(alpha) == len(digits):
            result.append(alpha)
            return result
        

        for i in range(idx, len(digits)):
            for al in letter_map.get(digits[i]):
                self.dfs(i+1, digits, letter_map, alpha+al, result)        ### i+1로 다음 매핑 인덱스를 넘겨줘야 함


    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
                        "7":"pqrs", "8":"tuv", "9":"wxyz"}
        visited = [False]*26
        result = []

        if not digits:
            return result
            
        self.dfs(0, digits, letter_map, "", result)

        return result