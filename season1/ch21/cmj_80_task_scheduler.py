import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 한 번의 라운드에서 최대 n+1개의 작업을 할 수 있음
            for task, _ in counter.most_common(n + 1):      # 최빈값 n+1개 추출
                sub_count += 1             # 쿨링 타임
                result += 1
                counter.subtract(task)      # 현재 작업의 빈도 1 감소

                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            # 남은 작업이 없으면 루프 종료
            if not counter:
                break

            # 쿨링 타임 추가
            result += n - sub_count + 1

        return result