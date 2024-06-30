# ch6 문제 리뷰1
<br>

### 1. 유효한 팰린드롬
- 주어진 문자열이 팰린드롬(앞뒤가 똑같은 문자열)인지 확인하는 문제
- 공백, 쉼표 등 특수문자를 제외하는 것에 유의해야 함 
<br><br>

- 내 풀이 방식: 알파벳과 숫자로 이루어진 문자만 리스트에 저장한 뒤, 슬라이싱을 이용해 팰린드롬인지 비교
    ```python
    for word in s:
        if word.isalpha() or word.isdigit():           # 알파벳 또는 숫자인지 확인 isalnum()으로 대체가능
            alpha_numerics.append(word.lower())
        
    if alpha_numerics == alpha_numerics[::-1]:
        return True
    ```
<br>

- 단익님 풀이
- : 문자열의 반을 앞뒤로 보고 달라지는 경우 False 리턴
- 입력의 크기가 2 * 105인 걸 고려했을 때 시간복잡도 측면에서 효율적인 것 같음
    ```python
    for i in range(s_half) :
        if s_list[i] != s_list[s_size-1-i] :
            return False
    return True
    ```
<br>


### 2. 문자열 뒤집기
- 주어진 문자열 리스트를 뒤집는 문제
- 리턴없이 문자열을 직접 조작해야 함(in-place)
<br><br>

- 내 풀이 방식: 슬라이싱을 이용해 풀려고 했으나 s[:] = s[::-1]이 아닌 s = s[::-1]로 잘못 생각해서 문제는 직접 swap해서 해결했음
- 내장함수인 s.reverse()를 이용해서 해결할 수도 있음
    ```python
    # 리스트 중간까지
    # 리스트의 왼쪽 원소 <-> 오른쪽 원소 교환
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[len(s)-i-1]
        s[len(s)-i-1] = temp
    ```
<br>

### 3. 로그 파일 재정렬
- "식별자 콘텐츠1 콘텐츠2 ... 콘텐츠 n" 형식의 리스트에서
    1. 알파벳 로그가 숫자 로그보다 앞에 와야 함
    2. 알파벳 로그는 콘텐츠 별로 정렬, 콘텐츠가 같으면 식별자 순으로 정렬
- 위 조건을 만족하도록 리스트를 정렬하는 문제
<br><br>

- 내 풀이 방식: 알파벳 로그를 따로 리스트에 저장해서 sorted()를 이용해 정렬한 뒤, 숫자 로그와 연결
    ```python
    ordered_logs = []
    for log in logs:
        split_log = log.split()

        if split_log[1].isalpha():       # 알파벳 로그 먼저 추가
            ordered_logs.append(log)

    # 알파벳 로그를 사전순으로 정렬하고 digit log와 이어붙임
    ordered_logs = sorted(ordered_logs, key=lambda x: (x.split()[1:], x.split()[0])) 
                    + [log for log in logs if log.split()[1].isdigit()]

    ```
<br>

### 4. 가장 흔한 단어
- 주어진 문자열에서 금지어를 제외한 가장 흔한 단어를 출력하는 문제
- 내 풀이1: 문자열을 공백 단위로 split한 뒤 딕셔너리로 빈도수 계산
    - 공백 단위로 구분되지 않은 단어의 경우 단어가 제대로 분리되지 않는 문제 발생
    - 예외 케이스 <br>
        Input: "a, a, a, a, **b,b,b,c,** c" ["a"] <br>
        Output: "bbbc" <br>
        Expected: "b" <br>

- 내 풀이 2: 문자열을 split하기 전 모든 특수문자를 공백으로 먼저 대체
    ```python
    new_para = re.sub(r'[^\w]', ' ', paragraph)
    ```
- 정규표현식
    - \w: 알파벳, 숫자, 언더바에 해당하는 문자. [A-z0-9__]와 동일
    - \W: 알파벳, 숫자, 언더바를 제외한 **특수문자**. [^A-z0-9__]와 동일