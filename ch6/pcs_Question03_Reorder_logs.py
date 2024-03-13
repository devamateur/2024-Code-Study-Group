class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        n=0
        for i in logs:
            if i.split()[1].isnumeric(): #식별자 구분해서 식별자 외에 첫번재 오는 요소가 숫자이면
                answer.append(i) #새로운 리스트의 뒷쪽에 부착
            else:
                answer.insert(n,i) #문자인 경우에는 새로운 리스트의 앞쪽에 부착
                n=+1 #단, 붙는 순서를 고려하여 인덱스 번호 부여
        return answer
