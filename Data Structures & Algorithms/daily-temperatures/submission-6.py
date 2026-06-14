class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        final = [0]*len(temp)

        for i in range(len(temp)):
            if not stack or temp[i] <= temp[stack[-1]]:
                stack.append(i)
        
            elif temp[i] > temp[stack[-1]]:
                while stack and temp[stack[-1]] < temp[i]:
                    final[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
                     
        
               
        return final