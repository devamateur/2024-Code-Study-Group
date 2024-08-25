import collections
class Solution:
    def make(self):
        '''
            문자열 A, B가 주어질 때
            A를 B로 만들 수 있는 최소 연산의 수 구하기
            연산의 종류: 삽입, 삭제, 교체
        '''

        A = input()
        B = input()

        # 방법1. DP는 잘 모르겠고
        # A, B 모두에 있는 문자를 카운트하고
        # B에만 있는 문자 개수를 구하기
        # 이 경우, 예제 테케에서만 돌아감

        a_dict = collections.defaultdict(int)
        b_dict = collections.defaultdict(int)

        for a in A:
            a_dict[a] += 1

        for b in B:
            b_dict[b] += 1

        a_count = 0

        for key, val in b_dict.items():
            if key not in a_dict:          # 아예 없는 문자인경우
                a_count += 1
            elif val > a_dict[key]:        # 둘 다 문자가 있는데 갯수가 다른 경우, 다른 갯수만큼 더함
                a_count += val-a_dict[key] 
        print('야매:', a_count)

        # 방법2. DP
        # https://velog.io/@49crehbgr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98Algorithm-%ED%8E%B8%EC%A7%91%EA%B1%B0%EB%A6%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        
        # DP 테이블 초기화
        # 0행, 0열을 초기화
        for i in range(1,len(A)+1):
            dp[i][0] = i

        for j in range(1, len(B)+1):
            dp[0][j] = j
        #print(dp)

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:           # 문자가 다른 경우 삽입, 삭제, 갱신 중 최소 횟수 택함
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        print('dp:', dp[len(A)][len(B)])
s = Solution()
s.make()