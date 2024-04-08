class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        answer= [i for i in re.sub(r'\W',' ',paragraph.lower()).split() if i not in banned] 
        #대소문자 관련없고 금지어 없으면 리스트에 넣기
        
        dic = {} #빈도수 체크
        for _ in answer:
            if _ not in dic:
                dic[_] = 1
            else:
                dic[_] += 1

        answer = sorted(dic.items(),key=lambda x:x[1],reverse = True) # value기준으로 내림차순

        return answer[0][0]