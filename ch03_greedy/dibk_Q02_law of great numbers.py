'''
문제 번호 :
3장 실전 문제 2 : 큰 수의 법칙

문제 정의 :
입력 배열리스트에서 M번 더하여 가장 큰 수를 구하기.
배열의 해당값은 k번 반복하여 더할 수 있다.

첫번째 줄에 N(2~1000),M(1~10000),k(1~10000)
두번째 줄에 N개의 자연수(공백으로 구분)

풀이 시간 : 
20분

풀이 방법 :
입력 배열 리스트를 가장 큰 값 기준으로 정렬 후, 첫번째 값(가장 큰 값)을 k번 반복하여 계산 후, 두번째로 큰 값을 1번 더하고 다시 첫번째 값을 k번 더하는 방식.

'''

n,m,k = map(int,input('n,m,k 입력하기(공백으로 구분) :').split())
nums = list(map(int,input('n개의 자연수(공백으로 구분) :').split()))

nums.sort()
result = 0
st,nd = nums[-1],nums[-2]

while m :
    for i in range(k) :
        result += st
        m-=i
        
    result += nd
    m-=1
    
print("큰 수의 법칙 결과 :",result)
