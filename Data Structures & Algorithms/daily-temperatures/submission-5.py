class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        index = []
        final = [0]*len(temp)

        for i in range(len(temp)):
            if not index:
                index.append(i)
            elif index and temp[index[-1]] < temp[i]:
                while index and temp[index[-1]] < temp[i]:
                    final[index[-1]] = i - index[-1]
                    index.pop()
                index.append(i)
            else:
                index.append(i)
             
        return final 