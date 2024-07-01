class Solution:
    def get_changes(self, N) -> int:
        # N: 돈
        # changes 거스름돈 500, 100, 50, 10
        # 거슬러줘야 할 돈 N은 항상 10의 배수임
        result = 0
        changes = [500, 100, 50, 10]
        i = 0      # 거스름돈 인덱스

        while N != 0:
            if N >= changes[i]:
                result += N // changes[i]
                N %= changes[i]
                print('거스름돈:', changes[i])
            else:
                i += 1
        return result

s = Solution()    
print(s.get_changes(1260))