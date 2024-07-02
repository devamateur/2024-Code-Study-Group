'''
문제 번호 :
3장 예제 3-1

문제 정의 :
N원에 대한 최소 동전 개수의 거스름돈 계산하기.
N은 항상 10의 배수이며, 동전은 500,100,50,10 단위로 존재한다.

풀이 시간 : 
10분

풀이 방법 :
단위가 큰 동전순으로 나눗셈하여 값 구하기.

*작은 숫자를 다룰 때는 //,% 연산자가 더 빠르게 계산됨.
*큰 숫자를 다룰 때는 divmod를 권장함.

'''

coinage = [500,100,50,10]
result = 0

n = int(input('입력할 돈 :'))

for coin in coinage :
    quotient,remainder = divmod(n,coin)
    result +=quotient
    n = remainder

print("거스름 동전의 개수는",result,"개 이다.")
    
