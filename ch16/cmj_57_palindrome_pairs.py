class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []

        for i, word in enumerate(words):
            backward[word[::-1]] = i       # 단어를 거꾸로 저장 {단어: 인덱스}

        for i, word in enumerate(words):
            if word in backward and backward[word] != i:           # 같은 단어를 발견
                res.append([i, backward[word]])                    # 결과에 두 인덱스 추가
                
            if word != "" and "" in backward and word == word[::-1]:          
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                # 부분 문자열 탐색
                # 접미사: word[J:], 접두사: word[:j]

                if word[j:] in backward and word[:j] == word[j-1::-1]:         # word[j-1::-1]: word[:j]의 역순
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:         # word[:j-1:-1]: word[j:]의 역순
                    res.append([i, backward[word[:j]]])
                    
        return res
    '''
    당근 시간초과
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                pairs = words[i]+words[j]
                if i != j and pairs == pairs[::-1]:
                    result.append([i, j])
        return result
    '''