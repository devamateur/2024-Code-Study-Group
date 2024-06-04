class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []

        # 키 기준 내림차순 정렬
        # 키가 같은 경우, k를 기준으로 오름차순 정렬
        # k: 나보다 키가 크거나 같은 사람들 중 나의 순위
        people = list(sorted(people, key=lambda x:(x[0], -x[1]), reverse=True))
        
        for p in people:
            queue.insert(p[1], p)

        return queue