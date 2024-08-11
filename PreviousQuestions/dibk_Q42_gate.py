'''
🍪문제 번호 :
18장 그래프 이론 - 42번 탑승구

🍈문제 정의 :
탑승구는 1번부터 G번까지 번호로 구분된다. 
공항에는 P개의 비행기가 차례대로 도착할 예정이고 i번째 비행기를 1번부터 g번째 탑승구 중 하나에 영구적으로 지정해야한다.(다른 비행기가 설정되지 않은 탑승구만 가능)
만약 탑승구 도킹이 불가능한 경우 운행 중지
최대 도킹 가능한 비행기 수 출력하기


🍊풀이 시간 :
15~

🍒풀이 방법 :
i번째 비행기값(value)과 g정보값(key)을 딕셔너리에 담아두고, g값(key)을 기준으로 내림차순 정렬 후에 해당 키에서 하나의 value만 카운팅하기

'''

class Solution :
    
    def gate(self):
            
        # 입력
        G = int(input("탑승구 수G : "))
        P = int(input("비행기 수P : "))
        
        boarding_gate = {}
        
        for i in range(P) :
            g = int(input())
            boarding_gate[g] = boarding_gate.get(g, []) + [i+1]
        
        print("결과 : ",len(boarding_gate))
        return 
    
test = Solution()
test.gate()