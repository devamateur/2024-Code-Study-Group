class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 알파벳 로그 > 숫자 로그
        # 알파벳 로그: 로그 컨텐츠별로 사전순 정렬, 컨텐츠가 같으면 id별로 사전순 정렬

        ordered_logs = []
        for log in logs:
            split_log = log.split()

            if split_log[1].isalpha():       # 알파벳 로그 먼저 추가
                ordered_logs.append(log)

        # 알파벳 로그를 사전순으로 정렬하고 digit log와 이어붙임
        ordered_logs = sorted(ordered_logs, key=lambda x: (x.split()[1:], x.split()[0])) + [log for log in logs if log.split()[1].isdigit()]

        return ordered_logs