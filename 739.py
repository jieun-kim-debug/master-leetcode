#1. enumerate로 인덱스와 값 가져오기
#2. 현재 temp가 stack의 마지막 temp보다 높으면, 현재 index - stack의 마지막 temp
#3. index 별로 비교가 되어야 하므로 stack이 존재하는 동안, pop
#4. return answer

#**while문 조건을 간과하고 넘어가서 엄청 오래걸림

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        # print(answer)
        
        stack = []
        
        for i, temp in enumerate(T):
            while stack and temp>T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
                # print(f"answer:{answer}")
            stack.append(i)
            # print(f"stack:{stack}")

        return answer