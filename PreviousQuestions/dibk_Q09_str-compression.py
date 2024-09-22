'''
🍪문제 번호 :
12장 구현 - 09 : 문자열 압축

🍈문제 정의 :
입력된 문자열 S를 1개 이상 단위로 문자열을 압축하여 표현했을 때, 가장 짧은 길이를 return하기

🍊풀이 시간 :
failed

🍒풀이 방법 :
입력된 문자열에서 비교할 문자열 a,b로 나눈 후, a,b가 같아질 때까지 반복하기
- 대상이 되는 문자열의 중간인덱스를 구하고, 인덱스를 기준으로 a와 b를 비교(윈도우 사이즈 == 중간 인덱스까지의 길이)
    - 다르다면, 윈도우 사이즈를 -1해서 비교하는 작업 반복하기
예제5번 주의

solution과 내 풀이의 차이
윈도우 사이즈를 1부터 증가하는 방식, 중간 인덱스까지 확인. 두번째 for문에서 문자열을 전부 확인하는데 윈도우 사이즈만큼 step뛰기(포인트)

'''
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer



# failed
def solution(s):
    answer = ''
    
    def comparison(a,b):
        """
        두 리스트의 문자열을 비교하는 함수
        """
        for cha, chb in zip(a,b):
            if cha != chb :
                return False
        return True
    
    window = len(s)//2
    checkidx = window
    test = s
    
    tmp =''
    answer =[]
    
    while True :
        a = test[:checkidx]
        b = test[checkidx:checkidx+window] 
        
        if comparison(a,b):
            if answer and answer[-1][1] == a:
                answer[-1][0] +=1
            else :
                answer += [2,a],    
            
            test = tmp
            tmp =''
            window = len(a)
            checkidx +=1
            
        else :
            window -=1
            checkidx -=1
            tmp = s[checkidx+window:]
            
    return answer
