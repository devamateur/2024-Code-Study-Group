from collections import defaultdict
import numpy as np

def solution(str1, str2):
    answer = 0
    
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            str1_dict[(str1[i]+str1[i+1]).lower()] += 1
            
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            str2_dict[(str2[i]+str2[i+1]).lower()] += 1


    # 생성된 집합이 없으면 65536 리턴
    if len(str1_dict) == 0 and len(str2_dict) == 0:
        return 65536
    
    # 교집합
    for key, val in str1_dict.items():
        if key in str2_dict:
            answer += min(val, str2_dict[key])
    # 합집합
    union = 0
    
    for key, val in str1_dict.items():
        union += val
    for key, val in str2_dict.items():
        union += val
    
    union -= answer           # 교집합 빼줌

    answer = np.floor((answer/union)*65536)          # 소수점 버리기
    return answer