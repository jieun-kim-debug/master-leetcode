#1. 로그는 식별자로 구성
#2. 식별자 뒤에 숫자나 소문자가 옴
#3. letter-log가 앞에 오도록 정렬
#4. 식별자 뒤에 letter는 알파벳 순으로
#5. logs의 하나하나의 요소(for log in logs)를 split을 나누기
#6. letter-log와 digit-log를 정렬해서 빈리스트에 각자 담기
#7. 리스트는 더해진 순서대로 정렬되므로 letter-log + digit-log

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 람다식으로 sort를 진행하는데 식별자를 제외한 문자열[1:]을 키로하여 정렬
        # 동일한 경우 후순위로 식별자[0]를 지정해 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits