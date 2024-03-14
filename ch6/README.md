## **✏️ Chapter 6 : String Manipulation**
"파이썬 알고리즘 인터뷰" 6장 문자열 조작 내용을 정리하는 공간.  
 
<문제1> - 유효한 팰린드롬: *
#코드
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #모두 소문자로 변환
        for i in range(len(s)):
            if i < len(s)-(i+1):
                if (s[i].isalpha()) and (s[len(s)-(i+1)].isalpha()):  #둘 다 알파벳이면 
                    if s[i].isalpha() == s[len(s)-(i+1)].isalpha(): #둘이 같은 알파벳이면
                        continue
                    else:
                        return False # 서로 다르면 False

            elif i == len(s)-(i+1): #서로 비교하다가 같아진 경우 종료
                return True 

#문제 풀이 여부
테스트 케이스 2,3은 통과했지만 1은 통과하지 못하고 시간 종료
#리뷰
우선 최대한 외부 라이브러리 끌어오는 건 활용하지 않으려고 했음
리스트든 데크(디큐?), 정규식 활용하는 부분을 보고 너무 간단히 풀리는 것에 화가 나버린 상태.
자체 생각한 바로는 양옆에서 하나씩 비교해가며 문자열 중심으로 들어가며 비교하는 방법을 생각해냈었으나, 코드 구현 이슈로 마감. 

<문제2> - 문자열 뒤집기: *
#코드
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

#문제 풀이 여부
시간 안에 성공

#리뷰
이걸 풀었다고 해야할지는 모르겠지만, 
책에서 첫번째 풀이로 올린 두 포인터를 활용해서 하는 방법은 왼쪽 오른쪽에서 스왑하는 방식으로 이루어지는 듯하다.

<문제3> - 로그 파일 재정렬: *
#코드
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

#문제 풀이 여부
시간 안에 성공

#리뷰
문제의 테스트 케이스 2번에 대한 이해가 어려움
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
a8과 ab1의 위치는 왜 저렇게 이루어지는지 조언이 필요함.
Input: logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
Output: ["b fjt","j je","m le","7 zbr","o 33"]
-> 식별자가 아니라 그 뒤에 있는 문자들의 순서로 정해지는 듯함.(.sort(key=lambda x:복수개) 부분에 대한 복기 필요)

<문제4> - 가장 흔한 단어: *
#코드
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

#문제 풀이 여부
5분 정도 오버

#리뷰
lambda 쓰는 거에 익숙해질 필요가 있을지도 모르겠다는 생각을 했음



##전체적인 느낀점
오랜만이라 그런가 문제를 읽고 어떻게 코드로 옮겨적어야하는지 감이 안잡힘. 조금 더 익숙해져야할 필요가 있어보이고
머리로만 생각하는 건 어려울 듯 해서 노트를 활용해서 먼저 문제를 파악하는 걸 우선으로 하고있음. 화이팅...!
