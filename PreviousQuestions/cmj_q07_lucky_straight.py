class Solution:
    def lucky_straight(self):
        score = input()

        left_sum = sum(map(int, score[:len(score)//2]))
        right_sum = sum(map(int, score[len(score)//2:]))

        if left_sum == right_sum:
            print('LUCKY')
        else:
            print('READY')

s = Solution()
s.lucky_straight()