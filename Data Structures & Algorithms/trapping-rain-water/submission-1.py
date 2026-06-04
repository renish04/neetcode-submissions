class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        dict = {}

        for i in range(len(height)):
            dict[i] = height[i]

        i = 0
        while i < len(height) - 2:
            print(dict, i)
            dict.pop(i)
            j = i+1
            if not height[j] < height[i]:
                i += 1
            else:
                dict.pop(j)
                max_key = max(dict, key=dict.get)

                if height[max_key] > height[j]:
                    k = j + 1
                    counter = height[j]
                    
                    while height[k] <= height[j]:
                        counter += height[k]
                        dict.pop(k)
                        k += 1
                    if height[k] >= height[i]:
                        area += ((k-j)*height[i])-counter
                        i = k
                    else:
                        area += ((k-j)*height[k])-counter
                        i = k
                else:
                    i += 1
        return area


