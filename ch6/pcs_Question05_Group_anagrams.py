class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word,answer = {},{}
        for w in strs:
            k = ''.join(sorted(w)) #각 문자열 받아서 구성하고 있는 알파벳 추출 후 join -> 문자열로 다시 묶음
            word[w] = k

        for i in range (len(word)):
            if word[strs[i]] not in answer: #정답 딕셔너리에 정렬된 철자들 있는지 조회 
                n_k = word[strs[i]]
                answer[n_k] = [strs[i]] #없으면 넣고
            else:
                n_k = word[strs[i]]
                answer[n_k] += [strs[i]] #있으면 value값에 추가로 넣기
        return answer.values()