'''
🍪문제 번호 :
8장 실전문제 - 개미 전사

🍈문제 정의 :
인접하지 않은 창고들을 선택하여 최대 값 구하기

🍊풀이 시간 :
15분

🍒풀이 방법 :
바텀업방식으로 풀이.
inventory[2]부터 이전창고와 현재+현재-2창고합을 비교하여 max값을 저장하는 방식
최종 inventory에는 맥스값이 저장됨.

'''

class Solution :
    
    def antCombatant(self):
        # 입력
        N = int(input("창고 수 입력 : "))
        inventory = list(map(int,input().split()))
        
        if N <=2 :
            print('결과 : ', max(inventory))
            return
        
        for idx in range(2,N):
            inventory[idx] = max(inventory[idx-1],inventory[idx-2]+inventory[idx])
        
        print('결과 : ', inventory[-1])
        
        return 
    
test = Solution()
test.antCombatant()