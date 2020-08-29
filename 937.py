class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 로그를 재정렬
        #1. 로그의 가장 앞부분은 식별자
        #2. 문자로 구성된 로그 먼저 나오고 다음 숫자 로그
        #3. 문자가 동일할 경우, 식별자 순서로 정렬
        #4. 숫자는 입력 순서대로
        
        digits = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits