class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        count = 0
        
        for num in data:
            # 카운트가 0이면, 왼쪽 1의 개수가 몇개인지 확인
            if count == 0:
                if (num >> 5) == 0b110:
                    count = 1
                elif (num >> 4) == 0b1110:
                    count = 2
                elif (num >> 3) == 0b11110:
                    count = 3
                elif (num >> 7) != 0:
                    return False
                
            # 카운트가 0이 아니면, 이전 바이트의 continuation byte인지 확인
            else:
                if (num >> 6) != 0b10:
                    return False
                count -= 1
        
        return count == 0
    
    # 테케 52 / 53 testcases passed...
    def validUtf8(self, data: List[int]) -> bool:
        next_ = 'dummy'       # 다음 바이트 시작 문자열

        for num in data:
            new_num = bin(num)[2:]       # 이진수 변환, 앞에 '0b' 문자열 자름

            # 1인 경우, 변환값이 '1'이어서 바이트 길이로 맞춰줌
            if len(new_num) < 8:
                new_num += '0'*(8-len(new_num))
                new_num = new_num[::-1]

            #print('###', new_num)
            #print(next_)

            # 현재 바이트가 끝났는데, 다음 바이트가 또 있는 경우
            # ex) [240,162,138,147,145] = 11110000 10100010 10001010 10010011 '10010001'
                # 240이 11110으로 시작하는 4바이트 문자열인데, '10'으로 시작하는 시퀀스가 마지막에 한 번 더 나옴
            if next_ == '' and new_num.startswith('10'):
                return False

            # 다음 시퀀스가 있는 경우
            if '10' in next_:
                #print(next_)
                if not new_num.startswith('10'):      
                    return False
                else:         # 바이트가 '10'으로 시작하면 옳은 시퀀스
                    next_ = next_[2:]       # 다음 바이트 시작 문자열 갱신 ex) '1010' -> '10'

            # 1 byte
            if new_num.startswith('0'):
                next_ = ''
            # 2 byte
            if new_num.startswith('110'):
                next_ = '10'
            # 3 byte
            if new_num.startswith('1110'):
                next_ = '10'*2
            # 4 byte
            if new_num.startswith('11110'):
                next_ = '10'*3

        if next_ == '':
            return True
        return False