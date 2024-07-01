'''
비밀지도
https://school.programmers.co.kr/learn/courses/30/lessons/17681

[time] 15m
[풀이방식] :
- 두 개의 지도(배열의 행)을 이진수로 바꾼 후 OR연산 결과값으로 활용함.
- 결과값은 앞에 ob가 붙으므로 [2:]로 잘라주고, 왼쪽에서 0으로 자릿수 맞추고(zfill(자릿수)), 1과 0을 #과 공백으로 바꾸기.

'''

def solution(n, arr1, arr2):
    total_map = []
    
    for i,j in zip(arr1,arr2):
        tmp = bin(i|j)[2:].zfill(n)
        tmp = tmp.replace("1","#")
        tmp = tmp.replace("0"," ")

        total_map += tmp,
    
    return total_map
        