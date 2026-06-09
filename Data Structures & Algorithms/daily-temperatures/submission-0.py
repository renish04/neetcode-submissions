class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        if len(temp) == 1:
            return [0]
        
        stack = [0]
        final = [0]*len(temp)

        for i in range(1, len(temp)):
            if temp[i] <= temp[stack[-1]]:
                stack.append(i)
            else:
                while stack != [] and temp[stack[-1]] < temp[i]:
                    r = stack.pop()
                    final[r] = i - r
                stack.append(i)

        return final 

                

