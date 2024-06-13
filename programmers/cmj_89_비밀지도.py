def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        # or 연산
        num = arr1[i]|arr2[i]
        result = ''

        for bit in bin(num)[2:]:       # 이진법으로 변환
            if bit == '1':
                result += '#'
            else:
                result += ' '

        # 길이가 n보다 작으면
        # ex) n=6, 22 | 14 = 10110 | 01110 = 11110
        if len(result) < n:
            # 왼쪽에 공백 추가
            result = ' '*(n-len(result))+result
        answer.append(result)
            
    return answer