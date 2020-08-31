#1. range(len(height)) 만큼 index 생성, stack으로 쌓기
#2. 기둥의 조건: stack에 값이 있으면서 현재 height > 과거의 height
#3. stack에 값이 없으면 기둥이 안생기기에 break
#4. stack=index(순서), height=값
#5. dist=두번째 기둥 - 첫번째 기둥 -1(-1을 해주는 이유는 index라서)
#6. waters=작은 기둥 - 작은 기둥 전 기둥
#7. vol = dist*waters

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        vol = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
            
                dist = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                vol += dist * waters
                
            stack.append(i)
            
        return vol